from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.models import Bug, BugHistory, CampaignRun, File, System

from .base import AuditEnvironmentMixinRepository, BaseRepository


class BugRepository(BaseRepository[Bug], AuditEnvironmentMixinRepository[Bug]):
    """Repositorio específico para la entidad Bug."""

    def __init__(self, session: Session):
        super().__init__(session, Bug)

    def create_with_relations(self, data: dict) -> Bug:
        """Crea un nuevo Bug con relaciones opcionales (campaign_run, file) y obligatoria (system_id).
        También inicializa un registro en BugHistory."""

        self._validate_audit_environment_data(data)

        if not data.get("system_id"):
            raise ValueError(
                "Un Bug debe estar asociado a un sistema (system_id requerido)."
            )
        try:
            # Validar FK
            system = self.session.query(System).get(data["system_id"])
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
                file = self.session.query(File).get(file_id)
                if not file:
                    raise ValueError(f"File con id {file_id} no encontrado.")
            else:
                file = None

            # Crear el bug usando el método base
            bug_data = {
                "status": data["status"],
                "system_id": system.id,
                "campaign_run_id": campaign_run.id if campaign_run else None,
                "system_version": data["system_version"],
                "service_now_id": data.get("service_now_id"),
                "short_description": data["short_description"],
                "definition": data["definition"],
                "urgency": data["urgency"],
                "impact": data["impact"],
                "comments": data.get("comments"),
                "file_id": file.id if file else None,
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],
            }

            bug = self.create(**bug_data)

            # Crear registro en el historial
            history = BugHistory(
                bug_id=bug.id,
                changed_by=data.get("changed_by", "system"),
                change_summary="Bug creado",
            )

            self.session.add(history)
            self.session.flush()

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
            self.query(Bug)
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
