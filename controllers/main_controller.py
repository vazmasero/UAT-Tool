from typing import Optional, Any, List

from PySide6.QtWidgets import QTableView
from PySide6.QtCore import Slot, QItemSelectionModel

from config.app_config import BaseUI
from config.table_config import TABLES
from config.form_config import FORMS
from config.page_config import PAGES
from db.db import DatabaseManager
from managers.table_manager import TableManager
from managers.page_manager import PageManager
from managers.form_manager import FormManager
from services.form_service import FormRegistry, FormOpener
from managers.table_manager import TableManager
from utils.dict_utils import get_form_key


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

        self._connect_signals()
        
    def _connect_signals(self):
        
        # Connect signals coming from TableManager
        self.table_manager.table_double_clicked.connect(self.handle_table_double_click)
        self.table_manager.selection_changed.connect(self.handle_selection_changed)
        #self.table_manager.table_updated.connect(self.handle_table_updated)
        
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
    def handle_table_double_click(self, edit_mode: bool = True, data: Optional[Any]=None):
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        form_key = self.form_manager.get_form_key(current_page, tab_index)
        
        if not form_key:
            return
        self.form_manager.open_form(form_key, edit_mode, data)
        
    @Slot()
    def handle_selection_changed(self, table:Optional[QTableView], data:Optional[List[List]]):
        
        if table:
            if table.selectionModel().hasSelection():
                self.ui.btn_edit.setEnabled(True)
                self.ui.btn_remove.setEnabled(True)
            else:
                self.ui.btn_edit.setEnabled(False)
                self.ui.btn_remove.setEnabled(False)
        
        self.ui.btn_add.setEnabled(True)
        
    @Slot()
    def handle_new_form(self, edit: bool):
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        
        form_key = self.form_manager.get_form_key(current_page, tab_index)
        if not form_key:
            return
        
        data = None
        if edit:
            table_name = PAGES[current_page]["config"].tables[tab_index or 0]
            selected_data = self.table_manager.get_selected_rows_data(table_name)
            if not selected_data:
                return
            
        self.form_manager.open_form(form_key, edit, data)
    
            
            