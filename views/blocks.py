from typing import Dict, Optional, Any
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from base.base_form import BaseForm
from managers.table_manager import TableManager
from ui.ui_form_block import Ui_form_block
from controllers.block_controller import BlockController
from services.block_service import BlockService
from utils.form_mode import FormMode

from database.db import DatabaseManager


class FormBlock(BaseForm):

    def __init__(self, mode: FormMode, db_id: Optional[int]):
        super().__init__("blocks", mode, db_id)
        self.ui = Ui_form_block()

        # Create managers and controller
        self.db_manager = DatabaseManager()
        self.table_manager = TableManager()

        self.service = BlockService(self.db_manager)
        self.controller = BlockController(self.service, self.table_manager)

        self.selected_case_ids = set()

        # Setup form
        self.setup_form(Ui_form_block, self.controller)
        self._connect_signals()

    def _connect_signals(self):
        pass

    def _setup_custom_widgets(self):
        self.controller.setup_tables(self.ui, self.mode, self.db_id)
        self.ui.cb_system.currentTextChanged.connect(self._on_system_changed)
        self.ui.lw_cases.itemChanged.connect(
            self._handle_case_checkbox_changed)
        if self.mode != FormMode.EDIT:
            self._update_cases_list()

    def _on_system_changed(self):
        self.selected_case_ids = set()
        self._update_cases_list()

    def _handle_case_checkbox_changed(self, item: QListWidgetItem):
        case_id = item.data(Qt.UserRole)
        checked = item.checkState() == Qt.Checked

        case_data = self.controller.get_case_by_id(case_id)

        if checked:
            if not self.controller.is_case_in_table(case_id):
                self.controller.add_case_to_table(case_data)
        else:
            self.controller.remove_case_from_table(case_id)

    def _update_cases_list(self):
        self._clear_cases_table()
        system_name = self.ui.cb_system.currentText()
        cases = self.controller.get_cases_by_system(system_name)
        self.ui.lw_cases.clear()

        for case in cases:
            item = QListWidgetItem(
                f"{case['identification']} - {case['name']}")
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setData(Qt.UserRole, case.get("id"))
            if case.get("id") in self.selected_case_ids:
                item.setCheckState(Qt.Checked)
                self.controller.add_case_to_table(case)
            else:
                item.setCheckState(Qt.Unchecked)
            self.ui.lw_cases.addItem(item)

    def _clear_cases_table(self):
        """Limpia todas las filas de la tabla de casos."""
        model = self.ui.tbl_cases.model()
        if model:
            while model.rowCount() > 0:
                model.removeRow(0)

    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return
        self.ui.le_identification.setText(formatted_data['identification'])
        self.ui.le_name.setText(formatted_data['name'])
        self.ui.le_comments.setText(formatted_data['comments'])
        self.ui.cb_system.setCurrentText(formatted_data['system'])
        self.selected_case_ids = set(case.get("id")
                                     for case in formatted_data.get("cases", []))
        self._update_cases_list()

    def _obtain_form_data(self) -> Dict[str, Any]:
        return {
            'identification': self.ui.le_identification.text(),
            'name': self.ui.le_name.text(),
            'system': self.ui.cb_system.currentText(),
            'comments': self.ui.le_comments.text(),
            'cases': self.get_checked_case_ids()
        }

    def get_checked_case_ids(self):
        checked_ids = []
        for i in range(self.ui.lw_cases.count()):
            item = self.ui.lw_cases.item(i)
            if item.checkState() == Qt.Checked:
                checked_ids.append(item.data(Qt.UserRole))

        return checked_ids

    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []

        if not data['identification']:
            errors.append("Defining an identification is mandatory")
        if not data['name']:
            errors.append("Writing a name for the case is mandatory")
        if not data['system']:
            errors.append("Choosing one associated system is mandatory")

        return errors

    def _handle_submit(self):
        """Handles form submission for Block, including cases."""
        try:
            data = self._obtain_form_data()
            errors = self.validate_form(data)

            if errors:
                self.show_errors(errors)
                return

            cases_table = self.ui.tbl_cases
            self.controller.handle_form_submission(
                data, self.db_id, cases_table)
            self.data_updated.emit(self.form_key)
            self.close()
        except Exception as e:
            self.show_critical(f"Error submitting form: {str(e)}")
