from typing import List, Optional, Any, Dict, Callable
from PySide6.QtCore import QObject, Signal, QModelIndex, Qt
from PySide6.QtWidgets import QTableView, QHeaderView, QAbstractItemView, QMenu, QApplication
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction

from config.table_config import TableConfig, TABLES

class TableManager(QObject):
    
    # Señales para comunicación con otros componentes
    row_double_clicked = Signal(QTableView, int, list)  # tabla, fila, datos
    row_selected = Signal(QTableView, list)  # tabla, filas seleccionadas
    
    def __init__(self):
        super().__init__()
        self.tables: Dict[str, QTableView] = {}
        self.table_configs: Dict[str, Dict] = {}

    def setup_table(self, table: QTableView, name:str, data: List[List[Any]], headers: List[str], 
                   config: Optional[Dict] = None, register: bool=True):
        # Create and configure the model
        model = QStandardItemModel(0, len(headers))
        model.setHorizontalHeaderLabels(headers)
        
        # Populate with data
        self._populate_model(model, data, config)

        # Assign model to the table
        table.setModel(model)
        
        # Configure table properties
        self._configure_table_properties(table, config)

        # Configure headers
        self._configure_headers(table, config)
        
        # Register the table if required
        if register:
            self.register_table(table, name, config)
        
        
    def register_table(self, table: QTableView, name: str, config: Optional[Dict] = None):

        self.tables[name] = table
        self.table_configs[name] = config or {}
        
        table.doubleClicked.connect(
            lambda index: self._handle_double_click(table, index)
        )
    
    def _populate_model(self, model: QStandardItemModel, data: List[List[Any]], 
                       config: Optional[Dict]):
        
        for row_data in data:
            items = []
            for i, cell_data in enumerate(row_data):
                item = QStandardItem(str(cell_data) if cell_data is not None else "")
                
                # Apply specific column configuration to the item (if it exists)
                if config and 'column_config' in config:
                    col_config = config['column_config'].get(i, {})
                    self._apply_item_config(item, col_config)
                
                # Non editable and non drop enabled items by default
                item.setEditable(config.get('editable', False) if config else False)
                item.setDropEnabled(config.get('drop_enabled', False) if config else False)
                items.append(item)
            
            model.appendRow(items)
    
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
    
    def get_row_data(self, table: QTableView, row: int) -> List[Any]:

        model = table.model()
        if not model or row < 0 or row >= model.rowCount():
            return []
        
        row_data = []
        for column in range(model.columnCount()):
            index = model.index(row, column)
            data = model.data(index, Qt.ItemDataRole.DisplayRole)
            row_data.append(data)
        
        return row_data
    
    def get_selected_rows_data(self, table: QTableView) -> List[List[Any]]:

        selection_model = table.selectionModel()
        if not selection_model or not selection_model.hasSelection():
            return []
        
        selected_rows = set()
        for index in selection_model.selectedIndexes():
            selected_rows.add(index.row())
        
        return [self.get_row_data(table, row) for row in sorted(selected_rows)]
    
    def get_selected_row_indices(self, table: QTableView) -> List[int]:
        
        selection_model = table.selectionModel()
        if not selection_model or not selection_model.hasSelection():
            return []
        
        selected_rows = set()
        for index in selection_model.selectedIndexes():
            selected_rows.add(index.row())
        
        return sorted(selected_rows)
    
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
        """Maneja el evento de doble clic en una tabla."""
        if index.isValid():
            row_data = self.get_row_data(table, index.row())
            self.row_double_clicked.emit(table, index.row(), row_data)
    
    def _handle_selection_changed(self, table: QTableView):
        """Maneja el cambio de selección en una tabla."""
        selected_data = self.get_selected_rows_data(table)
        self.row_selected.emit(table, selected_data)