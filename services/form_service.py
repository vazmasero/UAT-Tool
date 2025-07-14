from PySide6.QtCore import Qt

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
    """Opens forms based on a certain configuration."""
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