"""
db.models.requirements
----------------

Modelos de los requisitos de usuario del sistema. Cada requisito puede estar asociado a varios sistemas
y secciones, y puede estar vinculado a casos de prueba y bugs.
"""

from sqlalchemy import Column, String, Text, UniqueConstraint
from sqlalchemy.orm import (
    relationship,
)

from uat_tool.infrastructure import AuditMixin, Base, EnvironmentMixin


# ---- REQUIREMENTS ---- #
class Requirement(AuditMixin, EnvironmentMixin, Base):
    """Requisitos de usuario del sistema. Cada requisito puede estar asociado a varios sistemas
    y secciones, y puede estar vinculado a casos de prueba y bugs.
    """

    __tablename__ = "requirements"
    code = Column(String, nullable=False, index=True)
    definition = Column(Text, nullable=False)

    systems = relationship(
        "System", secondary="requirement_systems", back_populates="requirements"
    )
    sections = relationship(
        "Section", secondary="requirement_sections", back_populates="requirements"
    )
    steps = relationship(
        "Step", secondary="step_requirements", back_populates="requirements"
    )
    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_requirement_code_env"),
    )

    environment = relationship(
        "Environment", back_populates="requirements"
    )
    bugs = relationship(
        "Bug", secondary="bug_requirements", back_populates="requirements"
    )
