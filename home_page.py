from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui.ui_main import Ui_main_window
from ui.ui_dialog_action import Ui_dialog_action
from campaigns import ExecutionCampaign
from db import get_all_bugs, get_all_campaigns

from config.app_config import AppConfig
from config.forms_config import PageType, FormType
from managers.form_manager import FormManager
from managers.page_manager import PageManager
from managers.table_manager import TableManager  # Asumo que existe

class HomePage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowTitle("UAT Tool")

        self.form_manager = FormManager()
        self.page_manager = PageManager(self.ui.stacked_main, self.ui)
        self.table_manager = TableManager()
        
        self._setup_managers()
        self._connect_signals()
        
        self.page_manager.change_page(PageType.BUGS)

    def _setup_managers(self):
        self.page_manager.register_data_loader(PageType.BUGS, self._load_bugs_data)
        self.page_manager.register_data_loader(PageType.CAMPAIGNS, self._load_campaign_data)

        self.ui.tbl_bugs.doubleClicked.connect(self._handle_double_clicked_bug)

    
    def _connect_signals(self):
        self._connect_menu_actions()
        self._connect_buttons()
    
    def _connect_menu_actions(self):
        view_actions = [
            (self.ui.action_view_bugs, PageType.BUGS),
            (self.ui.action_view_campaigns, PageType.CAMPAIGNS),
            (self.ui.action_view_cases, PageType.CASES),
            (self.ui.action_view_requirements, PageType.REQUIREMENTS),
            (self.ui.action_view_assets, PageType.ASSETS),
        ]

        for action, page_type in view_actions:
            action.triggered.connect(lambda checked, pt=page_type: self.page_manager.change_page(pt))

        config = AppConfig()
        for form_key, form_config in config.FORMS_CONFIG.items():
            if form_config.menu_action_attr:
                action = getattr(self.ui, form_config.menu_action_attr, None)
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
        self._handle_form_action(edit_mode=True)

    def _handle_form_action(self, edit_mode: bool = False):
        current_page = self.page_manager.current_page
        tab_index = self.page_manager.get_current_tab_index()
        
        config = AppConfig()
        page_forms = config.PAGE_FORM_MAPPING.get(current_page, [])
        
        if not page_forms:
            return
        
        if tab_index is not None and tab_index < len(page_forms):
            form_key = page_forms[tab_index]
        else:
            form_key = page_forms[0]
        
        self.form_manager.open_form(form_key, edit_mode)
    
    def _handle_remove_button(self):
        dialog = Dialog()
        dialog.ui.lbl_dialog.setText("Are you sure you want to delete it? Changes will not be reversible.")
        dialog.setWindowTitle("Confirmation")
        dialog.exec_()

    @Slot()
    def _execute_campaign(self):
        form = ExecutionCampaign()
        form.setWindowTitle("Execute campaign")
        self.form_manager.register_form(form, "Execute campaign")
        form.show()
    
    @Slot()
    def _handle_double_clicked_bug(self, index):
        if not self.ui.tbl_bugs.selectionModel().hasSelection():
            return
        
        row_data = self.table_manager.get_row_data(self.ui.tbl_bugs, index.row())
        self.form_manager.open_form("bug", edit_mode=True, data=row_data)

    def _load_bugs_data(self):
        data = get_all_bugs()
        headers = [
            "Status", "System", "Version", "Creation Time", "Last Update",
            "ServiceNow ID", "Campaign", "Requirements", "Short Description",
            "Definition", "Urgency", "Impact", "Comments"
        ]
        self.table_manager.setup_table(self.ui.tbl_bugs, data, headers)

    def _load_campaign_data(self):
        data = get_all_campaigns()
        headers = [
            "Id", "Description", "System", "Version", "Test blocks", "Passed",
            "Success", "Creation Time", "Start date", "End date", "Last Update"
        ]
        self.table_manager.setup_table(self.ui.tbl_campaigns, data, headers)

    def closeEvent(self, event):
        self.form_manager.close_all_forms()
        super().closeEvent(event)

class Dialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog_action()
        self.ui.setupUi(self)