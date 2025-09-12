import os
from PySide6.QtWidgets import QFileDialog
from base.base_form import BaseForm
from controllers.assets_controller import AssetsController
from services.assets_service import AssetsService
from database.db import DatabaseManager
from config.assets_config import ASSET_CONFIGS
from utils.form_mode import FormMode
from typing import Optional, Dict, Any, List
import importlib


class BaseAssetForm(BaseForm):

    def __init__(self, asset_type: str, mode: FormMode,
                 db_id: Optional[int] = None):
        # Obtener configuración
        self.asset_config = ASSET_CONFIGS[asset_type]

        super().__init__(self.asset_config.form_key, mode, db_id)

        # Crear dependencias
        db_manager = DatabaseManager()
        service = AssetsService(db_manager)
        controller = AssetsController(service, self.asset_config)

        # Importar UI dinámicamente
        ui_module = importlib.import_module(self.asset_config.ui_module)
        ui_class = getattr(ui_module, self.asset_config.ui_class)

        # Setup form
        self.setup_form(ui_class, controller)

        # Setup file browsers
        self._setup_file_browsers()

    def _setup_file_browsers(self):
        if hasattr(self.ui, 'btn_browse_file'):
            self.ui.btn_browse_file.clicked.connect(self._browse_file)

    def _browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            self.ui.le_file_path.setText(file_path)

    def _obtain_form_data(self) -> Dict[str, Any]:
        """Obtiene datos del formulario basado en la configuración"""
        data = {}
        for field in self.asset_config.fields:
            if field == 'file':
                if hasattr(self.ui, 'le_file_path'):
                    file_path = self.ui.le_file_path.text()
                    if file_path:
                        # Read file content
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                data[field] = f.read()
                        except Exception as e:
                            print(f"Error reading file: {e}")
                            data[field] = ""
                    else:
                        data[field] = ""
            else:
                widget_name = f"le_{field}"

                if hasattr(self.ui, widget_name):
                    widget = getattr(self.ui, widget_name)
                    if hasattr(widget, 'text'):
                        data[field] = widget.text()
                    elif hasattr(widget, 'currentText'):  # For comboboxes
                        data[field] = widget.currentText()

        return data

    def validate_form(self, data: Dict[str, Any]) -> List[str]:
        """Valida usando las reglas de configuración"""
        errors = []
        for field, error_message in self.asset_config.validation_rules.items():
            if field == 'file':
                file_path = self.ui.le_file_path.text() if hasattr(
                    self.ui, 'le_file_path') else ""
                if not file_path:
                    errors.append(error_message)
                elif not os.path.exists(file_path):
                    errors.append("Selected file does not exist")
                elif not file_path.lower().endswith('.json'):
                    errors.append("File must be a JSON file")
            else:
                if not data.get(field):
                    errors.append(error_message)
        return errors

    def load_data(self, data: Dict[str, Any]):
        """Carga datos usando la configuración"""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return

        for field in self.asset_config.fields:
            if field == 'file':
                file_content = formatted_data.get(field, "")
                if file_content and hasattr(self.ui, 'le_file_path'):
                    self.ui.le_file_path.setText("[File loaded from database]")
            else:
                widget_name = f"le_{field}"

                if hasattr(self.ui, widget_name):
                    widget = getattr(self.ui, widget_name)
                    value = formatted_data.get(field, "")

                    if hasattr(widget, 'setText'):
                        widget.setText(str(value))
                    elif hasattr(widget, 'setCurrentText'):  # For comboboxes
                        widget.setCurrentText(str(value))
