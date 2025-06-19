from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QDialog

from ui.ui_execution_campaign import Ui_execution_campaign
from ui.ui_form_campaign import Ui_form_campaign


# Page to manage the execution of test campaigns
class ExecutionCampaign(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_execution_campaign()
        self.ui.setupUi(self)

# Page to manage the creation or edition of campaigns
class FormCampaign(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_campaign()
        self.ui.setupUi(self)