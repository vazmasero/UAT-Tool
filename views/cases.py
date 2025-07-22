from typing import Dict, Callable, Optional, Type, Any, List
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget, QDialog, QTableView

#from managers.form_manager import FormManager
#from managers.page_manager import PageManager
#from managers.table_manager import TableManager

from base.base_form import BaseForm
from ui.ui_form_case import Ui_form_case
from controllers.case_controller import CaseController
from services.case_service import CaseService
from utils.form_mode import FormMode
from views.campaigns import ExecutionCampaign
from views.dialogs import Dialog

#from config.page_config import PAGES
#from config.form_config import FORMS

#from controllers.main_controller import MainController
from db.db import DatabaseManager

class FormCase(BaseForm):
    data_updated = Signal(str)

    def __init__(self, mode:FormMode, db_id: Optional[int]):
        super().__init__("cases", mode, db_id)

        # Create managers and controller
        db_manager = DatabaseManager()
        service = CaseService(db_manager)
        controller = CaseController(service)

        # Setup form
        self.setup_form(Ui_form_case, controller)

    def _setup_custom_widgets(self):
        lw_data = self.controller.get_lw_data()
        self.setup_checkbox_list(self.ui.lw_system, lw_data["systems"])
        self.setup_checkbox_list(self.ui.lw_section, lw_data["sections"])
        self.setup_checkbox_list(self.ui.lw_operator, lw_data["operators"])
        self.setup_checkbox_list(self.ui.lw_drone, lw_data["drones"])
        self.setup_checkbox_list(self.ui.lw_uhub_user, lw_data["uhub_users"])

    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return
        
        self.ui.le_id.setText(formatted_data['code'])
        self.ui.le_definition.setText(formatted_data['definition'])
        self.set_checked_items(self.ui.lw_system, formatted_data['systems'])
        self.set_checked_items(self.ui.lw_section, formatted_data['sections'])