from typing import Dict, Optional, Any
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from base.base_form import BaseForm
from ui.ui_execution_campaign import Ui_execution_campaign
from ui.ui_form_campaign import Ui_form_campaign
from controllers.campaing_form_controller import CampaignFormController
from services.campaign_form_service import CampaignFormService
from utils.form_mode import FormMode

from db.db import DatabaseManager


# Page to manage the creation or edition of campaigns
class FormCampaign(BaseForm):
    def __init__(self, mode: FormMode, db_id: Optional[int]):
        super().__init__("campaigns", mode, db_id)
        self.ui = Ui_form_campaign()
        
        self.selected_block_ids = set()
        
        # Create managers and controller
        self.db_manager = DatabaseManager()

        self.service = CampaignFormService(self.db_manager)
        self.controller = CampaignFormController(self.service)
        
        # Setup form
        self.setup_form(Ui_form_campaign, self.controller)
        self._on_system_changed()
        
    def _setup_custom_widgets(self):
        self.ui.cb_system.currentTextChanged.connect(self._on_system_changed)
        if self.mode != FormMode.EDIT:
            self._update_blocks_list()
        
    def _on_system_changed(self):
        self.selected_block_ids = set()
        self._update_blocks_list()
        
    def _update_blocks_list(self):
        system_name = self.ui.cb_system.currentText()
        blocks = self.controller.get_blocks_by_system(system_name)
        self.ui.lw_blocks.clear()

        for block in blocks:
            item = QListWidgetItem(
                f"{block['identification']} - {block['name']}")
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setData(Qt.UserRole, block.get("id"))
            if block.get("id") in self.selected_block_ids:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.ui.lw_blocks.addItem(item)
            
    def load_data(self, data):
        """Loads data into the form."""
        formatted_data = self.controller.prepare_form_data(data)
        if not formatted_data:
            return

        # Set the form fields with the formatted data
        self.ui.le_identification.setText(formatted_data['identification'])
        self.ui.le_description.setText(formatted_data['description'])
        self.ui.le_version.setText(formatted_data['version'])
        self.set_checked_items(self.ui.lw_blocks, formatted_data['blocks'])
        
    def _handle_submit(self):
        """Handles form submission for a campaign, including associated blocks."""
        try:
            data = self._obtain_form_data()
            errors = self.validate_form(data)

            if errors:
                self.show_errors(errors)
                return

            self.controller.handle_form_submission(
                data, self.db_id)
            self.data_updated.emit(self.form_key)
            self.close()
        except Exception as e:
            self.show_critical(f"Error submitting form: {str(e)}")
            
    def _obtain_form_data(self) -> Dict[str, Any]:
        return {
            'identification': self.ui.le_identification.text(),
            'description': self.ui.le_description.text(),
            'system': self.ui.cb_system.currentText(),
            'version': self.ui.le_version.text(),
            'blocks': self.get_checked_block_ids()
        }
        
    def get_checked_block_ids(self):
        checked_ids = []
        for i in range(self.ui.lw_blocks.count()):
            item = self.ui.lw_blocks.item(i)
            if item.checkState() == Qt.Checked:
                checked_ids.append(item.data(Qt.UserRole))

        return checked_ids
    
    def validate_form(self, data):
        """Validates form data."""
        errors = []

        if not data['identification']:
            errors.append("Defining an identification is mandatory")
        if not data['description']:
            errors.append("Writing a description for the campaign is mandatory")
        if not data['system']:
            errors.append("Choosing one associated system is mandatory")
        if not data['version']:
            errors.append("Writing a system version is mandatory")
        if not data['blocks']:
            errors.append("Selecting at least one test block is mandatory")

        return errors
        
    
        
    
        
        
        
        
        
        
        
        
        
        
# Page to manage the execution of test campaigns
class ExecutionCampaign(BaseForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_execution_campaign()
        self.ui.setupUi(self)
