from PySide6.QtWidgets import QMessageBox

from uat_tool.application import (
    ApplicationContext,
    RequirementService,
)
from uat_tool.application.dto import (
    RequirementFormDTO,
    RequirementTableDTO,
)
from uat_tool.presentation import RequirementProxyModel, RequirementTableModel
from uat_tool.presentation.dialogs.requirement_dialog import RequirementDialog
from uat_tool.shared import get_logger

from .base_tab_controller import BaseTabController

logger = get_logger(__name__)


class RequirementTabController(BaseTabController):
    """Controlador específico para la pestaña de Requisitos."""

    def __init__(self, app_context: ApplicationContext):
        super().__init__(app_context, "requirements")
        self.requirement_service: RequirementService = self.app_context.get_service(
            "requirement_service"
        )
        self.table_model = RequirementTableModel()
        self.proxy_model = RequirementProxyModel()
        self.proxy_model.setSourceModel(self.table_model)

    def load_data(self):
        """Carga los datos de requisitos enriquecidos para la tabla."""
        try:
            logger.info("Iniciando carga de datos...")
            self.loading_state_changed.emit(True)

            requirement_table_dto = self.get_all_items()
            logger.info(
                f"{len(requirement_table_dto)} requisitos obtenidos y enriquecidos"
            )

            self._on_data_loaded(requirement_table_dto)

        except Exception as e:
            print(f"ERROR en load_data: {e}")
            self.loading_state_changed.emit(False)
            self.error_occurred.emit(f"Error cargando datos: {str(e)}")

    def _on_data_loaded(self, requirements: list[RequirementTableDTO]):
        """Actualiza el modelo de tabla con los datos enriquecidos."""
        try:
            print("Actualizando table_model con requirements...")
            self.table_model.update_data(requirements)
            self._current_data = requirements

            self.data_loaded.emit(requirements)
            logger.info(f"Datos cargados para requirements: {len(requirements)} items")

        except Exception as e:
            logger.error(f"Error actualizando modelo con requirements: {e}")
            self.error_occurred.emit(f"Error actualizando datos: {str(e)}")
        finally:
            self.loading_state_changed.emit(False)

    # --- MÉTODOS PARA INTERACCIÓN CON LA UI ---

    def handle_new_register(self):
        """Maneja la creación de un nuevo requisito."""
        try:
            logger.info("Abriendo diálogo para nuevo requisito...")

            # Crear y mostrar diálogo de formulario
            dialog = RequirementDialog(self.app_context)
            if dialog.exec():
                form_dto = dialog.get_form_data()
                new_item = self.create_item(form_dto)
                self.item_created.emit(new_item)
                logger.info(f"Nuevo requisito creado: {new_item.code}")

                # Mostrar mensaje de éxito
                QMessageBox.information(
                    None,
                    "Éxito",
                    f"Requisito creado correctamente (Code: '{new_item.code}')",
                )

        except Exception as e:
            logger.error(f"Error creando nuevo requisito: {e}")
            self.error_occurred.emit(f"Error creando requisito: {str(e)}")

    def handle_edit_register(self):
        """Maneja la edición del requisito seleccionado."""
        if not self._selected_item_id:
            self.error_occurred.emit("No hay ningún requisito seleccionado para editar")
            return

        try:
            logger.info(f"Editando requisito {self._selected_item_id}...")

            # Obtener datos actuales del requisito
            requirement = self.get_item_form_dto_by_id(self._selected_item_id)
            if not requirement:
                self.error_occurred.emit(
                    f"Requirement {self._selected_item_id} no encontrado"
                )
                return

            # Crear diálogo con datos actuales
            dialog = RequirementDialog(self.app_context, requirement)
            if dialog.exec():
                form_dto = dialog.get_form_data()
                updated_item = self.update_item(self._selected_item_id, form_dto)
                self.item_updated.emit(updated_item)
                logger.info(f"Requisito {self._selected_item_id} actualizado")

                # Mostrar mensaje de éxito
                QMessageBox.information(
                    None,
                    "Éxito",
                    f"Requisito actualizado correctamente (Code: '{self._selected_item_id}')",
                )

        except Exception as e:
            logger.error(f"Error editando requisito: {e}")
            self.error_occurred.emit(f"Error editando requisito: {str(e)}")

    def handle_remove_register(self):
        """Maneja la eliminación del requisito seleccionado."""
        if not self._selected_item_id:
            self.error_occurred.emit(
                "No hay ningún requisito seleccionado para eliminar"
            )
            return

        try:
            logger.info(f"Eliminando requisito {self._selected_item_id}...")

            # Confirmar eliminación
            reply = QMessageBox.question(
                None,
                "Confirmar eliminación",
                f"¿Estás seguro de que quieres eliminar el requisito {self._selected_item_id}?\n\nEsta acción no se puede deshacer.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                success = self.delete_item(self._selected_item_id)
                if success:
                    logger.info(f"Requisito {self._selected_item_id} eliminado")
                    self.item_deleted.emit(self._selected_item_id)
                    self.set_selected_item(None)

                    # Mostrar mensaje de éxito
                    QMessageBox.information(
                        None,
                        "Éxito",
                        "Requisito eliminado correctamente",
                    )
                else:
                    self.error_occurred.emit(
                        f"Error eliminando requisito {self._selected_item_id}"
                    )
        except Exception as e:
            logger.error(f"Error eliminando requisito: {e}")
            self.error_occurred.emit(f"Error eliminando requisito: {str(e)}")

    def handle_double_click(self, index):
        """Maneja doble clic en la tabla (equivale a editar)."""
        try:
            # Obtener el ID del requirement clickeado
            source_index = self.proxy_model.mapToSource(index)
            if 0 <= source_index.row() < len(self.table_model.requirements):
                requirement_dto = self.table_model.requirements[source_index.row()]
                requirement_id = requirement_dto.id

                # Establecer como seleccionado y editar
                self.set_selected_item(requirement_id)
                self.handle_edit_register()
            else:
                self.error_occurred.emit("Índice fuera de rango")
        except Exception as e:
            logger.error(f"Error manejando doble clic: {e}")
            self.error_occurred.emit(f"Error manejando doble clic: {str(e)}")

    def get_item_table_dto_by_id(self, item_id) -> RequirementTableDTO | None:
        """Obtiene un requirement enriquecido por su ID."""
        for requirement in self._current_data:
            if requirement.id == item_id:
                return requirement
        return None

    def get_item_form_dto_by_id(self, item_id) -> RequirementFormDTO | None:
        """Obtiene un requirement como formulario DTO por su ID."""
        requirement_dto = self.requirement_service.get_requirement_dto_by_id(item_id)
        if not requirement_dto:
            return None

        return RequirementFormDTO.from_service_dto(requirement_dto)

    def delete_item(self, item_id: int) -> bool:
        """Elimina un requirement."""
        try:
            success = self.requirement_service.delete_requirement(item_id)
            return success
        except Exception as e:
            logger.error(f"Error eliminando requirement {item_id}: {e}")
            return False

    def get_all_items(self) -> list[RequirementTableDTO]:
        """Obtiene todos los requirements enriquecidos para la tabla."""
        logger.info("Obteniendo todos los items...")
        return self.requirement_service.get_all_requirements_for_table()

    def create_item(self, form_dto: RequirementFormDTO) -> RequirementTableDTO:
        """Crea un nuevo requirement desde formulario."""
        logger.info("Creando nuevo requirement...")

        # CONTEXTO HARDCODEADO PROVISIONAL. EN EL FUTURO SERÁ VARIABLE DE CONFIGURACIÓN DEFINIDA
        # POR EL USUARIO AL INICIAR EL PROGRAMA.
        context = {
            "modified_by": "provisional",
            "environment_id": 1,
        }

        # Enviar al servicio para crear
        created_service_dto = self.requirement_service.create_requirement_from_form(
            form_dto, context
        )

        # Convertir a TableDTO para la tabla
        return self.requirement_service._enrich_requirement_for_table(
            created_service_dto
        )

    def update_item(
        self, item_id: int, form_dto: RequirementFormDTO
    ) -> RequirementTableDTO:
        """Actualiza un requirement desde formulario."""
        logger.info(f"Actualizando requirement {item_id}...")

        # CONTEXTO HARDCODEADO PROVISIONAL. EN EL FUTURO SERÁ VARIABLE DE CONFIGURACIÓN DEFINIDA
        # POR EL USUARIO AL INICIAR EL PROGRAMA.
        context = {
            "modified_by": "provisional",
            "environment_id": "id",
        }

        # Enviar al servicio para actualizar
        updated_service_dto = self.requirement_service.update_requirement_from_form(
            item_id, form_dto, context
        )
        if not updated_service_dto:
            raise ValueError(f"Requirement con ID {item_id} no encontrado")

        # Convertir a TableDTO para la tabla
        return self.requirement_service._enrich_requirement_for_table(
            updated_service_dto
        )
