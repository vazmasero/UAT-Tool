from PySide6.QtWidgets import QWidget
from ui.ui_form_bug import Ui_form_bug


# Page to manage the creation or edition of bugs
class FormBug(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_bug()
        self.ui.setupUi(self)

    def load_data(self, data):
        self.ui.lbl_bug.setText(f"Edit bug #{data[5]}")
        
        # Para combobox simple (solo texto)
        # Status - posición 0 en data
        index = self.ui.cb_status.findText(data[0])
        if index >= 0:
            self.ui.cb_status.setCurrentIndex(index)
        
        # System - posición 1 en data
        index = self.ui.cb_system.findText(data[1])
        if index >= 0:
            self.ui.cb_system.setCurrentIndex(index)
            
        # Para combobox con userData - ejemplo: requirements
        # Si en un combobox hemos guardado IDs como userData
        # y queremos seleccionar por el ID que viene en data[7]
        requirements_id = data[7]  # Asumimos que data[7] contiene el ID
        if requirements_id:
            for i in range(self.ui.cb_requirements.count()):
                if str(self.ui.cb_requirements.itemData(i)) == str(requirements_id):
                    self.ui.cb_requirements.setCurrentIndex(i)
                    break
        
        # Para urgency - posición 10 en data
        index = self.ui.cb_urgency.findText(str(data[10]))
        if index >= 0:
            self.ui.cb_urgency.setCurrentIndex(index)
            
        # Para impact - posición 11 en data
        index = self.ui.cb_impact.findText(str(data[11]))
        if index >= 0:
            self.ui.cb_impact.setCurrentIndex(index)
            
        # Campos de texto normales
        self.ui.le_version.setText(f"{data[2]}")
        self.ui.le_id.setText(f"{data[5]}")
        self.ui.le_creation.setText(f"{data[3]}")
        self.ui.le_update.setText(f"{data[4]}")
        self.ui.le_short.setText(f"{data[8]}")
        self.ui.le_definition.setText(f"{data[9]}")


