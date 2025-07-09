from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal

class BaseForm(QWidget):
    """Clase base para formularios, centraliza lógica común."""
    operation_completed = Signal()

    def __init__(self, db_manager, ui):
        super().__init__()
        self.db_manager = db_manager
        self.ui = ui
        self._setup_buttons()

    def _setup_buttons(self):
        """Conecta botones comunes como aceptar y cancelar."""
        self.ui.btn_accept.clicked.connect(self._handle_db_register)
        self.ui.btn_cancel.clicked.connect(self.close)

    def _handle_db_register(self):
        """Maneja el registro o edición en la base de datos."""
        data = self._obtain_form_data()
        errors = self.validate_form(data)
        if errors:
            self.show_errors(errors)
            return
        try:
            self.save_data(data)
            self.operation_completed.emit()
            self.close()
        except Exception as e:
            self.show_critical(str(e))

    def validate_form(self, data):
        """Valida los datos del formulario. Implementar en subclases."""
        return []

    def _obtain_form_data(self):
        """Obtiene los datos del formulario. Implementar en subclases."""
        return {}

    def save_data(self, data):
        """Guarda los datos en la base de datos. Implementar en subclases."""
        pass

    def show_errors(self, errors):
        """Muestra errores de validación."""
        QMessageBox.warning(self, "Errores de validación", "\n".join(errors))

    def show_critical(self, msg):
        """Muestra errores críticos."""
        QMessageBox.critical(self, "Error", msg)

    def get_checked_items(self, list_widget):
        """Obtiene los elementos seleccionados de un QListWidget."""
        checked_items = []
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            checkbox = list_widget.itemWidget(item)
            if checkbox.isChecked():
                checked_items.append(checkbox.text())
        return checked_items
