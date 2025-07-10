from typing import Dict, Callable, Optional, Type, Any, List
from PySide6.QtCore import Slot, QObject
from PySide6.QtWidgets import QMainWindow, QDialog, QTableView

from ui.ui_main import Ui_main_window
from pages.campaigns import ExecutionCampaign
from pages.dialogs import Dialog
from db.db import DatabaseManager

from config.form_config import FORMS
from config.table_config import TABLES
from config.page_config import PAGES
from managers.form_manager import FormRegistry, FormOpener
from managers.page_manager import PageManager
from managers.table_manager import TableManager

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self._setup_managers()
        self._setup_buttons()
        
        self._connect_signals()
        
        self.page_manager.change_page("bugs")

    def _setup_managers(self):
        """Inicializa los managers y configura la interacción entre ellos."""
        self.form_registry = FormRegistry()
        self.form_opener = FormOpener(self.form_registry, FORMS)
        self.page_manager = PageManager(self.ui.stacked_main, self.ui)
        self.table_manager = TableManager()
        self.db_manager = DatabaseManager()
    
        
        self._setup_tables()

    def _setup_tables(self):
        for key, table_dict in TABLES.items():
            table_info = table_dict["config"]
            table_widget = getattr(self.ui, table_info.widget_name)
            data = self.db_manager.get_all_data(key)
            self.table_manager.setup_table(table_widget, key, data, register=True)
    
    def _connect_signals(self):
        """Conecta señales entre managers y la vista."""
        self.ui.btn_add.clicked.connect(self._handle_add_button)
        self.ui.btn_edit.clicked.connect(self._handle_edit_button)
        self.ui.btn_remove.clicked.connect(self._handle_remove_button)
        self.ui.btn_start.clicked.connect(self._execute_campaign)
        
        self.table_manager.table_updated.connect(lambda: self.page_manager.refresh_page("bugs"))
        
        self._connect_menu_actions()
        
        self.table_manager.table_double_clicked.connect(lambda data: self._handle_form_action(edit_mode=True, data=data))
        self.table_manager.selection_changed.connect(lambda table, data: self._update_button_states(table, data))
        self.table_manager.table_updated.connect(self._refresh_table)
        
    def _connect_menu_actions(self):
        view_actions = [
            (self.ui.action_view_bugs, "bugs"),
            (self.ui.action_view_campaigns, "campaigns"),
            (self.ui.action_view_management, "management"),
            (self.ui.action_view_requirements, "requirements"),
            (self.ui.action_view_assets, "assets"),
        ]

        for action, page_type in view_actions:
            action.triggered.connect(lambda _, pt=page_type: self.page_manager.change_page(pt))

        for form_key, form_info in FORMS.items():
            config = form_info["config"]
            if config.menu_action_attr:
                action = getattr(self.ui, config.menu_action_attr, None)
                if action:
                    action.triggered.connect(lambda _, fk=form_key: self.form_manager.open_form(fk))
    
    def _setup_buttons(self):
        """Conecta botones principales de la interfaz."""
        self.ui.btn_add_bug.clicked.connect(lambda: self.form_opener.open_form("bugs"))
        self.ui.btn_add_campaign.clicked.connect(lambda: self.form_opener.open_form("campaigns"))

        # Initially, both edit and delete buttons are disabled
        self.ui.btn_edit.setEnabled(False)
        self.ui.btn_remove.setEnabled(False)

    def _handle_add_button(self):
        tab_index = self.page_manager.get_current_tab_index()
        current_page = self.page_manager.current_page
        page_config = PAGES[current_page]["config"]
        page_forms = page_config.forms
        if not page_forms:
            print("The page you are currently visiting does not have any form associated to it")
            return

        if tab_index is not None and tab_index < len(page_forms):
            form_key = page_forms[tab_index]
        else:
            form_key = page_forms[0]
        self.form_opener.open_form(form_key, edit_mode=False)
    
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

    @Slot()
    def _handle_form_action(self, edit_mode: bool = False, data: Optional[Any]=None):
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        page_config = PAGES[current_page]["config"]
        page_forms = page_config.forms
        if not page_forms:
            print("The page you are currently visiting does not have any form associated to it")
            return
        
        if tab_index is not None and tab_index < len(page_forms):
            form_key = page_forms[tab_index]
        else:
            form_key = page_forms[0]
        self.form_manager.open_form(form_key, edit_mode, data)
    
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
