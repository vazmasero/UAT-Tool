from base.base_form import BaseForm
from ui.ui_add_step import Ui_add_step
from controllers.step_controller import StepController
from services.step_service import StepService
from db.db import DatabaseManager
from utils.form_mode import FormMode
from typing import Optional, Dict, Any
from PySide6.QtCore import Signal


class FormStep(BaseForm):

    new_step_data = Signal(dict)

    def __init__(self, mode: FormMode, db_id: Optional[int] = None,
                 data: Optional[Dict] = None, row_index: Optional[int] = None):
        if data and not db_id:
            db_id = data.get('Id')

        super().__init__("steps", mode, db_id)
        self.initial_data = data
        self.row_index = row_index

        # Create managers and controller
        db_manager = DatabaseManager()
        service = StepService(db_manager)
        controller = StepController(service)

        # Setup form
        self.setup_form(Ui_add_step, controller)

    def _setup_initial_data(self):
        """Sets up initial data for the form if edit mode."""
        if self.mode == FormMode.EDIT:
            if self.initial_data:
                # Usar datos pasados directamente (desde tabla)
                self.load_data(self.initial_data)
            elif self.db_id:
                # Cargar desde BD (comportamiento original)
                data = self.controller.get_item_by_id(self.db_id)
                if data:
                    self.load_data(data)

    def _setup_custom_widgets(self):
        lw_data = self.controller.get_lw_data()
        self.setup_checkbox_list(
            self.ui.lw_requirements,
            lw_data["requirements"])

    def _handle_submit(self):
        """Handles form submission."""
        try:
            data = self._obtain_form_data()
            errors = self.validate_form(data)

            if errors:
                self.show_errors(errors)
                return

            if self.mode == FormMode.CREATE:
                self.new_step_data.emit(data)
            else:
                data['id'] = self.db_id
                data['row_index'] = self.row_index[0]
                self.new_step_data.emit(data)

            self.close()
        except Exception as e:
            self.show_critical(f"Error submitting form: {str(e)}")

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
        if not data['expected_result']:
            errors.append(
                "Writing an expected result for the step is mandatory")
        if not data['affected_requirements']:
            errors.append(
                "Choosing (at least) one affected requirement is mandatory")

        return errors

    # Función que cargue los datos al formulario obteniendolos de la variable
    # data que viene de open form (si existe, si no return).
    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return

        self.ui.le_action.setText(formatted_data['action'])
        self.ui.le_expected_result.setText(formatted_data['expected_result'])
        self.set_checked_items(
            self.ui.lw_requirements,
            formatted_data['affected_requirements'])
        self.ui.le_comments.setText(formatted_data['comments'])
