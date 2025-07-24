from services.step_service import StepService
from config.model_domains import Step
from typing import Optional, Dict

class StepController:
    def __init__(self, service: StepService):
            self.service = service

    def get_lw_data(self):
        requirements = self.service.get_requirements()
        return {
            "requirements": requirements
        }
    
    def handle_form_submission(self, form_data: Dict, db_id: Optional[int]) -> None:
        step = Step(
            id=db_id,
            action=form_data['action'],
            expected_result=form_data['expected_result'],
            affected_requirements=form_data['affected_requirements'],
            comments=form_data['comments']
        )
        
        self.save_step(step)

    def prepare_form_data(self, data):
        return self.service.format_step_data(data)

    def save_step(self, step_data):
        """Handles temporarily saving a step into the table model."""
        new_step_row = self.service.create_step_data(step_data)
        if not new_step_row:
            return "Error: Step data is incomplete or invalid."
        
        if 'steps' not in self.table_manager.tables:
            return "Error: Steps table not registered."
            
        table = self.table_manager.tables['steps']
        self.table_manager.add_row(table, new_step_row)
        return True

    def edit_step(self, step_id, new_data):
        """Handles editing a step."""
        try:
            self.service.edit_step(step_id, new_data)
        except ValueError as e:
            return f"Error: {str(e)}"

    def get_item_by_id(self, db_id):
        """Fetches a step item by its ID."""
        return self.service.get_step(db_id)

    def get_all_setps(self):
        """Fetches all requirements."""
        return self.service.get_all_steps()
