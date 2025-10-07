# application/dto/assets_dto.py
from dataclasses import dataclass, field

from uat_tool.application.dto.base_dto import BaseFormDTO, BaseServiceDTO, BaseTableDTO
from uat_tool.domain import Drone, Email, Operator, UasZone, UhubOrg, UhubUser, Uspace


# ===== EMAIL =====
@dataclass
class EmailServiceDTO(BaseServiceDTO):
    """DTO para Email - comunicación entre servicios."""

    name: str
    email: str
    password: str

    @classmethod
    def from_model(cls, email: "Email") -> "EmailServiceDTO":
        return cls(
            id=email.id,
            created_at=email.created_at,
            updated_at=email.updated_at,
            modified_by=email.modified_by,
            environment_id=email.environment_id,
            name=email.name,
            email=email.email,
            password=email.password,
        )


@dataclass
class EmailTableDTO(BaseTableDTO):
    """DTO para Email - visualización en tablas."""

    name: str
    email: str
    password: str

    @classmethod
    def from_service_dto(cls, service_dto: EmailServiceDTO) -> "EmailTableDTO":
        return cls(
            id=service_dto.id,
            name=service_dto.name,
            email=service_dto.email,
            password=service_dto.password,
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class EmailFormDTO(BaseFormDTO):
    """DTO para Email - formularios de creación/edición."""

    le_name: str
    le_email: str
    le_password: str

    def __post_init__(self):
        if not self.le_name.strip():
            raise ValueError("El nombre es requerido")
        if not self.le_email.strip() or "@" not in self.le_email:
            raise ValueError("Email válido es requerido")
        if not self.le_password.strip():
            raise ValueError("La contraseña es requerida")

    def to_service_dto(self, context_data: dict) -> EmailServiceDTO:
        return EmailServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            name=self.le_name,
            email=self.le_email,
            password=self.le_password,
        )

    @classmethod
    def from_service_dto(cls, service_dto: EmailServiceDTO) -> "EmailFormDTO":
        return cls(
            le_name=service_dto.name,
            le_email=service_dto.email,
            le_password=service_dto.password,
        )


# ===== OPERATOR =====
@dataclass
class OperatorServiceDTO(BaseServiceDTO):
    """DTO para Operator - comunicación entre servicios."""

    name: str
    easa_id: str
    verification_code: str
    password: str
    phone: str
    email_id: int

    @classmethod
    def from_model(cls, operator: "Operator") -> "OperatorServiceDTO":
        return cls(
            id=operator.id,
            created_at=operator.created_at,
            updated_at=operator.updated_at,
            modified_by=operator.modified_by,
            environment_id=operator.environment_id,
            name=operator.name,
            easa_id=operator.easa_id,
            verification_code=operator.verification_code,
            password=operator.password,
            phone=operator.phone,
            email_id=operator.email_id,
        )


@dataclass
class OperatorTableDTO(BaseTableDTO):
    """DTO para Operator - visualización en tablas."""

    name: str
    easa_id: str
    phone: str
    password: str
    email: str = "N/A"  # Campo "email" del email, no ID

    @classmethod
    def from_service_dto(
        cls, service_dto: OperatorServiceDTO, email_email: str = ""
    ) -> "OperatorTableDTO":
        return cls(
            id=service_dto.id,
            name=service_dto.name,
            easa_id=service_dto.easa_id,
            phone=service_dto.phone,
            password=service_dto.password,
            email=email_email or "N/A",
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class OperatorFormDTO(BaseFormDTO):
    """DTO para Operator - formularios de creación/edición."""

    le_name: str
    le_easa_id: str
    le_verification_code: str
    le_password: str
    le_phone: str
    cb_email: str  # ID del email como string

    def __post_init__(self):
        if not all(
            [self.le_name.strip(), self.le_easa_id.strip(), self.le_phone.strip()]
        ):
            raise ValueError("Nombre, EASA ID y teléfono son requeridos")

    def to_service_dto(self, context_data: dict) -> OperatorServiceDTO:
        return OperatorServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            name=self.le_name,
            easa_id=self.le_easa_id,
            verification_code=self.le_verification_code,
            password=self.le_password,
            phone=self.le_phone,
            email_id=int(self.cb_email),
        )

    @classmethod
    def from_service_dto(cls, service_dto: OperatorServiceDTO) -> "OperatorFormDTO":
        return cls(
            le_name=service_dto.name,
            le_easa_id=service_dto.easa_id,
            le_verification_code=service_dto.verification_code,
            le_password=service_dto.password,
            le_phone=service_dto.phone,
            cb_email=str(service_dto.email_id),
        )


# ===== DRONE =====
@dataclass
class DroneServiceDTO(BaseServiceDTO):
    """DTO para Drone - comunicación entre servicios."""

    name: str
    serial_number: str
    manufacturer: str
    model: str
    tracker_type: str  # "GCS-API", "SIMULATOR", "TRACKER"
    transponder_id: str
    operator_id: int

    @classmethod
    def from_model(cls, drone: "Drone") -> "DroneServiceDTO":
        return cls(
            id=drone.id,
            created_at=drone.created_at,
            updated_at=drone.updated_at,
            modified_by=drone.modified_by,
            environment_id=drone.environment_id,
            name=drone.name,
            serial_number=drone.serial_number,
            manufacturer=drone.manufacturer,
            model=drone.model,
            tracker_type=drone.tracker_type,
            transponder_id=drone.transponder_id,
            operator_id=drone.operator_id,
        )


@dataclass
class DroneTableDTO(BaseTableDTO):
    """DTO para Drone - visualización en tablas."""

    name: str
    serial_number: str
    manufacturer: str
    model: str
    tracker_type: str
    operator: str = "N/A"  # Nombre del operador, no ID

    @classmethod
    def from_service_dto(
        cls, service_dto: DroneServiceDTO, operator_name: str = ""
    ) -> "DroneTableDTO":
        return cls(
            id=service_dto.id,
            name=service_dto.name,
            serial_number=service_dto.serial_number,
            manufacturer=service_dto.manufacturer,
            model=service_dto.model,
            tracker_type=service_dto.tracker_type,
            operator=operator_name or "N/A",
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class DroneFormDTO(BaseFormDTO):
    """DTO para Drone - formularios de creación/edición."""

    le_name: str
    le_sn: str
    le_manufacturer: str
    le_model: str
    cb_tracker_type: str
    le_transponder_id: str
    cb_operator: str  # ID del operador como string

    def __post_init__(self):
        if not all([self.le_name.strip(), self.le_sn.strip()]):
            raise ValueError("Nombre y número de serie son requeridos")

    def to_service_dto(self, context_data: dict) -> DroneServiceDTO:
        return DroneServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            name=self.le_name,
            serial_number=self.le_sn,
            manufacturer=self.le_manufacturer,
            model=self.le_model,
            tracker_type=self.cb_tracker_type,
            transponder_id=self.le_transponder_id,
            operator_id=int(self.cb_operator),
        )

    @classmethod
    def from_service_dto(cls, service_dto: DroneServiceDTO) -> "DroneFormDTO":
        return cls(
            le_name=service_dto.name,
            le_sn=service_dto.serial_number,
            le_manufacturer=service_dto.manufacturer,
            le_model=service_dto.model,
            cb_tracker_type=service_dto.tracker_type,
            le_transponder_id=service_dto.transponder_id,
            cb_operator=str(service_dto.operator_id),
        )


# ===== UHUB ORG =====
@dataclass
class UhubOrgServiceDTO(BaseServiceDTO):
    """DTO para UhubOrg - comunicación entre servicios."""

    name: str
    email: str
    phone: str
    jurisdiction: str
    aoi: str
    role: str
    type: str  # "INFORMATIVE", "OPERATIVE"

    @classmethod
    def from_model(cls, org: "UhubOrg") -> "UhubOrgServiceDTO":
        return cls(
            id=org.id,
            created_at=org.created_at,
            updated_at=org.updated_at,
            modified_by=org.modified_by,
            environment_id=org.environment_id,
            name=org.name,
            email=org.email,
            phone=org.phone,
            jurisdiction=org.jurisdiction,
            aoi=org.aoi,
            role=org.role,
            type=org.type,
        )


@dataclass
class UhubOrgTableDTO(BaseTableDTO):
    """DTO para UhubOrg - visualización en tablas."""

    name: str
    email: str
    phone: str
    jurisdiction: str
    aoi: str
    role: str
    type: str

    @classmethod
    def from_service_dto(cls, service_dto: UhubOrgServiceDTO) -> "UhubOrgTableDTO":
        return cls(
            id=service_dto.id,
            name=service_dto.name,
            email=service_dto.email,
            phone=service_dto.phone,
            type=service_dto.type,
            role=service_dto.role,
            aoi=service_dto.aoi,
            jurisdiction=service_dto.jurisdiction,
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class UhubOrgFormDTO(BaseFormDTO):
    """DTO para UhubOrg - formularios de creación/edición."""

    le_name: str
    le_email: str
    le_phone: str
    le_jurisdiction: str
    le_aoi: str
    le_role: str
    cb_type: str  # "INFORMATIVE", "OPERATIVE"

    def __post_init__(self):
        if not all([self.le_name.strip(), self.le_email.strip()]):
            raise ValueError("Nombre y email son requeridos")

    def to_service_dto(self, context_data: dict) -> UhubOrgServiceDTO:
        return UhubOrgServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            name=self.le_name,
            email=self.le_email,
            phone=self.le_phone,
            jurisdiction=self.le_jurisdiction,
            aoi=self.le_aoi,
            role=self.le_role,
            type=self.cb_type,
        )

    @classmethod
    def from_service_dto(cls, service_dto: UhubOrgServiceDTO) -> "UhubOrgFormDTO":
        return cls(
            le_name=service_dto.name,
            le_email=service_dto.email,
            le_phone=service_dto.phone,
            le_jurisdiction=service_dto.jurisdiction,
            le_aoi=service_dto.aoi,
            le_role=service_dto.role,
            cb_type=service_dto.type,
        )


# ===== UHUB USER =====
@dataclass
class UhubUserServiceDTO(BaseServiceDTO):
    """DTO para UhubUser - comunicación entre servicios."""

    username: str
    password: str
    email: str
    dni: str
    phone: str
    type: str  # "ADMIN", "USER"
    role: str
    jurisdiction: str
    aoi: str
    organization_id: int

    @classmethod
    def from_model(cls, user: "UhubUser") -> "UhubUserServiceDTO":
        return cls(
            id=user.id,
            created_at=user.created_at,
            updated_at=user.updated_at,
            modified_by=user.modified_by,
            environment_id=user.environment_id,
            email=user.email,
            dni=user.dni,
            phone=user.phone,
            username=user.username,
            password=user.password,
            type=user.type,
            role=user.role,
            jurisdiction=user.jurisdiction,
            aoi=user.aoi,
            organization_id=user.organization_id,
        )


@dataclass
class UhubUserTableDTO(BaseTableDTO):
    """DTO para UhubUser - visualización en tablas."""

    email: str
    username: str
    password: str
    type: str
    role: str
    jurisdiction: str
    aoi: str
    organization: str = "N/A"  # Nombre de la organización, no ID

    @classmethod
    def from_service_dto(
        cls, service_dto: UhubUserServiceDTO, org_name: str = ""
    ) -> "UhubUserTableDTO":
        return cls(
            id=service_dto.id,
            email=service_dto.email,
            username=service_dto.username,
            password=service_dto.password,
            type=service_dto.type,
            role=service_dto.role,
            jurisdiction=service_dto.jurisdiction,
            aoi=service_dto.aoi,
            organization=org_name or "N/A",
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class UhubUserFormDTO(BaseFormDTO):
    """DTO para UhubUser - formularios de creación/edición."""

    le_email: str
    le_dni: str
    le_phone: str
    le_username: str
    le_password: str
    cb_type: str  # "ADMIN", "USER"
    le_role: str
    le_jurisdiction: str
    le_aoi: str
    cb_organization: str  # ID de la organización como string

    def __post_init__(self):
        if not all([self.le_email.strip(), self.le_username.strip()]):
            raise ValueError("Email y username son requeridos")

    def to_service_dto(self, context_data: dict) -> UhubUserServiceDTO:
        return UhubUserServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            email=self.le_email,
            dni=self.le_dni,
            phone=self.le_phone,
            username=self.le_username,
            password=self.le_password,
            type=self.cb_type,
            role=self.le_role,
            jurisdiction=self.le_jurisdiction,
            aoi=self.le_aoi,
            organization_id=int(self.cb_organization),
        )

    @classmethod
    def from_service_dto(cls, service_dto: UhubUserServiceDTO) -> "UhubUserFormDTO":
        return cls(
            le_email=service_dto.email,
            le_dni=service_dto.dni,
            le_phone=service_dto.phone,
            le_username=service_dto.username,
            le_password=service_dto.password,
            cb_type=service_dto.type,
            le_role=service_dto.role,
            le_jurisdiction=service_dto.jurisdiction,
            le_aoi=service_dto.aoi,
            cb_organization=str(service_dto.organization_id),
        )


# ===== UAS ZONE =====
@dataclass
class UasZoneServiceDTO(BaseServiceDTO):
    """DTO para UasZone - comunicación entre servicios."""

    name: str
    area_type: str  # "POLYGON", "CIRCLE", "CORRIDOR"
    circle_radius: int | None
    corridor_width: int | None
    lower_limit: int
    upper_limit: int
    reference_lower: str  # "AGL", "AMSL"
    reference_upper: str  # "AGL", "AMSL"
    application: str  # "TEMPORAL", "PERMANENT"
    restriction_type: str  # "INFORMATIVE", "PROHIBITED", etc.
    message: str | None
    clearance_required: bool
    reasons: list[int] = field(default_factory=list)
    organizations: list[int] = field(default_factory=list)

    @classmethod
    def from_model(cls, zone: "UasZone") -> "UasZoneServiceDTO":
        return cls(
            id=zone.id,
            created_at=zone.created_at,
            updated_at=zone.updated_at,
            modified_by=zone.modified_by,
            environment_id=zone.environment_id,
            name=zone.name,
            area_type=zone.area_type,
            circle_radius=zone.circle_radius,
            corridor_width=zone.corridor_width,
            lower_limit=zone.lower_limit,
            upper_limit=zone.upper_limit,
            reference_lower=zone.reference_lower,
            reference_upper=zone.reference_upper,
            application=zone.application,
            restriction_type=zone.restriction_type,
            message=zone.message,
            clearance_required=zone.clearance_required,
            reasons=[reason.id for reason in zone.reasons] if zone.reasons else [],
            organizations=[org.id for org in zone.organizations]
            if zone.organizations
            else [],
        )


@dataclass
class UasZoneTableDTO(BaseTableDTO):
    """DTO para UasZone - visualización en tablas."""

    name: str
    area_type: str
    restriction_type: str
    application: str
    limits: str  # Formateado: "0-120 m AGL"

    reasons: str = "N/A"  # Lista de razones
    organizations: str = "N/A"  # Lista de organizaciones

    @classmethod
    def from_service_dto(
        cls,
        service_dto: UasZoneServiceDTO,
        reasons: list[str] = None,
        organizations: list[str] = None,
    ) -> "UasZoneTableDTO":
        limits = f"{service_dto.lower_limit}-{service_dto.upper_limit} ft {service_dto.reference_lower}"

        # Formatear razones y organizaciones
        reasons_display = ", ".join(reasons) if reasons and reasons else "N/A"

        organizations_display = (
            ", ".join(organizations) if organizations and organizations else "N/A"
        )

        return cls(
            id=service_dto.id,
            name=service_dto.name,
            area_type=service_dto.area_type,
            restriction_type=service_dto.restriction_type,
            application=service_dto.application,
            limits=limits,
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
            reasons=reasons_display,
            organizations=organizations_display,
        )


@dataclass
class UasZoneFormDTO(BaseFormDTO):
    """DTO para UasZone - formularios de creación/edición."""

    le_name: str
    cb_area_type: str
    le_radius: int | None = None
    le_width: int | None = None
    le_lower_limit: int = 0
    le_upper_limit: int = 0
    cb_reference_lower: str = "AGL"
    cb_reference_upper: str = "AGL"
    cb_application: str = "TEMPORAL"
    cb_restriction_type: str = "INFORMATIVE"
    le_message: str = ""
    cb_clearance: bool = False
    lw_reasons: list[int] = field(default_factory=list)
    lw_orgs: list[int] = field(default_factory=list)

    def __post_init__(self):
        if not self.le_name.strip():
            raise ValueError("El nombre es requerido")
        if self.cb_area_type == "CIRCLE" and not self.le_radius:
            raise ValueError("Radio requerido para área circular")
        if self.cb_area_type == "CORRIDOR" and not self.le_width:
            raise ValueError("Ancho requerido para corredor")

    def to_service_dto(self, context_data: dict) -> UasZoneServiceDTO:
        return UasZoneServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            name=self.le_name,
            area_type=self.cb_area_type,
            circle_radius=self.le_radius,
            corridor_width=self.le_width,
            lower_limit=self.le_lower_limit,
            upper_limit=self.le_upper_limit,
            reference_lower=self.cb_reference_lower,
            reference_upper=self.cb_reference_upper,
            application=self.cb_application,
            restriction_type=self.cb_restriction_type,
            message=self.le_message or None,
            clearance_required=self.cb_clearance,
            reasons=self.lw_reasons,
            organizations=self.lw_orgs,
        )

    @classmethod
    def from_service_dto(cls, service_dto: UasZoneServiceDTO) -> "UasZoneFormDTO":
        return cls(
            le_name=service_dto.name,
            cb_area_type=service_dto.area_type,
            le_radius=service_dto.circle_radius,
            le_width=service_dto.corridor_width,
            le_lower_limit=service_dto.lower_limit,
            le_upper_limit=service_dto.upper_limit,
            cb_reference_lower=service_dto.reference_lower,
            cb_reference_upper=service_dto.reference_upper,
            cb_application=service_dto.application,
            cb_restriction_type=service_dto.restriction_type,
            le_message=service_dto.message or "",
            cb_clearance=service_dto.clearance_required,
            lw_reasons=service_dto.reasons,
            lw_orgs=service_dto.organizations,
        )


# ===== USPACE =====
@dataclass
class UspaceServiceDTO(BaseServiceDTO):
    """DTO para Uspace - comunicación entre servicios."""

    code: str
    name: str
    sectors_count: int
    file_id: int

    @classmethod
    def from_model(cls, uspace: "Uspace") -> "UspaceServiceDTO":
        return cls(
            id=uspace.id,
            created_at=uspace.created_at,
            updated_at=uspace.updated_at,
            modified_by=uspace.modified_by,
            environment_id=uspace.environment_id,
            code=uspace.code,
            name=uspace.name,
            sectors_count=uspace.sectors_count,
            file_id=uspace.file_id,
        )


@dataclass
class UspaceTableDTO(BaseTableDTO):
    """DTO para Uspace - visualización en tablas."""

    code: str
    name: str
    sectors_count: int
    file_id: int  # ID para la descarga
    file_name: str = "N/A"  # Nombre del archivo, no ID

    @classmethod
    def from_service_dto(
        cls, service_dto: UspaceServiceDTO, file_name: str = ""
    ) -> "UspaceTableDTO":
        return cls(
            id=service_dto.id,
            code=service_dto.code,
            name=service_dto.name,
            sectors_count=service_dto.sectors_count,
            file_name=file_name or "N/A",
            file_id=service_dto.file_id,
            created_at=cls._format_date(service_dto.created_at),
            updated_at=cls._format_date(service_dto.updated_at),
            modified_by=service_dto.modified_by,
        )


@dataclass
class UspaceFormDTO(BaseFormDTO):
    """DTO para Uspace - formularios de creación/edición."""

    le_code: str
    le_name: str
    le_sectors_count: int
    le_file: str = ""  # Ruta/nombre del archivo temporal
    existing_file_id: int | None = None  # ID del archivo ya subido

    def __post_init__(self):
        if not all([self.le_code.strip(), self.le_name.strip()]):
            raise ValueError("Código y nombre son requeridos")

    def to_service_dto(self, context_data: dict) -> UspaceServiceDTO:
        return UspaceServiceDTO(
            id=0,
            modified_by=context_data["modified_by"],
            environment_id=context_data["environment_id"],
            code=self.le_code,
            name=self.le_name,
            sectors_count=self.le_sectors_count,
            file_id=self.existing_file_id or 0,  # Se asignará después de subir archivo
        )

    @classmethod
    def from_service_dto(cls, service_dto: UspaceServiceDTO) -> "UspaceFormDTO":
        return cls(
            le_code=service_dto.code,
            le_name=service_dto.name,
            le_sectors_count=service_dto.sectors_count,
            existing_file_id=service_dto.file_id,
        )
