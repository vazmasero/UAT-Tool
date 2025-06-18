from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QDialog

from ui.ui_main import Ui_main_window
from ui.ui_form_bug import Ui_form_bug
from ui.ui_dialog_action import Ui_dialog_action
from ui.ui_execution_campaign import Ui_execution_campaign
from ui.ui_form_campaign import Ui_form_campaign

# Home Page
class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setWindowTitle("UAT Tool")

        # Menubar actions
        self.ui.action_view_bugs.triggered.connect(lambda: self.change_page(0))
        self.ui.action_view_campaigns.triggered.connect(lambda: self.change_page(1))
        self.ui.action_view_cases.triggered.connect(lambda: self.change_page(2))
        self.ui.action_view_requirements.triggered.connect(lambda: self.change_page(3))
        self.ui.action_view_assets.triggered.connect(lambda: self.change_page(4))

        # Bugs section
        # Add bug button
        self.ui.btn_add_bug.clicked.connect(lambda: self.open_form_bug(0))
        # Edit bug button
        self.ui.btn_edit_bug.clicked.connect(lambda: self.open_form_bug(1))
        self.form_bug_window=None
        # Remove bug button
        self.ui.btn_remove_bug.clicked.connect(lambda: self.show_dialog(2))

        # Campaigns section
        # Start campaign button
        self.ui.btn_start_campaign.clicked.connect(self.open_execution_campaign)
        self.form_execution_campaign=None
        # Open campaign form
        self.ui.btn_add_campaign.clicked.connect(self.open_form_campaign)
        self.form_campaign=None
        # Remove bug button
        self.ui.btn_delete_campaign.clicked.connect(lambda: self.show_dialog(2))

        # Cases section
        # Start campaign button
        self.ui.btn_start_campaign.clicked.connect(self.open_execution_campaign)
        self.form_execution_campaign=None
        # Open campaign form
        self.ui.btn_add_campaign.clicked.connect(self.open_form_campaign)
        self.form_campaign=None
        # Remove bug button
        self.ui.btn_delete_campaign.clicked.connect(lambda: self.show_dialog(2))

        # Requirements section
        # Start campaign button
        self.ui.btn_start_campaign.clicked.connect(self.open_execution_campaign)
        self.form_execution_campaign=None
        # Open campaign form
        self.ui.btn_add_campaign.clicked.connect(self.open_form_campaign)
        self.form_campaign=None
        # Remove bug button
        self.ui.btn_delete_campaign.clicked.connect(lambda: self.show_dialog(2))

        # Assets section
        # Start campaign button
        self.ui.btn_start_campaign.clicked.connect(self.open_execution_campaign)
        self.form_execution_campaign=None
        # Open campaign form
        self.ui.btn_add_campaign.clicked.connect(self.open_form_campaign)
        self.form_campaign=None
        # Remove bug button
        self.ui.btn_delete_campaign.clicked.connect(lambda: self.show_dialog(2))


    def change_page(self,index):
        self.ui.stacked_main.setCurrentIndex(index)

    def open_form_bug(self,type):
        self.form_bug_window=FormBug()
        if type == 0:
            self.form_bug_window.setWindowTitle("Add bug")
            self.form_bug_window.ui.lbl_bug.setText("New bug")
        elif type == 1:
            self.form_bug_window.setWindowTitle("Edit bug")
            self.form_bug_window.ui.lbl_bug.setText("Edit bug")

        self.form_bug_window.show()

    def show_dialog(self,type):
        self.dialog=Dialog()
        if type == 2:
            self.dialog.ui.lbl_dialog.setText("Are you sure you want to delete it? Changes will not be reversible.")
            self.dialog.setWindowTitle("Confirmation")
            self.dialog.exec_()

    def open_execution_campaign(self):
        self.form_execution_campaign=ExecutionCampaign()
        self.form_execution_campaign.show()

    def open_form_campaign(self):
        self.form_campaign=FormCampaign()
        self.form_campaign.show()

class FormBug(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_bug()
        self.ui.setupUi(self)

class ExecutionCampaign(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_execution_campaign()
        self.ui.setupUi(self)

class FormCampaign(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_campaign()
        self.ui.setupUi(self)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog_action()
        self.ui.setupUi(self)



