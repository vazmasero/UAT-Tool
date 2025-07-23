from services.case_service import CaseService
from config.model_domains import Case
from config.case_table_config import CASE_TABLES
from config.step_form_config import STEP_FORMS
from typing import Optional, Dict
from managers.steps_table_manager import StepTableManager

class CaseController:
    def __init__(self, service: CaseService, table_manager: StepTableManager):
        self.service = service
        self.table_manager = table_manager
        self._connect_signals()

    def _connect_signals(self):
        # Connect signals coming from TableManager
        self.table_manager.table_double_clicked.connect(lambda: self.handle_new_step)
        #self.table_manager.selection_changed.connect(self.handle_selection_changed)
        #self.table_manager.table_updated.connect(self.handle_table_updated)

    def get_lw_data(self):
        systems = self.service.get_systems()
        sections = self.service.get_sections()
        operators = self.service.get_operators()
        drones = self.service.get_drones()
        uhub_users = self.service.get_uhub_users()
        return {
            "systems": systems,
            "sections": sections,
            "operators": operators,
            "drones": drones,
            "uhub_users": uhub_users
        }
        
    def handle_form_submission(self, form_data: Dict, db_id: Optional[int]) -> None:
        case = Case(
            id=db_id,
            code=form_data['identification'],
            name=form_data['name'],
            systems=form_data['systems'],
            sections=form_data['sections'],
            operators=form_data['operators'],
            drones=form_data['drones'],
            uhub_users=form_data['uhub_users'],
            comments=form_data['comments']
        )
        
        self.service.save_case(case)
        
    def handle_new_step(self, row_data=None):
        form_key = 'steps'

        edit = row_data is not None
        data = row_data if edit else None

        form_instance = self.service.open_step_form(form_key, edit, data)
        
        if form_instance and hasattr(form_instance, 'data_updated'):
            form_instance.data_updated.connect(self.refresh_table_data)
        
    def setup_tables(self, ui):
        self.service.setup_tables(ui)

    def refresh_table_data(self, table):
        self.service.refresh_table_data(table)
