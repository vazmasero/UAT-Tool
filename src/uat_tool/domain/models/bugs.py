"""
domain.models.bugs
----------------

Modelos relacionados con los bugs encontrados en la aplicación.
"""

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    relationship,
)

from uat_tool.infrastructure import AuditMixin, Base, EnvironmentMixin


# ---- BUGS ---- #
class Bug(AuditMixin, EnvironmentMixin, Base):
    """Errores encontrados en la aplicación. Pueden registrarse a través de la ejecución de una campaña
    o de forma manual."""

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
    urgency = Column(Integer, nullable=False)
    impact = Column(Integer, nullable=False)
    comments = Column(Text)
    requirements = relationship(
        "Requirement", secondary="bug_requirements", back_populates="bugs"
    )

    campaign_run = relationship("CampaignRun", back_populates="bugs")
    environment = relationship("Environment", back_populates="bugs")
    system = relationship("System", back_populates="bugs")
    history = relationship("BugHistory", back_populates="bug")


# ---- HISTORIAL DE BUGS ---- #
class BugHistory(Base):
    """Modelo que representa el historial de cambios de un bug.
    Se registra quién ha hecho el cambio, la fecha y un resumen del cambio.
    """

    __tablename__ = "bug_history"
    id = Column(Integer, primary_key=True, autoincrement=True)
    bug_id = Column(Integer, ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False)
    changed_by = Column(String, nullable=False)
    change_timestamp = Column(DateTime, server_default=func.now(), nullable=False)  # pylint: disable=not-callable
    change_summary = Column(Text, nullable=False)

    bug = relationship("Bug", back_populates="history")
