"""
Servicio base con funcionalidad común para todos los servicios.
Proporiona métodos de enriquecimiento, formato y helpers reutilizables.
"""

from datetime import datetime

from uat_tool.application import ApplicationContext
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class BaseService:
    """Servicio base con métodos comunes para todas las entidades."""

    def __init__(self, app_context: ApplicationContext):
        self.app_context = app_context

    # --- MÉTODOS DE ENRIQUECIMIENTO (obtener nombres por IDs) ---

    def _get_system_name(self, system_id: int | None) -> str:
        """Obtiene el nombre del sistema por su ID."""
        if not system_id:
            return "N/A"

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                system = uow.sys_repo.get_by_id(system_id)
                return system.name if system else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre del sistema {system_id}: {e}")
            return "Error"

    def _get_requirement_code(self, requirement_id: int | None) -> str:
        """Obtiene el código de un requisito por su ID."""
        if not requirement_id:
            return "N/A"

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                requirement = uow.req_repo.get_by_id(requirement_id)
                return requirement.code if requirement else "Unknown"
        except Exception as e:
            logger.error(
                f"Error obteniendo código de requisito {requirement_id}: {e}"
            )
            return ["Error"]

    def _get_file_name(self, file_id: int | None) -> str:
        """Obtiene el nombre del archivo por su ID."""
        if not file_id:
            return "No file attached"

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                file_record = uow.file_repo.get_by_id(file_id)
                return file_record.filename if file_record else "File not found"
        except Exception as e:
            logger.error(f"Error obteniendo nombre de archivo {file_id}: {e}")
            return "Error"

    # --- MÉTODOS DE FORMATEO (para UI) ---
    def _format_date(self, date_value: datetime | None) -> str:
        """Formatea una fecha para mostrarla en la UI."""
        if not date_value:
            return "N/A"
        return date_value.strftime("%d/%m/%Y %H:%M")

    def _format_date_short(self, date_value: datetime | None) -> str:
        """Formatea una fecha en formato corto para la UI."""
        if not date_value:
            return "N/A"
        return date_value.strftime("%d/%m/%Y")

    # --- MÉTODOS DE FORMATEO (para UI) ---
    def _validate_id_exists(self, entity_type: str, entity_id: int) -> bool:
        """Valida que un ID exista en la base de datos."""
        try:
            with self.app_context.get_unit_of_work_context() as uow:
                repo = getattr(uow, f"{entity_type.lower()}_repo")
                entity = repo.get_by_id(entity_id)
                return entity is not None
        except Exception as e:
            logger.error(f"Error validando {entity_type} ID {entity_id}: {e}")
            return False

    def _validate_required_fields(
        self, data: dict, required_fields: list[str]
    ) -> list[str]:
        """Valida que los campos requeridos estén presentes."""
        missing_fields = []
        for field in required_fields:
            if field not in data or data[field] in (None, "", 0):
                missing_fields.append(field)
        return missing_fields

    # --- MÉTODOS DE LOGGING Y ERRORES ---

    def _log_operation(
        self, operation: str, entity_type: str, entity_id: int | None = None
    ):
        """Log común para operaciones de servicio."""
        entity_info = (
            f" {entity_type} ID {entity_id}" if entity_id else f" {entity_type}s"
        )
        logger.info(f"Operación '{operation}' en{entity_info}")

    def _handle_service_error(
        self, operation: str, entity_type: str, error: Exception
    ) -> None:
        """Manejo común de errores en servicios."""
        logger.error(f"Error en {operation} de {entity_type}: {error}")
        # Puede lanzar una excepción específica del dominio si es necesario
        raise error
