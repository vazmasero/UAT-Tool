from typing import Any

from uat_tool.infrastructure import get_engine, get_session_factory, init_db
from uat_tool.shared import get_logger

from .uow import UnitOfWork, unit_of_work

logger = get_logger(__name__)


class ApplicationContext:
    """Contenedor de dependencias y contexto de la aplicación."""

    _instance: "ApplicationContext" = None

    def __init__(
        self, test_mode: bool = False, test_engine=None, load_initial_data: bool = True
    ):
        self._test_mode = test_mode
        self._load_initial_data = load_initial_data

        self._engine = test_engine or get_engine()

        self._session_factory = get_session_factory(self._engine, scoped=not test_mode)

        self._services: dict[str, Any] = {}
        self._is_initialized = False

    def initialize(self):
        """Inicializa el contexto de la aplicación."""
        if self._is_initialized:
            logger.warning("ApplicationContext ya está inicializado")
            return

        try:
            logger.info("Inicializando ApplicationContext...")

            self._initialize_database()
            self._initialize_services()

            self._is_initialized = True
            logger.info("ApplicationContext inicializado correctamente")

        except Exception as e:
            logger.error("Error inicializando ApplicationContext: %s", e)
            raise

    def _initialize_database(self):
        """Inicializa la base de datos (para tests o entorno real)."""
        try:
            logger.info("Inicializando base de datos...")
            init_db(
                drop_existing=self._test_mode,
                engine=self._engine,
                load_initial_data=self._load_initial_data,
            )
            logger.info("Base de datos inicializada correctamente")
        except Exception as e:
            logger.error("Error inicializando base de datos: %s", e)
            raise

    def _initialize_services(self):
        """Inicializa los servicios de la aplicación."""
        from uat_tool.application.services import (  # pylint: disable=import-outside-toplevel
            AuxiliaryService,
            BugService,
            RequirementService,
        )

        try:
            logger.info("Inicializando servicios...")

            bug_service = BugService(self)
            self.register_service("bug_service", bug_service)
            requirement_service = RequirementService(self)
            self.register_service("requirement_service", requirement_service)
            auxiliary_service = AuxiliaryService(self)
            self.register_service("auxiliary_service", auxiliary_service)

            # Inicializar otros servicios

            logger.info("Servicios inicializados correctamente")

        except Exception as e:
            logger.error("Error inicializando servicios: %s", e)
            raise

    def get_uow(self) -> UnitOfWork:
        """Proporciona una nueva unidad de trabajo."""
        session = self._session_factory()
        return UnitOfWork(session)

    def get_unit_of_work_context(self):
        """Proporciona el context manager de unit of work."""
        return unit_of_work()

    def get_service(self, service_name: str) -> Any:
        """Obtiene un servicio por su nombre."""
        if not self._is_initialized:
            raise RuntimeError("ApplicationContext no está inicializado")
        return self._services.get(service_name)

    def register_service(self, service_name: str, service_instance: Any) -> None:
        """Registra un nuevo servicio en el contexto."""
        self._services[service_name] = service_instance

    def is_initialized(self) -> bool:
        """Verifica si el contexto está inicializado."""
        return self._is_initialized

    def shutdown(self):
        """Cierra el contexto y libera recursos."""
        logger.info("Cerrando ApplicationContext...")

        errors = []

        for name, service in list(self._services.items()):
            if hasattr(service, "shutdown"):
                try:
                    service.shutdown()
                except Exception as e:
                    errors.append("%s: %s", name, e)
                    logger.error("Error cerrando servicio %s: %s", name, e)

        self._services.clear()
        self._is_initialized = False

        if errors:
            logger.error("Error(es) cerrando ApplicationContext: %s", ", ".join(errors))
        else:
            logger.info("ApplicationContext cerrado correctamente")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ApplicationContext()
        return cls._instance
