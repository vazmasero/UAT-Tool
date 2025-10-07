from uat_tool.application import (
    ApplicationContext,
)
from uat_tool.application.dto import BugServiceDTO, BugTableDTO
from uat_tool.application.services.base_service import BaseService
from uat_tool.domain import Bug
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class BugService(BaseService):
    """Servicio para manejar la lógica de negocio de Bugs."""

    def __init__(self, app_context: ApplicationContext):
        super().__init__(app_context)

    # --- MÉTODOS BÁSICOS (para la lógica de negocio y otros servicios) ---

    def get_all_bugs(self) -> list[Bug]:
        """Obtiene todos los bugs como objetos SQLAlchemy (para lógica de negocio)."""
        self._log_operation("get_all", "Bug")
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.bug_repo.get_all()

    def get_all_bugs_service_dto(self) -> list[BugServiceDTO]:
        """Obtiene todos los bugs como DTOs."""
        self._log_operation("get_all", "Bug")
        with self.app_context.get_unit_of_work_context() as uow:
            bugs_model = uow.bug_repo.get_all()
            # Convertir a DTOs DENTRO del contexto de sesión
            return [BugServiceDTO.from_model(bug) for bug in bugs_model]

    def get_bug_by_id(self, bug_id: int) -> Bug | None:
        """Obtiene un bug como objeto SQLAlchemy (para edición)."""
        self._log_operation("get_by_id", "Bug", bug_id)
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.bug_repo.get_by_id(bug_id)

    def get_bug_dto_by_id(self, bug_id: int) -> BugServiceDTO | None:
        """Obtiene un bug como ServiceDTO."""
        self._log_operation("get_by_id", "Bug", bug_id)
        with self.app_context.get_unit_of_work_context() as uow:
            bug = uow.bug_repo.get_by_id(bug_id)
            return BugServiceDTO.from_model(bug) if bug else None

    # --- MÉTODOS ENRIQUECIDOS (específicos para UI) ---

    def get_all_bugs_for_table(self) -> list[BugTableDTO]:
        """Obtiene todos los bugs enriquecidos para mostrar en la tabla UI."""
        self._log_operation("get_all_for_table", "Bug")

        # Obtener ServiceDTOs primero (dentro de su propia sesión)
        bugs_service_dto = self.get_all_bugs_service_dto()

        # Luego enriquecer (esto abre nuevas sesiones para cada entidad relacionada)
        return [self._enrich_bug_for_table(bug_dto) for bug_dto in bugs_service_dto]

    def _enrich_bug_for_table(self, bug_dto: BugServiceDTO) -> BugTableDTO:
        """Enriquece un BugServiceDTO con datos para la tabla UI."""
        try:
            # Usar métodos heredados de BaseService para enriquecimiento
            system_name = self._get_system_name(bug_dto.system_id)
            requirement_codes = [
                self._get_requirement_code(req_id) for req_id in bug_dto.requirements
            ]
            file_name = self._get_file_name(bug_dto.file_id)

            return BugTableDTO.from_service_dto(
                bug_dto=bug_dto,
                system_name=system_name,
                requirement_codes=requirement_codes,
                file_name=file_name,
            )
        except Exception as e:
            logger.error(f"Error enriqueciendo bug {bug_dto.id} para tabla: {e}")
            # Devolver un DTO básico en caso de error
            return BugTableDTO.from_service_dto(bug_dto)

    # --- MÉTODOS CRUD ---

    def create_bug(self, bug_data: dict) -> BugServiceDTO:
        """Crea un nuevo bug y devuelve ServiceDTO."""
        self._log_operation("create", "Bug")

        # Validar campos requeridos
        required_fields = [
            "status",
            "system_id",
            "system_version",
            "short_description",
            "definition",
        ]

        missing_fields = self._validate_required_fields(bug_data, required_fields)
        if missing_fields:
            raise ValueError(f"Campos requeridos faltantes: {missing_fields}")

        with self.app_context.get_unit_of_work_context() as uow:
            bug = Bug(**bug_data)
            created_bug = uow.bug_repo.create(bug)
            uow.commit()
            return BugServiceDTO.from_model(created_bug)

    def update_bug(self, bug_id: int, bug_data: dict) -> BugServiceDTO | None:
        """Actualiza un bug y devuelve ServiceDTO."""
        self._log_operation("update", "Bug", bug_id)

        with self.app_context.get_unit_of_work_context() as uow:
            existing_bug = uow.bug_repo.get_by_id(bug_id)
            if not existing_bug:
                return None

            # Actualizar solo campos permitidos (excluir id)
            for key, value in bug_data.items():
                if hasattr(existing_bug, key) and key != "id":
                    setattr(existing_bug, key, value)

            updated_bug = uow.bug_repo.update(bug_id, existing_bug)
            uow.commit()
            return BugServiceDTO.from_model(updated_bug) if updated_bug else None

    def delete_bug(self, bug_id: int) -> bool:
        """Elimina un bug."""
        self._log_operation("delete", "Bug", bug_id)

        with self.app_context.get_unit_of_work_context() as uow:
            success = uow.bug_repo.delete(bug_id)
            if success:
                uow.commit()
            return success

    # --- MÉTODOS ESPECÍFICOS DE BUGS ---

    def get_bugs_by_status(self, status: str) -> list[Bug]:
        """Obtiene bugs por estado."""
        self._log_operation("get_by_status", "Bug")
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.bug_repo.get_bugs_by_status(status)

    def get_bugs_by_status_for_table(self, status: str) -> list[BugTableDTO]:
        """Obtiene bugs por estado enriquecidos para tabla UI."""
        bugs = self.get_bugs_by_status(status)
        bugs_service_dto = [BugServiceDTO.from_model(bug) for bug in bugs]
        return [self._enrich_bug_for_table(bug_dto) for bug_dto in bugs_service_dto]
