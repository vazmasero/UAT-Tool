from typing import Any

from PySide6.QtCore import QObject, Signal

from uat_tool.application.app_context import ApplicationContext
from uat_tool.presentation.controllers.base_tab_controller import BaseTabController
from uat_tool.presentation.controllers.bug_tab_controller import BugTabController
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class MainController(QObject):
    """Controlador principal que coordina todos los controladores de pestañas."""

    # Señales
    tab_changed = Signal(str)
    application_ready = Signal()
    application_error = Signal(str)

    # Configuración de pestañas
    TAB_CONFIG = {
        "bugs": {
            "name": "Bugs",
            "model": "Bug",
            "controller_class": "BugTabController",
        },
        "campaigns": {
            "name": "Campaigns",
            "model": "Campaign",
            "controller_class": "CampaignTabController",
        },
        "test_management": {
            "name": "Test Management",
            "model": "Case",  # Configurar más modelos
            "controller_class": "TestManagementTabController",
        },
        "requirements": {
            "name": "Requirements",
            "model": "Requirement",
            "controller_class": "RequirementTabController",
        },
        "assets": {
            "name": "Assets",
            "model": "Email",  # Configurar más modelos
            "controller_class": "AssetsTabController",
        },
    }

    def __init__(self, app_context: ApplicationContext):
        super().__init__()
        self.app_context = app_context
        self._current_tab: str | None = None
        self._tab_controllers: dict[str, BaseTabController] = {}
        self._is_initialized = False

    def initialize(self):
        """Inicializa el controlador principal."""
        try:
            logger.info("Inicializando controlador principal...")

            # Inicializar controladores
            self._initialize_tab_controllers()

        except Exception as e:
            logger.error(f"Error inicializando controlador principal: {e}")
            self.application_error.emit(f"Error de inicialización: {str(e)}")
            raise

    def _initialize_tab_controllers(self):
        """Inicializa todos los controladores de pestañas."""
        try:
            logger.info("Inicializando controladores de pestañas...")

            # Inicializar controladores específicos
            self._tab_controllers["bugs"] = BugTabController(self.app_context)

            # Por ahora mantener el resto como controladores básicos, luego los implementaremos
            from presentation.controllers.base_tab_controller import BaseTabController

            for tab_id in self.TAB_CONFIG.keys():
                if tab_id != "bugs":
                    controller = BaseTabController(self.app_context, tab_id)
                    self._tab_controllers[tab_id] = controller

            # Conectar señales de error para todos
            for tab_id, controller in self._tab_controllers.items():
                controller.error_occurred.connect(
                    lambda error, tab=tab_id: self._on_tab_error(tab, error)
                )

            self._is_initialized = True
            self.application_ready.emit()

            logger.info(
                f"Controladores de pestañas inicializados: {list(self._tab_controllers.keys())}"
            )

            # Activar la pestaña por defecto (Bugs)
            self.switch_to_tab("bugs")

        except Exception as e:
            logger.error(f"Error inicializando controladores de pestañas: {e}")
            self.application_error.emit(f"Error inicializando pestañas: {str(e)}")

    def switch_to_tab(self, tab_name: str):
        """Cambia a la pestaña especificada."""
        if not self._is_initialized:
            logger.warning(
                "Controlador no inicializado, no se puede cambiar de pestaña"
            )
            return

        if tab_name not in self._tab_controllers:
            logger.error(f"Pestaña no encontrada: {tab_name}")
            self.application_error.emit(f"Pestaña no encontrada: {tab_name}")
            return

        try:
            # Desactivar pestaña actual si existe
            if self._current_tab and self._current_tab in self._tab_controllers:
                current_controller = self._tab_controllers[self._current_tab]
                current_controller.deactivate()

            # Activar nueva pestaña
            self._current_tab = tab_name
            new_controller = self._tab_controllers[tab_name]
            new_controller.activate()

            self.tab_changed.emit(tab_name)
            logger.info(f"Cambiado a pestaña: {tab_name}")

        except Exception as e:
            logger.error(f"Error cambiando a pestaña {tab_name}: {e}")
            self.application_error.emit(f"Error cambiando de pestaña: {str(e)}")

    def get_tab_controller(self, tab_name: str) -> BaseTabController | None:
        """Obtiene el controlador de una pestaña específica."""
        return self._tab_controllers.get(tab_name)

    def get_current_tab_controller(self) -> BaseTabController | None:
        """Obtiene el controlador de la pestaña actual."""
        return (
            self._tab_controllers.get(self._current_tab) if self._current_tab else None
        )

    def get_available_tabs(self) -> dict[str, str]:
        """Obtiene el diccionario de pestañas disponibles."""
        return {tab_id: config["name"] for tab_id, config in self.TAB_CONFIG.items()}

    def get_tab_config(self, tab_name: str) -> dict[str, Any]:
        """Obtiene la configuración de una pestaña específica."""
        return self.TAB_CONFIG.get(tab_name, {})

    def _on_tab_error(self, tab_name: str, error: str):
        """Maneja errores de controladores hijos."""
        tab_name_display = self.TAB_CONFIG.get(tab_name, {}).get("name", tab_name)
        logger.error(f"Error en pestaña {tab_name}: {error}")
        self.application_error.emit(f"Error en {tab_name_display}: {error}")

    def refresh_current_tab(self):
        """Recarga los datos de la pestaña actual."""
        if self._current_tab and self._current_tab in self._tab_controllers:
            controller = self._tab_controllers[self._current_tab]
            controller.refresh_data()

    def shutdown(self):
        """Cierra todos los controladores y libera recursos."""
        try:
            logger.info("Cerrando controlador principal...")

            # Cerrar todos los controladores de pestañas
            for _, controller in self._tab_controllers.items():
                controller.shutdown()

            self._tab_controllers.clear()
            self._is_initialized = False

            logger.info("Controlador principal cerrado correctamente")

        except Exception as e:
            logger.error(f"Error cerrando controlador principal: {e}")
