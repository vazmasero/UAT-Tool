"""
db.models.auxiliary
----------------

Tablas comunes a multiples modelos de la base de datos: relacionados con los activos y entidades operativas:
Environments, Systems, Sections, Reasons y Files.
Todos los modelos heredan EnvironmentMixin (excepto Environment) y Base para coherencia con el ORM.
"""

from sqlalchemy import Column, DateTime, Integer, String, Text, func
from sqlalchemy.orm import relationship

from data.database import Base


# ---- ENVIRONMENTS ---- #
class Environment(Base):
    """Modelo que representa un entorno de instalación de la aplicación.
    Sirve para particularizar las pruebas y los bugs por entorno."""

    __tablename__ = "environments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    environment_emails = relationship("Email", back_populates="environment_rel")
    environment_operators = relationship("Operator", back_populates="environment_rel")
    environment_drones = relationship("Drone", back_populates="environment_rel")
    environment_uhub_orgs = relationship("UhubOrg", back_populates="environment_rel")
    environment_uhub_users = relationship("UhubUser", back_populates="environment_rel")
    environment_uas_zones = relationship("UasZone", back_populates="environment_rel")
    environment_uspaces = relationship("Uspace", back_populates="environment_rel")
    environment_bugs = relationship("Bug", back_populates="environment_rel")
    environment_campaigns = relationship("Campaign", back_populates="environment_rel")
    environment_campaign_runs = relationship(
        "CampaignRun", back_populates="environment_rel"
    )
    environment_requirements = relationship(
        "Requirement", back_populates="environment_rel"
    )


# ---- SYSTEMS ---- #
class System(Base):
    """Lista de sistemas dentro de U-hub. Por defecto se corresponden con:
    USSP, CISP, AUDI, EXCHANGE y NA (No Aplica)"""

    __tablename__ = "systems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    requirements = relationship(
        "Requirement", secondary="requirement_systems", back_populates="systems"
    )
    cases = relationship("Case", secondary="case_systems", back_populates="systems")
    bugs = relationship("Bug", back_populates="system")
    campaigns = relationship("Campaign", back_populates="system")


# --- SECTIONS ---- #
class Section(Base):
    """Lista de secciones agrupadoras de requisitos y casos de prueba de acuerdo
    con el documento original de requisitos de usuario de la herramienta U-space."""

    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    requirements = relationship(
        "Requirement", secondary="requirement_sections", back_populates="sections"
    )
    cases = relationship("Case", secondary="case_sections", back_populates="sections")


# --- REASONS ---- #
class Reason(Base):
    """Lista de motivos asociados a una zona UAS de acuerdo con el estándar ED-318."""

    __tablename__ = "reasons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    uas_zones = relationship(
        "UasZone", secondary="zone_reasons", back_populates="reasons"
    )


# ---- FILES ---- #
class File(Base):
    """Modelo que representa un archivo subido al sistema, asociado a un registro en otra tabla."""

    __tablename__ = "files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_type = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)
    size = Column(String, nullable=False)
    uploaded_by = Column(String, nullable=False)
    uploaded_at = Column(DateTime, server_default=func.now(), nullable=False)

    uspace = relationship("Uspace", back_populates="file")
    bug_files = relationship("Bug", back_populates="file")
    step_runs_files = relationship("StepRun", back_populates="file")
