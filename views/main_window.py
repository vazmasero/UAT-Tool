from typing import Dict, Callable, Optional, Type, Any, List
from PySide6.QtCore import Slot, QObject
from PySide6.QtWidgets import QMainWindow, QDialog, QTableView

from ui.ui_main import Ui_main_window
from views.campaigns import ExecutionCampaign
from views.dialogs import Dialog

from config.form_config import FORMS
from config.page_config import PAGES

from controllers.main_controller import MainController

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        
        self._setup_controller()
        
        self._setup_tables()
        self._setup_buttons()

        self._connect_signals()
        
        self.controller._change_page("bugs")
        
    def _setup_controller(self):
        """Initializes controller"""
        self.controller = MainController(self.ui)
          
    def _setup_tables(self):
        self.controller.setup_tables()

    def _connect_signals(self):
        """Connects signals between managers and the view."""
        self._connect_menu_actions() # Menu bar actions
        
        self.ui.btn_add.clicked.connect(self.controller.handle_add_button)
        self.ui.btn_edit.clicked.connect(self._handle_edit_button)
        self.ui.btn_remove.clicked.connect(self._handle_remove_button)
        self.ui.btn_start.clicked.connect(self._execute_campaign)
        
    def _connect_menu_actions(self):
        view_actions = [
            (self.ui.action_view_bugs, "bugs"),
            (self.ui.action_view_campaigns, "campaigns"),
            (self.ui.action_view_management, "management"),
            (self.ui.action_view_requirements, "requirements"),
            (self.ui.action_view_assets, "assets"),
        ]

        for action, page_type in view_actions:
            action.triggered.connect(lambda _, pt=page_type: self.controller._change_page(pt))

        for form_key, form_info in FORMS.items():
            config = form_info["config"]
            if config.menu_action_attr:
                action = getattr(self.ui, config.menu_action_attr, None)
                if action:
                    action.triggered.connect(lambda _, fk=form_key: self.handle.open_form(fk))
    
    def _setup_buttons(self):
        """Sets up view's buttons (Add, Edit and Remove)."""

        # Initially, both edit and delete buttons are disabled
        self.ui.btn_edit.setEnabled(False)
        self.ui.btn_remove.setEnabled(False)
    
    def _handle_edit_button(self):
        tab_index = self.page_manager.get_current_tab_index()
        current_page = self.page_manager.current_page
        current_table = self.table_manager.get_current_table(current_page, tab_index)
        
        if not current_table:
            return
        
        selected_data = self.table_manager.get_selected_rows_data(current_table)
        if not selected_data:
            return
        
        self._handle_form_action(edit_mode=True, data=selected_data[0])
    
    def _handle_remove_button(self):
        current_table = self._get_current_table()
        if not current_table:
            return
        
        selected_rows = self.table_manager.get_selected_row_indices(current_table)
        if not selected_rows:
            return
        
        
        dialog = Dialog()
        dialog.ui.lbl_dialog.setText("Are you sure you want to delete {len(selected_rows)} item(s)? Changes will not be reversible.")
        dialog.setWindowTitle("Confirmation")
        
        if dialog.exec_() == QDialog.accepted:
            # Implementar aquí la lógica de la eliminación de registro (PENDIENTE).
            return
    
    @Slot()
    def _update_button_states(self, table=Optional[QTableView], data=Optional[List[List]]):
        
        if table:
            if table.selectionModel().hasSelection():
                self.ui.btn_edit.setEnabled(True)
                self.ui.btn_remove.setEnabled(True)
            else:
                self.ui.btn_edit.setEnabled(False)
                self.ui.btn_remove.setEnabled(False)
        
        self.ui.btn_add.setEnabled(True)

    @Slot()
    def _execute_campaign(self):
        form = ExecutionCampaign()
        form.setWindowTitle("Execute campaign")
        self.form_manager.register_form(form, "Execute campaign")
        form.show()
    
    @Slot()
    def _load_table_data(self, index):
        
        # Sender identifies which widget sent the signal. 
        sender = self.sender()
        
        if sender.objectName() == "stacked_main":
            # If sender is stacked_main, index is page index
            page_key = next(
                (key for key, info in PAGES.items() if info["config"].index == index), None
            )
            table_key = PAGES[page_key]["config"].tables[0]
        elif sender.objectName() == "tab_widget_management":
            # If sender is any of the tabs, index is the new tab
            page_key = "management"
            table_key = PAGES[page_key]["config"].tables[index]
        elif sender.objectName() == "tab_widget_assets":
            page_key = "assets"
            table_key = PAGES[page_key]["config"].tables[index]
        
        data = self.db_manager.get_all_data(table_key)
        self.table_manager.update_table_model(table_key, data)
        self._update_button_states(self.table_manager.tables[table_key], None)

    def _refresh_table(self, table_key):
        data = self.db_manager.get_all_data(table_key)
        self.table_manager.update_table_model(table_key, data)

    def closeEvent(self, event):
        self.form_manager.close_all_forms()
        super().closeEvent(event)
