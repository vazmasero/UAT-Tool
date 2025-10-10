from uat_tool.application import (
    ApplicationContext,
)
from uat_tool.application.dto import (
    RequirementServiceDTO,
    RequirementTableDTO,
)
from uat_tool.application.dto.requirement_dto import RequirementFormDTO
from uat_tool.application.services.base_service import BaseService
from uat_tool.domain import Requirement
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class RequirementService(BaseService):
    """Servicio para manejar la lógica de negocio de Requisitos."""

    def __init__(self, app_context: ApplicationContext):
        super().__init__(app_context)

    # --- MÉTODOS BÁSICOS (para la lógica de negocio y otros servicios) ---

    def get_all_requirements(self) -> list[Requirement]:
        """Obtiene todos los requisitos como objetos SQLAlchemy (para lógica de negocio)."""
        self._log_operation("get_all", "Requirement")
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.req_repo.get_all_with_relations()

    def get_all_requirements_service_dto(self) -> list[RequirementServiceDTO]:
        """Obtiene todos los requisitos como DTOs."""
        self._log_operation("get_all", "Requirement")
        with self.app_context.get_unit_of_work_context() as uow:
            requirements_model = uow.req_repo.get_all_with_relations()
            # Convertir a DTOs DENTRO del contexto de sesión
            return [RequirementServiceDTO.from_model(req) for req in requirements_model]

    def get_requirement_by_id(self, requirement_id: int) -> Requirement | None:
        """Obtiene un requisito como objeto SQLAlchemy (para edición)."""
        self._log_operation("get_by_id", "Requirement", requirement_id)
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.req_repo.get_with_relations(requirement_id)

    def get_requirement_dto_by_id(
        self, requirement_id: int
    ) -> RequirementServiceDTO | None:
        """Obtiene un requisito como ServiceDTO."""
        self._log_operation("get_by_id", "Requirement", requirement_id)
        with self.app_context.get_unit_of_work_context() as uow:
            requirement = uow.req_repo.get_with_relations(requirement_id)
            return (
                RequirementServiceDTO.from_model(requirement) if requirement else None
            )

    # --- MÉTODOS ENRIQUECIDOS (específicos para UI) ---

    def get_all_requirements_for_table(self) -> list[RequirementTableDTO]:
        """Obtiene todos los requisitos enriquecidos para mostrar en la tabla UI."""
        self._log_operation("get_all_for_table", "Requirement")

        with self.app_context.get_unit_of_work_context() as uow:
            requirements = uow.req_repo.get_all_with_relations()
            return [self._enrich_requirement_for_table(req) for req in requirements]

    def _enrich_requirement_for_table(
        self, requirement: Requirement
    ) -> RequirementTableDTO:
        """Enriquece un Requirement directamente con sus relaciones cargadas."""
        try:
            # Extraer nombres directamente de las relaciones ya cargadas
            system_names = [system.name for system in requirement.systems]
            section_names = [section.name for section in requirement.sections]

            # Crear ServiceDTO desde el modelo
            service_dto = RequirementServiceDTO.from_model(requirement)

            return RequirementTableDTO.from_service_dto(
                service_dto=service_dto,
                system_names=system_names,
                section_names=section_names,
            )

        except Exception as e:
            logger.error(
                f"Error enriqueciendo requisito {requirement.id} para tabla: {e}"
            )
            # Fallback básico - crear TableDTO directamente sin ServiceDTO
            system_names = [
                system.name for system in getattr(requirement, "systems", [])
            ]
            section_names = [
                section.name for section in getattr(requirement, "sections", [])
            ]

            systems_display = ", ".join(system_names) if system_names else "N/A"
            sections_display = ", ".join(section_names) if section_names else "N/A"

            return RequirementTableDTO(
                id=getattr(requirement, "id", 0),
                code=getattr(requirement, "code", "N/A"),
                definition=getattr(requirement, "definition", "N/A"),
                systems=systems_display,
                sections=sections_display,
                created_at=RequirementTableDTO._format_date(
                    getattr(requirement, "created_at", None)
                ),
                updated_at=RequirementTableDTO._format_date(
                    getattr(requirement, "updated_at", None)
                ),
                modified_by=getattr(requirement, "modified_by", "Unknown"),
            )

    # --- MÉTODOS CRUD ---

    def create_requirement_from_form(
        self, form_dto: RequirementFormDTO, context: dict
    ) -> RequirementServiceDTO:
        """Crea un nuevo requisito desde FormDTO."""
        self._log_operation("create", "Requirement")

        # 1. FormDTO -> ServiceDTO
        service_dto = form_dto.to_service_dto(context)

        # 2. ServiceDTO -> Repositorio
        with self.app_context.get_unit_of_work_context() as uow:
            created_requirement = uow.req_repo.create(
                data=service_dto.to_dict(),
                environment_id=service_dto.environment_id,
                modified_by=service_dto.modified_by,
            )

            # Recargar con relaciones para respuesta completa
            requirement_with_relations = uow.req_repo.get_with_relations(
                created_requirement.id
            )
            return RequirementServiceDTO.from_model(requirement_with_relations)

    def update_requirement_from_form(
        self, requirement_id: int, form_dto: RequirementFormDTO, context: dict
    ) -> RequirementServiceDTO:
        """Actualiza un requisito desde FormDTO."""
        self._log_operation("update", "Requirement", requirement_id)

        # 1. FormDTO → ServiceDTO
        service_dto = form_dto.to_service_dto(context)

        # 2. ServiceDTO → Repositorio (con todas las relaciones incluidas)
        with self.app_context.get_unit_of_work_context() as uow:
            updated_requirement = uow.req_repo.update(
                requirement_id=requirement_id,
                data=service_dto.to_dict(),  # ← Usar el diccionario del ServiceDTO
                environment_id=service_dto.environment_id,
                modified_by=service_dto.modified_by,
            )

            # Recargar con relaciones para respuesta completa
            requirement_with_relations = uow.req_repo.get_with_relations(
                updated_requirement.id
            )
            return RequirementServiceDTO.from_model(requirement_with_relations)

    def get_requirement_for_edit(
        self, requirement_id: int
    ) -> RequirementFormDTO | None:
        """Obtiene un requisito como FormDTO para edición."""
        service_dto = self.get_requirement_dto_by_id(requirement_id)
        if service_dto:
            return RequirementFormDTO.from_service_dto(service_dto)
        return None

    def delete_requirement(self, requirement_id: int) -> bool:
        """Elimina un requisito."""
        self._log_operation("delete", "Requirement", requirement_id)

        with self.app_context.get_unit_of_work_context() as uow:
            success = uow.req_repo.delete(requirement_id)
            return success
