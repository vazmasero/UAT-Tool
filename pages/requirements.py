from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QDialog
from ui.ui_form_requirements import Ui_form_requirement

# Page to manage the creation or edition of bugs
class FormRequirement(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_requirement()
        self.ui.setupUi(self)