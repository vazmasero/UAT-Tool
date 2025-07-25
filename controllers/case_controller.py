from managers.table_manager import TableManager
from services.case_service import CaseService
from config.model_domains import Case
from config.case_table_config import CASE_TABLES
from config.step_form_config import STEP_FORMS
from typing import Optional, Dict

from utils.form_mode import FormMode

class CaseController:
    def __init__(self, service: CaseService, table_manager: TableManager = None):
        self.service = service
        self.table_manager = table_manager

    def setup_tables(self, ui, mode, db_id):
        table_name = 'steps'
        table_info = CASE_TABLES[table_name]["config"]
        table_widget = getattr(ui, table_info.widget_name, None)
        if not table_widget:
            print(f"Widget for table '{table_name}' not found. ")
            return

        data = []
        if mode == FormMode.EDIT and db_id is not None:
            data = self.service.get_steps_by_case_id(db_id)

        self.table_manager.setup_table(table_widget, table_name, data, register=True)

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

    def handle_new_step(self, edit: bool, table_name: str, row_data: Dict):
        from managers.form_manager import FormManager

        form_manager = FormManager()

        form_key = table_name

        # Opens the form using FormManager and returns the form instance
        form_instance = form_manager.open_form(form_key, edit, row_data, data_instead_id=True)

        # Returned form instance is used to handle event of updated data in db 
        # (to refresh the appropriate table)
        if form_instance and hasattr(form_instance, 'new_step_data'):
            form_instance.new_step_data.connect(self._handle_new_step_data)
            
    def _handle_new_step_data(self, step_data:Dict):
        if not self.table_manager or 'steps' not in self.table_manager.tables:
            print("Error: Steps table not available")
            return

        steps_table = self.table_manager.tables['steps']

        formatted_data = self._format_step_for_table(step_data)

        if 'id' in step_data:
            pass
            #self.table_manager.update_row(steps_table, formatted_data, step_data['id'])
        else:
        # Creación: añadir nueva fila
            self.table_manager.add_row(steps_table, formatted_data)

    def _format_step_for_table(self, step_data:Dict) -> Dict:
        return {
            'action': step_data.get('action', ''),
            'expected_result': step_data.get('expected_result', ''),
            'affected_requirements': ', '.join(step_data.get('affected_requirements', [])),
            'comments': step_data.get('comments', '')
        }
    
    def refresh_table_data(self, table):
        self.service.refresh_table_data(table)
