from datetime import datetime
from typing import List, Optional, Any, Dict
from PySide6.QtCore import QObject, Signal, QModelIndex, Qt, QSortFilterProxyModel
from PySide6.QtWidgets import QTableView, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItem, QStandardItemModel

from config.table_config import TABLES
from config.page_config import PAGES

from services.table_service import TableService

from utils.dict_utils import get_base_table_config

class TableManager(QObject):
    
    table_double_clicked = Signal(str,object)
    selection_changed = Signal(object)
    table_updated = Signal()
        
    def __init__(self):
        super().__init__()
        self.tables: Dict[str, QTableView] = {}
        self.table_configs: Dict[str, Dict] = {}

    def setup_table(self, table: QTableView, name: str, data: List[Dict[str, Any]], config: Optional[Dict] = None, register=False):
        
        """Creates and associates models to a particular TableView object. If needed, the table is registered when created."""
        
        merged_config = TableService.merge_table_config(name, config)

        # Provisional: determine the model according to name provided
        headers = merged_config.get("headers", [])
        model = QStandardItemModel(0, len(headers))
        model.setHorizontalHeaderLabels(headers)
        self._populate_model(name, model, data)
            
        # Setup proxy model for filtering and sorting
        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(model)
        table.setModel(proxy_model)
        
        headers = merged_config.get("headers", [])
        for i, header in enumerate(headers):
            proxy_model.setHeaderData(i, Qt.Horizontal, header)
            
        # Hide ID if there is a column named "Id" or "ID"
        for i, header in enumerate(headers):
            if header.lower() in ['id']:
                table.setColumnHidden(i, True)
                break
            
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(merged_config.get("alternating_row_colors", False))
        # table.setSortingEnabled(merged_config.get("sort_enabled", False))
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        if register:
            self._register_table(table, name, config)
    
    def _populate_model(self, name: str, model: QStandardItemModel, data: List[Dict[str, Any]]):
        
        """Populates the model associated to a table with the elements obtained from the database"""
        
        if not data:
            return

        config = get_base_table_config(name)
        column_map = config.column_map
        headers = [model.headerData(col, Qt.Orientation.Horizontal) for col in range(model.columnCount())]
        
        for row_data in data:
            items = []
            for col, header in enumerate(headers):
                db_column = column_map.get(header, header)
                value = row_data.get(db_column)
                item = self._create_item(value, config, col)
                
                # Save DB Id in the first column as UserRole
                if col == 0: 
                    item.setData(row_data.get('id'), Qt.ItemDataRole.UserRole +1)
                
                items.append(item)
            
            if items:
                model.appendRow(items)
    
    def _create_item(self, value: Any, config: Optional[Dict], column_index: int) -> QStandardItem:
        """Creates a new item for a certain mode"""
        
        if value is None:
            value = ""
        elif isinstance(value, datetime):
            # Converts a datetime object to a string so it can be displayed on the table
            value = value.strftime(("%Y-%m-%d %H:%M:%S"))
        
        item = QStandardItem(str(value))
        
        # Saves the original value as item data
        item.setData(value, Qt.ItemDataRole.UserRole)
        
        if config and hasattr(config, 'column_config'):
            col_config = getattr(config, 'column_config',{}).get(column_index,{})
            self._apply_item_config(item, col_config)
        
        # Non editable and non drop enabled items by default
        item.setEditable(getattr(config, 'editable', False) if config else False)
        item.setDropEnabled(getattr(config,'drop_enabled', False) if config else False)
        
        return item
    
    def _register_table(self, table: QTableView, name: str, config: Optional[Dict] = None) -> bool:
        """Registers a table and sets up its signals."""
        if name in self.tables:
            raise ValueError(f"The table named '{name} is already registered")
        
        self.tables[name] = table
        self.table_configs[name] = config or {}
        
        # Connect signals after the model is established
        table.doubleClicked.connect(
            lambda index: self._handle_double_click(name, table, index)
        )
        
        if table.selectionModel():
            table.selectionModel().selectionChanged.connect(
                lambda selected, deselected: self._handle_selection_changed(name)
                
            )
        
        # Table registered successfully
        return True
    
    def _apply_item_config(self, item: QStandardItem, col_config: Dict):
        
        if 'alignment' in col_config:
            item.setTextAlignment(col_config['alignment'])
        
        if 'background_color' in col_config:
            item.setBackground(col_config['background_color'])
        
        if 'text_color' in col_config:
            item.setForeground(col_config['text_color'])
        
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
    
    def get_row_data(self, name: str, table: QTableView, row: int) -> Dict[str, Any]:
        """Obtains data from a row as a dictionary using the DB column names."""
        model = table.model()
        if not model or row < 0 or row >= model.rowCount():
            return {}
            
        # Obtener el mapeo de columnas
        config = self.table_configs.get(name, {})
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
    
    def get_selected_rows_data(self, name: str) -> Optional[dict]:

        table = self.tables.get(name)
        if not table:
            return None
        
        selection_model = table.selectionModel()
        proxy_indices = selection_model.selectedRows()
        if not proxy_indices:
            return None
        
        proxy_index = proxy_indices[0]
        
        record_id = self.get_selected_record_id(name)
        if not record_id:
            return None
        
        row_data = self.get_row_data(name, table, proxy_index.row())
        
        row_data['id'] = record_id
        
        return row_data
    
    def get_selected_record_id(self, table_name:str) -> Optional[int]:
        
        table = self.tables.get(table_name)
        if not table or not table.selectionModel().hasSelection():
            return None
        
        selection_model = table.selectionModel()
        proxy_indices = selection_model.selectedRows()
        if not proxy_indices:
            return None
        
        # Obtain selected index in proxy model
        proxy_index = proxy_indices[0]
        
        # Map to index source if there is proxy model
        if hasattr(table.model(), 'mapToSource'):
            source_index = table.model().mapToSource(proxy_index)
            source_model = table.model().sourceModel()
            # Obtain Id stored in first colum
            first_item = source_model.item(source_index.row(), 0)
            if first_item:
                return first_item.data(Qt.ItemDataRole.UserRole + 1)
            
        else:
            #If there is no proxy model, user model directly
            first_item = table.model().item(proxy_index.row(), 0)
            if first_item:
                return first_item.data(Qt.ItemDataRole.UserRole + 1)
            
        return None
    
    def get_selected_row_indices(self, table:QTableView) -> List[int]:
        if not table or not table.selectionModel():
            return[]
        
        indices = table.selectionModel.selectedRows()
        return [index.row() for index in indices]
    
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
    
    def _handle_double_click(self, name: str, table:QTableView, index: QModelIndex):
        """Handles the double click on a table item event."""
        if index.isValid():
            row_data = self.get_row_data(name, table, index.row())  
            self.table_double_clicked.emit(name,row_data)
        else:
            return
            
    def _handle_selection_changed(self, name : str):
        """Handles the selection change on a table event."""
        table = self.tables[name]
        self.selection_changed.emit(table)
    
    def update_table_model(self, table_name: str, new_data: list):
        table_widget = self.tables.get(table_name)
        if not table_widget:
            print(f"Table '{table_name}' not found in registered tables")
            return
        
        model = table_widget.model()
        source_model = model
        
        if hasattr(model, 'sourceModel'):
            source_model = model.sourceModel()
        
        source_model.clear()
        
        config = get_base_table_config(table_name)
        headers = config.headers if hasattr(config, 'headers') else []
        if headers:
            source_model.setHorizontalHeaderLabels(headers)
        
        self._populate_model(table_name, source_model, new_data)
        
        for i, header in enumerate(headers):
            if header.lower() in ['id']:
                table_widget.setColumnHidden(i, True)
                break
        
        print(f"Table model '{table_name}' updated with {len(new_data)} records")
    
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