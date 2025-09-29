from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.models import Bug, BugHistory, CampaignRun, File, System

from .base import AuditEnvironmentMixinRepository


class BugRepository(AuditEnvironmentMixinRepository[Bug]):
    """Repositorio específico para la entidad Bug."""

    def __init__(self, session: Session):
        super().__init__(session, Bug)

    def create(self, data: dict, environment_id: int, modified_by: str) -> Bug:
        """Crea un nuevo Bug con relaciones opcionales (campaign_run, file) y obligatoria (system_id).
        También inicializa un registro en BugHistory."""

        if not data.get("system_id"):
            raise ValueError(
                "Un Bug debe estar asociado a un sistema (system_id requerido)."
            )
        try:
            # Validar FK
            system = self.session.get(System, data["system_id"])
            if not system:
                raise ValueError(f"System con id {data['system_id']} no encontrado.")

            campaign_run_id = data.get("campaign_run_id")
            if campaign_run_id:
                campaign_run = self.session.query(CampaignRun).get(campaign_run_id)
                if not campaign_run:
                    raise ValueError(
                        f"CampaignRun con id {campaign_run_id} no encontrado."
                    )
            else:
                campaign_run = None

            file_id = data.get("file_id")
            if file_id:
                file = self.session.get(File, file_id)
                if not file:
                    raise ValueError(f"File con id {file_id} no encontrado.")
            else:
                file = None

            # Crear el bug usando el método base
            bug_data = {
                **data,
                "system_id": system.id,
                "campaign_run_id": campaign_run.id if campaign_run else None,
                "file_id": file.id if file else None,
            }

            bug = self.create_with_audit_env(bug_data, environment_id, modified_by)

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

            if "file_id" in data:
                file_id = data["file_id"]
                if file_id:
                    file = self.session.get(File, file_id)
                    if not file:
                        raise ValueError(f"File con id {file_id} no encontrado.")
                # Si file_id es None, se permite (puede ser desasociado)

            # Guardar estado anterior para el historial si es relevante
            old_status = bug.status if "status" in data else None

            # Actualizar el bug usando el método base
            bug = self.update_with_audit_env(bug, data, modified_by, environment_id)

            # Registrar en el historial
            history_message = change_summary
            if old_status and "status" in data and data["status"] != old_status:
                history_message += f" (Estado cambiado: {old_status}->{data['status']})"

            self.add_history(bug_id, modified_by, history_message)

            return bug

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
