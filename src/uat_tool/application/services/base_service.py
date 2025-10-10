"""
Servicio base con funcionalidad común para todos los servicios.
Proporiona métodos de enriquecimiento, formato y helpers reutilizables.
"""

from uat_tool.application import ApplicationContext
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class BaseService:
    """Servicio base con métodos comunes para todas las entidades."""

    def __init__(self, app_context: ApplicationContext):
        self.app_context = app_context

    # --- MÉTODOS DE ENRIQUECIMIENTO (obtener parámetros concretos por IDs) ---

    def _get_system_name(self, system_id: int) -> str:
        """Obtiene el nombre del sistema por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                system = uow.sys_repo.get_by_id(system_id)
                return system.name if system else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre del sistema {system_id}: {e}")
            return "Error"

    def _get_section_name(self, section_id: int) -> str:
        """Obtiene el nombre de la sección por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                section = uow.section_repo.get_by_id(section_id)
                return section.name if section else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre de la sección {section_id}: {e}")
            return "Error"

    def _get_reason_name(self, reason_id: int) -> str:
        """Obtiene el nombre de la razón de una zona UAS por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                reason = uow.reason_repo.get_by_id(reason_id)
                return reason.name if reason else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre de la razón {reason_id}: {e}")
            return "Error"

    def _get_requirement_code(self, requirement_id: int) -> str:
        """Obtiene el código de un requisito por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                requirement = uow.req_repo.get_by_id(requirement_id)
                return requirement.code if requirement else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo código de requisito {requirement_id}: {e}")
            return ["Error"]

    def _get_file_name(self, file_id: int) -> str:
        """Obtiene el nombre del archivo por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                file_record = uow.file_repo.get_by_id(file_id)
                return file_record.filename if file_record else "File not found"
        except Exception as e:
            logger.error(f"Error obteniendo nombre de archivo {file_id}: {e}")
            return "Error"

    def _get_file_path(self, file_id: int) -> str:
        """Obtiene la ruta del archivo por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                file_record = uow.file_repo.get_by_id(file_id)
                return file_record.filepath if file_record else "File not found"
        except Exception as e:
            logger.error(f"Error obteniendo ruta de archivo {file_id}: {e}")
            return "Error"

    def _get_operator_name(self, operator_id: int) -> str:
        """Obtiene el nombre del operador por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                operator = uow.ope_repo.get_by_id(operator_id)
                return operator.name if operator else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre del operador {operator_id}: {e}")
            return "Error"

    def _get_organization_name(self, organization_id: int) -> str:
        """Obtiene el nombre de la organización por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                organization = uow.org_repo.get_by_id(organization_id)
                return organization.name if organization else "Unknown"
        except Exception as e:
            logger.error(
                f"Error obteniendo nombre de la organización {organization_id}: {e}"
            )
            return "Error"

    def _get_email_email(self, email_id: int) -> str:
        """Obtiene el campo email de un email por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                email = uow.email_repo.get_by_id(email_id)
                return email.email if email else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo email de {email_id}: {e}")
            return "Error"

    def _get_drone_serial_number(self, drone_id: int) -> str:
        """Obtiene el número de serie de un dron por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                drone = uow.drone_repo.get_by_id(drone_id)
                return drone.serial_number if drone else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo número de serie de {drone_id}: {e}")
            return "Error"

    def _get_uas_zone_name(self, uas_zone_id: int) -> str:
        """Obtiene el nombre de una zona UAS por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                uas_zone = uow.zone_repo.get_by_id(uas_zone_id)
                return uas_zone.name if uas_zone else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre de zona UAS de {uas_zone_id}: {e}")
            return "Error"

    def _get_uhub_user_username(self, uhub_user_id: int) -> str:
        """Obtiene el nombre de usuario de un usuario de uHub por su ID."""

        try:
            with self.app_context.get_unit_of_work_context() as uow:
                user = uow.user_repo.get_by_id(uhub_user_id)
                return user.username if user else "Unknown"
        except Exception as e:
            logger.error(f"Error obteniendo nombre de usuario de {uhub_user_id}: {e}")
            return "Error"

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
