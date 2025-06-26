# managers/table_manager.py
from typing import List, Optional, Any, Dict, Callable
from PySide6.QtCore import QObject, Signal, QModelIndex, Qt
from PySide6.QtWidgets import QTableView, QHeaderView, QAbstractItemView, QMenu, QApplication
from PySide6.QtGui import QStandardItem, QStandardItemModel, QAction

class TableManager(QObject):
    """Gestor centralizado para el manejo de tablas en la aplicación."""
    
    # Señales para comunicación con otros componentes
    row_double_clicked = Signal(QTableView, int, list)  # tabla, fila, datos
    row_selected = Signal(QTableView, list)  # tabla, filas seleccionadas
    context_menu_requested = Signal(QTableView, int, object)  # tabla, fila, posición
    
    def __init__(self):
        super().__init__()
        self.tables: Dict[str, QTableView] = {}
        self.table_configs: Dict[str, Dict] = {}
        
    def register_table(self, table: QTableView, name: str, config: Optional[Dict] = None):
        """
        Registra una tabla en el gestor.
        
        Args:
            table: La tabla a registrar
            name: Nombre único para identificar la tabla
            config: Configuración opcional de la tabla
        """
        self.tables[name] = table
        self.table_configs[name] = config or {}
        
        # Conectar señales básicas
        table.doubleClicked.connect(
            lambda index: self._handle_double_click(table, index)
        )
        table.selectionModel().selectionChanged.connect(
            lambda: self._handle_selection_changed(table)
        )
        
        # Configurar menú contextual si está habilitado
        if config and config.get('context_menu', False):
            table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            table.customContextMenuRequested.connect(
                lambda pos: self._show_context_menu(table, pos)
            )
    
    def setup_table(self, table: QTableView, data: List[List[Any]], headers: List[str], 
                   config: Optional[Dict] = None):
        """
        Configura una tabla con datos y headers.
        
        Args:
            table: La tabla a configurar
            data: Datos para poblar la tabla
            headers: Lista de nombres de columnas
            config: Configuración adicional de la tabla
        """
        # Crear y configurar el modelo
        model = QStandardItemModel()
        model.setColumnCount(len(headers))
        model.setHorizontalHeaderLabels(headers)
        
        # Poblar con datos
        self._populate_model(model, data, config)
        
        # Asignar modelo a la tabla
        table.setModel(model)
        
        # Configurar propiedades de la tabla
        self._configure_table_properties(table, config)
        
        # Configurar headers
        self._configure_headers(table, config)
    
    def _populate_model(self, model: QStandardItemModel, data: List[List[Any]], 
                       config: Optional[Dict]):
        """Puebla el modelo con los datos proporcionados."""
        for row_data in data:
            items = []
            for i, cell_data in enumerate(row_data):
                item = QStandardItem(str(cell_data) if cell_data is not None else "")
                
                # Aplicar configuración específica de columna si existe
                if config and 'column_config' in config:
                    col_config = config['column_config'].get(i, {})
                    self._apply_item_config(item, col_config)
                
                # Por defecto, hacer items no editables
                item.setEditable(config.get('editable', False) if config else False)
                items.append(item)
            
            model.appendRow(items)
    
    def _apply_item_config(self, item: QStandardItem, col_config: Dict):
        """Aplica configuración específica a un item de celda."""
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
            'alternating_row_colors': True,
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
        """Configura los headers de la tabla."""
        horizontal_header = table.horizontalHeader()
        vertical_header = table.verticalHeader()
        
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
        
        # Ocultar header vertical si se especifica
        if config and config.get('hide_vertical_header', False):
            vertical_header.setVisible(False)
    
    def get_row_data(self, table: QTableView, row: int) -> List[Any]:
        """
        Obtiene los datos de una fila específica.
        
        Args:
            table: La tabla de la cual obtener los datos
            row: Índice de la fila
            
        Returns:
            Lista con los datos de la fila
        """
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
        """
        Obtiene los datos de todas las filas seleccionadas.
        
        Args:
            table: La tabla de la cual obtener los datos
            
        Returns:
            Lista de listas con los datos de las filas seleccionadas
        """
        selection_model = table.selectionModel()
        if not selection_model.hasSelection():
            return []
        
        selected_rows = set()
        for index in selection_model.selectedIndexes():
            selected_rows.add(index.row())
        
        return [self.get_row_data(table, row) for row in sorted(selected_rows)]
    
    def get_selected_row_indices(self, table: QTableView) -> List[int]:
        """Obtiene los índices de las filas seleccionadas."""
        selection_model = table.selectionModel()
        if not selection_model.hasSelection():
            return []
        
        selected_rows = set()
        for index in selection_model.selectedIndexes():
            selected_rows.add(index.row())
        
        return sorted(selected_rows)
    
    def add_row(self, table: QTableView, row_data: List[Any], position: Optional[int] = None):
        """
        Añade una nueva fila a la tabla.
        
        Args:
            table: La tabla donde añadir la fila
            row_data: Datos de la nueva fila
            position: Posición donde insertar (None = al final)
        """
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
        """
        Elimina las filas seleccionadas.
        
        Args:
            table: La tabla de la cual eliminar filas
            
        Returns:
            True si se eliminaron filas, False en caso contrario
        """
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
        """
        Actualiza los datos de una fila específica.
        
        Args:
            table: La tabla a actualizar
            row: Índice de la fila
            row_data: Nuevos datos para la fila
            
        Returns:
            True si se actualizó correctamente, False en caso contrario
        """
        model = table.model()
        if not model or row < 0 or row >= model.rowCount():
            return False
        
        for column, data in enumerate(row_data):
            if column < model.columnCount():
                index = model.index(row, column)
                model.setData(index, str(data) if data is not None else "")
        
        return True
    
    def filter_table(self, table: QTableView, column: int, text: str):
        """
        Aplica un filtro simple a una columna de la tabla.
        
        Args:
            table: La tabla a filtrar
            column: Índice de la columna
            text: Texto a filtrar
        """
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
    
    def export_to_csv(self, table: QTableView, filename: str) -> bool:
        """
        Exporta los datos de la tabla a un archivo CSV.
        
        Args:
            table: La tabla a exportar
            filename: Nombre del archivo de destino
            
        Returns:
            True si se exportó correctamente, False en caso contrario
        """
        try:
            import csv
            
            model = table.model()
            if not model:
                return False
            
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Escribir headers
                headers = []
                for column in range(model.columnCount()):
                    header_data = model.headerData(column, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
                    headers.append(str(header_data) if header_data else f"Column {column}")
                writer.writerow(headers)
                
                # Escribir datos
                for row in range(model.rowCount()):
                    row_data = []
                    for column in range(model.columnCount()):
                        index = model.index(row, column)
                        data = model.data(index, Qt.ItemDataRole.DisplayRole)
                        row_data.append(str(data) if data else "")
                    writer.writerow(row_data)
            
            return True
        except Exception as e:
            print(f"Error exportando a CSV: {e}")
            return False
    
    def _handle_double_click(self, table: QTableView, index: QModelIndex):
        """Maneja el evento de doble clic en una tabla."""
        if index.isValid():
            row_data = self.get_row_data(table, index.row())
            self.row_double_clicked.emit(table, index.row(), row_data)
    
    def _handle_selection_changed(self, table: QTableView):
        """Maneja el cambio de selección en una tabla."""
        selected_data = self.get_selected_rows_data(table)
        self.row_selected.emit(table, selected_data)
    
    def _show_context_menu(self, table: QTableView, position):
        """Muestra el menú contextual de la tabla."""
        # Obtener la fila en la posición del clic
        index = table.indexAt(position)
        row = index.row() if index.isValid() else -1
        
        # Emitir señal para que otros componentes puedan manejar el menú
        global_pos = table.mapToGlobal(position)
        self.context_menu_requested.emit(table, row, global_pos)

# Ejemplo de configuraciones predefinidas para diferentes tipos de tabla
class TableConfigs:
    """Configuraciones predefinidas para diferentes tipos de tablas."""
    
    @staticmethod
    def get_bugs_table_config():
        """Configuración para la tabla de bugs."""
        return {
            'context_menu': True,
            'column_widths': [80, 100, 80, 120, 120, 100, 120, 150, 200, 300, 80, 80, 200],
            'column_config': {
                0: {'alignment': Qt.AlignmentFlag.AlignCenter},  # Status
                6: {'alignment': Qt.AlignmentFlag.AlignCenter},  # Campaign
                10: {'alignment': Qt.AlignmentFlag.AlignCenter}, # Urgency
                11: {'alignment': Qt.AlignmentFlag.AlignCenter}, # Impact
            },
            'max_section_size': 400,
            'alternating_row_colors': True,
            'sort_enabled': True
        }
    
    @staticmethod
    def get_campaigns_table_config():
        """Configuración para la tabla de campañas."""
        return {
            'context_menu': True,
            'column_widths': [50, 200, 100, 80, 120, 80, 80, 120, 120, 120, 120],
            'column_config': {
                0: {'alignment': Qt.AlignmentFlag.AlignCenter},  # Id
                5: {'alignment': Qt.AlignmentFlag.AlignCenter},  # Passed
                6: {'alignment': Qt.AlignmentFlag.AlignCenter},  # Success
            },
            'max_section_size': 300,
            'alternating_row_colors': True,
            'sort_enabled': True
        }
    
    @staticmethod
    def get_generic_table_config():
        """Configuración genérica para tablas."""
        return {
            'context_menu': False,
            'alternating_row_colors': True,
            'sort_enabled': True,
            'max_section_size': 250
        }