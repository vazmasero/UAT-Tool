from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import declarative_base, declared_attr, relationship

Base = declarative_base()


class EnvironmentMixin:
    @declared_attr
    def environment_id(cls):
        return Column(
            Integer,
            ForeignKey("environments.id", ondelete="RESTRICT"),
            nullable=False,
        )

    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )

    modified_by = Column(String, nullable=False)


"""Many - to - many relationships"""


# zone-organization
zone_organization = Table(
    "zone_organization",
    Base.metadata,
    Column(
        "zone_id",
        Integer,
        ForeignKey("uas_zones.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "org_id",
        Integer,
        ForeignKey("uhub_orgs.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

# zone-reasons
zone_reasons = Table(
    "zone_reason",
    Base.metadata,
    Column(
        "zone_id",
        Integer,
        ForeignKey("uas_zones.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "reason_id",
        Integer,
        ForeignKey("reasons.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

# Requirements
requirement_systems = Table(
    "requirement_systems",
    Base.metadata,
    Column(
        "requirement_id",
        Integer,
        ForeignKey("requirements.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "system_id",
        Integer,
        ForeignKey("systems.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

requirement_sections = Table(
    "requirement_sections",
    Base.metadata,
    Column(
        "requirement_id",
        Integer,
        ForeignKey("requirements.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "section_id",
        Integer,
        ForeignKey("sections.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

# Step-requirements
step_requirements = Table(
    "step_requirements",
    Base.metadata,
    Column(
        "step_id", Integer, ForeignKey("steps.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "requirement_id",
        Integer,
        ForeignKey("requirements.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

# Cases
case_systems = Table(
    "case_systems",
    Base.metadata,
    Column(
        "case_id", Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "system_id",
        Integer,
        ForeignKey("systems.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

case_sections = Table(
    "case_sections",
    Base.metadata,
    Column(
        "case_id", Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "section_id",
        Integer,
        ForeignKey("sections.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

case_operators = Table(
    "case_operators",
    Base.metadata,
    Column(
        "case_id", Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "operator_id",
        Integer,
        ForeignKey("operators.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

case_drones = Table(
    "case_drones",
    Base.metadata,
    Column(
        "case_id", Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "drone_id",
        Integer,
        ForeignKey("drones.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

case_uhub_users = Table(
    "case_uhub_users",
    Base.metadata,
    Column(
        "case_id", Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "uhub_user_id",
        Integer,
        ForeignKey("uhub_users.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

case_uas_zones = Table(
    "case_uas_zones",
    Base.metadata,
    Column(
        "case_id", Integer, ForeignKey("cases.id", ondelete="CASCADE"), primary_key=True
    ),
    Column(
        "uas_zone_id",
        Integer,
        ForeignKey("uas_zones.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

# Block - Case
block_cases = Table(
    "block_cases",
    Base.metadata,
    Column(
        "block_id",
        Integer,
        ForeignKey("blocks.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "case_id",
        Integer,
        ForeignKey("cases.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)

# Campaigns - Blocks
campaign_blocks = Table(
    "campaign_blocks",
    Base.metadata,
    Column(
        "campaign_id",
        Integer,
        ForeignKey("campaigns.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "block_id",
        Integer,
        ForeignKey("blocks.id", ondelete="RESTRICT"),
        primary_key=True,
    ),
)


# Bug-requirements
bug_requirements = Table(
    "bug_requirements",
    Base.metadata,
    Column("bug_id", Integer, ForeignKey("bugs.id"), primary_key=True),
    Column("requirement_id", Integer, ForeignKey("requirements.id"), primary_key=True),
)


# ---- Assets ---- #


class Email(EnvironmentMixin, Base):
    __tablename__ = "emails"

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_email_name_env"),
        UniqueConstraint("environment_id", "email", name="uq_email_email_env"),
    )

    operators = relationship("Operator", backref="email")


class Operator(EnvironmentMixin, Base):
    __tablename__ = "operators"
    name = Column(String, nullable=False)
    easa_id = Column(String, nullable=False)
    verification_code = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    email_id = Column(
        Integer,
        ForeignKey("emails.id", ondelete="RESTRICT"),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_operator_name_env"),
        UniqueConstraint("environment_id", "easa_id", name="uq_operator_easa_env"),
        UniqueConstraint("environment_id", "email_id", name="uq_operator_email_env"),
    )

    drones = relationship("Drone", backref="operator")
    cases = relationship("Case", secondary=case_operators, back_populates="operators")


class Drone(EnvironmentMixin, Base):
    __tablename__ = "drones"
    name = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    model = Column(String, nullable=False)
    tracker_type = Column(
        Enum("GCS-API", "SIMULATOR", "TRACKER", name="tracker_type_enum"),
        nullable=False,
    )
    transponder_id = Column(String, nullable=False)

    operator_id = Column(
        Integer, ForeignKey("operators.id", ondelete="RESTRICT"), nullable=False
    )
    cases = relationship("Case", secondary=case_drones, back_populates="drones")


class UhubOrg(EnvironmentMixin, Base):
    __tablename__ = "uhub_orgs"
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    phone = Column(String, nullable=False)
    jurisdiction = Column(String, nullable=False)
    aoi = Column(String, nullable=False)
    role = Column(String, nullable=False)
    type = Column(
        Enum("INFORMATIVE", "OPERATIVE", name="uhub_org_type_enum"), nullable=False
    )

    users = relationship("UhubUser", backref="uhub_org")
    uas_zones = relationship(
        "UasZone", secondary=zone_organization, back_populates="organizations"
    )

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_uhub_org_name_env"),
        UniqueConstraint("environment_id", "email", name="uq_uhub_org_email_env"),
    )


class UhubUser(EnvironmentMixin, Base):
    __tablename__ = "uhub_users"
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    dni = Column(String, nullable=False, index=True)
    phone = Column(String)
    username = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    type = Column(Enum("ADMIN", "USER", name="user_type_enum"), nullable=False)
    role = Column(String, nullable=False)
    jurisdiction = Column(String, nullable=False)
    aoi = Column(String, nullable=False)

    organization_id = Column(
        Integer,
        ForeignKey("uhub_orgs.id", ondelete="RESTRICT"),
        nullable=False,
    )
    case = relationship("Case", secondary=case_uhub_users, back_populates="uhub_users")

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_uhub_user_name_env"),
        UniqueConstraint("environment_id", "email", name="uq_uhub_user_email_env"),
        UniqueConstraint("environment_id", "dni", name="uq_uhub_user_dni_env"),
        UniqueConstraint(
            "environment_id", "username", name="uq_uhub_user_username_env"
        ),
    )


class UasZone(EnvironmentMixin, Base):
    __tablename__ = "uas_zones"
    name = Column(String, nullable=False, index=True)
    area_type = Column(
        Enum("POLYGON", "CIRCLE", "CORRIDOR", name="area_type_enum"), nullable=False
    )
    circle_radius = Column(Integer, nullable=True)
    corridor_width = Column(Integer, nullable=True)
    lower_limit = Column(Integer, nullable=False)
    upper_limit = Column(Integer, nullable=False)
    reference_lower = Column(
        Enum("AGL", "AMSL", name="reference_lower_enum"), nullable=False
    )
    reference_upper = Column(
        Enum("AGL", "AMSL", name="reference_upper_enum"), nullable=False
    )
    application = Column(
        Enum("TEMPORAL", "PERMANENT", name="application_enum"), nullable=False
    )
    restriction_type = Column(
        Enum(
            "INFORMATIVE",
            "PROHIBITED",
            "REQ.AUTHORISATION",
            "CONDITIONAL",
            name="restriction_type_enum",
        ),
        nullable=False,
    )
    message = Column(Text)
    clearance_required = Column(Boolean, nullable=False)
    reasons = relationship("Reason", secondary=zone_reasons, back_populates="uas_zones")
    organizations = relationship(
        "UhubOrg", secondary=zone_organization, back_populates="uas_zones"
    )
    cases = relationship("Case", secondary=case_uas_zones, back_populates="uas_zones")

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_uas_zone_name_env"),
        CheckConstraint(
            "(area_type != 'CIRCLE') OR (circle_radius IS NOT NULL)",
            name="ck_circle_requires_radius",
        ),
        CheckConstraint(
            "(area_type != 'CORRIDOR') OR (corridor_width IS NOT NULL)",
            name="ck_corridor_requires_width",
        ),
    )


class Uspace(EnvironmentMixin, Base):
    __tablename__ = "uspaces"
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    sectors_count = Column(Integer, nullable=False)
    file_id = Column(
        Integer,
        ForeignKey("files.id", ondelete="RESTRICT"),
        nullable=False,
        unique=True,
    )


# ---- REQUIREMENTS ---- #
class Requirement(EnvironmentMixin, Base):
    __tablename__ = "requirements"
    code = Column(String, nullable=False, index=True)
    definition = Column(Text, nullable=False)

    systems = relationship(
        "System", secondary=requirement_systems, back_populates="requirements"
    )
    sections = relationship(
        "Section", secondary=requirement_sections, back_populates="requirements"
    )
    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_requirement_code_env"),
    )


# ---- TEST MANAGEMENT ---- #
class Step(EnvironmentMixin, Base):
    __tablename__ = "steps"
    action = Column(Text, nullable=False)
    expected_result = Column(Text, nullable=False)
    comments = Column(Text, nullable=False)

    case_id = Column(
        Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False
    )

    affected_requirements = relationship(
        "Requirement", secondary=step_requirements, back_populates="steps"
    )
    step_runs = relationship("StepRun", backref="step")


class Case(EnvironmentMixin, Base):
    __tablename__ = "cases"
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    comments = Column(Text, nullable=False)

    operators = relationship(
        "Operator", secondary=case_operators, back_populates="cases"
    )
    drones = relationship("Drone", secondary=case_drones, back_populates="cases")
    uhub_users = relationship(
        "UhubUser", secondary=case_uhub_users, back_populates="cases"
    )
    uas_zones = relationship(
        "UasZone", secondary=case_uas_zones, back_populates="cases"
    )
    systems = relationship("System", secondary=case_systems, back_populates="cases")
    sections = relationship("Section", secondary=case_sections, back_populates="cases")

    steps = relationship("Step", backref="case")
    blocks = relationship("Block", secondary=block_cases, back_populates="cases")
    case_runs = relationship("CaseRun", backref="case")

    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_case_code_env"),
    )


class Block(EnvironmentMixin, Base):
    __tablename__ = "blocks"
    code = Column(String, nullable=False)
    name = Column(String)
    system_id = Column(
        Integer, ForeignKey("systems.id", ondelete="RESTRICT"), nullable=False
    )
    comments = Column(Text)

    cases = relationship("Case", secondary=block_cases, back_populates="blocks")
    campaigns = relationship(
        "Campaign", secondary=campaign_blocks, back_populates="blocks"
    )
    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_block_code_env"),
    )


class Campaign(EnvironmentMixin, Base):
    __tablename__ = "campaigns"
    code = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    system_id = Column(
        Integer, ForeignKey("systems.id", ondelete="RESTRICT"), nullable=False
    )
    system_version = Column(String, nullable=False)
    comments = Column(Text)
    status = Column(
        Enum("DRAFT", "RUNNING", "FINISHED", "CANCELLED", name="campaign_status_enum"),
        nullable=False,
    )

    blocks = relationship(
        "Block", secondary=campaign_blocks, back_populates="campaigns"
    )
    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_campaign_code_env"),
    )


# ---- EJECUCIÓN DE PRUEBAS ---- #
class CampaignRun(EnvironmentMixin, Base):
    __tablename__ = "campaign_runs"
    campaign_id = Column(
        Integer, ForeignKey("campaigns.id", ondelete="RESTRICT"), nullable=False
    )
    started_at = Column(DateTime, server_default=func.now())
    ended_at = Column(DateTime)
    executed_by = Column(String, nullable=False)
    notes = Column(Text)

    case_runs = relationship("CaseRun", backref="campaign_run")
    step_runs = relationship("StepRun", backref="campaign_run")
    bugs = relationship("Bug", backref="campaign_run")


class CaseRun(EnvironmentMixin, Base):
    __tablename__ = "case_runs"
    campaign_run_id = Column(
        Integer, ForeignKey("campaign_runs.id", ondelete="RESTRICT"), nullable=False
    )
    case_id = Column(
        Integer, ForeignKey("cases.id", ondelete="RESTRICT"), nullable=False
    )
    notes = Column(Text)

    step_runs = relationship("StepRun", backref="case_run")


class StepRun(EnvironmentMixin, Base):
    __tablename__ = "step_runs"
    campaign_run_id = Column(
        Integer, ForeignKey("campaign_runs.id", ondelete="RESTRICT"), nullable=False
    )
    case_run_id = Column(
        Integer, ForeignKey("case_runs.id", ondelete="RESTRICT"), nullable=False
    )
    step_id = Column(
        Integer, ForeignKey("steps.id", ondelete="RESTRICT"), nullable=False
    )
    passed = Column(Boolean)
    notes = Column(Text)
    file_id = Column(
        Integer, ForeignKey("files.id", ondelete="RESTRICT"), nullable=True
    )


# ---- BUGS ---- #


class Bug(EnvironmentMixin, Base):
    __tablename__ = "bugs"
    status = Column(
        Enum(
            "OPEN",
            "CLOSED SOLVED",
            "CLOSED UNSOLVED",
            "PENDING",
            "ON HOLD",
            name="bug_status_enum",
        ),
        nullable=False,
    )
    system_id = Column(
        Integer, ForeignKey("systems.id", ondelete="RESTRICT"), nullable=False
    )
    campaign_run_id = Column(
        Integer, ForeignKey("campaign_runs.id", ondelete="RESTRICT")
    )
    system_version = Column(String, nullable=False)
    service_now_id = Column(String)
    short_description = Column(String, nullable=False)
    definition = Column(Text, nullable=False)
    urgency = Column(Enum("1", "2", "3", name="urgency_enum"), nullable=False)
    impact = Column(Enum("1", "2", "3", name="impact_enum"), nullable=False)
    comments = Column(Text)
    file_id = Column(Integer, ForeignKey("files.id", ondelete="RESTRICT"))


class BugHistory(EnvironmentMixin, Base):
    __tablename__ = "bug_history"
    bug_id = Column(Integer, ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False)
    changed_by = Column(String, nullable=False)
    change_timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    change_summary = Column(Text, nullable=False)

    bugs = relationship("Bug", backref="bug_history")


# ---- TABLAS AUXILIARES ---- #
class Environment(Base):
    __tablename__ = "environments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    emails = relationship("Email", backref="environment")
    operators = relationship("Operator", backref="environment")


class System(Base):
    __tablename__ = "systems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    requirements = relationship(
        "Requirement", secondary=requirement_systems, back_populates="systems"
    )
    cases = relationship("Case", secondary=case_systems, back_populates="systems")
    bugs = relationship("Bug", backref="system")


class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    requirements = relationship(
        "Requirement", secondary=requirement_sections, back_populates="sections"
    )
    case = relationship("Case", secondary=case_sections, back_populates="sections")


class Reason(Base):
    __tablename__ = "reasons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    uas_zones = relationship(
        "UasZone", secondary=zone_reasons, back_populates="reasons"
    )


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_type = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)
    size = Column(String, nullable=False)
    uploaded_by = Column(String, nullable=False)
    uploaded_at = Column(DateTime, server_default=func.now(), nullable=False)

    uspace_files = relationship("Uspace", backref="file")
    step_runs_files = relationship("StepRun", backref="file")
    bug_files = relationship("Bug", backref="file")
