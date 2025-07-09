from datetime import datetime
from typing import List, Optional, Any, Dict, Callable
from PySide6.QtCore import QObject, Signal, QModelIndex, Qt
from PySide6.QtWidgets import QTableView, QHeaderView, QAbstractItemView, QMenu, QApplication
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction

from config.table_config import TABLES
from config.page_config import PAGES

class TableManager(QObject):
    
    table_double_clicked = Signal(object)
    selection_changed = Signal(object, object)
    table_updated = Signal()
        
    def __init__(self):
        super().__init__()
        self.tables: Dict[str, QTableView] = {}
        self.table_configs: Dict[str, Dict] = {}

    def setup_table(self, table: QTableView, key:str, data: List[Dict[str, Any]], 
                   config: Optional[Dict] = None, register: bool=True):
        # Obtener la configuración de la tabla desde TABLES
        table_config = TABLES.get(key, {}).get("config")
        if table_config:
            # Combinar la configuración de TABLES con la configuración adicional
            merged_config = {
                'column_map': table_config.column_map,
                **(config or {})
            }
        else:
            merged_config = config or {}

        # Create and configure the model
        headers = table_config.headers
        model = QStandardItemModel(0, len(headers))
        model.setHorizontalHeaderLabels(headers)
        
        # Populate with data
        self._populate_model(key, model, data)

        # Assign model to the table
        table.setModel(model)
        
        # Configure table properties
        self._configure_table_properties(table, merged_config)

        # Configure headers
        self._configure_headers(table, merged_config)
        
        # Register the table after model is set
        if register:
            self.register_table(table, key, merged_config)
    
    def register_table(self, table: QTableView, key: str, config: Optional[Dict] = None):
        """Registra una tabla y configura sus signals."""
        self.tables[key] = table
        self.table_configs[key] = config or {}
        
        # Conectar signals después de que el modelo está establecido
        table.doubleClicked.connect(
            lambda index: self._handle_double_click(table, index)
        )
        
        if table.selectionModel():
            table.selectionModel().selectionChanged.connect(
                lambda selected, deselected, t=table: self._handle_selection_changed(t)
                
            )
    
    def _populate_model(self, key: str, model: QStandardItemModel, data: List[Dict[str, Any]]):
        if not data:
            return

        config = TABLES.get(key, {}).get("config")
        column_map = config.column_map
        headers = [model.headerData(col, Qt.Orientation.Horizontal) for col in range(model.columnCount())]
        
        for row_data in data:
            items = []
            for col, header in enumerate(headers):
                db_column = column_map.get(header, header)
                value = row_data.get(db_column)
                items.append(self._create_item(value, config, col))
            
            if items:
                model.appendRow(items)
    
    def _create_item(self, value: Any, config: Optional[Dict], column_index: int) -> QStandardItem:

        if value is None:
            value = ""
        elif isinstance(value, datetime):
            value = value.strftime(("%Y-%m-%d %H:%M:%S"))
        
        item = QStandardItem(str(value))
        
        # Guardar el valor original como datos del item
        item.setData(value, Qt.ItemDataRole.UserRole)
        
        if config and hasattr(config, 'column_config'):
            col_config = getattr(config, 'column_config',{}).get(column_index,{})
            self._apply_item_config(item, col_config)
        
        # Non editable and non drop enabled items by default
        item.setEditable(getattr(config, 'editable', False) if config else False)
        item.setDropEnabled(getattr(config,'drop_enabled', False) if config else False)
        
        return item
    
    def _apply_item_config(self, item: QStandardItem, col_config: Dict):
        
        # Alineación
        if 'alignment' in col_config:
            item.setTextAlignment(col_config['alignment'])
        
        # Color de fondo
        if 'background_color' in col_config:
            item.setBackground(col_config['background_color'])
        
        # Color de texto
        if 'text_color' in col_config:
            item.setForeground(col_config['text_color'])
        
        # Tooltip
        if 'tooltip' in col_config:
            item.setToolTip(col_config['tooltip'])
    
    def _configure_table_properties(self, table: QTableView, config: Optional[Dict]):
        """Configura las propiedades básicas de la tabla."""
        default_config = {
            'selection_behavior': QAbstractItemView.SelectionBehavior.SelectRows,
            'selection_mode': QAbstractItemView.SelectionMode.ExtendedSelection,
            'scroll_mode': QAbstractItemView.ScrollMode.ScrollPerItem,
            'edit_triggers': QAbstractItemView.EditTrigger.NoEditTriggers,
            'alternating_row_colors': False,
            'sort_enabled': True
        }
        
        # Fusionar configuración por defecto con la proporcionada
        final_config = {**default_config, **(config or {})}
        
        # Aplicar configuración
        table.setSelectionBehavior(final_config['selection_behavior'])
        table.setSelectionMode(final_config['selection_mode'])
        table.setVerticalScrollMode(final_config['scroll_mode'])
        table.setEditTriggers(final_config['edit_triggers'])
        table.setAlternatingRowColors(final_config['alternating_row_colors'])
        table.setSortingEnabled(final_config['sort_enabled'])
    
    def _configure_headers(self, table: QTableView, config: Optional[Dict]):
        """Configures table headers."""
        horizontal_header = table.horizontalHeader()
        
        # Configuración horizontal por defecto
        horizontal_header.setStretchLastSection(True)
        horizontal_header.setMaximumSectionSize(
            config.get('max_section_size', 300) if config else 300
        )
        
        # Modo de redimensionamiento
        resize_mode = QHeaderView.ResizeMode.ResizeToContents
        if config and 'resize_mode' in config:
            resize_mode = config['resize_mode']
        horizontal_header.setSectionResizeMode(resize_mode)
        
        # Configurar anchos específicos de columna si se proporcionan
        if config and 'column_widths' in config:
            for i, width in enumerate(config['column_widths']):
                if i < horizontal_header.count() and width > 0:
                    horizontal_header.setSectionResizeMode(
                        i, QHeaderView.ResizeMode.Fixed
                    )
                    horizontal_header.resizeSection(i, width)
    
    def get_row_data(self, table: QTableView, row: int) -> Dict[str, Any]:
        """Obtiene los datos de una fila como un diccionario usando los nombres de columna de la BD."""
        model = table.model()
        if not model or row < 0 or row >= model.rowCount():
            return {}
        
        # Buscar la tabla en la configuración para obtener el mapeo
        table_key = next((k for k, v in self.tables.items() if v == table), None)
        if not table_key:
            return {}
            
        # Obtener el mapeo de columnas
        config = self.table_configs.get(table_key, {})
        column_map = config.get('column_map', {})
        
        row_data = {}
        for column in range(model.columnCount()):
            index = model.index(row, column)
            header = model.headerData(column, Qt.Orientation.Horizontal)
            
            # Usar el mapeo para obtener el nombre de la columna en la BD
            db_column = column_map.get(header, header)
            
            # Obtener el valor original
            value = model.data(index, Qt.ItemDataRole.UserRole)
            if value is None:
                value = model.data(index, Qt.ItemDataRole.DisplayRole)
                
            row_data[db_column] = value
        
        return row_data
    
    def get_selected_rows_data(self, table: QTableView) -> List[List[Any]]:

        selection_model = table.selectionModel()
        if not selection_model or not selection_model.hasSelection():
            return []
        
        selected_rows = set()
        for index in selection_model.selectedIndexes():
            selected_rows.add(index.row())
        
        return [self.get_row_data(table, row) for row in sorted(selected_rows)]
    
    def add_row(self, table: QTableView, row_data: List[Any], position: Optional[int] = None):

        model = table.model()
        if not model:
            return
        
        items = [QStandardItem(str(data) if data is not None else "") for data in row_data]
        for item in items:
            item.setEditable(False)
        
        if position is None:
            model.appendRow(items)
        else:
            model.insertRow(position, items)
    
    def remove_selected_rows(self, table: QTableView) -> bool:

        selected_rows = self.get_selected_row_indices(table)
        if not selected_rows:
            return False
        
        model = table.model()
        if not model:
            return False
        
        # Eliminar de mayor a menor índice para evitar problemas de reindexación
        for row in reversed(selected_rows):
            model.removeRow(row)
        
        return True
    
    def update_row(self, table: QTableView, row: int, row_data: List[Any]) -> bool:

        model = table.model()
        if not model or row < 0 or row >= model.rowCount():
            return False
        
        for column, data in enumerate(row_data):
            if column < model.columnCount():
                index = model.index(row, column)
                model.setData(index, str(data) if data is not None else "")
        
        return True
    
    def filter_table(self, table: QTableView, column: int, text: str):

        # Nota: Para filtrado más avanzado, considerar usar QSortFilterProxyModel
        model = table.model()
        if not model:
            return
        
        for row in range(model.rowCount()):
            index = model.index(row, column)
            cell_data = model.data(index, Qt.ItemDataRole.DisplayRole) or ""
            should_hide = text.lower() not in cell_data.lower() if text else False
            table.setRowHidden(row, should_hide)
    
    def clear_table(self, table: QTableView):
        """Limpia todos los datos de la tabla."""
        model = table.model()
        if model:
            model.clear()
    
    def _handle_double_click(self, table: QTableView, index: QModelIndex):
        """Handles the double click on a table item event."""
        if index.isValid():
            row_data = self.get_row_data(table, index.row())  
            self.table_double_clicked.emit(row_data)
        else:
            return
            
    def _handle_selection_changed(self, table: QTableView):
        """Hndles the selection change on a table event."""
        selected_data = self.get_selected_rows_data(table)
        self.selection_changed.emit(table, selected_data)
    
    def update_table_model(self, table_key: str, data: list):
        table_widget = self.tables.get(table_key)
        if not table_widget:
            return
        model = table_widget.model()
        if model:
            model.removeRows(0, model.rowCount())
            self._populate_model(table_key, model, data)
        self.table_updated.emit()
    
    def get_current_table(self, page_key: str, tab_index:int=None)->Optional[QTableView]:
        page_config = PAGES.get(page_key, {}).get("config")
        if not page_config or not page_config.tables:
            return None
        tables = page_config.tables
        if tab_index is not None and 0 <= tab_index < len(tables):
            table_key = tables[tab_index]
        else:
            table_key = tables[0]
        return self.tables.get(table_key)