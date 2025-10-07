from uat_tool.application import (
    ApplicationContext,
    BugService,
)
from uat_tool.application.dto import BugFormDTO, BugServiceDTO, BugTableDTO
from uat_tool.presentation import BugProxyModel, BugTableModel
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

            bugs_table_dto = self.bug_service.get_all_bugs_for_table()
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

    def get_all_items(self) -> list[BugTableDTO]:
        """Obtiene todos los bugs enriquecidos para la tabla."""
        logger.info("Obteniendo todos los items...")
        return self.bug_service.get_all_bugs_for_table()

    def create_item(self, form_dto: BugFormDTO) -> BugTableDTO:
        """Crea un nuevo bug desde formulario."""
        logger.info("Creando nuevo bug...")

        # Convertir FormDTO → ServiceDTO (en el controller - transformación simple)
        service_dto = self._form_dto_to_service_dto(form_dto)

        # Enviar al servicio para crear
        created_service_dto = self.bug_service.create_bug(service_dto)

        # Convertir a TableDTO para la tabla
        return self.bug_service._enrich_bug_for_table(created_service_dto)

    def update_item(self, item_id: int, form_dto: BugFormDTO) -> BugTableDTO:
        """Actualiza un bug desde formulario."""
        logger.info(f"Actualizando bug {item_id}...")

        # Convertir FormDTO → dict para actualización
        update_data = self._form_dto_to_update_dict(form_dto)

        # Enviar al servicio para actualizar
        updated_service_dto = self.bug_service.update_bug(item_id, update_data)
        if not updated_service_dto:
            raise ValueError(f"Bug con ID {item_id} no encontrado")

        # Convertir a TableDTO para la tabla
        return self.bug_service._enrich_bug_for_table(updated_service_dto)

    def get_item_by_id(self, item_id: int) -> BugFormDTO:
        """Obtiene un bug para edición en formulario."""
        logger.info(f"Obteniendo bug {item_id} para edición...")

        service_dto = self.bug_service.get_bug_dto_by_id(item_id)
        if not service_dto:
            raise ValueError(f"Bug con ID {item_id} no encontrado")

        return self._service_dto_to_form_dto(service_dto)

    def delete_item(self, item_id: int) -> bool:
        """Elimina un bug."""
        logger.info(f"🔄 [BugTabController] Eliminando bug {item_id}...")
        return self.bug_service.delete_bug(item_id)

    # --- TRANSFORMACIONES SIMPLES (en el controller) ---

    def _service_dto_to_form_dto(self, service_dto: BugServiceDTO) -> BugFormDTO:
        """Convierte ServiceDTO → FormDTO para formularios de edición."""
        # TRANSFORMACIÓN SIMPLE - solo cambio de formato/nombres
        return BugFormDTO(
            cb_status=service_dto.status,
            cb_system=str(service_dto.system_id),  # Convertir a string para UI
            le_version=service_dto.system_version,
            cb_urgency=int(service_dto.urgency),
            cb_impact=int(service_dto.impact),
            le_short_desc=service_dto.short_description,
            le_definition=service_dto.definition,
            cb_campaign=service_dto.campaign_run_id,
            lw_requirements=service_dto.requirements,
            le_service_now_id=service_dto.service_now_id or "",
            comments=service_dto.comments or "",
            le_files=service_dto.file_id or 0,
        )

    def _form_dto_to_service_dto(self, form_dto: BugFormDTO) -> dict:
        """Convierte FormDTO → dict para crear nuevo bug."""
        # TRANSFORMACIÓN SIMPLE + datos de contexto
        return {
            "status": form_dto.cb_status,
            "system_id": int(form_dto.cb_system),  # Convertir a int
            "system_version": form_dto.le_version,
            "urgency": str(form_dto.cb_urgency),  # Convertir a string
            "impact": str(form_dto.cb_impact),
            "short_description": form_dto.le_short_desc,
            "definition": form_dto.le_definition,
            "campaign_run_id": form_dto.cb_campaign,
            "requirements": form_dto.lw_requirements,
            "service_now_id": form_dto.le_service_now_id or None,
            "comments": form_dto.comments or None,
            "file_id": form_dto.le_files if form_dto.le_files else None,
            "modified_by": "current_user",  # ← Datos de contexto
            "environment_id": 1,  # ← Datos de contexto
        }

    def _form_dto_to_update_dict(self, form_dto: BugFormDTO) -> dict:
        """Convierte FormDTO → dict para actualización (excluye algunos campos)."""
        update_data = self._form_dto_to_service_dto(form_dto)
        # Remover campos que no deberían actualizarse
        update_data.pop("modified_by", None)
        update_data.pop("environment_id", None)
        return update_data

    # Métodos específicos para Bugs
    def get_bugs_by_status(self, status: str) -> list[BugTableDTO]:
        """Obtiene bugs por estado."""
        bugs = self.bug_service.get_bugs_by_status(status)
        return [self.bug_service._to_dto(bug) for bug in bugs]

    def get_bugs_by_priority(self, priority: str) -> list[BugTableDTO]:
        """Obtiene bugs por prioridad."""
        bugs = self.bug_service.get_bugs_by_priority(priority)
        return [self.bug_service._to_dto(bug) for bug in bugs]
