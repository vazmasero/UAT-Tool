from PySide6.QtWidgets import QWidget
from ui.ui_form_bug import Ui_form_bug


# Page to manage the creation or edition of bugs
class FormBug(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_bug()
        self.ui.setupUi(self)

    def load_data(self,data):
        self.ui.lbl_bug.setText(f"Edit bug #{data[5]}")
        #self.ui.cb_status(f"{data[0]}")
        #self.ui.cb_system
        self.ui.le_version.setText(f"{data[2]}")
        self.ui.le_id.setText(f"{data[5]}")
        self.ui.le_creation.setText(f"{data[3]}")
        self.ui.le_update.setText(f"{data[4]}")
        #self.ui.cb_campaign.setText(f"{data[6]}")
        #self.ui.cb_campaign.setItemText(f"{data[7]}")
        self.ui.le_short.setText(f"{data[8]}")
        self.ui.le_definition.setText(f"{data[9]}")
        #self.ui.cb_urgency.setCurrentText(f"{data[10]}")
        #self.ui.cb_impact.setCurrentText(f"{data[11]}")


