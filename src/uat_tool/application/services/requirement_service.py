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
            requirements_dto = [
                RequirementServiceDTO.from_model(req) for req in requirements
            ]
        return [self._enrich_requirement_for_table(req) for req in requirements_dto]

    def _enrich_requirement_for_table(
        self, requirement_dto: RequirementServiceDTO
    ) -> RequirementTableDTO:
        """Enriquece un Requirement directamente con sus relaciones cargadas."""
        try:
            system_names = requirement_dto.system_names
            section_names = requirement_dto.section_names

            if not system_names and requirement_dto.systems:
                system_names = [
                    self._get_system_name(sys_id) for sys_id in requirement_dto.systems
                ]
            if not section_names and requirement_dto.sections:
                section_names = [
                    self._get_section_name(section_id)
                    for section_id in requirement_dto.sections
                ]

            return RequirementTableDTO.from_service_dto(
                service_dto=requirement_dto,
                system_names=system_names,
                section_names=section_names,
            )

        except Exception as e:
            logger.error(
                f"Error enriqueciendo requisito {requirement_dto.id} para tabla: {e}"
            )
            return RequirementTableDTO.from_service_dto(requirement_dto)

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
