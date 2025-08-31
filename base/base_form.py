from typing import Optional, Dict, Any, List
from PySide6.QtWidgets import QWidget, QMessageBox, QListWidget, QCheckBox, QListWidgetItem, QComboBox
from PySide6.QtCore import Signal
from utils.form_mode import FormMode


class BaseForm(QWidget):
    """Unified base class for forms, providing common functionality."""
    data_updated = Signal(str)

    def __init__(self, form_key: str, mode: FormMode,
                 db_id: Optional[int] = None):
        super().__init__()
        self.form_key = form_key
        self.db_id = db_id
        self.mode = mode

        self.ui = None
        self.controller = None

        self._setup_window_title()

    def setup_form(self, ui_class, controller):
        """ Method to set up the UI and controller for the form. Called by subclasses. """
        self.ui = ui_class()
        self.ui.setupUi(self)
        self.controller = controller
        self._setup_buttons()

        self._setup_custom_widgets()

        self._setup_initial_data()

    def _setup_custom_widgets(self):
        """Override this method in subclasses to set up custom widgets."""

    def _setup_window_title(self):
        """Sets the window title based on the form mode."""
        from config.form_config import FORMS
        config = FORMS[self.form_key]['config']
        title = config.edit_title if self.mode == FormMode.EDIT else config.add_title
        self.setWindowTitle(title)

    def _setup_buttons(self):
        """Conects standard buttons."""
        if hasattr(self.ui, 'btn_accept'):
            self.ui.btn_accept.clicked.connect(self._handle_submit)
        if hasattr(self.ui, 'btn_cancel'):
            self.ui.btn_cancel.clicked.connect(self.close)

    def _setup_initial_data(self):
        """Sets up initial data for the form if edit mode."""
        if self.mode == FormMode.EDIT and self.db_id:
            try:
                data = self.controller.get_item_by_id(self.db_id)
                if data:
                    self.load_data(data)
            except Exception as e:
                self.show_critical(f"Error loading data: {str(e)}")

    def _handle_submit(self):
        """Handles form submission."""
        try:
            data = self._obtain_form_data()
            errors = self.validate_form(data)

            if errors:
                self.show_errors(errors)
                return

            self.controller.handle_form_submission(data, self.db_id)
            self.data_updated.emit(self.form_key)
            self.close()
        except Exception as e:
            self.show_critical(f"Error submitting form: {str(e)}")

    # Abstract methods to be implemented by subclasses
    def _obtain_form_data(self) -> Dict[str, Any]:
        """Abstract method to obtain form data."""
        raise NotImplementedError("Subclasses must implement this method.")

    def validate_form(self, data: Dict[str, Any]) -> List[str]:
        """Validates form data."""
        _ = data
        return []  # No errors by default

    def load_data(self, data: Dict[str, Any]):
        """Loads data into the form fields."""

    # Utility methods
    def show_errors(self, errors: List[str]):
        """Displays a message box with the provided errors."""
        QMessageBox.warning(self, "Validation Errors", "\n".join(errors))

    def show_critical(self, message: str):
        """Displays a critical error message."""
        QMessageBox.critical(self, "Critical Error", message)

    def setup_checkbox_list(
            self, list_widget: QListWidget, options: List[str]):
        """Sets up a QListWidget with checkboxes."""
        for option in options:
            item = QListWidgetItem(list_widget)
            checkbox = QCheckBox(option)
            list_widget.setItemWidget(item, checkbox)

    def setup_cb(self, combo_widget: QComboBox, options: List[str]):
        """Sets up a QComboBox with options."""
        combo_widget.clear()
        opts = list(options) if options else []
        if "NA" not in opts:
            opts.append("NA")
        for option in opts:
            combo_widget.addItem(option)

    def get_checked_items(self, list_widget: QListWidget) -> List[str]:
        """Returns a list of checked items from a QListWidget."""
        checked_items = []
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            checkbox = list_widget.itemWidget(item)
            if checkbox and checkbox.isChecked():
                checked_items.append(checkbox.text())
        return checked_items

    def set_checked_items(self, list_widget: QListWidget, items: List[str]):
        """Sets the checked state of items in a QListWidget."""
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            checkbox = list_widget.itemWidget(item)
            if checkbox:
                should_check = checkbox.text() in items
                checkbox.setChecked(should_check)
