from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QCheckBox
from ui.ui_form_requirements import Ui_form_requirement
from typing import List,Optional

from db.db import DatabaseManager
from utils.form_mode import FormMode
from controllers.requirements_controller import RequirementsController
from services.requirement_service import RequirementService

# Page to manage the creation or edition of bugs
class FormRequirement(QWidget):
    data_updated = Signal(str)

    def __init__(self, mode:FormMode, db_id: Optional[int]):
        super().__init__()
        self.ui = Ui_form_requirement()
        self.ui.setupUi(self)

        self.mode = mode
        self.db_id = db_id

        title = "Edit requirement" if mode == FormMode.EDIT else "Add requirement"
        self.setWindowTitle(title)

        # Create managers and controller
        db_manager = DatabaseManager()
        service = RequirementService(db_manager)
        self.controller = RequirementsController(service)

        lw_data = self.controller.get_lw_data()
        self.setup_lw(self.ui.lw_system, lw_data["systems"])
        self.setup_lw(self.ui.lw_section, lw_data["sections"])

        self._setup_buttons()

    def setup_lw(self, list_widget: QListWidget, options: List[str]):
        for option in options:
            item = QListWidgetItem(list_widget)
            checkbox = QCheckBox(option)
            list_widget.setItemWidget(item, checkbox)
    
    def _setup_buttons(self):
        self.ui.btn_accept.clicked.connect(lambda _:self._handle_db_register())
        self.ui.btn_cancel.clicked.connect(self.close)

    def _handle_db_register(self):

        data = self._obtain_form_data()
        errors = self.validate_form(data)
        
        if errors:
            self.show_errors(errors)
            return
            
        try:
            self.controller.handle_form_submission(data, self.db_id)
            self.data_updated.emit("requirements")
            self.close()
        except Exception as e:
            self.show_critical(str(e)) 

    # Función que obtenga los datos del formulario tal cual están introducidos
    def _obtain_form_data(self):

        selected_systems = []
        selected_sections = []
        
        for i in range(self.ui.lw_system.count()):
            item = self.ui.lw_system.item(i)
            checkbox = self.ui.lw_system.itemWidget(item) 
            if checkbox.isChecked():
                selected_systems.append(checkbox.text())
        
        for i in range(self.ui.lw_section.count()):
            item = self.ui.lw_section.item(i)
            checkbox = self.ui.lw_section.itemWidget(item)
            if checkbox.isChecked():
                selected_sections.append(checkbox.text())
        
        return {
            'code': self.ui.le_id.text(),
            'definition': self.ui.le_definition.text(),
            'systems': selected_systems,
            'sections': selected_sections
        }
    
    def validate_form(self, data):
        """Valida los datos del formulario."""
        errors = []
        
        if not data['code']: 
            errors.append("Defining an ID is mandatory")
        if not data['definition']: 
            errors.append("Writing a definition for the requirement is mandatory")
        if not data['systems']: 
            errors.append("Choosing (at least) one associated system is mandatory")
        if not data['sections']:
            errors.append("Choosing (at least) one associated section is mandatory")
            
        return errors
    
    def save_data(self, data):
        if self.mode == FormMode.CREATE:
            self.service.create_requirement(data)
        elif self.mode == FormMode.EDIT:
            self.service.edit_requirement(data)            
    
    # Función que cargue los datos al formulario obteniendolos de la variable data que viene de open form (si existe, si no return).
    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return
        
        # Load basic data
        self.ui.le_id.setText(formatted_data['code'])
        self.ui.le_definition.setText(formatted_data['definition'])

        # Load selected systems
        self._set_list_selections(self.ui.lw_system, formatted_data['systems'])

        # Load selected sections
        self._set_list_selections(self.ui.lw_section, formatted_data['sections']) 

    def _set_list_selections(self, list_widget: QListWidget, selected_items: List[str]):
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            checkbox = list_widget.itemWidget(item)
            checkbox.setChecked(checkbox.text() in selected_items)