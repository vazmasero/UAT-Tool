from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QDialog
from ui.ui_form_case import Ui_form_case
from ui.ui_form_block import Ui_form_block

# Page to manage the creation or edition of bugs
class FormCase(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_case()
        self.ui.setupUi(self)

# Page to manage the creation or edition of blocks
class FormBlock(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_block()
        self.ui.setupUi(self)