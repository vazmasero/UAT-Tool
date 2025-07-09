import sqlite3
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton, QVBoxLayout, QDialog , QListWidget, QListWidgetItem, QCheckBox
from ui.ui_form_requirements import Ui_form_requirement
from typing import List

from db.db import DatabaseManager
from db.models import System, Section
from base.base_form import BaseForm
from services.requirement_service import RequirementService

# Page to manage the creation or edition of bugs
class FormRequirement(BaseForm):
    
    operation_completed = Signal()
    
    def __init__(self):
        db_manager = DatabaseManager()
        super().__init__(db_manager=db_manager, ui=Ui_form_requirement())
        self.service = RequirementService(db_manager)

        # Obtaining systems and sections (req) from DB
        systems = self.db_manager.get_all_data('systems')
        sections = self.db_manager.get_all_data('sections')
        
        # Setup for list widgets
        self._setup_cb(self.ui.lw_system, [s['name'] for s in systems])
        self._setup_cb(self.ui.lw_section, [s['name'] for s in sections])
        
        self._setup_buttons()
        
    def _setup_cb(self, list_widget = QListWidget, options=List):
        
        for option in options: 
            item = QListWidgetItem(list_widget)
            checkbox = QCheckBox(option)
            list_widget.setItemWidget(item, checkbox)
            
    def _setup_buttons(self):
        self.ui.btn_accept.clicked.connect(lambda _:self._handle_db_register())
        self.ui.btn_cancel.clicked.connect(self.close)
        
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
        
        # Crear un diccionario con los datos
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
        if self.windowTitle() == "Add requirement":
            self.service.create_requirement(data)
        else:
            requirement_id = getattr(self, 'requirement_id', 0)
            self.service.edit_requirement(requirement_id, data)
    
    # Función que cargue los datos al formulario obteniendolos de la variable data que viene de open form (si existe, si no return).
    def load_data(self, data):
        """Carga los datos en el formulario."""
        if not data:
            return
            
        # Cargar datos básicos
        self.ui.le_id.setText(data.code)
        self.ui.le_definition.setText(data.definition)
        
        # Cargar sistemas seleccionados
        if data.systems:
            selected_systems = [s.strip() for s in data.systems.split(',')]
            for i in range(self.ui.lw_system.count()):
                item = self.ui.lw_system.item(i)
                checkbox = self.ui.lw_system.itemWidget(item)
                checkbox.setChecked(checkbox.text() in selected_systems)
        
        # Cargar secciones seleccionadas
        if data.sections:
            selected_sections = [s.strip() for s in data.sections.split(',')]
            for i in range(self.ui.lw_section.count()):
                item = self.ui.lw_section.item(i)
                checkbox = self.ui.lw_section.itemWidget(item)
                checkbox.setChecked(checkbox.text() in selected_sections)