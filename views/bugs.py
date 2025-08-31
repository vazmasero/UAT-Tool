from typing import Dict, Optional, Any
from PySide6.QtWidgets import QFileDialog

from base.base_form import BaseForm
from ui.ui_form_bug import Ui_form_bug
from controllers.bug_controller import BugController
from services.bug_service import BugService
from utils.form_mode import FormMode

from db.db import DatabaseManager

class FormBug(BaseForm):
    def __init__(self, mode: FormMode, db_id: Optional[int]):
        """Initializes bug management form.
        
        This form allows the creation and edition of bugs, including:
        - Basic information about the bug
        - Status and priority
        - System and version affected
        - Related requirements
        - Attached files
        - Change log
        
        Args
        ----
            mode (FormMode): form mode (create/edit)
            db_id (Optional[int]): Database id for the bug if edit mode
            
        """
        super().__init__("bugs", mode, db_id)
        self.ui = Ui_form_bug()

        # Create managers and controller
        self.db_manager = DatabaseManager()

        self.service = BugService(self.db_manager)
        self.controller = BugController(self.service)

        # Setup form
        self.setup_form(Ui_form_bug, self.controller)
        self._connect_signals()

    def _setup_custom_widgets(self):

        # Add file
        if hasattr(self.ui, 'btn_files'):
            self.ui.btn_files.clicked.connect(self._browse_file)

        # Combo boxes and selectables
        lw_data = self.controller.get_lw_data()
        self.setup_checkbox_list(
            self.ui.lw_requirements,
            lw_data["requirements"])
        self.setup_cb(self.ui.cb_campaign, lw_data["campaigns"])
        self.setup_cb(self.ui.cb_system, lw_data["systems"])

        # Log history setup
        self.ui.lw_history.clear()
        self.ui.lw_history.addItem("No history registered yet.")

    def _browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            self.ui.le_files.setText(file_path)

    def _connect_signals(self):
        pass

    def load_data(self, data):

        # Load data
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return

        self.ui.cb_status.setCurrentText(formatted_data['status'])
        self.ui.cb_system.setCurrentText(formatted_data['system_id'])
        self.ui.le_version.setText(formatted_data['version'])
        self.ui.le_service_now_id.setText(formatted_data['service_now_id'])
        self.ui.cb_campaign.setCurrentText(formatted_data['campaign_id'])
        self.set_checked_items(
            self.ui.lw_requirements,
            formatted_data['requirements'])
        self.ui.cb_urgency.setCurrentText(formatted_data['urgency'])
        self.ui.cb_impact.setCurrentText(formatted_data['impact'])
        self.ui.le_short_desc.setText(formatted_data['short_desc'])
        self.ui.le_definition.setText(formatted_data['definition'])
        file_content = formatted_data.get('file', "")
        if file_content:
            self.ui.le_files.setText("[File loaded from database]")

        # Load bug history
        log = data.get("log", "")
        self.ui.lw_history.clear()
        if not log:
            self.ui.lw_history.addItem("No history registered yet.")
        else:
            for entry in log.split("\n"):
                self.ui.lw_history.addItem(entry)

    def _obtain_form_data(self) -> Dict[str, Any]:
        data = {
            'status': self.ui.cb_status.currentText(),
            'system': self.ui.cb_system.currentText(),
            'version': self.ui.le_version.text(),
            'service_now_id': self.ui.le_service_now_id.text(),
            'campaign': self.ui.cb_campaign.currentText(),
            'requirements': self.get_checked_items(self.ui.lw_requirements),
            'urgency': self.ui.cb_urgency.currentText(),
            'impact': self.ui.cb_impact.currentText(),
            'short_desc': self.ui.le_short_desc.text(),
            'definition': self.ui.le_definition.text(),
        }

        file_path = self.ui.le_files.text()
        if file_path:
            # Read file content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data['file'] = f.read()
            except Exception as e:
                print(f"Error reading file: {e}")
                data['file'] = ""
        else:
            data['file'] = ""

        return data

    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []

        if not data['status']:
            errors.append("Defining a status is mandatory")
        if not data['system']:
            errors.append("Chosing a system is mandatory")
        if not data['version']:
            errors.append("Typing in a system version is mandatory")
        if not data['campaign']:
            errors.append("Choosing one associated campaign is mandatory")
        if not data['urgency']:
            errors.append("Choosing an associate urgency is mandatory")
        if not data['impact']:
            errors.append("Choosing an associate impact is mandatory")
        if not data['short_desc']:
            errors.append("Writing a short description is mandatory")
        if not data['definition']:
            errors.append("Writing a definition is mandatory")

        return errors
