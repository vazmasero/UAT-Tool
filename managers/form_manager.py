from typing import Dict, Optional, Type, Any
from PySide6.QtWidgets import QWidget, QDialog

from config.app_config import AppConfig
from config.forms_config import FormConfig, FORMS

class FormManager:
    """Forms centralized management"""

    def __init__(self):
        self.active_forms: Dict[str, QWidget] = {}
        self.config = AppConfig()

    def open_form(self, form_key: str, edit_mode: bool = False, data: Optional[Any] = None) -> Optional[QWidget]:
        """Opens a form based on its configuration key."""
        config = FORMS.get(form_key, {}).get("config")
        if not config:
            print(f"Configuration not founded for form: {form_key}")
            return None
        
        title = config.edit_title if edit_mode else config.add_title

        #Brings form up front if already open
        if title in self.active_forms:
            form = self.active_forms[title]
            form.raise_()
            form.activateWindow()
            return form
        
        # Creates new form
        form = config.form_class()
        form.setWindowTitle(title)

        # Configures label if necessary
        if config.label_attr and hasattr(form.ui, config.label_attr):
            label_text = config.edit_label if edit_mode else config.add_label
            if label_text:
                getattr(form.ui, config.label_attr).setText(label_text)

        # Loads data if available
        if data and hasattr(form, 'load_data'):
            form.load_data(data)

        # Registers form
        self.register_form(form, title)
        form.show()

        return form
    
    def register_form(self, form: QWidget, key: str):
        """Registers a form in the manager"""
        self.active_forms[key] = form
        form.destroyed.connect(lambda: self.active_forms.pop(key, None))

    def close_form(self, key: str):
        """Closes a specific form"""
        if key in self.active_forms:
            self.active_forms[key].close()

    def close_all_forms(self):
        """Closes all active forms"""
        for form in list(self.active_forms.values()):
            form.close()