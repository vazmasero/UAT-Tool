from typing import Dict, Optional, Type, Any, List
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, Signal

from config.form_config import FORMS
from config.page_config import PAGES
from utils.form_mode import FormMode

class BaseForm(QWidget):

    def __init__(self, db_manager, ui):
        super().__init__()
        self.db_manager = db_manager
        self.ui = ui
        self._setup_buttons()

    def _setup_buttons(self):
        """Conecta botones comunes como aceptar y cancelar."""
        self.ui.btn_accept.clicked.connect(self._handle_db_register)
        self.ui.btn_cancel.clicked.connect(self.close)

    def _handle_db_register(self):
        """Maneja el registro o edición en la base de datos."""
        data = self._obtain_form_data()
        errors = self.validate_form(data)
        if errors:
            self.show_errors(errors)
            return
        try:
            self.save_data(data)
            self.close()
        except Exception as e:
            self.show_critical(str(e))

    def validate_form(self, data):
        """Valida los datos del formulario. Implementar en subclases."""
        raise NotImplementedError("Subclasses must implement validate_form")

    def _obtain_form_data(self):
        """Obtiene los datos del formulario. Implementar en subclases."""
        return {}

    def save_data(self, data):
        """Guarda los datos en la base de datos. Implementar en subclases."""
        raise NotImplementedError("Subclasses must implement save_data")

    def show_errors(self, errors):
        """Muestra errores en un QMessageBox."""
        QMessageBox.warning(self, "Validation Errors", "\n".join(errors))

    def show_critical(self, message):
        """Muestra errores críticos en un QMessageBox."""
        QMessageBox.critical(self, "Critical Error", message)

class FormManager:
    """Gestor de formularios, maneja apertura y cierre."""
    data_updated = Signal(str)
    
    def __init__(self):
        self.active_forms = {}

    def open_form(self, form_key:str, edit:bool, data:Optional[List]):
        """Abre un formulario basado en su clave y modo (agregar/editar)."""
        form_config = FORMS[form_key]['config']

        form_instance = form_config.form_class(
            mode=FormMode.EDIT if edit else FormMode.CREATE,
            db_id = data.get('id', None) if data else None
        )

        if edit and data:
            form_instance.load_data(data)

        form_instance.show()
        self.active_forms[form_key] = form_instance
        
        return form_instance

    def close_form(self, form_key):
        """Cierra un formulario y lo elimina de los formularios activos."""
        if form_key in self.active_forms:
            self.active_forms[form_key].close()
            del self.active_forms[form_key]
    
    def close_all_forms(self):
        """Cierra todos los formularios activos."""
        # Crear una copia de las claves para evitar modificar el diccionario durante la iteración
        form_keys = list(self.active_forms.keys())
        
        for form_key in form_keys:
            form_instance = self.active_forms[form_key]
            if form_instance:
                form_instance.close()
        
        # Limpiar el diccionario de formularios activos
        self.active_forms.clear()
            
    def get_form_key(self, current_page: str, tab_index: Optional[int]) -> Optional[str]:
        page_config = PAGES.get(current_page, {}).get("config")
        page_forms = page_config.forms if page_config else []
        if not page_forms:
            print(f"No forms associated with page '{current_page}'.")
            return None
        return page_forms[tab_index] if tab_index is not None and tab_index < len(page_forms) else page_forms[0]