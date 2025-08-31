from db.db import DatabaseManager
from typing import Dict, Any


class StepService:

    def __init__(self, db_manager: DatabaseManager, table_manager=None):
        self.db_manager = db_manager
        self.table_manager = table_manager

    def get_requirements(self):
        """Obtains all requirements for their selection in step"""
        requirements = self.db_manager.get_all_data("requirements")
        return [requirement["code"]
                for requirement in requirements] if requirements else []

    def create_step_data(
            self, step_form_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'action': step_form_data.action,
            'expected_result': step_form_data.expected_result,
            'affected_requirements': step_form_data.affected_requirements,
            'comments': step_form_data.comments,
        }

    def format_step_data(self, data):
        """Formatea datos de step para display en tabla"""
        if not data:
            return None

        if 'Id' in data:
            # Header as key (desde tabla):
            return {
                'id': data['Id'],
                'action': data['Action'],
                'expected_result': data['Expected result'],
                'affected_requirements': [r.strip() for r in data['Affected requirements'].split(',')] if data['Affected requirements'] else [],
                'comments': data['Comments'],
            }
        else:
            return data
