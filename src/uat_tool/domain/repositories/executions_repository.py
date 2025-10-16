from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from uat_tool.domain import (
    Campaign,
    CampaignRun,
    Case,
    CaseRun,
    Step,
    StepRun,
)

from .base import BaseRepository, EnvironmentMixinRepository
from .test_management_repository import CampaignRepository


class CampaignRunRepository(EnvironmentMixinRepository[CampaignRun]):
    """Repositorio para la entidad CampaignRun."""

    def __init__(self, session: Session):
        super().__init__(session, CampaignRun)

    def create(self, data: dict, environment_id: int) -> CampaignRun:
        """Inicia una nueva ejecución de campaña."""
        required_fields = ["campaign_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para CampaignRun")

        try:
            # Validar que la campaña existe
            campaign = self.session.get(Campaign, data["campaign_id"])
            if not campaign:
                raise ValueError(
                    f"Campaign con id {data['campaign_id']} no encontrada."
                )

            # Crear la ejecución de campaña
            campaign_run = self.create_with_environment(data, environment_id)

            # Validar que la campaign run se creó correctamente
            if not campaign_run.id:
                raise ValueError("Error al crear la ejecución de campaña")

            # Iniciar automáticamente los case runs para todos los casos de la campaña
            self._initialize_case_runs(campaign_run.id, campaign.id)

            # Cambiar estado de 'DRAFT' a 'RUNNING' para la campaign relacionada
            campaign_repo = CampaignRepository(self.session)
            campaign_repo.update(
                campaign.id, {"status": "RUNNING"}, environment_id, data["modified_by"]
            )

            self.session.flush()
            return campaign_run

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def _initialize_case_runs(self, campaign_run_id: int, campaign_id: int):
        """Inicializa los case runs para todos los casos de la campaña."""
        # Obtener todos los casos de la campaña a través de bloques
        from uat_tool.domain import Block

        campaign = (
            self.session.query(Campaign)
            .options(joinedload(Campaign.blocks).joinedload(Block.cases))
            .filter(Campaign.id == campaign_id)
            .first()
        )

        if not campaign:
            return

        # Recoger todos los casos únicos de todos los bloques
        all_cases = []
        for block in campaign.blocks:
            all_cases.extend(block.cases)

        # Crear case runs para cada caso
        case_run_repo = CaseRunRepository(self.session)
        for case in all_cases:
            case_run_data = {
                "campaign_run_id": campaign_run_id,
                "case_id": case.id,
            }
            case_run_repo.create(case_run_data)

    def finalize(
        self, campaign_run_id: int, modified_by: str, notes: str = None
    ) -> CampaignRun:
        """Finaliza una ejecución de campaña."""
        campaign_run = self.get_by_id(campaign_run_id, raise_if_not_found=True)
        campaign_run.ended_at = datetime.now()
        if notes:
            campaign_run.notes = notes

        # Cambiar estado de 'DRAFT' a 'FINISHED' para la campaign relacionada
        campaign_repo = CampaignRepository(self.session)
        campaign_repo.update(
            campaign_run.campaign_id,
            {"status": "FINISHED"},
            environment_id=campaign_run.environment_id,
            modified_by=modified_by,
        )

        self.session.flush()
        return campaign_run

    def cancel(self, campaign_run_id: int, modified_by: str) -> CampaignRun:
        """Finaliza una ejecución de campaña."""
        campaign_run = self.get_by_id(campaign_run_id, raise_if_not_found=True)
        campaign_run.ended_at = datetime.now()

        # Cambiar estado de 'DRAFT' a 'CANCELLED' para la campaign relacionada
        campaign_repo = CampaignRepository(self.session)
        campaign_repo.update(
            campaign_run.campaign_id,
            {"status": "CANCELLED"},
            environment_id=campaign_run.environment_id,
            modified_by=modified_by,
        )

        self.session.flush()
        return campaign_run

    def get_with_details(self, campaign_run_id: int) -> CampaignRun | None:
        """Obtiene una ejecución de campaña con todos sus detalles."""
        return (
            self.query()
            .options(
                joinedload(CampaignRun.case_runs).joinedload(CaseRun.step_runs),
                joinedload(CampaignRun.campaign),
                joinedload(CampaignRun.bugs),
            )
            .filter(CampaignRun.id == campaign_run_id)
            .one_or_none()
        )

    def get_by_campaign(self, campaign_id: int) -> list[CampaignRun]:
        """Obtiene todas las ejecuciones de una campaña."""
        return (
            self.query()
            .filter(CampaignRun.campaign_id == campaign_id)
            .order_by(CampaignRun.started_at.desc())
            .all()
        )


class CaseRunRepository(BaseRepository[CaseRun]):
    """Repositorio para la entidad CaseRun."""

    def __init__(self, session: Session):
        super().__init__(session, CaseRun)

    def create(self, data: dict) -> CaseRun:
        """Crea una ejecución de caso."""
        required_fields = ["campaign_run_id", "case_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para CaseRun")

        try:
            # Validar que el campaign run existe
            campaign_run = self.session.get(CampaignRun, data["campaign_run_id"])
            if not campaign_run:
                raise ValueError(
                    f"CampaignRun con id {data['campaign_run_id']} no encontrado."
                )

            # Validar que el caso existe
            case = self.session.get(Case, data["case_id"])
            if not case:
                raise ValueError(f"Case con id {data['case_id']} no encontrado.")

            # Crear la ejecución de caso
            case_run_data = {
                **data,
            }
            case_run = super().create(**case_run_data)

            # Iniciar automáticamente los step runs para todos los pasos del caso
            self._initialize_step_runs(campaign_run.id, case_run.id, case.id)

            self.session.flush()
            return case_run

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def _initialize_step_runs(
        self, campaign_run_id: int, case_run_id: int, case_id: int
    ):
        """Inicializa los step runs para todos los pasos del caso."""
        steps = self.session.query(Step).filter(Step.case_id == case_id).all()

        step_run_repo = StepRunRepository(self.session)
        for step in steps:
            step_run_repo.create(
                {
                    "campaign_run_id": campaign_run_id,
                    "case_run_id": case_run_id,
                    "step_id": step.id,
                }
            )

    def get_with_steps(self, case_run_id: int) -> CaseRun | None:
        """Obtiene una ejecución de caso con sus step runs."""
        return (
            self.query()
            .options(joinedload(CaseRun.step_runs))
            .filter(CaseRun.id == case_run_id)
            .one_or_none()
        )

    def get_by_campaign_run(self, campaign_run_id: int) -> list[CaseRun]:
        """Obtiene todas las ejecuciones de caso de una campaña."""
        return (
            self.query()
            .options(joinedload(CaseRun.case))
            .filter(CaseRun.campaign_run_id == campaign_run_id)
            .all()
        )


class StepRunRepository(BaseRepository[StepRun]):
    """Repositorio para la entidad StepRun."""

    def __init__(self, session: Session):
        super().__init__(session, StepRun)

    def create(self, data: dict) -> StepRun:
        """Crea una ejecución de paso."""
        required_fields = ["campaign_run_id", "case_run_id", "step_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para StepRun")

        try:
            # Validar que el case run existe
            case_run = self.session.get(CaseRun, data["case_run_id"])
            if not case_run:
                raise ValueError(f"CaseRun con id {data['case_run_id']} no encontrado.")

            # Validar que el paso existe
            step = self.session.get(Step, data["step_id"])
            if not step:
                raise ValueError(f"Step con id {data['step_id']} no encontrado.")

            # Crear la ejecución de paso
            step_run_data = {
                **data,
                "case_run_id": case_run.id,
                "step_id": step.id,
            }
            return super().create(**step_run_data)

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def update_step_result(
        self, step_run_id: int, passed: bool, notes: str = None
    ) -> StepRun:
        """Actualiza el resultado de un paso ejecutado."""
        step_run = self.get_by_id(step_run_id, raise_if_not_found=True)
        step_run.passed = passed
        if notes:
            step_run.notes = notes
        self.session.flush()
        return step_run

    def get_with_details(self, step_run_id: int) -> StepRun | None:
        """Obtiene una ejecución de paso con todos sus detalles."""
        return (
            self.query()
            .options(
                joinedload(StepRun.step),
                joinedload(StepRun.case_run),
                joinedload(StepRun.campaign_run),
            )
            .filter(StepRun.id == step_run_id)
            .one_or_none()
        )

    def get_by_case_run(self, case_run_id: int) -> list[StepRun]:
        """Obtiene todas las ejecuciones de paso de un caso."""
        return (
            self.query()
            .options(joinedload(StepRun.step))
            .filter(StepRun.case_run_id == case_run_id)
            .order_by(StepRun.step_id)
            .all()
        )
