import os
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
)

from uat_tool.application.dto import BugFormDTO, BugTableDTO, FileServiceDTO
from uat_tool.presentation.views.ui.form_bug_ui import Ui_form_bug
from uat_tool.shared import get_logger

logger = get_logger(__name__)


class BugDialog(QDialog, Ui_form_bug):
    """Diálogo para crear/editar bugs."""

    def __init__(self, app_context, bug: BugTableDTO = None):
        super().__init__()
        self.setupUi(self)
        self.app_context = app_context
        self.bug = bug
        self.selected_files = []

        self._setup_ui()
        self._connect_signals()

        if bug:
            self._load_existing_data()
        else:
            self.setWindowTitle("New Bug")

        logger.info("Diálogo inicializado correctamente")

    def _setup_ui(self):
        """Configura la UI del diálogo."""
        # Permitir selección múltiple en lista de requisitos
        self.lw_requirements.setSelectionMode(QAbstractItemView.MultiSelection)

        # Cargar datos en combos/listas
        self._load_systems()
        self._load_requirements()
        self._load_campaigns()
        self._load_urgency_impact()

    def _connect_signals(self):
        """Conecta las señales."""
        self.btn_accept.clicked.connect(self._on_accept)
        self.btn_cancel.clicked.connect(self.reject)
        self.btn_file_browse.clicked.connect(self._on_browse_files)
        #self.btn_file_download.clicked.connect(self._on_download_file)

    def _on_browse_files(self):
        """Abre el diálogo para seleccionar archivos."""
        try:
            # Abrir diálogo para seleccionar múltiples archivos
            file_dialog = QFileDialog()
            file_paths, _ = file_dialog.getOpenFileNames(
                self,
                "Select files",
                "",  # Directorio inicial (vacío por defecto)
                "All files (*.*)",
            )

            if file_paths:
                self.selected_files = file_paths
                # Mostrar nombres de archivos en line edit
                file_names = [os.path.basename(path) for path in file_paths]

                self.le_files.setText(", ".join(file_names))
                logger.info(f"Archivos seleccionados: {len(file_paths)} archivos")

        except Exception as e:
            logger.error(f"Error seleccionando archivos: {e}")
            QMessageBox.warning(
                self, "Error", f"Error seleccionando archivos: {str(e)}"
            )

    def _load_existing_data(self):
        """Carga los datos existentes para edición."""
        if self.bug:
            self.setWindowTitle(f"Editar Bug - {self.bug.le_code}")
            self.le_code.setText(self.bug.le_code)
            self.le_definition.setText(self.bug.le_definition)

            # Seleccionar sistemas y secciones (implementar según tu lógica)
            self._select_systems(self.bug.lw_systems)
            self._select_sections(self.bug.lw_sections)

    def _load_campaigns(self):
        """Carga el combobox de campañas disponibles."""
        # PENDIENTE DE IMPLEMENTAR CUANDO EXISTA EL CAMPAIGN SERVICE
        self.cb_campaign.clear()
        self.cb_campaign.addItem("Select a campaign", None)  # Opción por defecto

    def _load_urgency_impact(self):
        """Carga el combobox de urgencia e impacto."""
        self.cb_urgency.clear()
        self.cb_urgency.addItem("Select urgency", None)
        self.cb_urgency.addItem("Low", 3)
        self.cb_urgency.addItem("Medium", 2)
        self.cb_urgency.addItem("High", 1)

        self.cb_impact.clear()
        self.cb_impact.addItem("Select impact", None)
        self.cb_impact.addItem("Low", 3)
        self.cb_impact.addItem("Medium", 2)
        self.cb_impact.addItem("High", 1)

    def _load_systems(self):
        """Carga el combobox de sistemas disponibles."""
        try:
            service = self.app_context.get_service("auxiliary_service")
            systems = service.get_all_systems_service_dto()

            self.cb_system.clear()
            self.cb_system.addItem("Select a system", None)  # Opción por defecto
            for system in systems:
                self.cb_system.addItem(system.name, system.id)

        except Exception as e:
            logger.error(f"Error cargando sistemas: {e}")

    def _load_requirements(self):
        """Carga la lista de requisitos disponibles."""
        try:
            requirement_service = self.app_context.get_service("requirement_service")
            requirements = requirement_service.get_all_requirements_service_dto()

            self.lw_requirements.clear()
            for requirement in requirements:
                item = QListWidgetItem(requirement.code)
                item.setData(Qt.UserRole, requirement.id)  # Guardar ID
                self.lw_requirements.addItem(item)

        except Exception as e:
            logger.error(f"Error cargando requisitos: {e}")

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

        # PENDIENTE DE CREAR VALIDACIONES MÁS AVANZADAS
        if not self.le_definition.text().strip():
            QMessageBox.warning(self, "Error", "La definición es obligatoria")
            self.le_definition.setFocus()
            return False

        if not self.cb_system.currentText().strip():
            QMessageBox.warning(self, "Error", "El sistema es obligatorio")
            self.cb_system.setFocus()
            return False

        return True

    def get_form_data(self) -> BugFormDTO:
        """Obtiene los datos del formulario como DTO."""
        return BugFormDTO(
            le_short_desc=self.le_short_desc.text().strip(),
            le_definition=self.le_definition.text().strip(),
            cb_status=self.cb_status.currentText(),
            cb_campaign=self.cb_campaign.currentData(),
            le_service_now_id=self.le_service_now_id.text().strip(),
            le_comments=self.le_comments.text().strip(),
            le_version=self.le_version.text().strip(),
            cb_system=self.cb_system.currentData(),
            lw_requirements=self._get_selected_requirements(),
            cb_urgency=self.cb_urgency.currentData(),
            cb_impact=self.cb_impact.currentData(),
        )

    def _get_selected_requirements(self) -> list[int]:
        """Obtiene los IDs de los requisitos seleccionados."""
        return [
            item.data(Qt.UserRole)
            for item in self.lw_requirements.selectedItems()
            if item.data(Qt.UserRole) is not None
        ]

    def get_selected_files_data(self) -> list[FileServiceDTO]:
        """Obtiene los datos de los archivos seleccionados como FileServiceDTO."""
        files_dto = []

        for file_path in self.selected_files:
            try:
                # Obtener información del archivo
                file_info = self._get_file_info(file_path)
                if file_info:
                    files_dto.append(file_info)

            except Exception as e:
                logger.error(f"Error procesando archivo {file_path}: {e}")

        return files_dto

    def _get_file_info(self, file_path: str) -> FileServiceDTO | None:
        """Obtiene la información de un archivo específico."""
        try:
            if not os.path.exists(file_path):
                logger.error(f"Archivo no encontrado: {file_path}")
                return None

            # Obtener información del archivo
            file_stats = os.stat(file_path)
            file_name = os.path.basename(file_path)
            file_size = file_stats.st_size
            file_extension = os.path.splitext(file_name)[1].lower()

            # Mapear extensión a MIME type
            mime_map = {
                ".pdf": "application/pdf",
                ".txt": "text/plain",
                ".jpg": "image/jpeg",
                ".png": "image/png",
                ".doc": "application/msword",
                ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            }

            mime_type = mime_map.get(file_extension, "application/octet-stream")

            # HARDCODEADO PROVISIONAL
            context = {"uploaded_by": "provisional"}

            return FileServiceDTO(
                id=None,  # Asignado al guardar en BD
                owner_type="bug",
                filename=file_name,
                filepath=file_path,  # Ruta temporal hasta copiar el archivo
                mime_type=mime_type,
                size=self._format_file_size(file_size),
                uploaded_by=context["uploaded_by"],
                uploaded_at=datetime.now().isoformat(),
            )

        except Exception as e:
            logger.error(f"Error obteniendo info del archivo {file_path}: {e}")
            return None

    def _format_file_size(self, size_bytes: int) -> str:
        """Formatea el tamaño del archivo a string legible."""
        try:
            for unit in ["B", "KB", "MB", "GB"]:
                if size_bytes < 1024.0:
                    return f"{size_bytes:.2f} {unit}"
                size_bytes /= 1024.0
            return f"{size_bytes:.2f} TB"
        except Exception as e:
            logger.error(f"Error formateando tamaño de archivo: {e}")
            return "Unknown"
