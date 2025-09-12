from typing import Dict, Optional, Any
from PySide6.QtWidgets import QTableView

from base.base_form import BaseForm
from managers.table_manager import TableManager
from ui.ui_form_case import Ui_form_case
from controllers.case_controller import CaseController
from services.case_service import CaseService
from utils.form_mode import FormMode

from database.db import DatabaseManager


class FormCase(BaseForm):

    def __init__(self, mode: FormMode, db_id: Optional[int]):
        super().__init__("cases", mode, db_id)
        self.ui = Ui_form_case()

        # Create managers and controller
        self.db_manager = DatabaseManager()
        self.table_manager = TableManager()

        self.service = CaseService(self.db_manager)
        self.controller = CaseController(self.service, self.table_manager)

        # Setup form
        self.setup_form(Ui_form_case, self.controller)
        self.controller.setup_tables(self.ui, self.mode, self.db_id)
        self._connect_signals()

    def _connect_signals(self):
        # Ui buttons
        self.ui.btn_add_step.clicked.connect(
            lambda _: self.controller.handle_new_step(
                edit=False, table_name="steps", row_data=None))
        self.ui.btn_remove_step.clicked.connect(
            lambda _: self.controller.handle_remove_step())

        # Table signals
        self.table_manager.table_double_clicked.connect(
            lambda table_name, row_data: self.controller.handle_new_step(
                edit=True, table_name=table_name, row_data=row_data))
        self.table_manager.selection_changed.connect(
            self.handle_selection_changed)

    def _setup_custom_widgets(self):
        lw_data = self.controller.get_lw_data()
        self.setup_checkbox_list(self.ui.lw_system, lw_data["systems"])
        self.setup_checkbox_list(self.ui.lw_section, lw_data["sections"])
        self.setup_checkbox_list(self.ui.lw_operator, lw_data["operators"])
        self.setup_checkbox_list(self.ui.lw_drone, lw_data["drones"])
        self.setup_checkbox_list(self.ui.lw_uhub_user, lw_data["uhub_users"])

    def _setup_buttons(self):
        """Sets up view's buttons (Add Step and Remove Step)."""
        # Initially, remove button is disabled
        self.ui.btn_remove_step.setEnabled(False)

        # Connect accept and cancel buttons to their respective handlers
        if hasattr(self.ui, 'btn_accept'):
            self.ui.btn_accept.clicked.connect(self._handle_submit)
        if hasattr(self.ui, 'btn_cancel'):
            self.ui.btn_cancel.clicked.connect(self.close)

    def handle_selection_changed(self, table: QTableView):
        """Handles selection changes in the table."""
        if table:
            if table.selectionModel().hasSelection():
                self.ui.btn_remove_step.setEnabled(True)
            else:
                self.ui.btn_remove_step.setEnabled(False)

    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return

        # Set the form fields with the formatted data
        self.ui.le_identification.setText(formatted_data['identification'])
        self.ui.le_name.setText(formatted_data['name'])
        self.set_checked_items(self.ui.lw_system, formatted_data['systems'])
        self.set_checked_items(self.ui.lw_section, formatted_data['sections'])
        self.set_checked_items(
            self.ui.lw_operator,
            formatted_data['operators'])
        self.set_checked_items(self.ui.lw_drone, formatted_data['drones'])
        self.set_checked_items(
            self.ui.lw_uhub_user,
            formatted_data['uhub_users'])
        self.ui.le_comment.setText(formatted_data['comments'])

    def _obtain_form_data(self) -> Dict[str, Any]:
        return {
            'identification': self.ui.le_identification.text(),
            'name': self.ui.le_name.text(),
            'systems': self.get_checked_items(self.ui.lw_system),
            'sections': self.get_checked_items(self.ui.lw_section),
            'operators': self.get_checked_items(self.ui.lw_operator),
            'drones': self.get_checked_items(self.ui.lw_drone),
            'uhub_users': self.get_checked_items(self.ui.lw_uhub_user),
            'comments': self.ui.le_comment.text(),
        }

    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []

        if not data['identification']:
            errors.append("Defining an identification is mandatory")
        if not data['name']:
            errors.append("Writing a name for the case is mandatory")
        if not data['systems']:
            errors.append(
                "Choosing (at least) one associated system is mandatory")
        if not data['sections']:
            errors.append(
                "Choosing (at least) one associated section is mandatory")

        return errors

    def _handle_submit(self):
        """Handles form submission for Case, including steps."""
        try:
            data = self._obtain_form_data()
            errors = self.validate_form(data)

            if errors:
                self.show_errors(errors)
                return

            steps_table = self.ui.tbl_steps
            self.controller.handle_form_submission(
                data, self.db_id, steps_table)
            self.data_updated.emit(self.form_key)
            self.close()
        except Exception as e:
            self.show_critical(f"Error submitting form: {str(e)}")
