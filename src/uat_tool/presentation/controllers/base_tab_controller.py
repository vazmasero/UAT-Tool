from typing import Any

from PySide6.QtCore import QObject, Signal

from uat_tool.application import ApplicationContext
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class BaseTabController(QObject):
    """Controlador base para todas las pestañas de tabla CRUD."""

    # Señales comunes para todas las pestañas
    data_loaded = Signal(list)  # Emite lista de items
    item_created = Signal(object)  # Emite item creado
    item_updated = Signal(object)  # Emite item actualizado
    item_deleted = Signal(int)  # Emite id del item eliminado
    error_occurred = Signal(str)
    loading_state_changed = Signal(bool)

    def __init__(self, app_context: ApplicationContext, tab_name: str):
        super().__init__()
        self.app_context = app_context
        self.tab_name = tab_name
        self._is_active = False
        self._current_data = []

    def get_all_items(self) -> list[Any]:
        """Obtiene todos los items de la tabla."""
        raise NotImplementedError

    def create_item(self, item_data: dict) -> Any:
        """Crea un nuevo item."""
        raise NotImplementedError

    def update_item(self, item_id: int, item_data: dict) -> Any:
        """Actualiza un item existente."""
        raise NotImplementedError

    def delete_item(self, item_id: int) -> bool:
        """Elimina un item."""
        raise NotImplementedError

    def get_item_by_id(self, item_id: int) -> Any | None:
        """Obtiene un item por su ID."""
        raise NotImplementedError

    # Métodos comunes
    def activate(self):
        """Se ejecuta cuando la pestaña se activa."""
        self._is_active = True
        logger.info(f"Pestaña {self.tab_name} activada")
        self.load_data()

    def deactivate(self):
        """Se ejecuta cuando la pestaña se desactiva."""
        self._is_active = False
        logger.info(f"Pestaña {self.tab_name} desactivada")

    def refresh_data(self):
        """Recarga los datos de la pestaña."""
        if self._is_active:
            logger.info(f"Recargando datos de {self.tab_name}")
            self.load_data()

    def load_data(self):
        """Carga los datos de la tabla."""
        try:
            self.loading_state_changed.emit(True)
            items = self.get_all_items()
            self._current_data = items
            self.data_loaded.emit(items)
            logger.info(f"Datos cargados para {self.tab_name}: {len(items)} items")
        except Exception as e:
            logger.error(f"Error cargando datos de {self.tab_name}: {e}")
            self.error_occurred.emit(f"Error cargando datos: {str(e)}")
        finally:
            self.loading_state_changed.emit(False)

    def handle_create_item(self, item_data: dict):
        """Maneja la creación de un nuevo item."""
        try:
            new_item = self.create_item(item_data)
            self.item_created.emit(new_item)
            logger.info(f"Item creado en {self.tab_name}: {new_item.id}")
            # Recargar datos para reflejar cambios
            self.load_data()
        except Exception as e:
            logger.error(f"Error creando item en {self.tab_name}: {e}")
            self.error_occurred.emit(f"Error creando item: {str(e)}")

    def handle_update_item(self, item_id: int, item_data: dict):
        """Maneja la actualización de un item."""
        try:
            updated_item = self.update_item(item_id, item_data)
            self.item_updated.emit(updated_item)
            logger.info(f"Item actualizado en {self.tab_name}: {item_id}")
            # Recargar datos para reflejar cambios
            self.load_data()
        except Exception as e:
            logger.error(f"Error actualizando item en {self.tab_name}: {e}")
            self.error_occurred.emit(f"Error actualizando item: {str(e)}")

    def handle_delete_item(self, item_id: int):
        """Maneja la eliminación de un item."""
        try:
            success = self.delete_item(item_id)
            if success:
                self.item_deleted.emit(item_id)
                logger.info(f"Item eliminado de {self.tab_name}: {item_id}")
                # Recargar datos para reflejar cambios
                self.load_data()
            else:
                self.error_occurred.emit(f"No se pudo eliminar el item {item_id}")
        except Exception as e:
            logger.error(f"Error eliminando item de {self.tab_name}: {e}")
            self.error_occurred.emit(f"Error eliminando item: {str(e)}")

    def get_current_data(self) -> list[Any]:
        """Obtiene los datos actualmente cargados."""
        return self._current_data.copy()

    def shutdown(self):
        """Cierra el controlador y libera recursos."""
        logger.info(f"Cerrando controlador de {self.tab_name}")
        self._current_data.clear()
