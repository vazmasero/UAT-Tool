from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QMainWindow, QMessageBox

from uat_tool.presentation.controllers import MainController
from uat_tool.presentation.views.ui.ui_main import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    """Ventana principal de la aplicación adaptada al diseño existente."""

    def __init__(self, main_controller: MainController):
        super().__init__()
        self.main_controller = main_controller
        self.setupUi(self)

        self.bug_controller = None

        self._connect_signals()
        self._setup_menu_actions()
        self._setup_initial_state()

    def _connect_signals(self):
        """Conecta las señales del controlador principal."""
        self.main_controller.tab_changed.connect(self._on_tab_changed)
        self.main_controller.application_ready.connect(self._on_application_ready)
        self.main_controller.application_error.connect(self._on_application_error)

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

        # Conectar acciones de "Nuevo" a métodos específicos
        self.action_new_bug.triggered.connect(self._on_new_bug)
        self.action_new_campaign.triggered.connect(self._on_new_campaign)
        self.action_new_requirement.triggered.connect(self._on_new_requirement)
        self.action_new_case.triggered.connect(self._on_new_case)
        self.action_new_block.triggered.connect(self._on_new_block)

        # Conectar acciones de assets
        self.action_new_email.triggered.connect(self._on_new_email)
        self.action_new_operator.triggered.connect(self._on_new_operator)
        self.action_new_drone.triggered.connect(self._on_new_drone)
        self.action_new_uas_zone.triggered.connect(self._on_new_uas_zone)
        self.action_new_uhub_organization.triggered.connect(self._on_new_uhub_org)
        self.action_new_uhub_user.triggered.connect(self._on_new_uhub_user)
        self.action_new_uspace.triggered.connect(self._on_new_uspace)

        # Conectar botones de la barra inferior
        self.btn_start.clicked.connect(self._on_start_clicked)
        self.btn_add.clicked.connect(self._on_add_clicked)
        self.btn_edit.clicked.connect(self._on_edit_clicked)
        self.btn_remove.clicked.connect(self._on_remove_clicked)

    def _setup_initial_state(self):
        """Configura el estado inicial de la interfaz."""
        # Ocultar botones hasta que se seleccione una pestaña
        self._update_action_buttons(None)

        # Configurar tablas
        self._setup_tables()

        # Configurar modelos de tablas
        self._setup_table_models()

    def _setup_table_models(self):
        """Configura los modelos para las tablas."""
        # Configurar modelo de bugs
        self.bug_controller = self.main_controller.get_tab_controller("bugs")
        if self.bug_controller and hasattr(self.bug_controller, "proxy_model"):
            self.tbl_bugs.setModel(self.bug_controller.proxy_model)

            # Configurar headers específicos para bugs
            header = self.tbl_bugs.horizontalHeader()
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

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

                # Conectar doble clic para bugs
                if table == self.tbl_bugs:
                    table.doubleClicked.connect(self._on_bug_double_clicked)

    def _on_bug_double_clicked(self, index):
        """Maneja doble clic en un bug para editarlo."""
        if self.bug_controller:
            proxy_model = self.tbl_bugs.model()
            source_index = proxy_model.mapToSource(index)
            bug_dto = proxy_model.sourceModel().bugs[source_index.row()]
            bug_id = bug_dto.id

            QMessageBox.information(self, "Editar Bug", f"Editando bug ID: {bug_id}")

    def _on_tab_changed(self, tab_name: str):
        """Maneja el cambio de pestaña."""
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

            # Actualizar estado de los botones de acción
            self._update_action_buttons(tab_name)

            # Actualizar título de la ventana
            self._update_window_title(tab_name)

            # Cargar datos de la pestaña si es bugs
            if tab_name == "bugs" and self.bug_controller:
                self.bug_controller.load_data()

    def _update_action_buttons(self, tab_name: str):
        """Actualiza el estado y visibilidad de los botones de acción."""
        # Por ahora, mostrar todos los botones para cualquier pestaña
        # Más adelante podemos personalizar por pestaña
        self.btn_start.setVisible(True)
        self.btn_add.setVisible(True)
        self.btn_edit.setVisible(True)
        self.btn_remove.setVisible(True)

        # Actualizar textos según la pestaña
        if tab_name == "campaigns":
            self.btn_start.setText("Iniciar Campaña")
        elif tab_name == "test_management":
            self.btn_start.setText("Ejecutar Tests")
        else:
            self.btn_start.setText("Start")

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

        # Configurar modelos si no se hicieron antes
        if not self.bug_controller:
            self._setup_table_models()

        # Cargar datos iniciales para la pestaña actual
        current_controller = self.main_controller.get_current_tab_controller()
        if current_controller:
            current_controller.load_data()

    def _on_application_error(self, error_message: str):
        """Maneja errores de la aplicación."""
        QMessageBox.warning(self, "Error", error_message)
        self.status_bar.showMessage(f"Error: {error_message}")

    # Métodos para acciones "Nuevo"
    def _on_new_bug(self):
        """Maneja la creación de un nuevo bug."""
        if self.bug_controller:
            # Por ahora mostrar mensaje, luego implementaremos el diálogo
            QMessageBox.information(self, "Nuevo Bug", "Diálogo para crear nuevo bug")
            # TODO: Mostrar diálogo de creación y llamar a bug_controller.create_item()
        else:
            QMessageBox.warning(self, "Error", "Controlador de bugs no disponible")

    def _on_new_campaign(self):
        """Maneja la creación de una nueva campaña."""
        controller = self.main_controller.get_tab_controller("campaigns")
        if controller:
            # TODO: Mostrar diálogo de creación de campaña
            QMessageBox.information(
                self, "Nueva Campaña", "Diálogo para crear nueva campaña"
            )

    def _on_new_requirement(self):
        """Maneja la creación de un nuevo requisito."""
        controller = self.main_controller.get_tab_controller("requirements")
        if controller:
            # TODO: Mostrar diálogo de creación de requisito
            QMessageBox.information(
                self, "Nuevo Requisito", "Diálogo para crear nuevo requisito"
            )

    def _on_new_case(self):
        """Maneja la creación de un nuevo caso de test."""
        # Esto está dentro de test_management
        QMessageBox.information(
            self, "Nuevo Caso", "Diálogo para crear nuevo caso de test"
        )

    def _on_new_block(self):
        """Maneja la creación de un nuevo bloque de test."""
        # Esto está dentro de test_management
        QMessageBox.information(
            self, "Nuevo Bloque", "Diálogo para crear nuevo bloque de test"
        )

    # Métodos para assets
    def _on_new_email(self):
        """Maneja la creación de un nuevo email."""
        QMessageBox.information(self, "Nuevo Email", "Diálogo para crear nuevo email")

    def _on_new_operator(self):
        """Maneja la creación de un nuevo operador."""
        QMessageBox.information(
            self, "Nuevo Operador", "Diálogo para crear nuevo operador"
        )

    def _on_new_drone(self):
        """Maneja la creación de un nuevo dron."""
        QMessageBox.information(self, "Nuevo Dron", "Diálogo para crear nuevo dron")

    def _on_new_uas_zone(self):
        """Maneja la creación de una nueva zona UAS."""
        QMessageBox.information(
            self, "Nueva Zona UAS", "Diálogo para crear nueva zona UAS"
        )

    def _on_new_uhub_org(self):
        """Maneja la creación de una nueva organización U-hub."""
        QMessageBox.information(
            self, "Nueva Org U-hub", "Diálogo para crear nueva organización U-hub"
        )

    def _on_new_uhub_user(self):
        """Maneja la creación de un nuevo usuario U-hub."""
        QMessageBox.information(
            self, "Nuevo Usuario U-hub", "Diálogo para crear nuevo usuario U-hub"
        )

    def _on_new_uspace(self):
        """Maneja la creación de un nuevo U-space."""
        QMessageBox.information(
            self, "Nuevo U-space", "Diálogo para crear nuevo U-space"
        )

    # Métodos para botones de acción
    def _on_start_clicked(self):
        """Maneja el clic en el botón Start."""
        current_tab = self._get_current_tab_name()
        if current_tab == "campaigns":
            QMessageBox.information(
                self, "Iniciar Campaña", "Iniciando campaña de test..."
            )
        elif current_tab == "test_management":
            QMessageBox.information(self, "Ejecutar Tests", "Ejecutando tests...")
        else:
            QMessageBox.information(self, "Start", "Acción start para esta pestaña")

    def _on_add_clicked(self):
        """Maneja el clic en el botón Add."""
        current_tab = self._get_current_tab_name()
        if current_tab == "bugs":
            self._on_new_bug()
        else:
            QMessageBox.information(
                self, "Añadir", f"Añadir nuevo elemento en {current_tab}"
            )

    def _on_edit_clicked(self):
        """Maneja el clic en el botón Edit."""
        current_tab = self._get_current_tab_name()
        if current_tab == "bugs" and self.tbl_bugs.selectionModel().hasSelection():
            # Obtener bug seleccionado
            selected_indexes = self.tbl_bugs.selectionModel().selectedRows()
            if selected_indexes:
                index = selected_indexes[0]
                self._on_bug_double_clicked(index)
        else:
            QMessageBox.information(self, "Editar", f"Editar elemento en {current_tab}")

    def _on_remove_clicked(self):
        """Maneja el clic en el botón Remove."""
        current_tab = self._get_current_tab_name()
        if current_tab == "bugs" and self.tbl_bugs.selectionModel().hasSelection():
            # Obtener bug seleccionado
            selected_indexes = self.tbl_bugs.selectionModel().selectedRows()
            if selected_indexes:
                index = selected_indexes[0]
                proxy_model = self.tbl_bugs.model()
                source_index = proxy_model.mapToSource(index)
                bug_id = proxy_model.sourceModel().bugs[source_index.row()].id

                # Confirmar eliminación
                reply = QMessageBox.question(
                    self,
                    "Eliminar Bug",
                    f"¿Estás seguro de eliminar el bug ID: {bug_id}?",
                    QMessageBox.Yes | QMessageBox.No,
                )
                if reply == QMessageBox.Yes and self.bug_controller:
                    self.bug_controller.handle_delete_item(bug_id)
        else:
            QMessageBox.information(
                self, "Eliminar", f"Eliminar elemento en {current_tab}"
            )

    def _get_current_tab_name(self) -> str:
        """Obtiene el nombre de la pestaña actual."""
        current_index = self.stacked_widget.currentIndex()
        tab_mapping = {
            0: "bugs",
            1: "campaigns",
            2: "test_management",
            3: "requirements",
            4: "assets",
        }
        return tab_mapping.get(current_index, "unknown")

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
