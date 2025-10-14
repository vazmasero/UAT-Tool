import shutil
import sys
import uuid
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox

from uat_tool.application import (
    ApplicationContext,
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
        temp_file_dtos = []

        try:
            logger.info("Abriendo diálogo para nuevo bug...")

            # Crear y mostrar diálogo de formulario
            dialog = BugDialog(self.app_context)
            if dialog.exec():
                # 1. Obtener datos del formulario
                form_dto = dialog.get_form_data()
                file_dtos = dialog.get_selected_files_data()

                # 2. Mostrar advertencia si hay archivos grandes
                if file_dtos:
                    QMessageBox.information(
                        None,
                        "Procesando archivos",
                        f"Preparando {len(file_dtos)} archivo(s)...",
                    )

                # 3. Copiar archivos a ubicación temporal con UUID
                temp_file_dtos = self._copy_files_to_temp(file_dtos)

                # Si el usuario canceló archivos muy grandes
                if file_dtos and not temp_file_dtos:
                    logger.info("Usuario canceló la operación por archivos muy grandes")
                    return

                # 4. Crear el bug (sin archivos)
                new_item = self.create_item(form_dto)

                # 5. Mover archivos a ubicación definitiva con ID real
                final_file_dtos = self._move_files_to_final_location(
                    temp_file_dtos, new_item.id
                )

                # 6. Actualizar bug con referencias a archivos
                self._associate_files_with_bug(new_item.id, final_file_dtos)

                # 7. Emitir señal
                self.item_created.emit(new_item)
                logger.info(f"Nuevo bug creado: {new_item.id}")

                # Mostrar mensaje de éxito
                success_msg = f"Bug creado correctamente (Id: '{new_item.id}')"
                if final_file_dtos:
                    success_msg += f"\n\nArchivos asociados: {len(final_file_dtos)}"

                QMessageBox.information(None, "Éxito", success_msg)

        except Exception as e:
            # 8. Limpiar archivos temporales en caso de error
            if temp_file_dtos:  # ← Solo si hay archivos temporales
                self._cleanup_temp_files(temp_file_dtos)
                logger.info("Archivos temporales limpiados debido a error")

            logger.error(f"Error creando nuevo bug: {e}")
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
                self.item_updated.emit(updated_item)
                logger.info(f"Bug {self._selected_item_id} actualizado")

                # Mostrar mensaje de éxito
                QMessageBox.information(
                    None,
                    "Éxito",
                    f"Bug actualizado correctamente (Code: '{self._selected_item_id}')",
                )

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
                f"¿Estás seguro de que quieres eliminar el bug {self._selected_item_id}?\n\nEsta acción no se puede deshacer.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                success = self.delete_item(self._selected_item_id)
                if success:
                    logger.info(f"Bug {self._selected_item_id} eliminado")
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
            "environment_id": "id",
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
        logger.info(f"🔄 [BugTabController] Eliminando bug {item_id}...")
        return self.bug_service.delete_bug(item_id)

    # Métodos específicos para Bugs
    def get_bugs_by_status(self, status: str) -> list[BugTableDTO]:
        """Obtiene bugs por estado."""
        bugs = self.bug_service.get_bugs_by_status(status)
        return [self.bug_service._to_dto(bug) for bug in bugs]

    def get_bugs_by_priority(self, priority: str) -> list[BugTableDTO]:
        """Obtiene bugs por prioridad."""
        bugs = self.bug_service.get_bugs_by_priority(priority)
        return [self.bug_service._to_dto(bug) for bug in bugs]

    # Métodos de archivos
    def _get_app_root(self) -> Path:
        """Obtiene la ruta raíz de la aplicación."""
        # Si está empaquetado con PyInstaller
        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent
        else:
            return Path(__file__).parent.parent.parent  # Ajustar según tu estructura

    def _copy_files_to_temp(
        self, file_dtos: list[FileServiceDTO]
    ) -> list[FileServiceDTO]:
        """Copia archivos a carpeta temporal con manejo de archivos grandes."""
        # Si no hay archivos, retornar lista vacía inmediatamente
        if not file_dtos:
            return []

        temp_dir = self._get_app_root() / "files" / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)

        # Verificar archivos muy grandes (>500MB)
        very_large_files = self._get_very_large_files(file_dtos)
        if very_large_files:
            if not self._confirm_very_large_files(very_large_files):
                return []

        temp_file_dtos = []

        for file_dto in file_dtos:
            try:
                file_path = Path(file_dto.filepath)
                if not file_path.exists():
                    logger.warning(f"Archivo no encontrado: {file_dto.filepath}")
                    continue

                file_size = file_path.stat().st_size
                temp_path = None

                # Estrategia de copia según tamaño
                if file_size > 100 * 1024 * 1024:  # > 100MB
                    temp_path = self._copy_large_file_by_chunks(file_dto, temp_dir)
                else:  # < 100MB
                    temp_path = self._copy_file_normal(file_dto, temp_dir)

                if temp_path:
                    temp_id = str(uuid.uuid4())
                    new_file_dto = FileServiceDTO(
                        id=0,
                        owner_type="bug_temp",
                        filename=file_path.name,
                        filepath=str(temp_path),
                        mime_type=file_dto.mime_type,
                        size=self._format_file_size(file_size),
                        uploaded_by=file_dto.uploaded_by,
                        uploaded_at=file_dto.uploaded_at,
                        temp_id=temp_id,
                    )

                    temp_file_dtos.append(new_file_dto)
                    logger.info(
                        f"Archivo copiado: {file_dto.filename} ({self._format_file_size(file_size)})"
                    )

            except Exception as e:
                logger.error(f"Error moviendo archivo a temporal: {e}")
                raise

        return temp_file_dtos

    def _get_very_large_files(self, file_dtos: list[FileServiceDTO]) -> list[tuple]:
        """Identifica archivos muy grandes (>500MB)."""
        very_large_files = []
        for dto in file_dtos:
            try:
                file_size = Path(dto.filepath).stat().st_size
                if file_size > 500 * 1024 * 1024:  # 500MB
                    very_large_files.append(
                        (dto.filename, self._format_file_size(file_size))
                    )
            except Exception as e:
                logger.warning(f"No se pudo obtener tamaño de {dto.filename}: {e}")

        return very_large_files

    def _confirm_very_large_files(self, large_files: list[tuple]) -> bool:
        """Pide confirmación para archivos muy grandes."""
        file_list = "\n".join([f"- {name} ({size})" for name, size in large_files])

        reply = QMessageBox.question(
            None,
            "Archivos muy grandes detectados",
            f"Los siguientes archivos son muy grandes:\n{file_list}\n\n"
            f"La copia puede tomar varios minutos.\n¿Desea continuar?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        return reply == QMessageBox.Yes

    def _copy_file_normal(self, file_dto: FileServiceDTO, temp_dir: Path) -> Path:
        """Copia normal para archivos pequeños/medianos."""
        original_path = Path(file_dto.filepath)
        temp_id = str(uuid.uuid4())
        temp_filename = f"{temp_id}_{original_path.name}"
        temp_path = temp_dir / temp_filename

        shutil.copy2(original_path, temp_path)
        return temp_path

    def _copy_large_file_by_chunks(
        self, file_dto: FileServiceDTO, temp_dir: Path
    ) -> Path:
        """Copia archivos grandes por chunks permitiendo que la UI respire."""
        original_path = Path(file_dto.filepath)
        temp_id = str(uuid.uuid4())
        temp_filename = f"{temp_id}_{original_path.name}"
        temp_path = temp_dir / temp_filename

        file_size = original_path.stat().st_size
        chunk_size = self._get_optimal_chunk_size(file_size)

        try:
            copied_bytes = 0
            with open(original_path, "rb") as src, open(temp_path, "wb") as dst:
                while True:
                    chunk = src.read(chunk_size)
                    if not chunk:
                        break
                    dst.write(chunk)
                    copied_bytes += len(chunk)

                    # Cada 5 chunks, permitir que la UI se actualice
                    if copied_bytes % (chunk_size * 5) == 0:
                        QApplication.processEvents()

            return temp_path

        except Exception:
            # Limpiar en caso de error
            if temp_path.exists():
                temp_path.unlink()
            raise

    def _get_optimal_chunk_size(self, file_size: int) -> int:
        """Determina el tamaño óptimo del chunk según el tamaño del archivo."""
        if file_size > 1024 * 1024 * 1024:  # > 1GB
            return 50 * 1024 * 1024  # 50MB chunks
        elif file_size > 500 * 1024 * 1024:  # > 500MB
            return 20 * 1024 * 1024  # 20MB chunks
        else:  # 100MB - 500MB
            return 10 * 1024 * 1024  # 10MB chunks

    def _move_files_to_final_location(
        self, temp_file_dtos: list[FileServiceDTO], bug_id: int
    ) -> list[FileServiceDTO]:
        """Mueve archivos de temporal a ubicación definitiva."""
        bugs_dir = self._get_app_root() / "files" / "bugs" / str(bug_id)
        bugs_dir.mkdir(parents=True, exist_ok=True)

        final_file_dtos = []

        for temp_dto in temp_file_dtos:
            try:
                temp_path = Path(temp_dto.filepath)
                final_filename = temp_path.name.replace(
                    f"{temp_dto.temp_id}_", ""
                )  # Eliminar UUID
                final_path = bugs_dir / final_filename

                # Mover (no copiar) de temp a definitivo
                shutil.move(str(temp_path), str(final_path))

                # Crear DTO final
                final_file_dto = FileServiceDTO(
                    id=0,
                    owner_type="bug",
                    filename=final_filename,
                    filepath=str(final_path),
                    mime_type=temp_dto.mime_type,
                    size=temp_dto.size,
                    uploaded_by=temp_dto.uploaded_by,
                    uploaded_at=temp_dto.uploaded_at,
                )
                final_file_dtos.append(final_file_dto)

            except Exception as e:
                logger.error(f"Error moviendo archivo a ubicación final: {e}")
                raise

        return final_file_dtos

    def _cleanup_temp_files(self, temp_file_dtos: list[FileServiceDTO]):
        """Limpia archivos temporales en caso de error."""
        for temp_dto in temp_file_dtos:
            try:
                temp_path = Path(temp_dto.filepath)
                if temp_path.exists():
                    temp_path.unlink()
            except Exception as e:
                logger.warning(f"No se pudo limpiar archivo temporal {temp_path}: {e}")

    def _format_file_size(self, size_bytes: int) -> str:
        """Formatea el tamaño del archivo a string legible."""
        try:
            for unit in ["B", "KB", "MB", "GB"]:
                if size_bytes < 1024.0:
                    return f"{size_bytes:.1f} {unit}"
                size_bytes /= 1024.0
            return f"{size_bytes:.1f} TB"
        except Exception as e:
            logger.error(f"Error formateando tamaño de archivo: {e}")
            return "Unknown size"

    def _associate_files_with_bug(self, bug_id: int, file_dtos: list[FileServiceDTO]):
        """Asocia archivos con un bug en la base de datos."""
        try:
            if not file_dtos:
                logger.info(f"No hay archivos para asociar con bug {bug_id}")
                return

            logger.info(f"Asociando {len(file_dtos)} archivos con bug {bug_id}")

            # Obtener el servicio de archivos
            file_service = self.app_context.get_service("file_service")

            # Actualizar los file_dtos con el bug_id como owner_id
            for file_dto in file_dtos:
                file_dto.owner_id = bug_id  # Si tu FileServiceDTO tiene este campo
                # O usar el contexto si no tienes owner_id en el DTO

            # Crear los archivos en la base de datos
            created_files = file_service.create_files_for_bug(file_dtos, bug_id)

            logger.info(
                f"Archivos asociados correctamente: {len(created_files)} archivos para bug {bug_id}"
            )

        except Exception as e:
            logger.error(f"Error asociando archivos con bug {bug_id}: {e}")
            raise
