from managers.table_manager import TableManager
from services.campaign_form_service import CampaignFormService
from config.model_domains import Campaign
from typing import Optional, Dict

from utils.form_mode import FormMode


class CampaignFormController:
    def __init__(self, service: CampaignFormService,
                 table_manager: TableManager = None):
        self.service = service
        self.table_manager = table_manager

    def get_blocks_by_system(self, system_name: str) -> list:
        """Fetches all cases associated with a system."""
        return self.service.get_blocks_by_system(system_name)

    def handle_form_submission(
        self, form_data: Dict, db_id: Optional[int]) -> None:
    
        campaign = Campaign(
            id=db_id,
            identification=form_data['identification'],
            description=form_data['description'],
            system=form_data['system'],
            version=form_data['version'],
            blocks=form_data['blocks']
        )
        
        selected_blocks_ids = form_data.get('blocks', [])
        
        if db_id:
            self.service.save_campaign(campaign, selected_blocks_ids, db_id)
        else:
            self.service.save_campaign(campaign, selected_blocks_ids)

    def prepare_form_data(self, data: Dict) -> Dict:
        if not data:
            return None

        if 'Id' in data:
            # Header as key:
            return {
                'id': data['Id'],
                'identification': data['Identification'],
                'description': data['Description'],
                'system': data['system'],
                'version': data['version']
            }
        return data
    
    def get_item_by_id(self, db_id):
        """Fetches a vampaign item by its ID."""
        return self.service.get_campaign(db_id)
