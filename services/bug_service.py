from db.db import DatabaseManager
from config.model_domains import Bug
from typing import Any, Dict, Optional, List

class BugService:
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.active_forms = {}

    def get_systems(self):
        systems = self.db_manager.get_all_data("systems")
        return [system["name"] for system in systems] if systems else []

    def get_campaigns(self):
        campaigns = self.db_manager.get_all_data("campaigns")
        return [campaign["name"] for campaign in campaigns] if campaigns else []

    def get_requirements(self):
        requirements = self.db_manager.get_all_data("requirements")
        return [requirement["code"] for requirement in requirements] if requirements else []

    def save_bug(self, bug: Bug) -> None:
        data = {
            'status': bug.status,
            'system_id': bug.system_id,
            'campaign_id': bug.campaign_id,
            'requirements': bug.requirements,
            'version': bug.version,
            'service_now_id': bug.service_now_id,
            'short_desc': bug.short_desc,
            'definition': bug.definition,
            'urgency': bug.urgency,
            'impact': bug.impact,
            'file': bug.file
        }

        if bug.id:
            self.db_manager.edit_register("bugs", bug.id, data)
            return None
        else:
            bug_id = self.db_manager.create_register("bugs", data)
            return bug_id
    
    def get_bug(self, db_id: int):
        return self.db_manager.get_by_id("bugs", db_id)

    def _on_form_closed(self, form_key: str):
        self.active_forms.pop(form_key, None)
