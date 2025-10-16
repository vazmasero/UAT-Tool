import os
import shutil
from pathlib import Path

from PySide6.QtWidgets import QMessageBox

from uat_tool.application import (
    ApplicationContext,
    AuxiliaryService,
    BugService,
)
from uat_tool.application.dto import BugFormDTO, BugTableDTO, FileServiceDTO
from uat_tool.presentation import BugProxyModel, BugTableModel
from uat_tool.presentation.dialogs.bug_dialog import BugDialog
from uat_tool.shared import get_logger

from .base_tab_controller import BaseTabController

logger = get_logger(__name__)


class BugTabController(BaseTabController):
    """Controlador específico para la pestaña de Bugs."""

    def __init__(self, app_context: ApplicationContext):
        super().__init__(app_context, "bugs")
        self.bug_service: BugService = self.app_context.get_service("bug_service")
        self.aux_service: AuxiliaryService = self.app_context.get_service(
            "auxiliary_service"
        )
        self.table_model = BugTableModel()
        self.proxy_model = BugProxyModel()
        self.proxy_model.setSourceModel(self.table_model)

    def load_data(self):
        """Carga los datos de bugs enriquecidos para la tabla."""
        try:
            print("Iniciando carga de datos...")
            self.loading_state_changed.emit(True)

            bugs_table_dto = self.get_all_items()
            logger.info(f"{len(bugs_table_dto)} bugs obtenidos y enriquecidos")

            self._on_data_loaded(bugs_table_dto)

        except Exception as e:
            print(f"ERROR en load_data: {e}")
            self.loading_state_changed.emit(False)
            self.error_occurred.emit(f"Error cargando datos: {str(e)}")

    def _on_data_loaded(self, bugs: list[BugTableDTO]):
        """Actualiza el modelo de tabla con los datos enriquecidos."""
        try:
            print("Actualizando table_model...")
            self.table_model.update_data(bugs)

            self.data_loaded.emit(bugs)

            logger.info(f"Datos cargados para bugs: {len(bugs)} items")
        except Exception as e:
            logger.error(f"Error actualizando modelo con bugs: {e}")
            self.error_occurred.emit(f"Error actualizando datos: {str(e)}")
        finally:
            self.loading_state_changed.emit(False)

    # --- MÉTODOS PARA INTERACCIÓN CON LA UI ---

    def handle_new_register(self):
        """Maneja la creación de un nuevo bug desde formulario"""
        dialog = None
        try:
            logger.info("Abriendo diálogo para nuevo bug...")

            # Crear y mostrar diálogo de formulario
            dialog = BugDialog(self.app_context)
            if dialog.exec():
                # Obtener datos del formulario
                form_dto = dialog.get_form_data()
                file_dtos = dialog.get_selected_files_data()

                # Crear el bug (sin archivos)
                new_item = self.create_item(form_dto)
                bug_id = new_item.id

                logger.info(f"Bug creado con ID: {bug_id}")

                # Si hay archivos, procesarlos
                if file_dtos:
                    try:
                        self._process_bug_files(bug_id, file_dtos)

                    except Exception as file_error:
                        logger.error(f"Error procesando archivos: {file_error}")

                        # Eliminar bug si fallan archivos
                        self._rollback_bug_creation(bug_id)

                        # Mostrar error y mantener diálogo abierto
                        QMessageBox.critical(
                            dialog,  # Usar dialog como parent para mantenerlo abierto
                            "Error en archivos",
                            f"Error procesando archivos: {str(file_error)}\n\nEl bug no se ha creado. Puede intentarlo de nuevo.",
                        )
                        return

                # Éxito completo
                QMessageBox.information(
                    None,
                    "Éxito",
                    f"Bug creado correctamente con {len(file_dtos)} archivos adjuntos",
                )

                # Emit signal para actualizar
                self.item_created.emit(new_item)

        except Exception as e:
            logger.error(f"Error creando nuevo bug: {e}")

            if dialog and dialog.isVisible():
                QMessageBox.critical(
                    dialog,
                    "Error creando bug",
                    f"Error creando bug: {str(e)}\n\nPuede intentarlo de nuevo.",
                )
            else:
                self.error_occurred.emit(f"Error creando bug: {str(e)}")

    def handle_edit_register(self):
        """Maneja la edición del bug seleccionado desde formulario."""
        if not self._selected_item_id:
            self.error_occurred.emit("No hay ningún bug seleccionado para editar")
            return

        try:
            logger.info(f"Editando bug {self._selected_item_id}...")

            # Obtener datos actuales del bug
            bug = self.get_item_form_dto_by_id(self._selected_item_id)
            if not bug:
                self.error_occurred.emit(f"Bug {self._selected_item_id} no encontrado")
                return

            # Crear diálogo con datos actuales
            dialog = BugDialog(self.app_context, bug)
            if dialog.exec():
                form_dto = dialog.get_form_data()
                updated_item = self.update_item(self._selected_item_id, form_dto)

                self._process_bug_files_edit(
                    bug_id=self._selected_item_id,
                    new_selected_files=form_dto.selected_files,
                )
                # Mostrar mensaje de éxito
                QMessageBox.information(
                    None,
                    "Éxito",
                    "Bug actualizado correctamente",
                )
                self.item_updated.emit(updated_item)
                logger.info(f"Bug {self._selected_item_id} actualizado")

        except Exception as e:
            logger.error(f"Error editando bug: {e}")
            self.error_occurred.emit(f"Error editando bug: {str(e)}")

    def handle_remove_register(self):
        """Maneja la eliminación del bug seleccionado."""
        if not self._selected_item_id:
            self.error_occurred.emit("No hay ningún bug seleccionado para eliminar")
            return

        try:
            logger.info(f"Eliminando bug {self._selected_item_id}...")

            # Confirmar eliminación
            reply = QMessageBox.question(
                None,
                "Confirmar eliminación",
                f"¿Estás seguro de que quieres eliminar el bug {self._selected_item_id} y sus archivos adjuntos?\n\nEsta acción no se puede deshacer.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                current_files = self.aux_service.get_files_by_bug_id(
                    self._selected_item_id
                )
                success = self.delete_item(self._selected_item_id)
                if success:
                    logger.info(f"Bug {self._selected_item_id} eliminado")
                    self._remove_bug_files(self._selected_item_id, current_files)
                    self.item_deleted.emit(self._selected_item_id)
                    self.set_selected_item(None)

                    # Mostrar mensaje de éxito
                    QMessageBox.information(
                        None,
                        "Éxito",
                        "Bug eliminado correctamente",
                    )
                else:
                    self.error_occurred.emit(
                        f"Error eliminando bug {self._selected_item_id}"
                    )
        except Exception as e:
            logger.error(f"Error eliminando bug: {e}")
            self.error_occurred.emit(f"Error eliminando bug: {str(e)}")

    def handle_double_click(self, index):
        """Maneja doble clic en la tabla (equivale a editar)."""
        try:
            # Obtener el ID del bug clickeado
            source_index = self.proxy_model.mapToSource(index)
            if 0 <= source_index.row() < len(self.table_model.bugs):
                bug_dto = self.table_model.bugs[source_index.row()]
                bug_id = bug_dto.id

                # Establecer como seleccionado y editar
                self.set_selected_item(bug_id)
                self.handle_edit_register()
            else:
                self.error_occurred.emit("Índice fuera de rango")
        except Exception as e:
            logger.error(f"Error manejando doble clic: {e}")
            self.error_occurred.emit(f"Error manejando doble clic: {str(e)}")

    def get_all_items(self) -> list[BugTableDTO]:
        """Obtiene todos los bugs enriquecidos para la tabla."""
        logger.info("Obteniendo todos los items...")
        return self.bug_service.get_all_bugs_for_table()

    def create_item(self, form_dto: BugFormDTO) -> BugTableDTO:
        """Crea un nuevo bug desde formulario."""
        logger.info("Creando nuevo bug...")

        # CONTEXTO HARDCODEADO PROVISIONAL. EN EL FUTURO SERÁ VARIABLE DE CONFIGURACIÓN DEFINIDA
        # POR EL USUARIO AL INICIAR EL PROGRAMA.
        context = {
            "modified_by": "provisional",
            "environment_id": 1,
        }

        # Enviar al servicio para crear
        created_service_dto = self.bug_service.create_bug_from_form(form_dto, context)

        # Convertir a TableDTO para la tabla
        return self.bug_service._enrich_bug_for_table(created_service_dto)

    def update_item(self, item_id: int, form_dto: BugFormDTO) -> BugTableDTO:
        """Actualiza un bug desde formulario."""
        logger.info(f"Actualizando bug {item_id}...")

        # CONTEXTO HARDCODEADO PROVISIONAL. EN EL FUTURO SERÁ VARIABLE DE CONFIGURACIÓN DEFINIDA
        # POR EL USUARIO AL INICIAR EL PROGRAMA.
        context = {
            "modified_by": "provisional",
            "environment_id": 1,
        }

        # Enviar al servicio para actualizar
        updated_service_dto = self.bug_service.update_bug_from_form(
            item_id, form_dto, context
        )
        if not updated_service_dto:
            raise ValueError(f"Bug con ID {item_id} no encontrado")

        # Convertir a TableDTO para la tabla
        return self.bug_service._enrich_bug_for_table(updated_service_dto)

    def get_item_table_dto_by_id(self, item_id) -> BugTableDTO | None:
        """Obtiene un bug enriquecido por su ID."""
        for bug in self._current_data:
            if bug.id == item_id:
                return bug
        return None

    def get_item_form_dto_by_id(self, item_id) -> BugFormDTO | None:
        """Obtiene un bug como formulario DTO por su ID."""
        bug_dto = self.bug_service.get_bug_dto_by_id(item_id)
        if not bug_dto:
            return None

        return BugFormDTO.from_service_dto(bug_dto)

    def delete_item(self, item_id: int) -> bool:
        """Elimina un bug."""
        logger.info(f"Eliminando bug {item_id}...")
        return self.bug_service.delete_bug(item_id)

    def _rollback_bug_creation(self, bug_id: int):
        """Eliminar un bug creado y sus archivos en caso de error."""
        try:
            logger.info(f"Realizando rollback del bug {bug_id}")

            bug_dir = self.ensure_bug_directory(bug_id)
            if bug_dir.exists():
                import shutil

                shutil.rmtree(bug_dir)
                logger.info(f"Carpeta de archivos eliminada: {bug_dir}")

                self.delete_item(bug_id)
                logger.info(f"Bug {bug_id} eliminado de la base de datos")

        except Exception as rollback_error:
            logger.error(f"Error en rollback del bug {bug_id}: {rollback_error}")
            # TO DO Informar sobre un estado inconsistente

    # Métodos específicos para Bugs
    def get_bugs_by_status(self, status: str) -> list[BugTableDTO]:
        """Obtiene bugs por estado."""
        bugs = self.bug_service.get_bugs_by_status(status)
        return [self.bug_service._to_dto(bug) for bug in bugs]

    def get_bugs_by_priority(self, priority: str) -> list[BugTableDTO]:
        """Obtiene bugs por prioridad."""
        bugs = self.bug_service.get_bugs_by_priority(priority)
        return [self.bug_service._to_dto(bug) for bug in bugs]

    # Manejo de archivos
    def _process_bug_files(self, bug_id: int, file_dtos: list[FileServiceDTO]):
        """Procesa y guarda los archivos de un bug."""
        try:
            # Crear directorio para el bug
            bug_dir = self.ensure_bug_directory(bug_id)
            saved_files = []

            # Copiar cada archivo y actualizar el DTO
            for file_dto in file_dtos:
                # Generar nombre único para el archivo
                original_name = Path(file_dto.filepath).name
                unique_name = self._generate_unique_filename(bug_dir, original_name)
                destination_path = bug_dir / unique_name

                # Copiar archivo
                shutil.copy2(file_dto.filepath, destination_path)

                # Actualizar FileServiceDTO con la ruta definitiva
                file_dto.filepath = str(destination_path)
                file_dto.owner_type = "bug"
                saved_files.append(file_dto)

                logger.info(f"Archivo copiado: {original_name} -> {destination_path}")

                # Crear registros en BD
                if saved_files:
                    self.aux_service.create_files_for_bug(saved_files, bug_id)
                    logger.info(
                        f"{len(saved_files)} archivos guardados en BD para bug {bug_id}"
                    )

        except Exception as e:
            logger.error(f"Error procesando archivos para bug {bug_id}: {e}")
            self._cleanup_saved_files(saved_files, bug_dir)
            raise  # Relanzar excepción para manejo superior

    def _process_bug_files_edit(
        self,
        bug_id: int,
        new_selected_files: list[FileServiceDTO],
    ):
        """Procesa archivos durante edición - reemplaza todos los anteriores."""
        try:
            current_files = self.aux_service.get_files_by_bug_id(bug_id)

            files_to_keep = []
            files_to_add = []

            for new_file in new_selected_files:
                existing_file = self._find_matching_file(new_file, current_files)
                if existing_file:
                    files_to_keep.append(existing_file)
                else:
                    files_to_add.append(new_file)

            files_to_remove = [f for f in current_files if f not in files_to_keep]

            if files_to_remove:
                self._remove_bug_files(bug_id, files_to_remove)

            if files_to_add:
                self._process_bug_files(bug_id, files_to_add)

            logger.info(
                f"Edición archivos bug {bug_id}: +{len(files_to_add)} -{len(files_to_remove)}"
            )

        except Exception as e:
            logger.error(f"Error procesando archivos en edición para bug {bug_id}: {e}")
            raise

    def _find_matching_file(
        self, new_file: FileServiceDTO, existing_files: list[FileServiceDTO]
    ) -> FileServiceDTO | None:
        """Encuentra un archivo existente que coincida con el nuevo."""
        for existing in existing_files:
            if (
                new_file.filename == existing.filename
                and new_file.size == existing.size
            ):
                return existing
        return None

    def _remove_bug_files(self, bug_id: int, files_to_remove: list[FileServiceDTO]):
        """Elimina archivos de un bug (BD y físico)."""
        try:
            with self.app_context.get_unit_of_work_context() as uow:
                for file_dto in files_to_remove:
                    # Eliminar de BD
                    success = uow.file_repo.delete(file_dto.id)
                    if success:
                        logger.info(f"Archivo {file_dto.filename} eliminado de BD")

                        # Eliminar archivo físico
                        if os.path.exists(file_dto.filepath):
                            os.remove(file_dto.filepath)
                            logger.info(
                                f"Archivo físico eliminado: {file_dto.filepath}"
                            )
        except Exception as e:
            logger.error(f"Error eliminando archivos del bug {bug_id}:{e}")
            raise

    def _cleanup_copied_files(self, copied_files: list, bug_dir: Path):
        """Elimina archivos copiados en caso de error"""
        try:
            # Eliminar archivos individuales copiados
            for file_path in copied_files:
                if file_path.exists():
                    file_path.unlink()
                    logger.info(f"Archivo eliminado por error: {file_path}")

            # Eliminar carpeta si está vacía
            if bug_dir and bug_dir.exists() and not any(bug_dir.iterdir()):
                bug_dir.rmdir()
                logger.info(f"Carpeta vacía eliminada: {bug_dir}")

        except Exception as cleanup_error:
            logger.error(f"Error limpiando archivos copiados: {cleanup_error}")

    def _generate_unique_filename(self, directory: Path, filename: str) -> str:
        """Genera un nombre único para evitar colisiones"""
        path = directory / filename
        if not path.exists():
            return filename

        # Si existe, añadir sufijo numérico
        stem = path.stem
        suffix = path.suffix
        counter = 1

        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = directory / new_name
            if not new_path.exists():
                return new_name
            counter += 1

    def get_bug_files_base_path(self) -> Path:
        """Obtiene la ruta base para archivos de bugs"""
        base_dir = self.aux_service.get_app_root()

        return base_dir / "files" / "bugs"

    def ensure_bug_directory(self, bug_id: int) -> Path:
        """Crea y devuelve la carpeta para un bug específico."""
        bug_dir = self.get_bug_files_base_path() / str(bug_id)
        bug_dir.mkdir(parents=True, exist_ok=True)
        return bug_dir
