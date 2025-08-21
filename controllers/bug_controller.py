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
    

