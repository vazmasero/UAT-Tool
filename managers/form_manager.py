from typing import Dict, Optional, Type, Any, List
from PySide6.QtCore import QObject, Signal
from base.base_form import BaseForm 
from config.form_config import FORMS
from config.page_config import PAGES
from utils.form_mode import FormMode

class FormManager(QObject):
    """Gestor de formularios, maneja apertura y cierre."""
    data_updated = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.active_forms: Dict[str, BaseForm] = {}

    def open_form(self, form_key:str, edit:bool, data:Optional[List], data_instead_id: bool = False):
        """Opens a form based on its key and mode (create/edit)."""

        # Closes previous form if opened
        if form_key in self.active_forms:
            self.active_forms[form_key].close()
            self.active_forms.pop(form_key, None)
        
        # Obtain form configuration
        form_config = FORMS[form_key]['config']

        # Determine form mode and databse ID if editing and item
        mode = FormMode.EDIT if edit else FormMode.CREATE

        # Handle if the form wants id or full data
        if data_instead_id:
            form_instance = form_config.form_class(mode=mode, data=data)
        else:
            db_id = data.get('id', None) if data else None
            form_instance = form_config.form_class(mode=mode, db_id=db_id)

        # Connects signals for event handling (in particular, a form being closed)
        form_instance.destroyed.connect(lambda: self._on_form_closed(form_key))

        # Shows the form and store it in active forms
        form_instance.show()
        self.active_forms[form_key] = form_instance
        
        return form_instance

    def _on_form_closed(self, form_key: str):
        self.active_forms.pop(form_key, None)

    def close_form(self, form_key):
        """Cierra un formulario y lo elimina de los formularios activos."""
        if form_key in self.active_forms:
            self.active_forms[form_key].close()

    def close_all_forms(self):
        """Cierra todos los formularios activos."""
        for form_instance in list(self.active_forms.values()):
            form_instance.close()
        self.active_forms.clear()
            
    def get_form_key(self, current_page: str, tab_index: Optional[int]) -> Optional[str]:
        page_config = PAGES.get(current_page, {}).get("config")
        page_forms = page_config.forms if page_config else []
        if not page_forms:
            print(f"No forms associated with page '{current_page}'.")
            return None
        return page_forms[tab_index] if tab_index is not None and tab_index < len(page_forms) else page_forms[0]