import sys
from pathlib import Path

from uat_tool.application.dto import FileServiceDTO, SectionServiceDTO, SystemServiceDTO
from uat_tool.application.services.base_service import BaseService
from uat_tool.domain import Section, System
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class AuxiliaryService(BaseService):
    """Servicio para manejar la lógica de negocio de modelos auxiliares."""

    # --- MÉTODOS BÁSICOS (para la lógica de negocio y otros servicios) ---

    def get_all_systems(self) -> list[System]:
        """Obtiene todos los sistemas como objetos SQLAlchemy (para lógica de negocio)."""
        self._log_operation("get_all", "System")
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.sys_repo.get_all()

    def get_all_systems_service_dto(self) -> list[SystemServiceDTO]:
        """Obtiene todos los sistemas como DTOs."""
        self._log_operation("get_all", "System")
        with self.app_context.get_unit_of_work_context() as uow:
            systems_model = uow.sys_repo.get_all()
            # Convertir a DTOs DENTRO del contexto de sesión
            return [SystemServiceDTO.from_model(sys) for sys in systems_model]

    def get_system_by_id(self, system_id: int) -> System | None:
        """Obtiene un sistema como objeto SQLAlchemy (para edición)."""
        self._log_operation("get_by_id", "System", system_id)
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.sys_repo.get_by_id(system_id)

    def get_system_dto_by_id(self, system_id: int) -> SystemServiceDTO | None:
        """Obtiene un sistema como ServiceDTO."""
        self._log_operation("get_by_id", "System", system_id)
        with self.app_context.get_unit_of_work_context() as uow:
            system = uow.sys_repo.get_by_id(system_id)
            return SystemServiceDTO.from_model(system) if system else None

    # --- Sections (similar a Systems) ---

    def get_all_sections(self) -> list[Section]:
        """Obtiene todos los sistemas como objetos SQLAlchemy (para lógica de negocio)."""
        self._log_operation("get_all", "Section")
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.section_repo.get_all()

    def get_all_sections_service_dto(self) -> list[SectionServiceDTO]:
        """Obtiene todos los sistemas como DTOs."""
        self._log_operation("get_all", "Section")
        with self.app_context.get_unit_of_work_context() as uow:
            sections_model = uow.section_repo.get_all()
            # Convertir a DTOs DENTRO del contexto de sesión
            return [SectionServiceDTO.from_model(sec) for sec in sections_model]

    def get_section_by_id(self, section_id: int) -> Section | None:
        """Obtiene una sección como objeto SQLAlchemy (para edición)."""
        self._log_operation("get_by_id", "Section", section_id)
        with self.app_context.get_unit_of_work_context() as uow:
            return uow.section_repo.get_by_id(section_id)

    def get_section_dto_by_id(self, section_id: int) -> SectionServiceDTO | None:
        """Obtiene una sección como ServiceDTO."""
        self._log_operation("get_by_id", "Section", section_id)
        with self.app_context.get_unit_of_work_context() as uow:
            section = uow.section_repo.get_by_id(section_id)
            return SectionServiceDTO.from_model(section) if section else None

    # --- Files ---

    def create_files_for_bug(
        self, file_dtos: list[FileServiceDTO], bug_id: int
    ) -> list[FileServiceDTO]:
        """Crea múltiples archivos asociados a un bug."""
        try:
            logger.info("Creando %i archivos para bug %i", len(file_dtos), bug_id)

            created_files = []
            with self.app_context.get_unit_of_work_context() as uow:
                for file_dto in file_dtos:
                    try:
                        # Crear archivo en la base de datos
                        file_data = {
                            "owner_type": "bug",
                            "owner_id": bug_id,
                            "filename": file_dto.filename,
                            "filepath": file_dto.filepath,
                            "mime_type": file_dto.mime_type,
                            "size": file_dto.size,
                            "uploaded_by": file_dto.uploaded_by,
                        }

                        created_file = uow.file_repo.create(**file_data)

                        # Convertir a DTO
                        file_dto_created = FileServiceDTO.from_model(created_file)
                        created_files.append(file_dto_created)

                        logger.info(
                            "Archivo creado: %s (ID: %i)",
                            file_dto.filename,
                            created_file.id,
                        )

                    except Exception as file_error:
                        logger.error(
                            "Error creando archivo %s: %s",
                            file_dto.filename,
                            file_error,
                        )
                        raise OSError(
                            f"Error creando archivo {file_dto.filename}"
                        ) from file_error

            return created_files

        except Exception as e:
            logger.error("Error creando archivos en BD para bug %i: %s", bug_id, e)
            raise

    def get_files_by_bug_id(self, bug_id: int) -> list[FileServiceDTO]:
        """Obtiene todos los archivos asociados a un bug."""
        try:
            with self.app_context.get_unit_of_work_context() as uow:
                files = uow.file_repo.get_by_owner("bug", bug_id)
                return [FileServiceDTO.from_model(file) for file in files]

        except Exception as e:
            logger.error("Error obteniendo archivos para bug %i: %s", bug_id, e)
            return []

    # Métodos de archivos
    def get_app_root(self) -> Path:
        """Obtiene la ruta raíz de la aplicación."""
        # Si está empaquetado con PyInstaller
        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent
        return Path(__file__).parent.parent.parent  # Ajustar según la estructura final
