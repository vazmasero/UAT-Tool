# requirement_dto.py
from dataclasses import dataclass, field

from uat_tool.application.dto.base_dto import BaseFormDTO, BaseServiceDTO, BaseTableDTO
from uat_tool.domain import Requirement


@dataclass
class RequirementServiceDTO(BaseServiceDTO):
    """DTO 1:1 con el modelo de dominio para operaciones CRUD y lógica de negocio.
    Propósito: comunicación entre servicios y con repositorios.
    Debe reflejar fielmente la entidad de dominio"""

    # Campos requeridos (sin default)
    code: str
    definition: str

    # Campos opcionales (con default)
    systems: list[int] = field(default_factory=list)
    sections: list[int] = field(default_factory=list)

    @classmethod
    def from_model(cls, requirement: "Requirement") -> "RequirementServiceDTO":
        """Conversión directa modelo -> DTO (sin enriquecimiento).

        Args:
            requirement (Requirement): modelo SQLAlchemy de la entidad a transformar.

        Returns:
            RequirementServiceDTO: modelo DTO de la entidad transformada.
        """
        return cls(
            id=requirement.id,
            created_at=requirement.created_at,
            updated_at=requirement.updated_at,
            modified_by=requirement.modified_by,
            environment_id=requirement.environment_id,
            code=requirement.code,
            definition=requirement.definition,
            systems=[sys.id for sys in requirement.systems]
            if requirement.systems
            else [],
            sections=[section.id for section in requirement.sections]
            if requirement.sections
            else [],
        )


@dataclass
class RequirementTableDTO(BaseTableDTO):
    """DTO optimizado para visualización en tablas UI.
    Propósito: mostrar datos enriquecidos y formateados al usuario."""

    # Campos requeridos (sin default)
    code: str
    definition: str

    # Campos opcionales (con default)
    systems: str = "N/A"  # Lista de nombres de sistemas
    sections: str = "N/A"  # Lista de nombres de secciones

    @classmethod
    def from_service_dto(
        cls,
        service_dto: RequirementServiceDTO,
        system_names: list[str] = None,
        section_names: list[str] = None,
    ) -> "RequirementTableDTO":
        """Transforma ServiceDTO -> TableDTO con datos enriquecidos.

        Args:
            service_dto (RequirementServiceDTO): ServiceDTO a transformar.
            **enrichments: datos enriquecidos (nombre de los sistemas y secciones)

        Returns:
            RequirementTableDTO: TableDTO transformado.
        """

        # Formatear sistemas y secciones
        systems_display = ", ".join(system_names) if system_names else "N/A"
        sections_display = ", ".join(section_names) if section_names else "N/A"

        return cls(
            id=service_dto.id,
            code=service_dto.code,
            definition=service_dto.definition,
            systems=systems_display,
            sections=sections_display,
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class RequirementFormDTO(BaseFormDTO):
    """DTO específica para formularios de creación/edición.
    Propósito: Capturar datos de formularios UI y validarlos."""

    # Campos requeridos (sin default)
    le_code: str
    le_definition: str

    # Campos opcionales (con default)
    lw_systems: list[int] = field(default_factory=list)
    lw_sections: list[int] = field(default_factory=list)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if len(self.le_definition.strip()) < 10:
            raise ValueError("La definición debe tener al menos 10 caracteres")
        if not self.le_code.strip():
            raise ValueError("La versión del sistema es requerida")

    def to_service_dto(self, context_data: dict) -> RequirementServiceDTO:
        """Convierte datos de formulario -> ServiceDTO para guardar."""
        return RequirementServiceDTO(
            id=0,  # 0 para nuevos requisitos, se asignará en BD
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            systems=self.lw_systems,
            sections=self.lw_sections,
            definition=self.le_definition,
            code=self.le_code,
        )

    @classmethod
    def from_service_dto(
        cls, service_dto: RequirementServiceDTO
    ) -> "RequirementFormDTO":
        """Convierte ServiceDTO -> FormDTO para precargar formulario."""
        return cls(
            le_code=service_dto.code,
            le_definition=service_dto.definition,
            lw_systems=service_dto.systems,
            lw_sections=service_dto.sections,
        )
