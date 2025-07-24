from db.db import DatabaseManager
from config.model_domains import Case
from config.case_table_config import CASE_TABLES
from config.step_form_config import STEP_FORMS
from utils.form_mode import FormMode
from typing import Dict, Optional, List

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
        return [operator["name"] for operator in operators] if operators else []

    def get_drones(self):
        drones = self.db_manager.get_all_data("drones")
        return [drone["name"] for drone in drones] if drones else []

    def get_uhub_users(self):
        uhub_users = self.db_manager.get_all_data('uhub_users')
        return [uhub_user["username"] for uhub_user in uhub_users] if uhub_users else []
    
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

        if case.id:
            self.db_manager.edit_register("cases", case.id, data)
        else:
            self.db_manager.create_register("cases", data)
            
    def setup_tables(self, ui):
        for table_name, table_dict in CASE_TABLES.items():
            table_info = table_dict["config"]
            table_widget = getattr(ui, table_info.widget_name, None)
            if not table_widget:
                print(f"Widget for table '{table_name}' not found. ")
                continue
            data = self.db_manager.get_all_data(table_info.db_table)
            self.table_manager.setup_table(table_widget, table_name, data, register=True)
            
    def open_step_form(self, form_key:str, edit:bool, data:Optional[List]):
        if form_key in self.active_forms:
            self.active_forms[form_key].close()
            self.active_forms.pop(form_key, None)
            
        form_config = STEP_FORMS[form_key]['config']
        
        mode = FormMode.EDIT if edit else FormMode.CREATE
        db_id = data.get('id', None) if data and edit else None
        
        form_instance = form_config.form_class(mode=mode, db_id=db_id, table_manager=self.table_manager)

        #form_instance.data_updated.connect(self.data_updated.emit)
        form_instance.destroyed.connect(lambda: self._on_form_closed(form_key))

        form_instance.show()
        self.active_forms[form_key] = form_instance
        
        return form_instance
    
    def _on_form_closed(self, form_key: str):
        self.active_forms.pop(form_key, None)

    def refresh_table_data(self, table):
        pass

    def get_steps_by_case_id(self, db_id):
        # PENDIENTE: Hay que filtrar los pasos por el caso actual
        # Asumiendo que el caso actual está almacenado en algún lugar
        return self.db_manager.get_all_data("steps")