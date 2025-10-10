from PySide6.QtCore import Qt
from PySide6.QtWidgets import QAbstractItemView, QDialog, QListWidgetItem, QMessageBox

from uat_tool.application.dto import RequirementFormDTO, RequirementTableDTO
from uat_tool.presentation.views.ui.form_requirement_ui import Ui_form_requirement
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class RequirementDialog(QDialog, Ui_form_requirement):
    """Diálogo para crear/editar requisitos."""

    def __init__(self, app_context, requirement: RequirementTableDTO = None):
        super().__init__()
        self.setupUi(self)
        self.app_context = app_context
        self.requirement = requirement

        self._setup_ui()
        self._connect_signals()

        if requirement:
            self._load_existing_data()
        else:
            self.setWindowTitle("New Requirement")

    def _setup_ui(self):
        """Configura la UI del diálogo."""
        # Permitir selección múltiple en listas
        self.lw_systems.setSelectionMode(QAbstractItemView.MultiSelection)
        self.lw_sections.setSelectionMode(QAbstractItemView.MultiSelection)

        # Cargar datos en combos/listas
        self._load_systems()
        self._load_sections()

    def _connect_signals(self):
        """Conecta las señales."""
        self.btn_accept.clicked.connect(self._on_accept)
        self.btn_cancel.clicked.connect(self.reject)

    def _load_existing_data(self):
        """Carga los datos existentes para edición."""
        if self.requirement:
            self.setWindowTitle(f"Editar Requirement - {self.requirement.code}")
            self.le_code.setText(self.requirement.code)
            self.le_definition.setText(self.requirement.definition)

            # Seleccionar sistemas y secciones (implementar según tu lógica)
            self._select_systems(self.requirement.systems)
            self._select_sections(self.requirement.sections)

    def _load_systems(self):
        """Carga la lista de sistemas disponibles."""
        try:
            system_service = self.app_context.get_service("system_service")
            systems = system_service.get_all_systems()

            self.lw_systems.clear()
            for system in systems:
                item = QListWidgetItem(system.name)
                item.setData(Qt.UserRole, system.id)  # Guardar ID
                self.lw_systems.addItem(item)

        except Exception as e:
            logger.error(f"Error cargando sistemas: {e}")

    def _load_sections(self):
        """Carga la lista de secciones disponibles."""
        try:
            section_service = self.app_context.get_service("section_service")
            sections = section_service.get_all_sections()

            self.lw_sections.clear()
            for section in sections:
                item = QListWidgetItem(section.name)
                item.setData(Qt.UserRole, section.id)  # Guardar ID
                self.lw_sections.addItem(item)

        except Exception as e:
            logger.error(f"Error cargando secciones: {e}")

    def _select_systems(self, system_ids):
        """Selecciona sistemas en la lista."""
        for i in range(self.lw_systems.count()):
            item = self.lw_systems.item(i)
            if item.data(Qt.UserRole) in system_ids:
                item.setSelected(True)

    def _select_sections(self, section_ids):
        """Selecciona secciones en la lista."""
        for i in range(self.lw_sections.count()):
            item = self.lw_sections.item(i)
            if item.data(Qt.UserRole) in section_ids:
                item.setSelected(True)

    def _on_accept(self):
        """Valida y acepta el formulario."""
        try:
            if self._validate_form():
                self.accept()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error validando formulario: {str(e)}")

    def _validate_form(self) -> bool:
        """Valida los datos del formulario."""
        if not self.le_code.text().strip():
            QMessageBox.warning(self, "Error", "El código es obligatorio")
            self.le_code.setFocus()
            return False

        if not self.le_definition.text().strip():
            QMessageBox.warning(self, "Error", "La definición es obligatoria")
            self.le_definition.setFocus()
            return False

        return True

    def get_form_data(self) -> RequirementFormDTO:
        """Obtiene los datos del formulario como DTO."""
        return RequirementFormDTO(
            code=self.le_code.text().strip(),
            definition=self.le_definition.text().strip(),
            systems=self._get_selected_systems(),
            sections=self._get_selected_sections(),
        )

    def _get_selected_systems(self) -> list[int]:
        """Obtiene los IDs de los sistemas seleccionados."""
        selected_ids = []
        for item in self.lw_systems.selectedItems():
            system_id = item.data(Qt.UserRole)
            if system_id:
                selected_ids.append(system_id)
        return selected_ids

    def _get_selected_sections(self) -> list[int]:
        """Obtiene los IDs de las secciones seleccionadas."""
        selected_ids = []
        for item in self.lw_sections.selectedItems():
            section_id = item.data(Qt.UserRole)
            if section_id:
                selected_ids.append(section_id)
        return selected_ids
