# bug_dto.py
from dataclasses import dataclass, field
from datetime import datetime

from uat_tool.application.dto.auxiliary_dto import FileServiceDTO
from uat_tool.application.dto.base_dto import BaseFormDTO, BaseServiceDTO, BaseTableDTO
from uat_tool.domain import Bug, BugHistory


@dataclass
class BugHistoryServiceDTO:
    """DTO para el historial de bugs - comunicación entre servicios."""

    id: int
    bug_id: int
    changed_by: str
    change_timestamp: datetime
    change_summary: str

    @classmethod
    def from_model(cls, history: "BugHistory") -> "BugHistoryServiceDTO":
        return cls(
            id=history.id,
            bug_id=history.bug_id,
            changed_by=history.changed_by,
            change_timestamp=history.change_timestamp,
            change_summary=history.change_summary,
        )


@dataclass
class BugHistoryTableDTO:
    """DTO para el historial de bugs - visualización en UI."""

    changed_by: str
    change_timestamp: str  # Fecha formateada
    change_summary: str

    @classmethod
    def from_service_dto(
        cls, service_dto: BugHistoryServiceDTO
    ) -> "BugHistoryTableDTO":
        timestamp_str = (
            service_dto.change_timestamp.strftime("%d/%m/%Y %H:%M")
            if service_dto.change_timestamp
            else "Not assigned"
        )

        return cls(
            changed_by=service_dto.changed_by,
            change_timestamp=timestamp_str,
            change_summary=service_dto.change_summary,
        )


@dataclass
class BugServiceDTO(BaseServiceDTO):
    """DTO 1:1 con el modelo de dominio para operaciones CRUD y lógica de negocio.
    Propósito: comunicación entre servicios y con repositorios.
    Debe reflejar fielmente la entidad de dominio"""

    # Campos requeridos (sin default)
    status: str  # "OPEN", "CLOSED SOLVED", etc.
    system_id: int
    system_version: str
    short_description: str
    definition: str
    urgency: int  # 1, 2, 3
    impact: int  # 1, 2, 3

    # Campos opcionales (con default)
    campaign_run_id: str | None = None
    service_now_id: str | None = None
    requirements: list[int] = field(default_factory=list)
    comments: str | None = None

    # Campos auxiliares (opcionales)
    system_name: str = ""
    requirement_codes: list[str] = field(default_factory=list)
    files: list[FileServiceDTO] = field(default_factory=list)

    # Historial (se carga bajo demanda)
    history: list[BugHistoryServiceDTO] = field(default_factory=list)

    @classmethod
    def from_model(cls, bug: "Bug") -> "BugServiceDTO":
        """Conversión directa modelo -> DTO (enriquecidos con datos relacionados).

        Args:
            bug (Bug): modelo SQLAlchemy de la entidad a transformar.

        Returns:
            BugServiceDTO: modelo DTO de la entidad transformada.
        """
        system_name = bug.system.name if bug.system else ""
        requirement_codes = (
            [req.code for req in bug.requirements] if bug.requirements else []
        )

        return cls(
            id=bug.id,
            created_at=bug.created_at,
            updated_at=bug.updated_at,
            modified_by=bug.modified_by,
            environment_id=bug.environment_id,
            status=bug.status,
            system_id=bug.system_id,
            system_version=bug.system_version,
            short_description=bug.short_description,
            definition=bug.definition,
            urgency=bug.urgency,
            impact=bug.impact,
            campaign_run_id=bug.campaign_run_id,
            service_now_id=bug.service_now_id,
            comments=bug.comments,
            requirements=[req.id for req in bug.requirements]
            if bug.requirements
            else [],
            history=[BugHistoryServiceDTO.from_model(hist) for hist in bug.history]
            if bug.history
            else [],
            system_name=system_name,
            requirement_codes=requirement_codes,
            files=[],  # Se puebla en el servicio
        )


@dataclass
class BugTableDTO(BaseTableDTO):
    """DTO optimizado para visualización en tablas UI.
    Propósito: mostrar datos enriquecidos y formateados al usuario."""

    # Campos requeridos (sin default)
    status: str  # Estado formateado para UI ("Open, Closed Solved")
    system: str  # Nombre del sistema (no ID)
    system_version: str
    short_description: str
    definition: str
    urgency: str  # "Alta", "Media", "Baja"
    impact: str  # "Alta", "Media", "Baja"

    # Campos opcionales (con default)
    service_now_id: str = "N/A"
    campaign_run: str = "N/A"  # Nombre de la campaña (no ID)
    requirements: str = "N/A"  # Lista de nombres de requisitos
    comments: str = ""
    file_count: int = 0  # Número de archivos adjuntos
    file_names: str = "No files attached"  # Nombres concatenados
    history_count: int = 0  # Número de entradas en el historial

    @classmethod
    def from_service_dto(
        cls,
        service_dto: BugServiceDTO,
        system_name: str = "",
        requirement_codes: list[str] = None,
    ) -> "BugTableDTO":
        """Transforma ServiceDTO -> TableDTO con datos enriquecidos.

        Args:
            service_dto (BugServiceDTO): ServiceDTO a transformar.
            **enrichments: datos enriquecidos (nombre del sistema, código de requisitos, etc)

        Returns:
            BugTableDTO: TableDTO transformado.
        """

        # Mapear urgencia/impacto numérico a texto
        urgency_map = {1: "Baja", 2: "Media", 3: "Alta"}
        impact_map = {1: "Baja", 2: "Media", 3: "Alta"}

        # Formatear fechas (manejar caso de None para nuevos bugs)
        created_at_str = (
            service_dto.created_at.strftime("%d/%m/%Y %H:%M")
            if service_dto.created_at
            else "Not assigned"
        )
        updated_at_str = (
            service_dto.updated_at.strftime("%d/%m/%Y %H:%M")
            if service_dto.updated_at
            else "Not assigned"
        )

        # Formatear requisitos
        requirements_display = (
            ", ".join(requirement_codes)
            if requirement_codes and requirement_codes
            else "N/A"
        )

        file_count = len(service_dto.files)
        file_names = ", ".join(
            [f.filename for f in service_dto.files[:3]]
        )  # Primeros 3

        if file_count > 3:
            file_names += f" ... (+{file_count - 3} más)"

        return cls(
            id=service_dto.id,
            status=service_dto.status.title(),
            system=system_name or "Unknown",
            system_version=service_dto.system_version,
            created_at=created_at_str,
            updated_at=updated_at_str,
            modified_by=service_dto.modified_by,
            service_now_id=service_dto.service_now_id or "N/A",
            campaign_run=service_dto.campaign_run_id or "N/A",
            requirements=requirements_display,
            short_description=service_dto.short_description,
            definition=service_dto.definition,
            urgency=urgency_map.get(service_dto.urgency, "Unknown"),
            impact=impact_map.get(service_dto.impact, "Unknown"),
            comments=service_dto.comments or "",
            file_count=file_count,
            file_names=file_names if file_count > 0 else "No files attached",
            history_count=len(service_dto.history),
        )


@dataclass
class BugFormDTO(BaseFormDTO):
    """DTO específica para formularios de creación/edición.
    Propósito: Capturar datos de formularios UI y validarlos."""

    # Campos requeridos (sin default)
    cb_status: str  # "OPEN", "CLOSED SOLVED", etc.
    cb_system: str  # ID del sistema seleccionado
    le_version: str  # Versión del sistema
    cb_urgency: int  # 1, 2, 3
    cb_impact: int  # 1, 2, 3
    le_short_desc: str  # Descripción corta
    le_definition: str  # Definición

    # Campos OPCIONALES (con default)
    cb_campaign: int | None = None  # ID de la campaña (puede ser None)
    lw_requirements: list[int] = field(
        default_factory=list
    )  # Lista de IDs de requisitos seleccionados
    le_service_now_id: str = ""  # ID de ServiceNow
    le_comments: str = ""  # Comentarios

    # Archivos
    selected_files: list[FileServiceDTO] = field(
        default_factory=list
    )  # Archivos nuevos
    existing_file_ids: list[int] = field(
        default_factory=list
    )  # ID del archivos ya existentes
    existing_file_names: str = ""  # Nombres para mostrar en QLineEdit

    # Historial
    history: list[BugHistoryTableDTO] = field(default_factory=list)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if len(self.le_short_desc.strip()) < 5:
            raise ValueError("La descripción corta debe tener al menos 5 caracteres")
        if len(self.le_definition.strip()) < 10:
            raise ValueError("La definición debe tener al menos 10 caracteres")
        if not self.le_version.strip():
            raise ValueError("La versión del sistema es requerida")

    def to_service_dto(self, context_data: dict) -> BugServiceDTO:
        """Convierte datos de formulario -> ServiceDTO para guardar."""
        return BugServiceDTO(
            id=None,  # Nuevo bug
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            created_at=None,  # None inicialmente para nuevos registros (los gestiona BBDD)
            updated_at=None,  # Idem
            status=self.cb_status,
            system_id=self.cb_system,
            system_version=self.le_version,
            service_now_id=self.le_service_now_id or None,
            campaign_run_id=self.cb_campaign,
            requirements=self.lw_requirements,
            urgency=self.cb_urgency,  # Mantener como entero
            impact=self.cb_impact,  # Mantener como entero
            short_description=self.le_short_desc,
            definition=self.le_definition,
            comments=self.le_comments or None,
            files=[],
            history=[],  # Historial vacío para nuevos bugs
        )

    @classmethod
    def from_service_dto(cls, service_dto: BugServiceDTO) -> "BugFormDTO":
        """Convierte ServiceDTO -> FormDTO para precargar formulario."""

        existing_file_ids = [f.id for f in service_dto.files if f.id]
        existing_file_names = ", ".join([f.filename for f in service_dto.files])

        history_dtos = []
        for change in service_dto.history:
            history_dtos.append(BugHistoryTableDTO.from_service_dto(change))

        return cls(
            id=service_dto.id,
            cb_status=service_dto.status,
            cb_system=service_dto.system_id,  # int -> string
            le_version=service_dto.system_version,
            cb_urgency=service_dto.urgency,
            cb_impact=service_dto.impact,
            le_short_desc=service_dto.short_description,
            le_definition=service_dto.definition,
            cb_campaign=service_dto.campaign_run_id,
            lw_requirements=service_dto.requirements,
            le_service_now_id=service_dto.service_now_id or "",
            le_comments=service_dto.comments or "",
            existing_file_ids=existing_file_ids,
            existing_file_names=existing_file_names or "No attached files",
            history=history_dtos,
        )


@dataclass
class BugDetailDTO:
    """DTO completo para visualización detallada de un bug con todo su historial."""

    bug: BugTableDTO
    history: list[BugHistoryTableDTO]
    files: list[FileServiceDTO] = field(default_factory=list)

    @classmethod
    def from_service_dto(
        cls,
        bug_service_dto: BugServiceDTO,
        system_name: str = "",
        requirement_codes: list[str] = None,
    ) -> "BugDetailDTO":
        """Crea un DTO detallado con bug e historial."""
        bug_table_dto = BugTableDTO.from_service_dto(
            bug_service_dto, system_name, requirement_codes
        )

        history_table_dtos = [
            BugHistoryTableDTO.from_service_dto(hist)
            for hist in bug_service_dto.history
        ]

        return cls(
            bug=bug_table_dto, history=history_table_dtos, files=bug_service_dto.files
        )
