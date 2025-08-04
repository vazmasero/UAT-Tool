from managers.table_manager import TableManager
from services.bug_service import BugService
from config.model_domains import Bug
from config.case_table_config import CASE_TABLES
from typing import Optional, Dict

from utils.form_mode import FormMode

class BugController:
    def __init__(self, service: BugService):
        self.service = service

    def get_lw_data(self):
        systems = self.service.get_systems()
        campaigns = self.service.get_campaigns()
        requirements = self.service.get_requirements()

        return {
            "systems": systems,
            "campaigns": campaigns,
            "requirements": requirements,
        }
        
    def handle_form_submission(self, form_data: Dict, db_id: Optional[int]) -> None:
        # Creates the bug and obtain de new id
        bug = Bug(
            id=db_id,
            status=form_data['status'],
            system_id=form_data['system'],
            campaign_id=form_data['campaign'],
            requirements=form_data['requirements'],
            version=form_data['version'],
            service_now_id=form_data['service_now_id'],
            short_desc=form_data['short_desc'],
            definition=form_data['definition'],
            urgency=form_data['urgency'],
            impact=form_data['impact'],
            file=form_data['file']
        )

        # Save the bug (new or edition)
        self.service.save_bug(bug)

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
        """Fetches a bug item by its ID."""
        return self.service.get_bug(db_id)

    def prepare_form_data(self, data: Dict) -> Dict:
        if not data:
            return None
        
        if 'Id' in data:
            # Header as key:
            return {
                'id': data['Id'],
                'status': data['Status'],
                'system': data['System'],
                'version': data['Version'],
                'service_now_id': data['ServiceNow ID'],
                'campaign_id': data['Campaign'],
                'requirements': [r.strip() for r in data[''].split(',')] if data['Requirements'] else [],
                'short_desc': data['Short Description'],
                'definition': data['Definition'],
                'urgency': data['Urgency'],
                'impact': data['Impact'],
                'file': data['Associated files'],
            }
        
        else:
            return data
    

