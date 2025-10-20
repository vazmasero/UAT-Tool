# test_management_dto.py
from dataclasses import dataclass, field

from uat_tool.application.dto.base_dto import BaseFormDTO, BaseServiceDTO, BaseTableDTO
from uat_tool.domain import Block, Campaign, Case, Step


# ===== STEP DTOs =====
@dataclass
class StepServiceDTO:
    """DTO para Step - comunicación entre servicios."""

    id: int = 0
    action: str = ""
    expected_result: str = ""
    comments: str = ""
    case_id: int = 0
    requirements: list[int] = field(default_factory=list)

    @classmethod
    def from_model(cls, step: "Step") -> "StepServiceDTO":
        return cls(
            id=step.id,
            action=step.action,
            expected_result=step.expected_result,
            comments=step.comments,
            case_id=step.case_id,
            requirements=[req.id for req in step.requirements]
            if step.requirements
            else [],
        )


@dataclass
class StepTableDTO:
    """DTO para Step - visualización en tablas."""

    id: int
    action: str
    expected_result: str
    comments: str
    requirements: str = "N/A"

    @classmethod
    def from_service_dto(
        cls, service_dto: StepServiceDTO, requirement_codes: list[str] = None
    ) -> "StepTableDTO":
        requirements_display = (
            ", ".join(requirement_codes) if requirement_codes else "N/A"
        )

        return cls(
            id=service_dto.id,
            action=service_dto.action,
            expected_result=service_dto.expected_result,
            comments=service_dto.comments,
            requirements=requirements_display,
        )


@dataclass
class StepFormDTO(BaseFormDTO):
    """DTO para Step - formularios de creación/edición."""

    le_action: str
    le_expected_result: str
    le_comments: str
    lw_requirements: list[int] = field(default_factory=list)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if not self.le_action.strip():
            raise ValueError("La acción es requerida")
        if not self.le_expected_result.strip():
            raise ValueError("El resultado esperado es requerido")

    def to_service_dto(self) -> StepServiceDTO:
        """Convierte datos de formulario -> ServiceDTO."""
        return StepServiceDTO(
            action=self.le_action,
            expected_result=self.le_expected_result,
            comments=self.le_comments,
            requirements=self.lw_requirements,
        )

    @classmethod
    def from_service_dto(cls, service_dto: StepServiceDTO) -> "StepFormDTO":
        """Convierte ServiceDTO -> FormDTO para precargar formulario."""
        return cls(
            id=service_dto.id,
            le_action=service_dto.action,
            le_expected_result=service_dto.expected_result,
            le_comments=service_dto.comments,
            lw_requirements=service_dto.requirements,
        )


# ===== CASE DTOs =====
@dataclass
class CaseServiceDTO(BaseServiceDTO):
    """DTO para Case - comunicación entre servicios."""

    code: str
    name: str
    comments: str

    # Relaciones many-to-many
    operators: list[int] = field(default_factory=list)
    drones: list[int] = field(default_factory=list)
    uhub_users: list[int] = field(default_factory=list)
    uas_zones: list[int] = field(default_factory=list)
    systems: list[int] = field(default_factory=list)
    sections: list[int] = field(default_factory=list)

    # Steps (se manejan como lista de DTOs)
    steps: list[StepServiceDTO] = field(default_factory=list)

    @classmethod
    def from_model(cls, case: "Case") -> "CaseServiceDTO":
        return cls(
            id=case.id,
            created_at=case.created_at,
            updated_at=case.updated_at,
            modified_by=case.modified_by,
            environment_id=case.environment_id,
            code=case.code,
            name=case.name,
            comments=case.comments,
            operators=[op.id for op in case.operators] if case.operators else [],
            drones=[drone.id for drone in case.drones] if case.drones else [],
            uhub_users=[user.id for user in case.uhub_users] if case.uhub_users else [],
            uas_zones=[zone.id for zone in case.uas_zones] if case.uas_zones else [],
            systems=[sys.id for sys in case.systems] if case.systems else [],
            sections=[section.id for section in case.sections] if case.sections else [],
            steps=[StepServiceDTO.from_model(step) for step in case.steps]
            if case.steps
            else [],
        )


@dataclass
class CaseTableDTO(BaseTableDTO):
    """DTO para Case - visualización en tablas."""

    code: str
    name: str
    comments: str
    systems: str = "N/A"
    sections: str = "N/A"
    steps_count: int = 0

    @classmethod
    def from_service_dto(
        cls,
        service_dto: CaseServiceDTO,
        system_names: list[str] = None,
        section_names: list[str] = None,
    ) -> "CaseTableDTO":
        systems_display = ", ".join(system_names) if system_names else "N/A"
        sections_display = ", ".join(section_names) if section_names else "N/A"

        return cls(
            id=service_dto.id,
            code=service_dto.code,
            name=service_dto.name,
            comments=service_dto.comments,
            systems=systems_display,
            sections=sections_display,
            steps_count=len(service_dto.steps),
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class CaseFormDTO(BaseFormDTO):
    """DTO para Case - formularios de creación/edición."""

    le_code: str
    le_name: str
    le_comments: str

    # Relaciones many-to-many
    lw_systems: list[int] = field(default_factory=list)
    lw_sections: list[int] = field(default_factory=list)
    lw_operators: list[int] = field(default_factory=list)
    lw_drones: list[int] = field(default_factory=list)
    lw_uhub_users: list[int] = field(default_factory=list)
    lw_uas_zones: list[int] = field(default_factory=list)

    # Steps (se manejan como lista de FormDTOs)
    steps: list[StepFormDTO] = field(default_factory=list)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if not self.le_code.strip():
            raise ValueError("El código es requerido")
        if not self.le_name.strip():
            raise ValueError("El nombre es requerido")

    def to_service_dto(self, context_data: dict) -> CaseServiceDTO:
        """Convierte datos de formulario -> ServiceDTO."""
        steps_service_dto = [step.to_service_dto() for step in self.steps]

        return CaseServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            created_at=None,
            updated_at=None,
            code=self.le_code,
            name=self.le_name,
            comments=self.le_comments,
            systems=self.lw_systems,
            sections=self.lw_sections,
            operators=self.lw_operators,
            drones=self.lw_drones,
            uhub_users=self.lw_uhub_users,
            uas_zones=self.lw_uas_zones,
            steps=steps_service_dto,
        )

    @classmethod
    def from_service_dto(cls, service_dto: CaseServiceDTO) -> "CaseFormDTO":
        """Convierte ServiceDTO -> FormDTO para precargar formulario."""
        steps_form_dto = [
            StepFormDTO.from_service_dto(step) for step in service_dto.steps
        ]

        return cls(
            id=service_dto.id,
            le_code=service_dto.code,
            le_name=service_dto.name,
            le_comments=service_dto.comments,
            lw_systems=service_dto.systems,
            lw_sections=service_dto.sections,
            lw_operators=service_dto.operators,
            lw_drones=service_dto.drones,
            lw_uhub_users=service_dto.uhub_users,
            lw_uas_zones=service_dto.uas_zones,
            steps=steps_form_dto,
        )


# ===== BLOCK DTOs =====
@dataclass
class BlockServiceDTO(BaseServiceDTO):
    """DTO para Block - comunicación entre servicios."""

    code: str
    name: str
    system_id: int
    comments: str

    # Relaciones
    cases: list[int] = field(default_factory=list)

    @classmethod
    def from_model(cls, block: "Block") -> "BlockServiceDTO":
        return cls(
            id=block.id,
            created_at=block.created_at,
            updated_at=block.updated_at,
            modified_by=block.modified_by,
            environment_id=block.environment_id,
            code=block.code,
            name=block.name,
            system_id=block.system_id,
            comments=block.comments,
            cases=[case.id for case in block.cases] if block.cases else [],
        )


@dataclass
class BlockTableDTO(BaseTableDTO):
    """DTO para Block - visualización en tablas."""

    code: str
    name: str
    system: str
    comments: str
    cases_count: int = 0

    @classmethod
    def from_service_dto(
        cls,
        service_dto: BlockServiceDTO,
        system_name: str = "",
    ) -> "BlockTableDTO":
        return cls(
            id=service_dto.id,
            code=service_dto.code,
            name=service_dto.name,
            system=system_name or "Unknown",
            comments=service_dto.comments,
            cases_count=len(service_dto.cases),
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class BlockFormDTO(BaseFormDTO):
    """DTO para Block - formularios de creación/edición."""

    le_code: str
    le_name: str
    cb_system: str  # ID del sistema como string
    le_comments: str

    # Relaciones
    lw_cases: list[int] = field(default_factory=list)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if not self.le_code.strip():
            raise ValueError("El código es requerido")
        if not self.cb_system.strip():
            raise ValueError("El sistema es requerido")

    def to_service_dto(self, context_data: dict) -> BlockServiceDTO:
        """Convierte datos de formulario -> ServiceDTO."""
        return BlockServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            created_at=None,
            updated_at=None,
            code=self.le_code,
            name=self.le_name,
            system_id=int(self.cb_system),
            comments=self.le_comments,
            cases=self.lw_cases,
        )

    @classmethod
    def from_service_dto(cls, service_dto: BlockServiceDTO) -> "BlockFormDTO":
        """Convierte ServiceDTO -> FormDTO para precargar formulario."""
        return cls(
            id=service_dto.id,
            le_code=service_dto.code,
            le_name=service_dto.name,
            cb_system=str(service_dto.system_id),
            le_comments=service_dto.comments,
            lw_cases=service_dto.cases,
        )


# ===== CAMPAIGN DTOs =====
@dataclass
class CampaignServiceDTO(BaseServiceDTO):
    """DTO para Campaign - comunicación entre servicios."""

    code: str
    description: str
    system_id: int
    system_version: str
    comments: str
    status: str = "DRAFT"  # Por defecto DRAFT como mencionaste

    # Relaciones
    blocks: list[int] = field(default_factory=list)

    @classmethod
    def from_model(cls, campaign: "Campaign") -> "CampaignServiceDTO":
        return cls(
            id=campaign.id,
            created_at=campaign.created_at,
            updated_at=campaign.updated_at,
            modified_by=campaign.modified_by,
            environment_id=campaign.environment_id,
            code=campaign.code,
            description=campaign.description,
            system_id=campaign.system_id,
            system_version=campaign.system_version,
            comments=campaign.comments,
            status=campaign.status,
            blocks=[block.id for block in campaign.blocks] if campaign.blocks else [],
        )


@dataclass
class CampaignTableDTO(BaseTableDTO):
    """DTO para Campaign - visualización en tablas."""

    code: str
    description: str
    system: str
    system_version: str
    status: str
    comments: str
    blocks_count: int = 0

    @classmethod
    def from_service_dto(
        cls,
        service_dto: CampaignServiceDTO,
        system_name: str = "",
    ) -> "CampaignTableDTO":
        return cls(
            id=service_dto.id,
            code=service_dto.code,
            description=service_dto.description,
            system=system_name or "Unknown",
            system_version=service_dto.system_version,
            status=service_dto.status,
            comments=service_dto.comments,
            blocks_count=len(service_dto.blocks),
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class CampaignFormDTO(BaseFormDTO):
    """DTO para Campaign - formularios de creación/edición."""

    le_code: str
    le_description: str
    cb_system: str  # ID del sistema como string
    le_version: str
    le_comments: str

    # Relaciones
    lw_blocks: list[int] = field(default_factory=list)

    def __post_init__(self):
        """Validaciones específicas del formulario."""
        if not self.le_code.strip():
            raise ValueError("El código es requerido")
        if not self.le_description.strip():
            raise ValueError("La descripción es requerida")
        if not self.cb_system.strip():
            raise ValueError("El sistema es requerido")
        if not self.le_version.strip():
            raise ValueError("La versión del sistema es requerida")
        if not self.lw_blocks:
            raise ValueError("Debe seleccionar al menos un bloque de test")

    def to_service_dto(self, context_data: dict) -> CampaignServiceDTO:
        """Convierte datos de formulario -> ServiceDTO."""
        return CampaignServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            created_at=None,
            updated_at=None,
            code=self.le_code,
            description=self.le_description,
            system_id=int(self.cb_system),
            system_version=self.le_version,
            comments=self.le_comments,
            status="DRAFT",  # Siempre DRAFT al crear
            blocks=self.lw_blocks,
        )

    @classmethod
    def from_service_dto(cls, service_dto: CampaignServiceDTO) -> "CampaignFormDTO":
        """Convierte ServiceDTO -> FormDTO para precargar formulario."""
        return cls(
            id=service_dto.id,
            le_code=service_dto.code,
            le_description=service_dto.description,
            cb_system=str(service_dto.system_id),
            le_version=service_dto.system_version,
            le_comments=service_dto.comments,
            lw_blocks=service_dto.blocks,
        )
