from typing import Dict, Callable, Optional, Type, Any, List
from PySide6.QtCore import Slot, Signal

from base.base_form import BaseForm
from managers.table_manager import TableManager
from ui.ui_form_case import Ui_form_case
from controllers.case_controller import CaseController
from services.case_service import CaseService
from utils.form_mode import FormMode

from db.db import DatabaseManager

class FormCase(BaseForm):

    def __init__(self, mode:FormMode, db_id: Optional[int]):
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
        self.ui.btn_add_step.clicked.connect(lambda _:self.controller.handle_new_step(edit=False, table_name="steps", row_data=None))
        #self.ui.btn_remove_step.clicked.connect(lambda _:self.controller._handle_remove_step())

        # Table signals
        self.table_manager.table_double_clicked.connect(lambda table_name, row_data: self.controller.handle_new_step(edit=True, table_name=table_name, row_data=row_data))
        #self.table_manager.selection_changed.connect(self.controller.handle_selection_changed())

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
        
    def _obtain_form_data(self) -> Dict[str, Any]:
        return {
            'identification': self.ui.le_identification.text(),
            'name': self.ui.le_name.text(),
            'systems': self.get_checked_items(self.ui.lw_system),
            'sections': self.get_checked_items(self.ui.lw_section),
            'operators':self.get_checked_items(self.ui.lw_operator),
            'drones':self.get_checked_items(self.ui.lw_drone),
            'uhub_users':self.get_checked_items(self.ui.lw_uhub_user),
            'comments':self.get_checked_items(self.ui.le_comment)
        }
        
    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []
        
        if not data['identification']: 
            errors.append("Defining an identification is mandatory")
        if not data['name']: 
            errors.append("Writing a name for the case is mandatory")
        if not data['systems']:
            errors.append("Choosing (at least) one associated system is mandatory")
        if not data['sections']:
            errors.append("Choosing (at least) one associated section is mandatory")
            
        return errors