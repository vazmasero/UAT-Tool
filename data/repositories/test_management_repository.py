from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.models import (
    Block,
    Campaign,
    Case,
    Drone,
    Operator,
    Requirement,
    Section,
    Step,
    System,
    UasZone,
    UhubUser,
)

from .base import AuditEnvironmentMixinRepository, BaseRepository


class CampaignRepository(
    BaseRepository[Campaign], AuditEnvironmentMixinRepository[Campaign]
):
    """Repositorio para la entidad Campaign."""

    def __init__(self, session: Session):
        super().__init__(session, Campaign)

    def create_with_blocks(self, data: dict) -> Campaign:
        """Crea una campaña con bloques asociados."""
        self._validate_audit_environment_data(data)

        if not data.get("system_id"):
            raise ValueError("Las campañas deben tener un sistema asociado.")
        if not data.get("blocks"):
            raise ValueError(
                "Las campañas deben tener al menos un bloque de test asociado."
            )

        try:
            # Validar que el sistema existe
            system = self.session.query(System).get(data["system_id"])
            if not system:
                raise ValueError(f"Sistema con id {data['system_id']} no encontrado.")

            # Validar que los bloques existen
            block_ids = data["blocks"]
            blocks = self.session.query(Block).filter(Block.id.in_(block_ids)).all()

            if len(blocks) != len(block_ids):
                missing = set(block_ids) - {b.id for b in blocks}
                raise ValueError(f"Bloques no encontrados: {missing}")

            # Crear la campaña
            campaign_data = {
                "code": data["code"],
                "description": data["description"],
                "system_id": system.id,
                "system_version": data["system_version"],
                "comments": data.get("comments"),
                "status": data.get("status", "DRAFT"),
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],
            }
            campaign = self.create(**campaign_data)

            # Asociar bloques
            campaign.blocks = blocks
            self.session.flush()

            return campaign

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_blocks(self, campaign_id: int) -> Campaign | None:
        """Obtiene una campaña con sus bloques cargados."""
        return (
            self.query(Campaign)
            .options(joinedload(Campaign.blocks))
            .filter(Campaign.id == campaign_id)
            .one_or_none()
        )

    def get_by_code(self, code: str, environment_id: int) -> Campaign | None:
        """Busca una campaña por código y entorno."""
        return (
            self.query(Campaign)
            .filter(Campaign.code == code, Campaign.environment_id == environment_id)
            .first()
        )


class BlockRepository(BaseRepository[Block], AuditEnvironmentMixinRepository[Block]):
    """Repositorio para la entidad Block."""

    def __init__(self, session: Session):
        super().__init__(session, Block)

    def create_with_system(self, data: dict) -> Block:
        """Crea un bloque con sistema asociado."""
        self._validate_audit_environment_data(data)
        if not data.get("system_id"):
            raise ValueError("Los bloques deben tener un sistema asociado.")

        try:
            # Validar que el sistema existe
            system = self.session.query(System).get(data["system_id"])
            if not system:
                raise ValueError(f"Sistema con id {data['system_id']} no encontrado.")

            # Crear el bloque
            block_data = {
                "code": data["code"],
                "name": data.get("name"),
                "system_id": system.id,
                "comments": data.get("comments"),
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],
            }
            block = self.create(**block_data)

            # Asociar casos si se proporcionan
            if "cases" in data:
                case_ids = data["cases"]
                cases = self.session.query(Case).filter(Case.id.in_(case_ids)).all()
                if len(cases) != len(case_ids):
                    missing = set(case_ids) - {c.id for c in cases}
                    raise ValueError(f"Casos no encontrados: {missing}")
                block.cases = cases

            self.session.flush()
            return block

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_cases(self, block_id: int) -> Block | None:
        """Obtiene un bloque con sus casos cargados."""
        return (
            self.query(Block)
            .options(joinedload(Block.cases))
            .filter(Block.id == block_id)
            .one_or_none()
        )

    def get_by_code(self, code: str, environment_id: int) -> Block | None:
        """Busca un bloque por código y entorno."""
        return (
            self.query(Block)
            .filter(Block.code == code, Block.environment_id == environment_id)
            .first()
        )


class CaseRepository(BaseRepository[Case], AuditEnvironmentMixinRepository[Case]):
    """Repositorio para la entidad Case."""

    def __init__(self, session: Session):
        super().__init__(session, Case)

    def create_with_relations(self, data: dict) -> Case:
        """Crea un caso de prueba con todas sus relaciones."""
        self._validate_audit_environment_data(data)
        required_fields = ["code", "name", "comments"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para Case")

        try:
            # Crear el caso base
            case_data = {
                "code": data["code"],
                "name": data["name"],
                "comments": data["comments"],
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],
            }
            case = self.create(**case_data)

            # Asociar relaciones many-to-many
            relations_mapping = {
                "operators": (Operator, "operators"),
                "drones": (Drone, "drones"),
                "uhub_users": (UhubUser, "uhub_users"),
                "uas_zones": (UasZone, "uas_zones"),
                "systems": (System, "systems"),
                "sections": (Section, "sections"),
            }

            for relation_key, (model_class, attr_name) in relations_mapping.items():
                if relation_key in data:
                    ids = data[relation_key]
                    objects = (
                        self.session.query(model_class)
                        .filter(model_class.id.in_(ids))
                        .all()
                    )
                    if len(objects) != len(ids):
                        missing = set(ids) - {obj.id for obj in objects}
                        raise ValueError(f"{relation_key} no encontrados: {missing}")
                    setattr(case, attr_name, objects)

            self.session.flush()
            return case

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_full_relations(self, case_id: int) -> Case | None:
        """Obtiene un caso con todas sus relaciones cargadas."""
        return (
            self.query(Case)
            .options(
                joinedload(Case.operators),
                joinedload(Case.drones),
                joinedload(Case.uhub_users),
                joinedload(Case.uas_zones),
                joinedload(Case.systems),
                joinedload(Case.sections),
                joinedload(Case.steps),
                joinedload(Case.blocks),
            )
            .filter(Case.id == case_id)
            .one_or_none()
        )

    def get_by_code(self, code: str, environment_id: int) -> Case | None:
        """Busca un caso por código y entorno."""
        return (
            self.query(Case)
            .filter(Case.code == code, Case.environment_id == environment_id)
            .first()
        )


class StepRepository(BaseRepository[Step]):
    """Repositorio para la entidad Step."""

    def __init__(self, session: Session):
        super().__init__(session, Step)

    def create_with_requirements(self, data: dict) -> Step:
        """Crea un paso con requisitos asociados."""

        required_fields = ["action", "expected_result", "comments", "case_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para Step")

        try:
            # Validar que el caso existe
            case = self.session.query(Case).get(data["case_id"])
            if not case:
                raise ValueError(f"Case con id {data['case_id']} no encontrado.")

            # Crear el paso
            step_data = {
                "action": data["action"],
                "expected_result": data["expected_result"],
                "comments": data["comments"],
                "case_id": case.id,
            }
            step = self.create(**step_data)

            # Asociar requisitos si se proporcionan
            if "requirements" in data:
                req_ids = data["requirements"]
                requirements = (
                    self.session.query(Requirement)
                    .filter(Requirement.id.in_(req_ids))
                    .all()
                )
                if len(requirements) != len(req_ids):
                    missing = set(req_ids) - {r.id for r in requirements}
                    raise ValueError(f"Requisitos no encontrados: {missing}")
                step.requirements = requirements

            self.session.flush()
            return step

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_by_case(self, case_id: int) -> list[Step]:
        """Obtiene todos los pasos de un caso."""
        return self.query(Step).filter(Step.case_id == case_id).all()

    def get_with_requirements(self, step_id: int) -> Step | None:
        """Obtiene un paso con sus requisitos cargados."""
        return (
            self.query(Step)
            .options(joinedload(Step.requirements))
            .filter(Step.id == step_id)
            .one_or_none()
        )
