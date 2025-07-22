from base.base_form import BaseForm
from ui.ui_add_step import Ui_add_step
from controllers.step_controller import StepController
from services.step_service import StepService
from db.db import DatabaseManager
from utils.form_mode import FormMode
from typing import Optional, Dict, Any, List


class FormStep(BaseForm):

    def __init__(self, mode:FormMode, db_id: Optional[int]):
        super().__init__("steps", mode, db_id)

        # Create managers and controller
        db_manager = DatabaseManager()
        service = StepService(db_manager)
        controller = StepController(service)

        # Setup form
        self.setup_form(Ui_add_step, controller)    
        
    def _setup_custom_widgets(self):
        lw_data = self.controller.get_lw_data()
        self.setup_checkbox_list(self.ui.lw_requirements, lw_data["requirements"])

    def _obtain_form_data(self) -> Dict[str, Any]:
        return {
            'action': self.ui.le_action.text(),
            'expected_result': self.ui.le_expected_result.text(),
            'affected_requirements': self.get_checked_items(self.ui.lw_requirements),
            'comments': self.ui.le_comments.text(),
        }
    
    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []
        
        if not data['action']: 
            errors.append("Defining an action is mandatory")
        if not data['expected result']: 
            errors.append("Writing an expected result for the step is mandatory")
        if not data['affected_requirements']: 
            errors.append("Choosing (at least) one affected requirement is mandatory")
            
        return errors  
    
    # Función que cargue los datos al formulario obteniendolos de la variable data que viene de open form (si existe, si no return).
    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return
        
        self.ui.le_id.setText(formatted_data['code'])
        self.ui.le_definition.setText(formatted_data['definition'])
        self.set_checked_items(self.ui.lw_system, formatted_data['systems'])
        self.set_checked_items(self.ui.lw_section, formatted_data['sections'])