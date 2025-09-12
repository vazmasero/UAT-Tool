from typing import Any

from application.unit_of_work import UnitOfWork, unit_of_work
from data.database.engine import Session


class ApplicationContext:
    """Contenedor de dependencias y contexto de la aplicación."""

    _instance: "ApplicationContext" = None

    def __init__(self):
        self._session_factory = Session
        self._services: dict[str, Any] = {}
        self._initialize_services()

    def _initialize_services(self):
        # Aquí se inicializan los servicios de la aplicación
        # Ejemplo: self._services['bug_service'] = BugService(self)
        pass

    def get_uow(self) -> UnitOfWork:
        """Proporciona una nueva unidad de trabajo."""
        session = self._session_factory()
        return UnitOfWork(session)

    def get_unit_of_work_context(self):
        """Proporciona el context manager de unit of work."""
        return unit_of_work()

    def get_service(self, service_name: str) -> Any:
        """Obtiene un servicio por su nombre."""
        return self._services.get(service_name)

    def register_service(self, service_name: str, service_instance: Any) -> None:
        """Registra un nuevo servicio en el contexto."""
        self._services[service_name] = service_instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ApplicationContext()
        return cls._instance
