from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from uat_tool.domain import (
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


class CampaignRepository(AuditEnvironmentMixinRepository[Campaign]):
    """Repositorio para la entidad Campaign."""

    def __init__(self, session: Session):
        super().__init__(session, Campaign)

    def _validate_related_objects(
        self, model_class, ids: list[int], error_message: str
    ) -> list:
        """Valida que los objetos relacionados existan."""
        if not ids:
            return []

        objects = self.session.query(model_class).filter(model_class.id.in_(ids)).all()
        if len(objects) != len(ids):
            missing = set(ids) - {obj.id for obj in objects}
            raise ValueError(f"{error_message}: {missing}")
        return objects

    def create(self, data: dict, environment_id: int, modified_by: str) -> Campaign:
        """Crea una campaña con bloques asociados."""
        if not data.get("system_id"):
            raise ValueError("Las campañas deben tener un sistema asociado.")
        if not data.get("blocks"):
            raise ValueError(
                "Las campañas deben tener al menos un bloque de test asociado."
            )

        try:
            # Validar que el sistema existe
            system = self.session.get(System, data["system_id"])
            if not system:
                raise ValueError(f"Sistema con id {data['system_id']} no encontrado.")

            # Extraer bloques antes de crear (y validar que no está vacío)
            block_ids = data.pop("blocks")

            # Crear la campaña
            campaign = self.create_with_audit_env(data, environment_id, modified_by)

            # Validar y asociar bloques
            blocks = self._validate_related_objects(
                Block, block_ids, "Bloques no encontrados"
            )
            campaign.blocks = blocks

            self.session.flush()
            return campaign

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_blocks(self, campaign_id: int) -> Campaign | None:
        """Obtiene una campaña con sus bloques cargados."""
        return (
            self.query()
            .options(joinedload(Campaign.blocks))
            .filter(Campaign.id == campaign_id)
            .one_or_none()
        )

    def get_by_code(self, code: str, environment_id: int) -> Campaign | None:
        """Busca una campaña por código y entorno."""
        return (
            self.query()
            .filter(Campaign.code == code, Campaign.environment_id == environment_id)
            .first()
        )

    def update(
        self, campaign_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Campaign:
        """Actualiza una campaña con bloques asociados."""
        try:
            campaign = self.get_by_id(campaign_id, raise_if_not_found=True)

            # Extraer bloques primero
            block_ids = data.pop("blocks", None)

            # Actualizar campos básicos
            campaign = self.update_with_audit_env(
                campaign, data, modified_by, environment_id
            )

            # Actualizar bloques si se proporcionan
            if block_ids is not None:
                blocks = self._validate_related_objects(
                    Block, block_ids, "Bloques no encontrados"
                )
                campaign.blocks = blocks

            self.session.flush()
            return campaign

        except SQLAlchemyError:
            self.session.rollback()
            raise


class BlockRepository(AuditEnvironmentMixinRepository[Block]):
    """Repositorio para la entidad Block."""

    def __init__(self, session: Session):
        super().__init__(session, Block)

    def _validate_related_objects(
        self, model_class, ids: list[int], error_message: str
    ) -> list:
        """Valida que los objetos relacionados existan."""
        if not ids:
            return []

        objects = self.session.query(model_class).filter(model_class.id.in_(ids)).all()
        if len(objects) != len(ids):
            missing = set(ids) - {obj.id for obj in objects}
            raise ValueError(f"{error_message}: {missing}")
        return objects

    def create(self, data: dict, environment_id: int, modified_by: str) -> Block:
        """Crea un bloque con sistema asociado."""
        if not data.get("system_id"):
            raise ValueError("Los bloques deben tener un sistema asociado.")

        try:
            # Validar que el sistema existe
            system = self.session.get(System, data["system_id"])
            if not system:
                raise ValueError(f"Sistema con id {data['system_id']} no encontrado.")

            # Extraer relaciones antes de crear
            case_ids = data.pop("cases", [])

            # Crear el bloque
            block = self.create_with_audit_env(data, environment_id, modified_by)

            # Asociar casos si se proporcionan
            if case_ids:
                cases = self._validate_related_objects(
                    Case, case_ids, "Casos no encontrados"
                )
                block.cases = cases

            self.session.flush()
            return block

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_cases(self, block_id: int) -> Block | None:
        """Obtiene un bloque con sus casos cargados."""
        return (
            self.query()
            .options(joinedload(Block.cases))
            .filter(Block.id == block_id)
            .one_or_none()
        )

    def get_by_code(self, code: str, environment_id: int) -> Block | None:
        """Busca un bloque por código y entorno."""
        return (
            self.query()
            .filter(Block.code == code, Block.environment_id == environment_id)
            .first()
        )

    def update(
        self, block_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Block:
        """Actualiza un bloque con casos asociados."""
        try:
            block = self.get_by_id(block_id, raise_if_not_found=True)

            # Extraer relaciones primero
            case_ids = data.pop("cases", None)

            # Actualizar campos básicos
            block = self.update_with_audit_env(block, data, modified_by, environment_id)

            # Actualizar casos si se proporcionan
            if case_ids is not None:
                cases = self._validate_related_objects(
                    Case, case_ids, "Casos no encontrados"
                )
                block.cases = cases

            self.session.flush()
            return block

        except SQLAlchemyError:
            self.session.rollback()
            raise


class CaseRepository(AuditEnvironmentMixinRepository[Case]):
    """Repositorio para la entidad Case."""

    def __init__(self, session: Session):
        super().__init__(session, Case)

    def _validate_related_objects(
        self, model_class, ids: list[int], error_message: str
    ) -> list:
        """Valida que los objetos relacionados existan."""
        if not ids:
            return []

        objects = self.session.query(model_class).filter(model_class.id.in_(ids)).all()
        if len(objects) != len(ids):
            missing = set(ids) - {obj.id for obj in objects}
            raise ValueError(f"{error_message}: {missing}")
        return objects

    def create(self, data: dict, environment_id: int, modified_by: str) -> Case:
        """Crea un caso de prueba con todas sus relaciones."""
        try:
            # Configuración de relaciones
            relations_config = {
                "operators": (Operator, "operators", "Operadores no encontrados"),
                "drones": (Drone, "drones", "Drones no encontrados"),
                "uhub_users": (UhubUser, "uhub_users", "Usuarios Uhub no encontrados"),
                "uas_zones": (UasZone, "uas_zones", "Zonas UAS no encontradas"),
                "systems": (System, "systems", "Sistemas no encontrados"),
                "sections": (Section, "sections", "Secciones no encontradas"),
            }

            # Extraer todas las relaciones del data
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, [])

            # Usar transacción para operación atómica
            with self.session.begin_nested():
                # Crear caso base
                case = self.create_with_audit_env(data, environment_id, modified_by)

                # Manejar relaciones many-to-many
                for relation_key, (
                    model_class,
                    attr_name,
                    error_msg,
                ) in relations_config.items():
                    ids = extracted_relations[relation_key]
                    if ids:
                        objects = self._validate_related_objects(
                            model_class, ids, error_msg
                        )
                        setattr(case, attr_name, objects)

                self.session.flush()
                return case

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_full_relations(self, case_id: int) -> Case | None:
        """Obtiene un caso con todas sus relaciones cargadas."""
        return (
            self.query()
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
            self.query()
            .filter(Case.code == code, Case.environment_id == environment_id)
            .first()
        )

    def update(
        self, case_id: int, data: dict, environment_id: int, modified_by: str
    ) -> UasZone:
        """Actualiza una zona UAS con relaciones."""
        try:
            case = self.get_by_id(case_id, raise_if_not_found=True)

            # Configuración de relaciones
            relations_config = {
                "operators": (Operator, "operators", "Operadores no encontrados"),
                "drones": (Drone, "drones", "Drones no encontrados"),
                "uhub_users": (UhubUser, "uhub_users", "Usuarios Uhub no encontrados"),
                "uas_zones": (UasZone, "uas_zones", "Zonas UAS no encontradas"),
                "systems": (System, "systems", "Sistemas no encontrados"),
                "sections": (Section, "sections", "Secciones no encontradas"),
            }

            # Extraer todas las relaciones del data
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, [])

            # Usar transacción para operación atómica
            with self.session.begin_nested():
                # Crear caso base
                case = self.update_with_audit_env(
                    case, data, environment_id, modified_by
                )

                # Actualizar relaciones si se proporcionan
                for relation_key, (
                    model_class,
                    attr_name,
                    error_msg,
                ) in relations_config.items():
                    ids = extracted_relations[relation_key]
                    if ids:
                        objects = self._validate_related_objects(
                            model_class, ids, error_msg
                        )
                        setattr(case, attr_name, objects)

                self.session.flush()
                return case

        except SQLAlchemyError:
            self.session.rollback()
            raise


class StepRepository(BaseRepository[Step]):
    """Repositorio para la entidad Step."""

    def __init__(self, session: Session):
        super().__init__(session, Step)

    def _validate_related_objects(
        self, model_class, ids: list[int], error_message: str
    ) -> list:
        """Valida que los objetos relacionados existan."""
        if not ids:
            return []

        objects = self.session.query(model_class).filter(model_class.id.in_(ids)).all()
        if len(objects) != len(ids):
            missing = set(ids) - {obj.id for obj in objects}
            raise ValueError(f"{error_message}: {missing}")
        return objects

    def create(self, data: dict) -> Step:
        """Crea un paso con requisitos asociados."""

        required_fields = ["action", "expected_result", "comments", "case_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para Step")

        try:
            # Validar que el caso existe
            case = self.session.get(Case, data["case_id"])
            if not case:
                raise ValueError(f"Case con id {data['case_id']} no encontrado.")

            # Extraer requisitos antes de crear el paso
            req_ids = data.pop("requirements", [])

            # Crear el paso
            step = super().create(**data)

            # Asociar requisitos si se proporcionan
            if req_ids:
                requirements = self._validate_related_objects(
                    Requirement, req_ids, "Requisitos no encontrados"
                )
                step.requirements = requirements

            self.session.flush()
            return step

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_by_case(self, case_id: int) -> list[Step]:
        """Obtiene todos los pasos de un caso."""
        return self.query().filter(Step.case_id == case_id).all()

    def get_with_requirements(self, step_id: int) -> Step | None:
        """Obtiene un paso con sus requisitos cargados."""
        return (
            self.query()
            .options(joinedload(Step.requirements))
            .filter(Step.id == step_id)
            .one_or_none()
        )

    def update(
        self, step_id: int, data: dict, environment_id: int, modified_by: str
    ) -> UasZone:
        """Actualiza un paso con requisitos asociados."""
        try:
            step = self.get_by_id(step_id, raise_if_not_found=True)

            # Configuración de relaciones
            relations_config = {
                "requirements": (
                    Requirement,
                    "requirements",
                    "Requisitos no encontrados",
                ),
            }

            # Extraer relaciones primero
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, None)

            # Actualizar campos básicos
            step = super().update(step, **data)

            # Actualizar relaciones si se proporcionan
            for relation_key, (
                model_class,
                attr_name,
                error_msg,
            ) in relations_config.items():
                ids = extracted_relations[relation_key]
                if ids is not None:
                    objects = self._validate_related_objects(
                        model_class, ids, error_msg
                    )
                    setattr(step, attr_name, objects)

            self.session.flush()
            return step

        except SQLAlchemyError:
            self.session.rollback()
            raise
