from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QMainWindow, QMessageBox

from uat_tool.presentation.controllers import MainController
from uat_tool.presentation.views.ui.main_ui import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    """Ventana principal de la aplicación adaptada al diseño existente."""

    def __init__(self, main_controller: MainController):
        super().__init__()
        self.main_controller = main_controller
        self.setupUi(self)

        # Referencias a controladores de pestañas
        self.bug_controller = None
        self.requirement_controller = None

        self._connect_signals()
        self._setup_menu_actions()
        self._setup_initial_state()

    def _connect_signals(self):
        """Conecta las señales del controlador principal."""

        # Cambio de pestaña principal - Delegado al controlador principal
        self.stacked_widget.currentChanged.connect(self.main_controller.on_tab_changed)

        # Botones globales - Delegado al controlador principal
        self.btn_add.clicked.connect(self.main_controller.on_add_clicked)
        self.btn_edit.clicked.connect(self.main_controller.on_edit_clicked)
        self.btn_remove.clicked.connect(self.main_controller.on_remove_clicked)
        self.btn_start.clicked.connect(self.main_controller.on_start_clicked)

        # Señales del controlador principal
        self.main_controller.ui_state_changed.connect(self._on_ui_state_changed)
        self.main_controller.application_ready.connect(self._on_application_ready)
        self.main_controller.application_error.connect(self._on_application_error)
        self.main_controller.tab_changed.connect(self._on_tab_changed)

    def _on_ui_state_changed(self, ui_state: dict):
        """Actualiza el estado de los botones según la pestaña actual."""
        self.btn_start.setVisible(ui_state.get("btn_start_visible", False))
        self.btn_add.setEnabled(ui_state.get("btn_add_enabled", True))
        self.btn_edit.setEnabled(ui_state.get("btn_edit_enabled", False))
        self.btn_remove.setEnabled(ui_state.get("btn_remove_enabled", False))

    def _setup_menu_actions(self):
        """Configura las acciones del menú para cambiar de pestaña."""
        # Conectar acciones de vista a cambio de pestañas
        self.action_view_bugs.triggered.connect(
            lambda: self.main_controller.switch_to_tab("bugs")
        )
        self.action_view_campaigns.triggered.connect(
            lambda: self.main_controller.switch_to_tab("campaigns")
        )
        self.action_view_management.triggered.connect(
            lambda: self.main_controller.switch_to_tab("test_management")
        )
        self.action_view_requirements.triggered.connect(
            lambda: self.main_controller.switch_to_tab("requirements")
        )
        self.action_view_assets.triggered.connect(
            lambda: self.main_controller.switch_to_tab("assets")
        )

        # Conectar acciones de "Nuevo" - deelegado al controlador principal
        self.action_new_bug.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_campaign.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_requirement.triggered.connect(
            self.main_controller.on_add_clicked
        )
        self.action_new_case.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_block.triggered.connect(self.main_controller.on_add_clicked)

        # Conectar acciones de assets - delegado al controlador principal
        self.action_new_email.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_operator.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_drone.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_uas_zone.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_uhub_organization.triggered.connect(
            self.main_controller.on_add_clicked
        )
        self.action_new_uhub_user.triggered.connect(self.main_controller.on_add_clicked)
        self.action_new_uspace.triggered.connect(self.main_controller.on_add_clicked)

    def _setup_initial_state(self):
        """Configura el estado inicial de la interfaz."""
        self._setup_tables()

    def _setup_tables(self):
        """Configura las propiedades comunes de todas las tablas."""
        tables = [
            self.tbl_bugs,
            self.tbl_campaigns,
            self.tbl_cases,
            self.tbl_blocks,
            self.tbl_requirements,
            self.tbl_emails,
            self.tbl_operators,
            self.tbl_drones,
            self.tbl_uas_zones,
            self.tbl_uhub_orgs,
            self.tbl_uhub_users,
            self.tbl_uspaces,
        ]

        for table in tables:
            if table:
                table.setAlternatingRowColors(True)
                table.setSelectionBehavior(QAbstractItemView.SelectRows)
                table.setSortingEnabled(True)
                table.horizontalHeader().setStretchLastSection(True)

    def _setup_table_models(self):
        """Configura los modelos para las tablas (se llama cuando la aplicación está ready)."""
        # Configurar modelo de bugs
        self.bug_controller = self.main_controller.get_tab_controller("bugs")
        if self.bug_controller and hasattr(self.bug_controller, "proxy_model"):
            self.tbl_bugs.setModel(self.bug_controller.proxy_model)

            # Configurar headers específicos para bugs
            header = self.tbl_bugs.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

            # Conectar selección y doble clic
            self.tbl_bugs.selectionModel().selectionChanged.connect(
                self._on_bug_selection_changed
            )
            self.tbl_bugs.doubleClicked.connect(
                lambda index: self.bug_controller.handle_double_click(index)
            )

        # Configurar modelo de requirements
        self.requirement_controller = self.main_controller.get_tab_controller(
            "requirements"
        )
        if self.requirement_controller and hasattr(
            self.requirement_controller, "proxy_model"
        ):
            self.tbl_requirements.setModel(self.requirement_controller.proxy_model)

            # Configurar headers específicos para requirements
            header = self.tbl_requirements.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

            # Conectar selección y doble clic
            self.tbl_requirements.selectionModel().selectionChanged.connect(
                self._on_requirement_selection_changed
            )
            self.tbl_requirements.doubleClicked.connect(
                lambda index: self.requirement_controller.handle_double_click(index)
            )

    def _on_bug_selection_changed(self, selected, deselected):
        """Maneja cambios de selección en la tabla de bugs."""
        has_selection = len(selected.indexes()) > 0
        if has_selection and self.bug_controller:
            # Obtener ID del bug seleccionado
            index = selected.indexes()[0]
            source_index = self.bug_controller.proxy_model.mapToSource(index)
            bug_dto = self.bug_controller.table_model.bugs[source_index.row()]
            self.bug_controller.set_selected_item(bug_dto.id)
        else:
            self.bug_controller.set_selected_item(None)

    def _on_requirement_selection_changed(self, selected, deselected):
        """Maneja cambios de selección en la tabla de requirements."""
        has_selection = len(selected.indexes()) > 0
        if has_selection and self.requirement_controller:
            # Obtener ID del requirement seleccionado
            index = selected.indexes()[0]
            source_index = self.requirement_controller.proxy_model.mapToSource(index)
            requirement_dto = self.requirement_controller.table_model.requirements[
                source_index.row()
            ]
            self.requirement_controller.set_selected_item(requirement_dto.id)
        else:
            self.requirement_controller.set_selected_item(None)

    def _on_tab_changed(self, tab_name: str):
        """Maneja el cambio de pestaña (señal del controller)."""
        # Mapear nombres internos a índices del stacked widget
        tab_mapping = {
            "bugs": 0,
            "campaigns": 1,
            "test_management": 2,
            "requirements": 3,
            "assets": 4,
        }

        if tab_name in tab_mapping:
            self.stacked_widget.setCurrentIndex(tab_mapping[tab_name])
            self._update_window_title(tab_name)

    def _update_window_title(self, tab_name: str):
        """Actualiza el título de la ventana según la pestaña activa."""
        tab_titles = {
            "bugs": "Bugs - UAT Tool",
            "campaigns": "Campañas - UAT Tool",
            "test_management": "Gestión de Tests - UAT Tool",
            "requirements": "Requisitos - UAT Tool",
            "assets": "Assets - UAT Tool",
        }

        title = tab_titles.get(tab_name, "UAT Tool")
        self.setWindowTitle(title)

    def _on_application_ready(self):
        """Se ejecuta cuando la aplicación está lista."""
        self.status_bar.showMessage("Aplicación lista")

        # Configurar modelos de tabla
        self._setup_table_models()

        # Cargar datos iniciales para la pestaña actual
        current_controller = self.main_controller.get_current_tab_controller()
        if current_controller:
            current_controller.load_data()

    def _on_application_error(self, error_message: str):
        """Maneja errores de la aplicación."""
        QMessageBox.warning(self, "Error", error_message)
        self.status_bar.showMessage(f"Error: {error_message}")

    def closeEvent(self, event):
        """Maneja el cierre de la aplicación."""
        reply = QMessageBox.question(
            self,
            "Confirmar salida",
            "¿Estás seguro de que quieres salir?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.main_controller.shutdown()
            event.accept()
        else:
            event.ignore()
