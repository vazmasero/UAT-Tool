from PySide6.QtWidgets import QDialog
from ui.ui_dialog_action import Ui_dialog_action

class Dialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog_action()
        self.ui.setupUi(self)