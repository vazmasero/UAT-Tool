from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QDialog, QHeaderView, QAbstractItemView
from PySide6.QtGui import QStandardItem, QStandardItemModel

from ui.ui_main import Ui_main_window
from ui.ui_dialog_action import Ui_dialog_action
from campaigns import ExecutionCampaign, FormCampaign
from bugs import FormBug
from cases import FormCase, FormBlock
from requirements import FormRequirement
from assets import (FormDrone, FormEmail, FormOperator,
            FormUASZone, FormUhubOrg, FormUhubUser, FormUspace)

from db import get_all_bugs

# Home Page
class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowTitle("UAT Tool")
        self.change_page(0)
        # self.configure_bug_table_headers() Reactivar cuando se arregle esta función

        self.form_windows = {}

        # Menubar actions
        # View
        self.ui.action_view_bugs.triggered.connect(lambda: self.change_page(0))
        self.ui.action_view_campaigns.triggered.connect(lambda: self.change_page(1))
        self.ui.action_view_cases.triggered.connect(lambda: self.change_page(2))
        self.ui.action_view_requirements.triggered.connect(lambda: self.change_page(3))
        self.ui.action_view_assets.triggered.connect(lambda: self.change_page(4))

        # Create
        self.ui.action_add_bug.triggered.connect(lambda:self.open_form(FormBug, "Add bug", "lbl_bug", "New bug"))
        self.ui.action_new_campaign.triggered.connect(lambda:self.open_form(FormCampaign, "Add campaign", "lbl_campaign", "New campaign"))
        self.ui.action_new_case.triggered.connect(lambda:self.handle_test(0))
        self.ui.action_new_block.triggered.connect(lambda:self.handle_test(1))
        self.ui.action_new_requirement.triggered.connect(lambda:self.open_form(FormRequirement, "Add requirement"))
        self.ui.action_new_email.triggered.connect(lambda:self.handle_asset(0))
        self.ui.action_new_operator.triggered.connect(lambda:self.handle_asset(1))
        self.ui.action_new_drone.triggered.connect(lambda:self.handle_asset(2))
        self.ui.action_new_uas_zone.triggered.connect(lambda:self.handle_asset(3))
        self.ui.action_new_uhub_organization.triggered.connect(lambda:self.handle_asset(4))
        self.ui.action_new_uhub_user.triggered.connect(lambda:self.handle_asset(5))
        self.ui.action_new_uspace.triggered.connect(lambda:self.handle_asset(6))

        # General add/remove buttons
        self.ui.btn_add.clicked.connect(self.handle_add_button)
        self.ui.btn_remove.clicked.connect(lambda: self.show_dialog(2))

        #Generic edit buttons
        self.ui.btn_edit.clicked.connect(self.handle_edit_button)

        # Start campaign (pendiente de generar botón de start campaign)
        self.ui.btn_start.clicked.connect(self.execute_campaign)

    @Slot(int)
    def change_page(self,index):
        self.ui.stacked_main.setCurrentIndex(index)
        if index == 1:
            self.ui.btn_start.show()
        else:
            self.ui.btn_start.hide()

        if index == 0:
            self.load_bugs_data()

    def show_dialog(self,dialogue_type):
        self.dialog=Dialog()
        if dialogue_type == 2:
            self.dialog.ui.lbl_dialog.setText("Are you sure you want to delete it? Changes will not be reversible.")
            self.dialog.setWindowTitle("Confirmation")
            self.dialog.exec_()

    def open_form(self, FormClass, title:str, label_attr:str=None, label_text:str=None):
        form = FormClass()
        form.setWindowTitle(title)
        if label_attr and hasattr(form.ui, label_attr):
            getattr(form.ui, label_attr).setText(label_text)

        self.form_windows[title] = form
        form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f,None))

        form.show()

    @Slot()
    def handle_add_button(self):
        page = self.ui.stacked_main.currentIndex()
        tab_tests = self.ui.tab_widget_management.currentIndex() if page == 2 else -1
        tab_assets = self.ui.tab_widget_assets.currentIndex() if page == 4 else -1

        form_map = {
            0: lambda: self.open_form(FormBug, "Add bug", "lbl_bug", "New bug"),
            1: lambda: self.open_form(FormCampaign, "Add campaign", "lbl_campaign", "New campaign"),
            2: lambda: self.handle_test(tab_tests),
            3: lambda: self.open_form(FormRequirement, "Add requirement"),
            4: lambda: self.handle_asset(tab_assets)
        }

        if page in form_map:
            form_map[page]()

    @Slot()
    def handle_edit_button(self):
        page = self.ui.stacked_main.currentIndex()
        tab_tests = self.ui.tab_widget_management.currentIndex() if page == 2 else -1
        tab_assets = self.ui.tab_widget_assets.currentIndex() if page == 4 else -1

        form_map = {
            0: lambda: self.open_form(FormBug, "Edit bug", "lbl_bug", "Edit bug"),
            1: lambda: self.open_form(FormCampaign, "Edit campaign", "lbl_campaign", "Edit campaign"),
            2: lambda: self.handle_test(tab_tests,edit=True),
            3: lambda: self.open_form(FormRequirement, "Edit requirement"),
            4: lambda: self.handle_asset(tab_assets, edit=True)
        }

        if page in form_map:
            form_map[page]()

    def handle_test(self,tab_index, edit=False):
        titles = [
            ("Add case", "New test case","Edit case", "Edit test case"),
            ("Add block", "New test block","Edit block", "Edit test block")
        ]

        form_classes = [FormCase, FormBlock]

        if 0 <= tab_index < len(form_classes):
            FormClass = form_classes[tab_index]
            title = titles[tab_index][2] if edit else titles[tab_index][0]
            label_text = titles[tab_index][3] if edit else titles[tab_index][1]

            form = FormClass()
            form.setWindowTitle(title)

            if FormClass == FormCase:
                form.ui.lbl_case.setText(label_text)
            else:
                form.ui.lbl_block.setText(label_text)

            self.form_windows[form] = form
            form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f, None))
            form.show()

    def handle_asset(self, tab_index, edit=False):
        titles = [
            ("Add email", "Edit email"),
            ("Add operator", "Edit operator"),
            ("Add drone", "Edit drone"),
            ("Add UAS zone", "Edit UAS zone"),
            ("Add U-hub org", "Edit U-hub org"),
            ("Add U-hub user", "Edit U-hub user"),
            ("Add U-space", "Edit U-space"),
        ]
        form_classes = [
            FormEmail, FormOperator, FormDrone, FormUASZone,
            FormUhubOrg, FormUhubUser, FormUspace
        ]

        if 0 <= tab_index < len(form_classes):
            FormClass = form_classes[tab_index]
            title = titles[tab_index][1] if edit else titles[tab_index][0]
            form = FormClass()
            form.setWindowTitle(title)
            self.form_windows[form] = form
            form.destroyed.connect(lambda _, f=form: self.form_windows.pop(f, None))
            form.show()

    @Slot()
    def execute_campaign(self):
        form = ExecutionCampaign()
        form.setWindowTitle("Execute campaign")
        self.form_windows["Execute campaign"] = form
        form.destroyed.connect(lambda _, f=form: self.form_windows.pop("Execute campaign", None))
        form.show()

    # Configuration of headers for bugs table
    def configure_bug_table_headers(self):
        header = self.ui.tbl_bugs.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)

        for i in range(self.ui.tbl_bugs.model().columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        header.setStretchLastSection(False)
        header.setSectionResizeMode(QHeaderView.Stretch)

    # Loading bugs table
    def load_bugs_data(self):
        data = get_all_bugs()
        headers = [
            "Status", "System", "Version", "Creation Time", "Last Update",
            "ServiceNow ID", "Campaign", "Requirements", "Short Description",
            "Definition", "Urgency", "Impact", "Comments"
        ]

        model = QStandardItemModel()
        model.setColumnCount(13)
        model.setHorizontalHeaderLabels(headers)

        for row in data:
            items = [QStandardItem(str(cell) if cell is not None else "") for cell in row]
            for item in items:
                item.setEditable(False)
            model.appendRow(items)

        self.ui.tbl_bugs.setModel(model)
        self.ui.tbl_bugs.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tbl_bugs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.configure_bug_table_headers()

# Generic dialog window
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog_action()
        self.ui.setupUi(self)



