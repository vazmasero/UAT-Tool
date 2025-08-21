from typing import Optional, List

from PySide6.QtWidgets import QTableView
from PySide6.QtCore import Slot

from config.app_config import BaseUI
from config.table_config import TABLES
from config.page_config import PAGES
from db.db import DatabaseManager
from managers.table_manager import TableManager
from managers.page_manager import PageManager
from managers.form_manager import FormManager

class MainController:
    def __init__(self, 
                 ui: BaseUI,
                 page_manager: Optional[PageManager],
                 form_manager: FormManager,
             table_manager: TableManager,
                 db_manager: DatabaseManager):
        self.ui = ui
        self.page_manager = page_manager
        self.form_manager = form_manager
        self.table_manager = table_manager
        self.db_manager = db_manager
        
    def _change_page(self, page_name:str):
        if self.page_manager:
            self.page_manager.change_page(page_name)
        else:
            print("This windows does not have multiple pages")
    
    def setup_tables(self):
        for table_name, table_dict in TABLES.items():
            table_info = table_dict["config"]
            table_widget = getattr(self.ui, table_info.widget_name, None)
            if not table_widget:
                print(f"Widget for table '{table_name}' not found. ")
                continue
            data = self.db_manager.get_all_data(table_info.db_table)
            self.table_manager.setup_table(table_widget, table_name, data, register=True)
        
    @Slot()
    def handle_selection_changed(self, table:Optional[QTableView]):
        
        if table:
            if table.selectionModel().hasSelection():
                self.ui.btn_edit.setEnabled(True)
                self.ui.btn_remove.setEnabled(True)
            else:
                self.ui.btn_edit.setEnabled(False)
                self.ui.btn_remove.setEnabled(False)
        
        self.ui.btn_add.setEnabled(True)
      
    @Slot()  
    def _handle_remove_button(self):
        
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        
        form_key = self.form_manager.get_form_key(current_page, tab_index)
        if not form_key:
            return
    
        record_id = None 
        
        table_name = PAGES[current_page]["config"].tables[tab_index or 0]
        record_id = self.table_manager.get_selected_record_id(table_name)
        if not record_id:
            return
        
        try:
            self.db_manager.delete_register(table_name, record_id)
            self.refresh_table_data(table_name)
            
        except Exception as e:
            print(f"Error deleting register {record_id} from table '{table_name}': {e}")
        
    @Slot()
    def handle_new_form(self, edit: bool):
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        
        form_key = self.form_manager.get_form_key(current_page, tab_index)
        if not form_key:
            return
        
        data = None
        record_id = None 
        
        if edit:
            table_name = PAGES[current_page]["config"].tables[tab_index or 0]
            # Obtain real Id from database
            record_id = self.table_manager.get_selected_record_id(table_name)
            if not record_id:
                return
            
            # Obtain full data from db
            data = self.db_manager.get_by_id(table_name, record_id)
            if not data:
                return
        
        # Opens the form using FormManager and returns the form instance
        form_instance = self.form_manager.open_form(form_key, edit, data)

        # Returned form instance is used to handle event of updated data in db 
        # (to refresh the appropriate table)
        if form_instance and hasattr(form_instance, 'data_updated'):
            form_instance.data_updated.connect(self.refresh_table_data)
            
    @Slot()
    def handle_menu_add(self, form_key: str, edit: bool, data: Optional[List]=None):
        form_instance = self.form_manager.open_form(form_key, edit, data)
        
        if form_instance and hasattr(form_instance, 'data_updated'):
            form_instance.data_updated.connect(self.refresh_table_data)
            
    @Slot()
    def refresh_table_data(self, table_name: str):
        try:
            new_data = self.db_manager.get_all_data(table_name)
            
            self.table_manager.update_table_model(table_name, new_data)
            print(f"Table '{table_name}' updated successfully")
        except Exception as e:
            print(f"Error updating table '{table_name}': {e}")
            
    def close_program(self):
        self.form_manager.close_all_forms()
            
            