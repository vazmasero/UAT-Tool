from database.db import DatabaseManager
from config.model_domains import Campaign
from typing import Any, Dict, List, Optional


class CampaignFormService:

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.active_forms = {}

    def get_blocks_by_system(self, system_name: str) -> list:
        """ Retrieves all blocks associated with a specific system """
        all_blocks = self.db_manager.get_all_data("blocks")
        filtered = []
        for block in all_blocks:
            system = block.get('system', [])
            if isinstance(system, str):
                system = [s.strip() for s in system.split(',')]
            if system_name in system:
                filtered.append(block)
        return filtered

    def save_campaign(self, campaign: Campaign, block_ids: List[int], db_id: Optional[int]=None) -> None:
        data = {
            'identification': campaign.identification,
            'description': campaign.description,
            'system': campaign.system,
            'version': campaign.version,
            'blocks': block_ids
        }
        
        campaign_id = db_id

        if campaign_id:
            self.db_manager.edit_register("campaigns", campaign_id, data)
        else:
            campaign_id = self.db_manager.create_register("campaigns", data)

        return campaign_id

    def _on_form_closed(self, form_key: str):
        self.active_forms.pop(form_key, None)

    def get_campaign(self, campaign_id: int) -> Campaign:
        data = self.db_manager.get_by_id("campaigns", campaign_id)
        return data
