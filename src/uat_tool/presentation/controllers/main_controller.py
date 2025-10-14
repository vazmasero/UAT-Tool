from typing import Any

from PySide6.QtCore import QObject, Signal

from uat_tool.application.app_context import ApplicationContext
from uat_tool.presentation.controllers.base_tab_controller import BaseTabController
from uat_tool.presentation.controllers.bug_tab_controller import BugTabController
from uat_tool.presentation.controllers.requirement_tab_controller import (
    RequirementTabController,
)
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class MainController(QObject):
    """Controlador principal que coordina todos los controladores de pestañas."""

    # Señales
    tab_changed = Signal(str)
    application_ready = Signal()
    application_error = Signal(str)
    ui_state_changed = Signal(dict)

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
        self._has_selection = False

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
            self._tab_controllers["requirements"] = RequirementTabController(
                self.app_context
            )

            # Por ahora mantener el resto como controladores básicos, luego los implementaremos
            from .base_tab_controller import BaseTabController

            for tab_id in self.TAB_CONFIG.keys():
                if tab_id != "bugs" and tab_id != "requirements":
                    controller = BaseTabController(self.app_context, tab_id)
                    self._tab_controllers[tab_id] = controller

            # Conectar señales de error para todos
            for tab_id, controller in self._tab_controllers.items():
                controller.error_occurred.connect(
                    lambda error, tab=tab_id: self._on_tab_error(tab, error)
                )
                # Conectar señal de cambio de selección
                if hasattr(controller, "selection_state_changed"):
                    controller.selection_state_changed.connect(
                        lambda state, tab=tab_id: self._on_tab_selection_changed(
                            tab, state
                        )
                    )

            self._is_initialized = True

            logger.info(
                f"Controladores de pestañas inicializados: {list(self._tab_controllers.keys())}"
            )

            # Activar la pestaña por defecto (Bugs)
            self.switch_to_tab("bugs")

        except Exception as e:
            logger.error(f"Error inicializando controladores de pestañas: {e}")
            # TO DO: que la vista reciba correctamente este emit
            # self.application_error.emit(f"Error inicializando pestañas: {str(e)}")

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

            # Actualizar estado de selección basado en la nueva pestaña
            self._update_selection_state()

            # Actualizar estado de UI
            self._update_ui_state()

            logger.info(f"Cambiado a pestaña: {tab_name}")
            self.tab_changed.emit(tab_name)

        except Exception as e:
            logger.error(f"Error cambiando a pestaña {tab_name}: {e}")
            self.application_error.emit(f"Error cambiando de pestaña: {str(e)}")

    def _update_selection_state(self):
        """Actualiza el estado de selección basado en la pestaña actual."""
        if self._current_tab and self._current_tab in self._tab_controllers:
            controller = self._tab_controllers[self._current_tab]
            if hasattr(controller, "get_selected_item_id"):
                selected_id = controller.get_selected_item_id()
                self._has_selection = selected_id is not None
            else:
                self._has_selection = False
        else:
            self._has_selection = False

    def _update_ui_state(self):
        """Actualiza el estado de los botones según la pestaña actual y selección."""
        ui_state = {
            "btn_start_visible": self._current_tab == "campaigns",
            "btn_add_enabled": True,
            "btn_edit_enabled": self._has_selection,
            "btn_remove_enabled": self._has_selection,
        }
        self.ui_state_changed.emit(ui_state)

    def _on_tab_selection_changed(self, tab_name: str, has_selection: bool):
        """Maneja cambios de selección en los controladores hijos."""
        # Solo nos interesa si es la pestaña actual
        if tab_name == self._current_tab:
            self._has_selection = has_selection
            self._update_ui_state()

    def set_selection_state(self, has_selection: bool):
        """Actualiza el estado de selección (para compatibilidad con llamadas directas)."""
        self._has_selection = has_selection
        self._update_ui_state()

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

    def on_tab_changed(self, index: int):
        """Maneja el cambio de pestaña desde la vista.

        Args:
            index (int): Índice de la pestaña seleccionada devuelto por la
            señal de stacked widget.
        """
        tab_mapping = {
            0: "bugs",
            1: "campaigns",
            2: "test_management",
            3: "requirements",
            4: "assets",
        }
        tab_name = tab_mapping.get(index)
        if tab_name and tab_name != self._current_tab:
            self.switch_to_tab(tab_name)

    def on_add_clicked(self):
        """Delega la acción 'Add' al controlador de la pestaña actual."""
        controller = self.get_current_tab_controller()
        if controller and hasattr(controller, "handle_new_register"):
            controller.handle_new_register()
        else:
            logger.warning(
                f"Controlador {type(controller)} no tiene el método 'handle_new_register'"
            )
            self.application_error.emit("Acción no disponible en esta pestaña")

    def on_edit_clicked(self):
        """Delega la acción 'Edit' al controlador de la pestaña actual."""
        if not self._has_selection:
            self.application_error.emit("No hay ningún elemento seleccionado")
            return

        controller = self.get_current_tab_controller()
        if controller and hasattr(controller, "handle_edit_register"):
            controller.handle_edit_register()
        else:
            logger.warning(
                f"Controlador {type(controller)} no tiene el método 'handle_edit_register'"
            )
            self.application_error.emit("Edición no disponible en esta pestaña")

    def on_remove_clicked(self):
        """Delega la acción 'Remove' al controlador de la pestaña actual."""
        if not self._has_selection:
            self.application_error.emit("No hay ningún elemento seleccionado")
            return

        controller = self.get_current_tab_controller()
        if controller and hasattr(controller, "handle_remove_register"):
            controller.handle_remove_register()
        else:
            logger.warning(
                f"Controlador {type(controller)} no tiene el método 'handle_remove_register'"
            )
            self.application_error.emit("Eliminación no disponible en esta pestaña")

    def on_start_clicked(self):
        """Solo para campañas - delega al controlador de campaigns"""
        if self._current_tab == "campaigns":
            controller = self.get_current_tab_controller()
            if controller and hasattr(controller, "handle_start"):
                controller.handle_start()
            else:
                logger.warning(
                    f"Controlador {type(controller)} no tiene el método 'handle_start'"
                )
                self.application_error.emit("Inicio no disponible en esta pestaña")
        else:
            logger.warning("Tab actual no es 'campaigns', no se puede iniciar")
            self.application_error.emit(
                "La acción 'Iniciar' solo está disponible en Campañas"
            )
