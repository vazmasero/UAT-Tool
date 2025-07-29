from managers.table_manager import TableManager
from services.case_service import CaseService
from config.model_domains import Case
from config.case_table_config import CASE_TABLES
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
            data = self.get_item_by_id(db_id)['steps']
            for step in data:
                if isinstance(step.get('affected_requirements'), list):
                    step['affected_requirements'] = ', '.join(step['affected_requirements'])

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
        
    def handle_form_submission(self, form_data: Dict, db_id: Optional[int], steps_table=None) -> None:
        # Creates the case and obtain de new id
        case = Case(
            id=db_id,
            identification=form_data['identification'],
            name=form_data['name'],
            systems=form_data['systems'],
            sections=form_data['sections'],
            operators=form_data['operators'],
            drones=form_data['drones'],
            uhub_users=form_data['uhub_users'],
            comments=form_data['comments']
        )
        
        # Obtain steps from the table
        steps_data = []
        if steps_table is not None:
            table = self.table_manager.tables.get('steps')
            raw_steps = self.table_manager.get_table_data(table)
            column_map = CASE_TABLES['steps']['config'].column_map
            for step in raw_steps:
                db_step = {}
                for header, value in step.items():
                    db_column = column_map.get(header, header)
                    if db_column == 'affected_requirements' and isinstance(value, str):
                        db_step[db_column] = [v.strip() for v in value.split(', ') if v.strip()]
                    else:
                        db_step[db_column] = value
                steps_data.append(db_step)

        # Save the case and steps (new or edition)
        if db_id:
            # EDIT: update case and steps
            self.service.save_case_and_steps(case, steps_data)
        else:
            # CREATE: create case and steps
            new_case_id = self.service.save_case(case)
            for db_step in steps_data:
                db_step['case_id'] = new_case_id
                self.service.save_step(db_step)

    def handle_new_step(self, edit: bool, table_name: str, row_data: Dict):
        from managers.form_manager import FormManager

        form_manager = FormManager()
        form_key = table_name

        # Obtain row index if editing
        row_index = None
        if edit and row_data and 'steps' in self.table_manager.tables:
            steps_table = self.table_manager.tables['steps']
            row_index = self.table_manager.get_selected_row_indices(steps_table)

        # Opens the form using FormManager and returns the form instance
        form_instance = form_manager.open_form(form_key, edit, row_data, data_instead_id=True, row_index=row_index)

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

        if 'id' in step_data and 'row_index' in step_data:
            self.table_manager.update_row(steps_table, formatted_data, step_data['row_index'])
        else:
            # CREATE: add new row
            self.table_manager.add_row(steps_table, formatted_data)

    def _format_step_for_table(self, step_data:Dict) -> Dict:
        return {
            'action': step_data.get('action', ''),
            'expected_result': step_data.get('expected_result', ''),
            'affected_requirements': ', '.join(step_data.get('affected_requirements', [])),
            'comments': step_data.get('comments', '')
        }
    
    def _handle_remove_step(self):   
        """Handles the removal of a step from the table."""   
        table = self.table_manager.tables.get('steps') 
        row_index = self.table_manager.get_selected_row_indices(table)
        if not row_index:
            return
        
        try:
            self.table_manager.delete_row(table, row_index[0])

        except Exception as e:
            print(f"Error deleting register {row_index} from table: {e}")

    def get_item_by_id(self, db_id):
        """Fetches a case item by its ID."""
        return self.service.get_case(db_id)

    def get_steps_by_case_id(self, case_id):
        """Fetches all steps associated with a case ID."""
        return self.service.get_steps_by_case_id(case_id)
    
    def prepare_form_data(self, data: Dict) -> Dict:
        if not data:
            return None
        
        if 'Id' in data:
            # Header as key:
            return {
                'id': data['Id'],
                'identification': data['Identification'],
                'name': data['Name'],
                'systems': [s.strip() for s in data['System(s)'].split(',')] if data['System(s)'] else [],
                'sections': [s.strip() for s in data['Section(s)'].split(',')] if data['Section(s)'] else [],
                'operators': [o.strip() for o in data['Operator(s)'].split(',')] if data['Operator(s)'] else [],
                'drones': [d.strip() for d in data['Drone(s)'].split(',')] if data['Drone(s)'] else [],
                'uhub_users': [u.strip() for u in data['U-hub user(s)'].split(',')] if data['U-hub user(s)'] else [],
            }
        else:
            return data
    

