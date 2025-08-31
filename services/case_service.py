from db.db import DatabaseManager
from config.model_domains import Case
from config.case_table_config import CASE_TABLES
from typing import Any, Dict, List


class CaseService:

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.active_forms = {}

    def get_systems(self):
        systems = self.db_manager.get_all_data("systems")
        return [system["name"] for system in systems] if systems else []

    def get_sections(self):
        sections = self.db_manager.get_all_data("sections")
        return [section["name"] for section in sections] if sections else []

    def get_operators(self):
        operators = self.db_manager.get_all_data("operators")
        return [operator["name"]
                for operator in operators] if operators else []

    def get_drones(self):
        drones = self.db_manager.get_all_data("drones")
        return [drone["name"] for drone in drones] if drones else []

    def get_uhub_users(self):
        uhub_users = self.db_manager.get_all_data('uhub_users')
        return [uhub_user["username"]
                for uhub_user in uhub_users] if uhub_users else []

    def save_case(self, case: Case) -> None:
        data = {
            'identification': case.identification,
            'name': case.name,
            'systems': case.systems,
            'sections': case.sections,
            'operators': case.operators,
            'drones': case.drones,
            'uhub_users': case.uhub_users,
            'comments': case.comments
        }

        case_id=case.id
        if case.id:
            self.db_manager.edit_register("cases", case.id, data)
        else:
            case_id = self.db_manager.create_register("cases", data)

        return case_id

    def save_step(self, step_data: Dict[str, Any]) -> int:
        step_fields = {
            'action': step_data.get('action'),
            'expected_result': step_data.get('expected_result'),
            'affected_requirements': step_data.get('affected_requirements'),
            'comments': step_data.get('comments'),
            'case_id': step_data.get('case_id')
        }

        step_id = self.db_manager.create_register("steps", step_fields)
        return step_id

    def setup_tables(self, ui):
        for table_name, table_dict in CASE_TABLES.items():
            table_info = table_dict["config"]
            table_widget = getattr(ui, table_info.widget_name, None)
            if not table_widget:
                print(f"Widget for table '{table_name}' not found. ")
                continue
            data = self.db_manager.get_all_data(table_info.db_table)
            self.table_manager.setup_table(
                table_widget, table_name, data, register=True)

    def _on_form_closed(self, form_key: str):
        self.active_forms.pop(form_key, None)

    def get_case(self, case_id: int) -> Case:
        data = self.db_manager.get_by_id("cases", case_id)
        return data

    def save_case_and_steps(
            self, case: Case, steps_data: List[Dict[str, Any]]) -> None:
        """ Saves a case and updates/creates/eliminates the associated steps"""

        data = {
            'identification': case.identification,
            'name': case.name,
            'systems': case.systems,
            'sections': case.sections,
            'operators': case.operators,
            'drones': case.drones,
            'uhub_users': case.uhub_users,
            'comments': case.comments,
            'steps': steps_data
        }

        if case.id:
            # Edit case and associated steps
            self.db_manager.edit_register("cases", case.id, data)
        else:
            # Crear caso y steps asociados
            case_id = self.db_manager.create_register("cases", data)
            for step in steps_data:
                step['case_id'] = case_id
                self.save_step(step)
