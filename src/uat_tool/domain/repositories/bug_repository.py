from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from uat_tool.domain import (
    Bug,
    BugHistory,
    CampaignRun,
    Requirement,
    System,
)
from uat_tool.shared import get_logger

from .base import AuditEnvironmentMixinRepository

logger = get_logger(__name__)


class BugRepository(AuditEnvironmentMixinRepository[Bug]):
    """Repositorio específico para la entidad Bug."""

    def __init__(self, session: Session):
        super().__init__(session, Bug)

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

    def create(self, data: dict, environment_id: int, modified_by: str) -> Bug:
        """Crea un nuevo Bug con relaciones opcionales (campaign_run) y obligatoria (system_id).
        También inicializa un registro en BugHistory."""

        if not data.get("system_id"):
            raise ValueError(
                "Un Bug debe estar asociado a un sistema (system_id requerido)."
            )
        try:
            # Configuración de relaciones
            relations_config = {
                "requirements": (
                    Requirement,
                    "requirements",
                    "Requisitos no encontrados",
                )
            }

            # Extraer relaciones antes de crear la instancia
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, [])

            # Validar FK
            system = self.session.get(System, data["system_id"])
            if not system:
                raise ValueError(f"System con id {data['system_id']} no encontrado.")

            campaign_run_id = data.get("campaign_run_id")
            if campaign_run_id:
                campaign_run = self.session.get(CampaignRun, campaign_run_id)
                if not campaign_run:
                    raise ValueError(
                        f"CampaignRun con id {campaign_run_id} no encontrado."
                    )
            else:
                campaign_run = None

            # Crear el bug usando el método base
            bug_data = {
                **data,
                "system_id": system.id,
                "campaign_run_id": campaign_run.id if campaign_run else None,
            }

            bug = self.create_with_audit_env(bug_data, environment_id, modified_by)

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
                    setattr(bug, attr_name, objects)

            # Crear registro en el historial
            self.add_history(bug.id, modified_by, "Bug creado")

            return bug

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def update(
        self,
        bug_id: int,
        data: dict,
        environment_id: int,
        modified_by: str,
        change_summary: str = "Bug actualizado",
    ) -> Bug:
        """Actualiza un bug existente y registra el cambio en el historial."""
        try:
            bug = self.get_by_id(bug_id, raise_if_not_found=True)

            # Configuración de relaciones
            relations_config = {
                "requirements": (
                    Requirement,
                    "requirements",
                    "Requisitos no encontrados",
                )
            }

            # Extraer relaciones antes de crear la instancia
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, [])

            # Extraer historial
            data.pop("history", [])

            # Validar FK si se proporcionan
            if "system_id" in data:
                system = self.session.get(System, data["system_id"])
                if not system:
                    raise ValueError(
                        f"System con id {data['system_id']} no encontrado."
                    )

            if "campaign_run_id" in data:
                campaign_run_id = data["campaign_run_id"]
                if campaign_run_id:
                    campaign_run = self.session.query(CampaignRun).get(campaign_run_id)
                    if not campaign_run:
                        raise ValueError(
                            f"CampaignRun con id {campaign_run_id} no encontrado."
                        )
                # Si campaign_run_id es None, se permite (puede ser desasociado)

            # Guardar estado anterior para el historial si es relevante
            old_status = bug.status if "status" in data else None

            # Actualizar el bug usando el método base
            bug = self.update_with_audit_env(bug, data, modified_by, environment_id)

            # Relaciones many to many
            for relation_key, (
                model_class,
                attr_name,
                error_msg,
            ) in relations_config.items():
                ids = extracted_relations[relation_key]
                # Si se proporciona la relación, actualizarla
                if (
                    ids is not None
                ):  # Importante: permite lista vacía para eliminar todos
                    objects = self._validate_related_objects(
                        model_class, ids, error_msg
                    )
                    setattr(bug, attr_name, objects)

            # Registrar en el historial
            history_message = change_summary
            if old_status and "status" in data and data["status"] != old_status:
                history_message += f" (Estado cambiado: {old_status}->{data['status']})"

            self.add_history(bug_id, modified_by, history_message)

            return bug

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def delete(self, bug_id: int) -> bool:
        """Elimina un bug y su historial relacionado."""
        try:
            bug = self.get_by_id(bug_id)
            if not bug:
                return False

            # Eliminar historial primero
            for history in bug.history:
                self.session.delete(history)

            # Eliminar el bug
            self.session.delete(bug)
            self.session.flush()

            return True

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def add_history(
        self, bug_id: int, changed_by: str, change_summary: str
    ) -> BugHistory:
        """Agrega una entrada al historial de un bug existente."""
        try:
            bug = self.get_by_id(bug_id)
            if not bug:
                raise ValueError(f"Bug con id {bug_id} no encontrado.")

            history = BugHistory(
                bug_id=bug_id,
                changed_by=changed_by,
                change_summary=change_summary,
            )
            self.session.add(history)
            self.session.flush()
            return history
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_with_history(self, bug_id: int) -> Bug | None:
        """Devuelve un bug junto con su historial cargado."""
        return (
            self.session.query(Bug)
            .options(joinedload(Bug.history))
            .filter(Bug.id == bug_id)
            .one_or_none()
        )

    def update_status(
        self, bug_id: int, new_status: str, changed_by: str, change_summary: str
    ) -> Bug:
        """Actualiza el estado de un bug y registra el cambio en el historial."""
        bug = self.get_by_id(bug_id, raise_if_not_found=True)

        old_status = bug.status
        bug.status = new_status

        # Registrar en el historial
        self.add_history(
            bug_id=bug_id,
            changed_by=changed_by,
            change_summary=f"{change_summary} (Estado cambiado: {old_status}->{new_status})",
        )

        self.session.flush()
        return bug

    def get_bugs_by_system(self, system_id: int, environment_id: int) -> list[Bug]:
        """Obtiene todos los bugs asociados a un sistema específico."""
        return (
            self.query()
            .filter(Bug.system_id == system_id, Bug.environment_id == environment_id)
            .all()
        )

    def get_bugs_by_status(self, status: str, environment_id: int) -> list[Bug]:
        """Obtiene todos los bugs con un estado específico."""
        return (
            self.query()
            .filter(Bug.status == status, Bug.environment_id == environment_id)
            .all()
        )

    def get_by_service_now_id(
        self, service_now_id: str, environment_id: int
    ) -> Bug | None:
        """Busca un bug por Service Now ID y environment_id."""
        return (
            self.query()
            .filter(
                Bug.service_now_id == service_now_id,
                Bug.environment_id == environment_id,
            )
            .first()
        )

    def get_with_relations(self, bug_id: int) -> Bug | None:
        """Obtiene un bug con sus relaciones cargadas."""
        return (
            self.query()
            .options(
                joinedload(Bug.system),
                joinedload(Bug.campaign_run),
                joinedload(Bug.requirements),
                joinedload(Bug.history),
            )
            .filter(Bug.id == bug_id)
            .first()
        )

    def get_all_with_relations(self) -> list[Bug]:
        """Obtiene todos los bugs con sus relaciones cargadas."""
        return (
            self.query()
            .options(
                joinedload(Bug.system),
                joinedload(Bug.campaign_run),
                joinedload(Bug.requirements),
                joinedload(Bug.history),
            )
            .all()
        )
