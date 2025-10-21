"""
db.models.assets
----------------

Modelos relacionados con los activos y entidades operativas:
Emails, Operadores, Drones, Usuarios y Zonas UAS.
Todos los modelos heredan EnvironmentMixin y Base para coherencia con el ORM.
"""

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    relationship,
)

from uat_tool.infrastructure import AuditMixin, Base, EnvironmentMixin

# ---- EMAIL ---- #


class Email(AuditMixin, EnvironmentMixin, Base):
    """Modelo que representa un correo electrónico asociado (o no) a operadores USSP."""

    __tablename__ = "emails"

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_email_name_env"),
        UniqueConstraint("environment_id", "email", name="uq_email_email_env"),
        UniqueConstraint("environment_id", "password", name="uq_email_password_env"),
    )

    operators = relationship("Operator", back_populates="email")
    environment = relationship("Environment", back_populates="emails")


# ---- OPERATORS ---- #


class Operator(AuditMixin, EnvironmentMixin, Base):
    """Operador de USSP, asociado a un email y que puede tener múltiples drones."""

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
        UniqueConstraint("environment_id", "password", name="uq_operator_password_env"),
    )

    email = relationship("Email", back_populates="operators")
    drones = relationship("Drone", back_populates="operator")
    cases = relationship("Case", secondary="case_operators", back_populates="operators")
    environment = relationship(
        "Environment", back_populates="operators"
    )


# ---- DRONES ---- #
class Drone(AuditMixin, EnvironmentMixin, Base):
    """Dron operado por un operador USSP."""

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
    operator = relationship("Operator", back_populates="drones")
    cases = relationship("Case", secondary="case_drones", back_populates="drones")
    environment = relationship("Environment", back_populates="drones")


# ---- U-HUB ORGANIZATIONS ---- #


class UhubOrg(AuditMixin, EnvironmentMixin, Base):
    """Organización U-Hub, que puede tener o no un conjunto de usuarios y zonas UAS asociadas."""

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

    users = relationship("UhubUser", back_populates="organization")
    uas_zones = relationship(
        "UasZone", secondary="zone_organization", back_populates="organizations"
    )
    environment = relationship(
        "Environment", back_populates="uhub_orgs"
    )

    __table_args__ = (
        UniqueConstraint("environment_id", "name", name="uq_uhub_org_name_env"),
        UniqueConstraint("environment_id", "email", name="uq_uhub_org_email_env"),
    )


# - --- U-HUB USERS ---- #
class UhubUser(AuditMixin, EnvironmentMixin, Base):
    """Usuario de U-Hub, asociado a una organización"""

    __tablename__ = "uhub_users"
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
    organization = relationship("UhubOrg", back_populates="users")
    cases = relationship(
        "Case", secondary="case_uhub_users", back_populates="uhub_users"
    )
    environment = relationship(
        "Environment", back_populates="uhub_users"
    )

    __table_args__ = (
        UniqueConstraint("environment_id", "email", name="uq_uhub_user_email_env"),
        UniqueConstraint("environment_id", "dni", name="uq_uhub_user_dni_env"),
        UniqueConstraint(
            "environment_id", "username", name="uq_uhub_user_username_env"
        ),
    )


# ---- UAS ZONES ---- #
class UasZone(AuditMixin, EnvironmentMixin, Base):
    """Zona UAS, que puede estar asociada a múltiples organizaciones U-Hub."""

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
    reasons = relationship(
        "Reason", secondary="zone_reasons", back_populates="uas_zones"
    )
    organizations = relationship(
        "UhubOrg", secondary="zone_organization", back_populates="uas_zones"
    )

    cases = relationship("Case", secondary="case_uas_zones", back_populates="uas_zones")
    environment = relationship(
        "Environment", back_populates="uas_zones"
    )

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


# ---- USPACE ---- #
class Uspace(AuditMixin, EnvironmentMixin, Base):
    """Modelo que representa un espacio aéreo U-Space."""

    __tablename__ = "uspaces"
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    sectors_count = Column(Integer, nullable=False)

    environment = relationship("Environment", back_populates="uspaces")

    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_uspace_code_env"),
    )
