from services.case_service import CaseService
from config.model_domains import Case
from typing import Optional, Dict

class CaseController:
    def __init__(self, service: CaseService):
            self.service = service

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
        
    def handle_form_submission(self, form_data: Dict, db_id: Optional[int]) -> None:
        case = Case(
            id=db_id,
            code=form_data['identification'],
            name=form_data['name'],
            systems=form_data['systems'],
            sections=form_data['sections'],
            operators=form_data['operators'],
            drones=form_data['drones'],
            uhub_users=form_data['uhub_users'],
            comments=form_data['comments']
        )
        
        self.service.save_requirement(case)
        
    def handle_new_step(self):
        form_instance = self.service.open_step_form('steps', False, data=None)
        
        if form_instance and hasattr(form_instance, 'data_updated'):
            form_instance.data_updated.connect(self.refresh_table_data)
        
        
    def setup_tables(self, ui):
        self.service.setup_tables(ui)
        
    def refresh_table_data():
        pass
