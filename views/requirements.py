from base.base_form import BaseForm
from ui.ui_form_requirements import Ui_form_requirement
from controllers.requirements_controller import RequirementController
from services.requirement_service import RequirementService
from database.db import DatabaseManager
from utils.form_mode import FormMode
from typing import Optional, Dict, Any

class FormRequirement(BaseForm):

    def __init__(self, mode: FormMode, db_id: Optional[int]):
        """Initializes requirements form.
        
        This form allows the creation and edition of requirements, including:
        - Identification code
        - Systems and sections assigned
        - Definition
        - Creation and update times

        Args
        ----
            mode (FormMode): form mode (create/edit)
            db_id (Optional[int]): Database id for the requirement if edit mode
            
        """
        super().__init__("requirements", mode, db_id)

        # Create managers and controller
        db_manager = DatabaseManager()
        service = RequirementService(db_manager)
        controller = RequirementController(service)

        # Setup form
        self.setup_form(Ui_form_requirement, controller)

    def _setup_custom_widgets(self):
        lw_data = self.controller.get_lw_data()
        self.setup_checkbox_list(self.ui.lw_system, lw_data["systems"])
        self.setup_checkbox_list(self.ui.lw_section, lw_data["sections"])

    def _obtain_form_data(self) -> Dict[str, Any]:
        return {
            'code': self.ui.le_id.text(),
            'definition': self.ui.le_definition.text(),
            'systems': self.get_checked_items(self.ui.lw_system),
            'sections': self.get_checked_items(self.ui.lw_section)
        }

    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []

        if not data['code']:
            errors.append("Defining an ID is mandatory")
        if not data['definition']:
            errors.append(
                "Writing a definition for the requirement is mandatory")
        if not data['systems']:
            errors.append(
                "Choosing (at least) one associated system is mandatory")
        if not data['sections']:
            errors.append(
                "Choosing (at least) one associated section is mandatory")

        return errors

    # Función que cargue los datos al formulario obteniendolos de la variable
    # data que viene de open form (si existe, si no return).
    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return

        self.ui.le_id.setText(formatted_data['code'])
        self.ui.le_definition.setText(formatted_data['definition'])
        self.set_checked_items(self.ui.lw_system, formatted_data['systems'])
        self.set_checked_items(self.ui.lw_section, formatted_data['sections'])
