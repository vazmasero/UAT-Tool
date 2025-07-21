from base.base_form import BaseForm
from controllers.assets_controller import AssetsController
from services.assets_service import AssetsService
from db.db import DatabaseManager
from config.assets_config import ASSET_CONFIGS
from utils.form_mode import FormMode
from typing import Optional, Dict, Any, List
import importlib

class BaseAssetForm(BaseForm):
    
    def __init__(self, asset_type: str, mode: FormMode, db_id: Optional[int] = None):
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
    
    def _obtain_form_data(self) -> Dict[str, Any]:
        """Obtiene datos del formulario basado en la configuración"""
        data = {}
        for field in self.asset_config.fields:
            widget_name = f"le_{field}"
            
            # Manejar casos especiales de nombres de widgets
            if field == 'tracker_type':
                widget_name = "cb_tracker"
            elif field == 'operator':
                widget_name = "cb_operator"

            if hasattr(self.ui, widget_name):
                widget = getattr(self.ui, widget_name)
                if hasattr(widget, 'text'):
                    data[field] = widget.text()
                elif hasattr(widget, 'currentText'):  # Para comboboxes
                    data[field] = widget.currentText()
        
        return data
    
    def validate_form(self, data: Dict[str, Any]) -> List[str]:
        """Valida usando las reglas de configuración"""
        errors = []
        for field, error_message in self.asset_config.validation_rules.items():
            if not data.get(field):
                errors.append(error_message)
        return errors
    
    def load_data(self, data: Dict[str, Any]):
        """Carga datos usando la configuración"""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return
        
        for field in self.asset_config.fields:
            widget_name = f"le_{field}"
            
            # Manejar casos especiales
            if field == 'serial_number':
                widget_name = "le_sn"
            elif field == 'tracker_type':
                widget_name = "cb_tracker"
            elif field == 'operator':
                widget_name = "cb_operator"
            elif field == 'transponder_id':
                widget_name = "le_transponder"
            
            if hasattr(self.ui, widget_name):
                widget = getattr(self.ui, widget_name)
                value = formatted_data.get(field, "")
                
                if hasattr(widget, 'setText'):
                    widget.setText(str(value))
                elif hasattr(widget, 'setCurrentText'):  # Para comboboxes
                    widget.setCurrentText(str(value))