from typing import Dict, Optional, Type, Any
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, Signal

from config.form_config import FORMS

class BaseForm(QWidget):
    """Clase base para formularios, centraliza lógica común."""
    operation_completed = Signal()

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
            self.operation_completed.emit()
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

class FormRegistry:
    """Gestiona formularios activos."""
    def __init__(self):
        self.active_forms = {}

    def register_form(self, form, key):
        self.active_forms[key] = form
        form.destroyed.connect(lambda: self._on_form_destroyed(key))

    def _on_form_destroyed(self, key):
        self.active_forms.pop(key, None)

class FormOpener:
    """Abre formularios basados en configuración."""
    def __init__(self, registry, config):
        self.registry = registry
        self.config = config

    def open_form(self, form_key, edit_mode=False, data=None):
        config = self.config.get(form_key, {}).get("config")
        if not config:
            print(f"Configuration not found for form: {form_key}")
            return None

        title = config.edit_title if edit_mode else config.add_title

        # Brings form up front if already open
        if title in self.registry.active_forms:
            form = self.registry.active_forms[title]
            form.raise_()
            form.activateWindow()
            return form

        # If not open, creates new form
        form = config.form_class()
        form.setWindowTitle(title)
        form.setAttribute(Qt.WA_DeleteOnClose)  # Deletes form when closed as well

        # Configures label if necessary
        if config.label_attr and hasattr(form.ui, config.label_attr):
            label_text = config.edit_label if edit_mode else config.add_label
            if label_text:
                getattr(form.ui, config.label_attr).setText(label_text)

        # Loads data if on edit mode and if data available
        if edit_mode:
            if data and hasattr(form, 'load_data'):
                form.load_data(data)

        # Registers form
        self.registry.register_form(form, title)
        form.show()

        return form

class FormManager:
    """Gestor de formularios, maneja apertura y cierre."""
    def __init__(self):
        self.active_forms = {}

    def open_form(self, form_key, mode, data=None):
        """Abre un formulario basado en su clave y modo (agregar/editar)."""
        form_config = FORMS[form_key]['config']
        form_instance = form_config.form_class()
        if mode == 'edit':
            form_instance.load_data(data)
        form_instance.show()
        self.active_forms[form_key] = form_instance

    def close_form(self, form_key):
        """Cierra un formulario y lo elimina de los formularios activos."""
        if form_key in self.active_forms:
            self.active_forms[form_key].close()
            del self.active_forms[form_key]