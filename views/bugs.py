from PySide6.QtWidgets import QWidget
from ui.ui_form_bug import Ui_form_bug


# Page to manage the creation or edition of bugs
class FormBug(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_bug()
        self.ui.setupUi(self)


