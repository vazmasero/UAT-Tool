from typing import Dict, Callable, Optional, Type, Any
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QDialog, QTableView
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui.ui_main import Ui_main_window
from pages.campaigns import ExecutionCampaign
from pages.dialogs import Dialog
from db import DatabaseManager

from config.forms_config import PageType, FormType, FORMS
from config.table_config import TABLES
from config.page_config import PAGES
from managers.form_manager import FormManager
from managers.page_manager import PageManager
from managers.table_manager import TableManager

class HomePage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        self.form_manager = FormManager()
        self.page_manager = PageManager(self.ui.stacked_main, self.ui)
        self.table_manager = TableManager()
        self.db_manager = DatabaseManager()
        
        self.current_page = self.page_manager.current_page
        
        self._setup_managers()
        self._connect_signals()
        
        self._update_button_states()
        
        self.page_manager.change_page(PageType.BUGS)

    def _setup_managers(self):
        self.page_manager.register_data_loader(PageType.BUGS, self._load_table_data)
        self.page_manager.register_data_loader(PageType.CAMPAIGNS, self._load_table_data)
        self.page_manager.register_data_loader(PageType.MANAGEMENT, self._load_table_data)
        self.page_manager.register_data_loader(PageType.REQUIREMENTS, self._load_table_data)
        self.page_manager.register_data_loader(PageType.ASSETS, self._load_table_data)    
        
        self._setup_tables()
        
        self.ui.tab_widget_management.currentChanged.connect(lambda index: self._load_table_data("management", index))
        self.ui.tab_widget_assets.currentChanged.connect(lambda index: self._load_table_data("assets", index))

    def _setup_tables(self):
        for name, table_info in TABLES.items():
            table_widget = getattr(self.ui, table_info.widget_name)
            data = self.db_manager.get_all_data(name)
            self.table_manager.setup_table(table_widget, name, data, table_info.headers, register=True)
    
    def _connect_signals(self):
        self._connect_menu_actions()
        self._connect_buttons()
        
        self.page_manager.page_changed.connect(self._update_button_states)
        
    
    def _connect_menu_actions(self):
        view_actions = [
            (self.ui.action_view_bugs, PageType.BUGS),
            (self.ui.action_view_campaigns, PageType.CAMPAIGNS),
            (self.ui.action_view_management, PageType.MANAGEMENT),
            (self.ui.action_view_requirements, PageType.REQUIREMENTS),
            (self.ui.action_view_assets, PageType.ASSETS),
        ]

        for action, page_type in view_actions:
            action.triggered.connect(lambda checked, pt=page_type: self.page_manager.change_page(pt))

        for form_key, form_info in FORMS.items():
            config = form_info["config"]
            if config.menu_action_attr:
                action = getattr(self.ui, config.menu_action_attr, None)
                if action:
                    action.triggered.connect(lambda checked, fk=form_key: self.form_manager.open_form(fk))
    
    def _connect_buttons(self):
        self.ui.btn_add.clicked.connect(self._handle_add_button)
        self.ui.btn_edit.clicked.connect(self._handle_edit_button)
        self.ui.btn_remove.clicked.connect(self._handle_remove_button)
        self.ui.btn_start.clicked.connect(self._execute_campaign)

    def _handle_add_button(self):
        self._handle_form_action(edit_mode=False)
    
    def _handle_edit_button(self):
        current_table = self._get_current_table()
        if not current_table:
            return
        
        selected_data = self.table_manager.get_selected_rows_data(current_table)
        if not selected_data:
            return
        
        self._handle_form_action(edit_mode=True, data=selected_data[0])

    def _handle_form_action(self, edit_mode: bool = False, data: Optional[Any]=None):
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        page_forms = PAGES.get(current_page, {}).get("forms", [])
        if not page_forms:
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
        
    def _handle_table_double_click(self, table:QTableView, row: int, row_data: list):
        form_key = self._get_form_key_for_table(table)
        if form_key:
            self.form_manager.open_form(form_key, edit_mode=True, data=row_data)
        
    def _handle_table_selection_changed(self, table: QTableView, selected_data: list):
        self._update_button_states()
        
    def _get_form_key_for_table(self, table: QTableView) -> Optional[str]:
        table_to_form_mapping={
            self.ui.tbl_bugs: "bug",
            self.ui.tbl_campaigns: "campaign", 
            self.ui.tbl_cases: "case",
            self.ui.tbl_requirements: "requirement",
            self.ui.tbl_emails: "email",
            self.ui.tbl_blocks: "block",
            self.ui.tbl_operators: "operator",
            self.ui.tbl_drones: "drone",
            self.ui.tbl_uas_zones: "uas_zone",
            self.ui.tbl_uhub_org: "uhub_org",
            self.ui.tbl_uhub_user: "uhub_user",
            self.ui.tbl_uspaces: "uspace",
        }
        return table_to_form_mapping.get(table)
    
    def _get_current_table(self) -> Optional[QTableView]:
        current_page = self.page_manager.current_page
        
        if current_page == PageType.BUGS:
            return self.ui.tbl_bugs
        elif current_page == PageType.CAMPAIGNS:
            return self.ui.tbl_campaigns
        elif current_page == PageType.REQUIREMENTS:
            return self.ui.tbl_requirements
        elif current_page == PageType.MANAGEMENT:
            tab_index = self.ui.tab_widget_management.currentIndex()
            if tab_index == 0:
                return self.ui.tbl_cases
            elif tab_index == 1:
                return self.ui.tbl_blocks
        elif current_page == PageType.ASSETS:
            tab_index = self.ui.tab_widget_assets.currentIndex()
            tables = [
                self.ui.tbl_emails,
                self.ui.tbl_operators, 
                self.ui.tbl_drones,
                self.ui.tbl_uas_zones,
                self.ui.tbl_uhub_orgs,
                self.ui.tbl_uhub_users,
                self.ui.tbl_uspaces
            ]
            if 0 <= tab_index < len(tables):
                return tables[tab_index]
        
        return None
        
    def _update_button_states(self):
        current_table = self._get_current_table()
        
        if not current_table:
            self.ui.btn_edit.setEnabled(False)
            self.ui.btn_remove.setEnabled(False)
            return

        has_selection = bool(self.table_manager.get_selected_row_indices(current_table))
        
        self.ui.btn_edit.setEnabled(has_selection)
        self.ui.btn_remove.setEnabled(has_selection)
        
        self.ui.btn_add.setEnabled(True)

    @Slot()
    def _execute_campaign(self):
        form = ExecutionCampaign()
        form.setWindowTitle("Execute campaign")
        self.form_manager.register_form(form, "Execute campaign")
        form.show()
    
    def _load_table_data(self, key: str, index: Optional[int]):
        if index is None:
            table_info = TABLES[key]
            table_widget = getattr(self.ui, table_info.widget_name)
            data = self.db_manager.get_all_data(key)
            self.table_manager.setup_table(table_widget, key, data, table_info.headers, register=True)
        else:
            # Buscar la tabla correspondiente a la pestaña
            # Suponemos que key es el nombre de la página (ej: 'management', 'assets')
            tab_table = None
            for tname, tinfo in TABLES.items():
                if tinfo.page.lower() == key.lower() and tinfo.tab == index:
                    tab_table = (tname, tinfo)
                    break
            if tab_table:
                subkey, table_info = tab_table
                table_widget = getattr(self.ui, table_info.widget_name)
                data = self.db_manager.get_all_data(subkey)
                self.table_manager.setup_table(table_widget, subkey, data, table_info.headers, register=True)
        self._update_button_states()

    def closeEvent(self, event):
        self.form_manager.close_all_forms()
        super().closeEvent(event)
