from database.db import DatabaseManager
from config.model_domains import Requirement


class RequirementService:

    def __init__(self, db_manager: DatabaseManager, table_manager=None):
        self.db_manager = db_manager
        self.table_manager = table_manager

    def get_requirement(self, requirement_id: int) -> Requirement:
        data = self.db_manager.get_by_id("requirements", requirement_id)
        return data

    def save_requirement(self, requirement: Requirement) -> None:
        data = {
            'code': requirement.code,
            'definition': requirement.definition,
            'systems': requirement.systems,
            'sections': requirement.sections
        }

        if requirement.id:
            self.db_manager.edit_register("requirements", requirement.id, data)
        else:
            self.db_manager.create_register("requirements", data)

    def get_systems(self):
        systems = self.db_manager.get_all_data("systems")
        return [system["name"] for system in systems] if systems else []

    def get_sections(self):
        sections = self.db_manager.get_all_data("sections")
        return [section["name"] for section in sections] if sections else []

    def format_requirement_data(self, data):
        if not data:
            return None

        if 'Id' in data:
            # Header as key:
            return {
                'id': data['Id'],
                'code': data['Assigned code'],
                'definition': data['Definition'],
                'systems': [s.strip() for s in data['System(s)'].split(',')] if data['System(s)'] else [],
                'sections': [s.strip() for s in data['Section(s)'].split(',')] if data['Section(s)'] else []
            }
        return data
