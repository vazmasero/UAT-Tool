from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.models import Campaign, CampaignRun, Case, CaseRun, File, Step, StepRun

from .base import AuditEnvironmentMixinRepository, BaseRepository


class CampaignRunRepository(
    BaseRepository[CampaignRun], AuditEnvironmentMixinRepository[CampaignRun]
):
    """Repositorio para la entidad CampaignRun."""

    def __init__(self, session: Session):
        super().__init__(session, CampaignRun)

    def start_campaign_run(self, data: dict) -> CampaignRun:
        """Inicia una nueva ejecución de campaña."""
        self._validate_audit_environment_data(data)
        required_fields = ["campaign_id", "executed_by"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para CampaignRun")

        try:
            # Validar que la campaña existe
            campaign = self.session.query(Campaign).get(data["campaign_id"])
            if not campaign:
                raise ValueError(
                    f"Campaign con id {data['campaign_id']} no encontrada."
                )

            # Crear la ejecución de campaña
            campaign_run_data = {
                "campaign_id": campaign.id,
                "executed_by": data["executed_by"],
                "notes": data.get("notes"),
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],
            }
            campaign_run = self.create(**campaign_run_data)

            # Iniciar automáticamente los case runs para todos los casos de la campaña
            self._initialize_case_runs(campaign_run.id, campaign.id)

            self.session.flush()
            return campaign_run

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def _initialize_case_runs(self, campaign_run_id: int, campaign_id: int):
        """Inicializa los case runs para todos los casos de la campaña."""
        # Obtener todos los casos de la campaña a través de bloques
        from core.models import Block, block_cases

        cases = (
            self.session.query(Case)
            .join(block_cases)
            .join(Block)
            .join(Campaign.blocks)
            .filter(Campaign.id == campaign_id)
            .all()
        )

        case_run_repo = CaseRunRepository(self.session)
        for case in cases:
            case_run_repo.create_case_run(
                {
                    "campaign_run_id": campaign_run_id,
                    "case_id": case.id,
                }
            )

    def end_campaign_run(self, campaign_run_id: int, notes: str = None) -> CampaignRun:
        """Finaliza una ejecución de campaña."""
        campaign_run = self.get_by_id(campaign_run_id)
        if campaign_run:
            campaign_run.ended_at = datetime.now()
            if notes:
                campaign_run.notes = notes
            self.session.flush()
        return campaign_run

    def get_with_details(self, campaign_run_id: int) -> CampaignRun | None:
        """Obtiene una ejecución de campaña con todos sus detalles."""
        return (
            self.query(CampaignRun)
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
            self.query(CampaignRun)
            .filter(CampaignRun.campaign_id == campaign_id)
            .order_by(CampaignRun.started_at.desc())
            .all()
        )


class CaseRunRepository(BaseRepository[CaseRun]):
    """Repositorio para la entidad CaseRun."""

    def __init__(self, session: Session):
        super().__init__(session, CaseRun)

    def create_case_run(self, data: dict) -> CaseRun:
        """Crea una ejecución de caso."""
        required_fields = ["campaign_run_id", "case_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para CaseRun")

        try:
            # Validar que el campaign run existe
            campaign_run = self.session.query(CampaignRun).get(data["campaign_run_id"])
            if not campaign_run:
                raise ValueError(
                    f"CampaignRun con id {data['campaign_run_id']} no encontrado."
                )

            # Validar que el caso existe
            case = self.session.query(Case).get(data["case_id"])
            if not case:
                raise ValueError(f"Case con id {data['case_id']} no encontrado.")

            # Crear la ejecución de caso
            case_run_data = {
                "campaign_run_id": campaign_run.id,
                "case_id": case.id,
                "notes": data.get("notes"),
            }
            case_run = self.create(**case_run_data)

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
            step_run_repo.create_step_run(
                {
                    "campaign_run_id": campaign_run_id,
                    "case_run_id": case_run_id,
                    "step_id": step.id,
                }
            )

    def get_with_steps(self, case_run_id: int) -> CaseRun | None:
        """Obtiene una ejecución de caso con sus step runs."""
        return (
            self.query(CaseRun)
            .options(joinedload(CaseRun.step_runs))
            .filter(CaseRun.id == case_run_id)
            .one_or_none()
        )

    def get_by_campaign_run(self, campaign_run_id: int) -> list[CaseRun]:
        """Obtiene todas las ejecuciones de caso de una campaña."""
        return (
            self.query(CaseRun)
            .options(joinedload(CaseRun.case))
            .filter(CaseRun.campaign_run_id == campaign_run_id)
            .all()
        )


class StepRunRepository(BaseRepository[StepRun]):
    """Repositorio para la entidad StepRun."""

    def __init__(self, session: Session):
        super().__init__(session, StepRun)

    def create_step_run(self, data: dict) -> StepRun:
        """Crea una ejecución de paso."""
        required_fields = ["campaign_run_id", "case_run_id", "step_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para StepRun")

        try:
            # Validar que el case run existe
            case_run = self.session.query(CaseRun).get(data["case_run_id"])
            if not case_run:
                raise ValueError(f"CaseRun con id {data['case_run_id']} no encontrado.")

            # Validar que el paso existe
            step = self.session.query(Step).get(data["step_id"])
            if not step:
                raise ValueError(f"Step con id {data['step_id']} no encontrado.")

            # Crear la ejecución de paso
            step_run_data = {
                "campaign_run_id": data["campaign_run_id"],
                "case_run_id": case_run.id,
                "step_id": step.id,
            }
            return self.create(**step_run_data)

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def update_step_result(
        self, step_run_id: int, passed: bool, notes: str = None, file_id: int = None
    ) -> StepRun:
        """Actualiza el resultado de un paso ejecutado."""
        step_run = self.get_by_id(step_run_id)
        if step_run:
            step_run.passed = passed
            if notes:
                step_run.notes = notes
            if file_id:
                # Validar que el archivo existe
                file = self.session.query(File).get(file_id)
                if not file:
                    raise ValueError(f"File con id {file_id} no encontrado.")
                step_run.file_id = file_id
            self.session.flush()
        return step_run

    def get_with_details(self, step_run_id: int) -> StepRun | None:
        """Obtiene una ejecución de paso con todos sus detalles."""
        return (
            self.query(StepRun)
            .options(
                joinedload(StepRun.step),
                joinedload(StepRun.case_run),
                joinedload(StepRun.campaign_run),
                joinedload(StepRun.file),
            )
            .filter(StepRun.id == step_run_id)
            .one_or_none()
        )

    def get_by_case_run(self, case_run_id: int) -> list[StepRun]:
        """Obtiene todas las ejecuciones de paso de un caso."""
        return (
            self.query(StepRun)
            .options(joinedload(StepRun.step))
            .filter(StepRun.case_run_id == case_run_id)
            .order_by(StepRun.step_id)
            .all()
        )
