from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QDialog
from ui.ui_form_email import Ui_form_email
from ui.ui_form_drone import Ui_form_drone
from ui.ui_form_operator import Ui_form_operator
from ui.ui_form_uas_zone import Ui_form_uas_zone
from ui.ui_form_uhub_org import Ui_form_uhub_org
from ui.ui_form_uhub_user import Ui_form_uhub_user_form
from ui.ui_form_uspace import Ui_form_uspace

class FormEmail(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_email()
        self.ui.setupUi(self)

class FormDrone(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_drone()
        self.ui.setupUi(self)


class FormOperator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_operator()
        self.ui.setupUi(self)

class FormUASZone(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_uas_zone()
        self.ui.setupUi(self)

class FormUhubOrg(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_uhub_org()
        self.ui.setupUi(self)

class FormUhubUser(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_uhub_user_form()
        self.ui.setupUi(self)

class FormUspace(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_uspace()
        self.ui.setupUi(self)