from datetime import datetime
from typing import Any

from PySide6.QtCore import QModelIndex, QObject, QSortFilterProxyModel, Qt, Signal
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QTableView

from services.table_service import TableService
from utils.dict_utils import get_base_table_config


class TableManager(QObject):
    table_double_clicked = Signal(str, object)
    selection_changed = Signal(object)

    def __init__(self):
        """Initializes table manager.

        This object handles tables in the application, including:
        - Its registration and configuration
        - Interaction signals handling
        -Data model management
        """
        super().__init__()
        self.tables: dict[str, QTableView] = {}
        self.table_configs: dict[str, dict] = {}

    def setup_table(
        self,
        table: QTableView,
        name: str,
        data: list[dict[str, Any]],
        config: dict | None = None,
        register=False,
    ):
        merged_config = TableService.merge_table_config(name, config)

        # Configure source model
        headers = merged_config.get("headers", [])
        model = QStandardItemModel(0, len(headers))
        model.setHorizontalHeaderLabels(headers)
        self._populate_model(name, model, data)

        # Setup proxy model for filtering and sorting
        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(model)
        table.setModel(proxy_model)

        # Hide ID if there is a column named "Id" or "ID"
        for i, header in enumerate(headers):
            if header.lower() in ["id"]:
                table.setColumnHidden(i, True)
                break

        # Configure table properties
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setAlternatingRowColors(
            merged_config.get("alternating_row_colors", False)
        )
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        if register:
            self._register_table(table, name, config)

    def _populate_model(
        self, name: str, model: QStandardItemModel, data: list[dict[str, Any]]
    ):
        """Populates the model associated to a table with the elements obtained from the database."""
        if not data:
            return

        config = get_base_table_config(name)
        column_map = config.column_map
        headers = [
            model.headerData(col, Qt.Orientation.Horizontal)
            for col in range(model.columnCount())
        ]

        for row_data in data:
            items = []
            for col, header in enumerate(headers):
                db_column = column_map.get(header, header)
                value = row_data.get(db_column)
                item = self._create_item(value, config, col)

                items.append(item)

            if items:
                model.appendRow(items)

    def _create_item(
        self, value: Any, config: dict | None, column_index: int
    ) -> QStandardItem:
        """Creates a new item for a certain mode."""
        if value is None:
            value = ""
        elif isinstance(value, datetime):
            # Converts a datetime object to a string so it can be displayed on
            # the table
            value = value.strftime("%Y-%m-%d %H:%M:%S")

        item = QStandardItem(str(value))

        # Saves the original value as item data
        item.setData(value, Qt.ItemDataRole.UserRole)

        if config and hasattr(config, "column_config"):
            col_config = getattr(config, "column_config", {}).get(column_index, {})
            self._apply_item_config(item, col_config)

        # Non editable and non drop enabled items by default
        item.setEditable(getattr(config, "editable", False) if config else False)
        item.setDropEnabled(getattr(config, "drop_enabled", False) if config else False)

        return item

    def _register_table(
        self, table: QTableView, name: str, config: dict | None = None
    ) -> bool:
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

    def _apply_item_config(self, item: QStandardItem, col_config: dict):
        if "alignment" in col_config:
            item.setTextAlignment(col_config["alignment"])

        if "background_color" in col_config:
            item.setBackground(col_config["background_color"])

        if "text_color" in col_config:
            item.setForeground(col_config["text_color"])

        if "tooltip" in col_config:
            item.setToolTip(col_config["tooltip"])

    def get_row_data(self, name: str, table: QTableView, row: int) -> dict[str, Any]:
        """Obtains data from a row as a dictionary using the DB column names."""
        model = table.model()
        if not model or row < 0 or row >= model.rowCount():
            return {}

        # Obtener el mapeo de columnas
        config = self.table_configs.get(name, {})
        column_map = config.get("column_map", {})

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

    def get_selected_record_id(self, table_name: str) -> int | None:
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
        if hasattr(table.model(), "mapToSource"):
            source_index = table.model().mapToSource(proxy_index)
            source_model = table.model().sourceModel()
            # Obtain Id stored in first colum
            first_item = source_model.item(source_index.row(), 0)
            if first_item:
                return first_item.data(Qt.ItemDataRole.UserRole)
        else:
            # If there is no proxy model, user model directly
            first_item = table.model().item(proxy_index.row(), 0)
            if first_item:
                return first_item.data(Qt.ItemDataRole.UserRole)

        return None

    def get_selected_row_indices(self, table: QTableView) -> list[int]:
        if not table or not table.selectionModel():
            return []

        indices = table.selectionModel().selectedRows()
        return [index.row() for index in indices]

    def get_table_data(self, table: QTableView) -> list[dict[str, Any]]:
        """Obtains all table data."""
        model = table.model()
        source_model = model.sourceModel() if hasattr(model, "sourceModel") else model
        rows = []
        for row in range(source_model.rowCount()):
            row_data = {}
            for col in range(source_model.columnCount()):
                index = source_model.index(row, col)
                header = source_model.headerData(col, Qt.Orientation.Horizontal)
                value = source_model.data(index, Qt.ItemDataRole.UserRole)
                row_data[header] = value
            rows.append(row_data)

        return rows

    def add_row(
        self,
        table: QTableView,
        row_data: list[Any],
        position: int | None = None,
        config_module=None,
    ):
        model = table.model()
        if not model:
            return

        source_model = model
        if hasattr(model, "sourceModel"):
            source_model = model.sourceModel()

        processed_items = []

        if isinstance(row_data, dict):
            # Obtener headers del modelo
            headers = []
            for col in range(source_model.columnCount()):
                header = source_model.headerData(col, Qt.Orientation.Horizontal)
                headers.append(header)

            # Buscar configuración en CASE_TABLES
            config = None

            config_modules = []
            if config_module:
                config_modules.append(config_module)
            else:
                from config.block_table_config import BLOCK_TABLES
                from config.case_table_config import CASE_TABLES

                config_modules = [CASE_TABLES, BLOCK_TABLES]

            for tables in config_modules:
                for _, table_config in tables.items():
                    if (
                        hasattr(table, "objectName")
                        and table.objectName() == table_config["config"].widget_name
                    ):
                        config = table_config["config"]
                        break
                if config:
                    break

            # Convertir diccionario a lista ordenada según headers
            ordered_data = []
            for header in headers:
                if config and hasattr(config, "column_map") and config.column_map:
                    db_column = config.column_map.get(
                        header, header.lower().replace(" ", "_")
                    )
                else:
                    db_column = header.lower().replace(" ", "_")

                # Si es la columna Id, agregar None ya que no tenemos ID para
                # nuevos registros
                if header.lower() == "id":
                    value = row_data.get(db_column, None)
                    ordered_data.append(value)
                else:
                    value = row_data.get(db_column, "")
                    ordered_data.append(value)

            row_data = ordered_data

        # Procesar cada elemento de la fila (ahora row_data es una lista)
        for _, data in enumerate(row_data):
            # Handle None values
            if data is None:
                data = ""

            # Handle many-to-many data (lists or comma-separated strings)
            if isinstance(data, list):
                # Convert list to comma-separated string for display
                display_value = ", ".join(str(item) for item in data)
            elif isinstance(data, str) and "," in data:
                # It's already a comma-separated string, keep as is for display
                display_value = data
            else:
                # Regular single value
                display_value = str(data)

            # Create the item
            item = QStandardItem(display_value)
            item.setEditable(False)

            # Store original data for later retrieval
            # This preserves the original format (list, string, etc.)
            item.setData(data, Qt.ItemDataRole.UserRole)

            # For the first column (Id), no need to store numeric ID since it's None for new records
            # The ID will be assigned when saved to database

            processed_items.append(item)

        # Add to source model (not proxy model)
        if position is None:
            source_model.appendRow(processed_items)
        else:
            source_model.insertRow(position, processed_items)

    def update_row(self, table: QTableView, row_data: dict[str, Any], row_index: int):
        """Updates an existing row in the table with new data."""
        model = table.model()
        if not model:
            print("No model found for the table")
            return False

        source_model = model
        if hasattr(model, "sourceModel"):
            source_model = model.sourceModel()

        # Check if the row index is valid
        if row_index < 0 or row_index >= source_model.rowCount():
            print(f"Invalid row index: {row_index}")
            return False

        # Obtain headers from the model
        headers = []
        for col in range(source_model.columnCount()):
            header = source_model.headerData(col, Qt.Orientation.Horizontal)
            headers.append(header)

        # Find the configuration for the table
        config = None
        table_name = None

        from config.case_table_config import CASE_TABLES

        for name, table_config in CASE_TABLES.items():
            if (
                hasattr(table, "objectName")
                and table.objectName() == table_config["config"].widget_name
            ):
                config = table_config["config"]
                table_name = name
                break

        # Update each column in the row
        for col, header in enumerate(headers):
            if config and hasattr(config, "column_map") and config.column_map:
                db_column = config.column_map.get(
                    header, header.lower().replace(" ", "_")
                )
            else:
                db_column = header.lower().replace(" ", "_")

            # Obtain the value from data dict
            if header.lower() == "id":
                # Maintain existing Id
                continue
            value = row_data.get(db_column, "")

            # Process value according to its type
            if value is None:
                display_value = ""
            elif isinstance(value, list):
                display_value = ", ".join(str(item) for item in value)
            elif isinstance(value, str) and "," in value:
                display_value = value
            else:
                display_value = str(value)

            # Actualizar el item en el modelo
            index = source_model.index(row_index, col)
            item = source_model.itemFromIndex(index)

            if item:
                item.setText(display_value)
                item.setData(value, Qt.ItemDataRole.UserRole)

            else:
                # If item does not exist, create a new one
                new_item = QStandardItem(display_value)
                new_item.setEditable(False)
                new_item.setData(value, Qt.ItemDataRole.UserRole)
                source_model.setItem(row_index, col, new_item)

        print(f"Row {row_index} updated successfully in table '{table_name}'")
        return True

    def delete_row(self, table: QTableView, row_index: int):
        """Deletes a row from the model given the row index."""
        model = table.model()
        if not model:
            print("No model found for the table")
            return False

        source_model = model
        if hasattr(model, "sourceModel"):
            source_model = model.sourceModel()

        if row_index < 0 or row_index >= source_model.rowCount():
            print(f"Invalid row index: {row_index}")
            return False

        source_model.removeRow(row_index)
        print(f"Row {row_index} deleted successfully")
        return True

    def _handle_double_click(self, name: str, table: QTableView, index: QModelIndex):
        """Handles the double click on a table item event."""
        if index.isValid():
            row_data = self.get_row_data(name, table, index.row())
            self.table_double_clicked.emit(name, row_data)

    def _handle_selection_changed(self, name: str):
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

        if hasattr(model, "sourceModel"):
            source_model = model.sourceModel()

        source_model.clear()

        config = get_base_table_config(table_name)
        headers = config.headers if hasattr(config, "headers") else []
        if headers:
            source_model.setHorizontalHeaderLabels(headers)

        self._populate_model(table_name, source_model, new_data)

        for i, header in enumerate(headers):
            if header.lower() in ["id"]:
                table_widget.setColumnHidden(i, True)
                break

        print(f"Table model '{table_name}' updated with {len(new_data)} records")
