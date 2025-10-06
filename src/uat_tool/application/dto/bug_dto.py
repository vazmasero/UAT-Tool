from dataclasses import dataclass, field
from datetime import datetime

from uat_tool.domain import Bug


@dataclass
class BugServiceDTO:
    """DTO 1:1 con el modelo Bug para comunicación entre servicios."""

    # Campos REQUERIDOS (sin default) - VAN PRIMERO
    id: int
    modified_by: str
    environment_id: int
    status: str  # "OPEN", "CLOSED SOLVED", etc.
    system_id: int
    system_version: str
    short_description: str
    definition: str
    urgency: str  # "1", "2", "3"
    impact: str  # "1", "2", "3"

    # Campos OPCIONALES (con default) - VAN DESPUÉS
    campaign_run_id: str | None = None
    service_now_id: str | None = None
    requirements: list[int] = field(default_factory=list)
    comments: str | None = None
    file_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    @classmethod
    def from_model(cls, bug: "Bug") -> "BugServiceDTO":
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
            file_id=bug.file_id,
            requirements=[req.id for req in bug.requirements]
            if bug.requirements
            else [],
        )


@dataclass
class BugFormDTO:
    """DTO específico de Bugs para su uso en formularios de UI."""

    # Campos REQUERIDOS (sin default) - VAN PRIMERO
    cb_status: str  # "OPEN", "CLOSED SOLVED", etc.
    cb_system: str  # ID del sistema seleccionado
    le_version: str  # Versión del sistema
    cb_urgency: int  # "1", "2", "3"
    cb_impact: int  # "1", "2", "3"
    le_short_desc: str  # Descripción corta
    le_definition: str  # Definición

    # Campos OPCIONALES (con default) - VAN DESPUÉS
    cb_campaign: int | None = None  # ID de la campaña (puede ser None)
    lw_requirements: list[int] = field(
        default_factory=list
    )  # Lista de IDs de requisitos seleccionados
    le_service_now_id: str = ""  # ID de ServiceNow
    comments: str = ""  # Comentarios
    le_files: int = 0  # Ruta/nombre del archivo (NO el ID todavía)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if len(self.le_short_desc.strip()) < 5:
            raise ValueError("La descripción corta debe tener al menos 5 caracteres")
        if len(self.le_definition.strip()) < 10:
            raise ValueError("La definición debe tener al menos 10 caracteres")
        if not self.le_version.strip():
            raise ValueError("La versión del sistema es requerida")

    def to_service_dto(self, environment_id: int, modified_by: str) -> BugServiceDTO:
        """Convierte a BugServiceDTO para enviar al servicio."""
        return BugServiceDTO(
            id=0,  # 0 para nuevos bugs, se asignará en BD
            modified_by=modified_by,
            environment_id=environment_id,
            status=self.cb_status,
            system_id=self.cb_system,
            system_version=self.le_version,
            service_now_id=self.le_service_now_id or None,
            campaign_run_id=self.cb_campaign,
            requirements=self.lw_requirements,
            urgency=str(self.cb_urgency),  # Convertir a string para consistencia
            impact=str(self.cb_impact),  # Convertir a string para consistencia
            short_description=self.le_short_desc,
            definition=self.le_definition,
            comments=self.comments or None,
            file_id=None,  # Se asignará después de subir el archivo
        )


@dataclass
class BugTableDTO:
    """DTO optimizado para mostrar en tablas."""

    # Campos REQUERIDOS (sin default) - VAN PRIMERO
    id: int
    status: str  # Estado formateado
    system: str  # Nombre del sistema (no ID)
    system_version: str
    created_at: str  # Fecha formateada
    updated_at: str  # Fecha formateada
    modified_by: str
    short_description: str
    definition: str

    # Campos OPCIONALES (con default) - VAN DESPUÉS
    service_now_id: str = "N/A"
    campaign: str = "N/A"  # Nombre de la campaña (no ID)
    requirements: str = "N/A"  # Lista de nombres de requisitos
    urgency: str = "Unknown"  # "Alta", "Media", "Baja"
    impact: str = "Unknown"  # "Alta", "Media", "Baja"
    comments: str = ""
    file_name: str = "No file attached"  # Nombre del archivo para descargar
    file_id: int | None = None  # ID para la descarga

    @classmethod
    def from_service_dto(
        cls,
        bug_dto: BugServiceDTO,
        system_name: str = "",
        campaign_code: str = "",
        requirement_codes: list[str] = None,
        file_name: str = "",
    ) -> "BugTableDTO":
        """Crea TableDTO desde ServiceDTO con datos formateados para UI."""

        # Mapear urgencia/impacto numérico a texto
        urgency_map = {"1": "Baja", "2": "Media", "3": "Alta"}
        impact_map = {"1": "Baja", "2": "Media", "3": "Alta"}

        # Formatear fechas (manejar caso de None para nuevos bugs)
        created_at_str = (
            bug_dto.created_at.strftime("%d/%m/%Y %H:%M")
            if bug_dto.created_at
            else "Not assigned"
        )
        updated_at_str = (
            bug_dto.updated_at.strftime("%d/%m/%Y %H:%M")
            if bug_dto.updated_at
            else "Not assigned"
        )

        return cls(
            id=bug_dto.id,
            status=bug_dto.status.replace("_", " ").title(),
            system=system_name,
            system_version=bug_dto.system_version,
            created_at=created_at_str,
            updated_at=updated_at_str,
            modified_by=bug_dto.modified_by,
            service_now_id=bug_dto.service_now_id or "N/A",
            campaign=campaign_code or "N/A",
            requirements=", ".join(requirement_codes) if requirement_codes else "N/A",
            short_description=bug_dto.short_description,
            definition=bug_dto.definition,
            urgency=urgency_map.get(bug_dto.urgency, "Unknown"),
            impact=impact_map.get(bug_dto.impact, "Unknown"),
            comments=bug_dto.comments or "",
            file_name=file_name or "No file attached",
            file_id=bug_dto.file_id,
        )
