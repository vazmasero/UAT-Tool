from PySide6.QtWidgets import QMainWindow, QDialog

from ui.ui_main import Ui_main_window
from ui.ui_dialog_action import Ui_dialog_action
from campaigns import ExecutionCampaign, FormCampaign
from bugs import FormBug
from cases import FormCase, FormBlock
from requirements import FormRequirement
from assets import (FormDrone, FormEmail, FormOperator, 
                    FormUASZone, FormUhubOrg, FormUhubUser, FormUspace)

# Home Page
class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowTitle("UAT Tool")
        self.change_page(0)

        self.form_windows = {}

        # Menubar actions
        self.ui.action_view_bugs.triggered.connect(lambda: self.change_page(0))
        self.ui.action_view_campaigns.triggered.connect(lambda: self.change_page(1))
        self.ui.action_view_cases.triggered.connect(lambda: self.change_page(2))
        self.ui.action_view_requirements.triggered.connect(lambda: self.change_page(3))
        self.ui.action_view_assets.triggered.connect(lambda: self.change_page(4))

        # General add/remove buttons
        self.ui.btn_add.clicked.connect(self.handle_add_button)
        self.ui.btn_remove.clicked.connect(lambda: self.show_dialog(2))

        #Generic edit buttons
        self.ui.btn_edit.clicked.connect(self.handle_edit_button)

        # Start campaign (pendiente de generar botón de start campaign)
        #self.ui.btn_start_campaign.clicked.connect(self.open_execution_campaign)


    def change_page(self,index):
        self.ui.stacked_main.setCurrentIndex(index)

    def show_dialog(self,dialogue_type):
        self.dialog=Dialog()
        if dialogue_type == 2:
            self.dialog.ui.lbl_dialog.setText("Are you sure you want to delete it? Changes will not be reversible.")
            self.dialog.setWindowTitle("Confirmation")
            self.dialog.exec_()

    # Botón de start campaign (pendiente)
    """def open_execution_campaign(self):
        self.form_execution_campaign=ExecutionCampaign()
        self.form_execution_campaign.show()"""

    def open_form(self, FormClass, title:str, label_attr:str=None, label_text:str=None):
        form = FormClass()
        form.setWindowTitle(title)
        if label_attr and hasattr(form.ui, label_attr):
            getattr(form.ui, label_attr).setText(label_text)

        self.form_windows[title] = form
        form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f,None))

        form.show()

    def handle_add_button(self):
        page = self.ui.stacked_main.currentIndex()
        tab_tests = self.ui.tab_widget_management.currentIndex() if page == 2 else -1
        tab_assets = self.ui.tab_widget_assets.currentIndex() if page == 4 else -1

        form_map = {
            0: lambda: self.open_form(FormBug, "Add bug", "lbl_bug", "New bug"),
            1: lambda: self.open_form(FormCampaign, "Add campaign", "lbl_campaign", "New campaign"),
            2: lambda: self.handle_add_test(tab_tests),
            3: lambda: self.open_form(FormRequirement, "Add requirement"),
            4: lambda: self.handle_add_asset(tab_assets)
        }

        if page in form_map:
            form_map[page]()

    def handle_edit_button(self):
        page = self.ui.stacked_main.currentIndex()
        tab_tests = self.ui.tab_widget_management.currentIndex() if page == 2 else -1
        tab_assets = self.ui.tab_widget_assets.currentIndex() if page == 4 else -1

        form_map = {
            0: lambda: self.open_form(FormBug, "Edit bug", "lbl_bug", "Edit bug"),
            1: lambda: self.open_form(FormCampaign, "Edit campaign", "lbl_campaign", "Edit campaign"),
            2: lambda: self.handle_edit_test(tab_tests),
            3: lambda: self.open_form(FormRequirement, "Edit requirement"),
            4: lambda: self.handle_edit_asset(tab_assets)
        }

        if page in form_map:
            form_map[page]()

    def handle_add_test(self,tab_index):
        form_classes = [
            (FormCase, "Add case", "New test case"),
            (FormBlock, "Add block", "New test block")
        ]
        if 0<= tab_index < len(form_classes):
            FormClass, title, lbl_text = form_classes[tab_index]
            form = FormClass()
            form.setWindowTitle(title)
            if FormClass == FormCase:
                form.ui.lbl_case.setText(lbl_text)
            elif FormClass == FormBlock:
                form.ui.lbl_block.setText(lbl_text)
            self.form_windows[form] = form
            form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f, None))
            form.show()

    def handle_edit_test(self, tab_index):
        edit_titles = [
            (FormBlock, "Edit block", "Edit test case"),
            (FormCase, "Edit case", "Edit test block")
        ]
        if 0 <= tab_index < len(edit_titles):
            FormClass, title, lbl_text = edit_titles[tab_index]
            form = FormClass()
            form.setWindowTitle(title)
            if FormClass == FormCase:
                form.ui.lbl_case.setText(lbl_text)
            elif FormClass == FormBlock:
                form.ui.lbl_block.setText(lbl_text)
            self.form_windows[form] = form
            form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f, None))
            form.show()  

    def handle_add_asset(self, tab_index):
        form_classes = [
            (FormEmail, "Add email"),
            (FormOperator, "Add operator"),
            (FormDrone, "Add drone"),
            (FormUASZone, "Add UAS zone"),
            (FormUhubOrg, "Add U-hub org"),
            (FormUhubUser, "Add U-hub user"),
            (FormUspace, "Add U-space"),
        ]
        if 0 <= tab_index < len(form_classes):
            FormClass, title = form_classes[tab_index]
            form = FormClass()
            form.setWindowTitle(title)
            self.form_windows[form] = form
            form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f, None))
            form.show()
    
    def handle_edit_asset(self, tab_index):
        edit_titles = [
            (FormEmail, "Edit email"),
            (FormOperator, "Edit operator"),
            (FormDrone, "Edit drone"),
            (FormUASZone, "Edit UAS zone"),
            (FormUhubOrg, "Edit U-hub org"),
            (FormUhubUser, "Edit U-hub user"),
            (FormUspace, "Edit U-space"),
        ]
        if 0 <= tab_index < len(edit_titles):
            FormClass, title = edit_titles[tab_index]
            form = FormClass()
            form.setWindowTitle(title)
            self.form_windows[form] = form
            form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f, None))
            form.show()

# Generic dialog window
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog_action()
        self.ui.setupUi(self)



