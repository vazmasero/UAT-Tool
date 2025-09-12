"""
db.models.auxiliary
----------------

Tablas comunes a multiples modelos de la base de datos: relacionados con los activos y entidades operativas:
Environments, Systems, Sections, Reasons y Files.
Todos los modelos heredan EnvironmentMixin (excepto Environment) y Base para coherencia con el ORM.
"""

from sqlalchemy import Column, DateTime, Integer, String, Text, func
from sqlalchemy.orm import (
    relationship,
)

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

    emails = relationship("Email", backref="environment")
    operators = relationship("Operator", backref="environment")
    drones = relationship("Drone", backref="environment")
    uhub_orgs = relationship("UhubOrg", backref="environment")
    uhub_users = relationship("UhubUser", backref="environment")
    uas_zones = relationship("UasZone", backref="environment")
    uspaces = relationship("Uspace", backref="environment")
    bugs = relationship("Bug", backref="environment")
    campaigns = relationship("Campaign", backref="environment")
    campaign_runs = relationship("CampaignRun", backref="environment")
    requirements = relationship("Requirement", backref="environment")


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
    bugs = relationship("Bug", backref="system")


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

    uspace_files = relationship("Uspace", backref="file")
    step_runs_files = relationship("StepRun", backref="file")
    bug_files = relationship("Bug", backref="file")
