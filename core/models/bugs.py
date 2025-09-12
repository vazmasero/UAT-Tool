"""
db.models.bugs
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

from data.database import Base, EnvironmentMixin


# ---- BUGS ---- #
class Bug(EnvironmentMixin, Base):
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
    urgency = Column(Enum("1", "2", "3", name="urgency_enum"), nullable=False)
    impact = Column(Enum("1", "2", "3", name="impact_enum"), nullable=False)
    comments = Column(Text)
    file_id = Column(Integer, ForeignKey("files.id", ondelete="RESTRICT"))


# ---- HISTORIAL DE BUGS ---- #
class BugHistory(EnvironmentMixin, Base):
    """Modelo que representa el historial de cambios de un bug.
    Se registra quién ha hecho el cambio, la fecha y un resumen del cambio.
    """

    __tablename__ = "bug_history"
    bug_id = Column(Integer, ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False)
    changed_by = Column(String, nullable=False)
    change_timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    change_summary = Column(Text, nullable=False)

    bugs = relationship("Bug", backref="bug_history")
