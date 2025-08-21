from typing import Optional
from PySide6.QtWidgets import QMainWindow

from managers.form_manager import FormManager
from managers.page_manager import PageManager
from managers.table_manager import TableManager
from ui.ui_main import Ui_main_window

from config.form_config import FORMS
from controllers.main_controller import MainController
from db.db import DatabaseManager

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # Create managers
        self.db_manager = DatabaseManager()
        self.page_manager = PageManager(self.ui.stacked_widget, self.ui)
        self.form_manager = FormManager()
        self.table_manager = TableManager()

        # Insert dependencies to the controller
        self.controller = MainController(
            ui=self.ui,
            page_manager=self.page_manager,
            form_manager=self.form_manager,
            table_manager=self.table_manager,
            db_manager=self.db_manager
        )
        
        # Initial view setup
        self.controller.setup_tables()
        self._setup_buttons()

        self._connect_signals()

        # Provisional: disables search bars and filters until they are implemented
        self._disable_search_bars()
    
    def _disable_search_bars(self):
        # Search bars are disabled until implemented
        self.ui.le_search_bug.setDisabled(True)
        self.ui.le_search_requirement.setDisabled(True)

        # Filters are disabled until implemented
        self.ui.cb_filter_status.setDisabled(True)
        self.ui.cb_filter_system.setDisabled(True)
        self.ui.cb_search_bug.setDisabled(True)
        self.ui.cb_system.setDisabled(True)

    def _connect_signals(self):
        """Connects signals between managers and the view."""
        self._connect_menu_actions() # Menu bar actions
        
        # Ui buttons
        self.ui.btn_add.clicked.connect(lambda _:self.controller.handle_new_form(edit=False))
        self.ui.btn_edit.clicked.connect(lambda _:self.controller.handle_new_form(edit=True))
        self.ui.btn_remove.clicked.connect(lambda _:self.controller._handle_remove_button())
        #self.ui.btn_start.clicked.connect(self._execute_campaign)

        # Table signals
        self.table_manager.table_double_clicked.connect(self.controller.handle_new_form)
        self.table_manager.selection_changed.connect(self.controller.handle_selection_changed)
        
    def _connect_menu_actions(self):

        for attr_name in dir(self.ui):
            if attr_name.startswith('action_view_'):
                action = getattr(self.ui, attr_name)
                page_type = attr_name.replace('action_view_', '')
                action.triggered.connect(
                lambda checked, pt=page_type: self.controller._change_page(pt)
            )
            elif attr_name.startswith("action_new_"):
                action = getattr(self.ui, attr_name)
                form_name = self._find_form_key_for_action(attr_name)
                if form_name:
                    action.triggered.connect(
                        lambda _, fn=form_name: self.controller.handle_menu_add(fn, edit=False, data=None)
                )
                
    def _find_form_key_for_action(self, action_name: str) -> Optional[str]:
        """Encuentra el form_key correspondiente a una acción del menú"""
        for form_key, form_info in FORMS.items():
            form_config = form_info.get('config')
            if form_config and form_config.menu_action_attr == action_name:
                return form_key
        return None
                
    def _setup_buttons(self):
        """Sets up view's buttons (Add, Edit and Remove)."""
        # Initially, both edit and delete buttons are disabled
        self.ui.btn_edit.setEnabled(False)
        self.ui.btn_remove.setEnabled(False)
        
    def closeEvent(self, event):
        self.controller.close_program()
        super().closeEvent(event)
            
