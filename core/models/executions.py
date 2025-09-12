"""
db.models.executions
----------------

Modelos relacionados con la ejecución de campañas de pruebas. Indica los estados de las campañas y están
relacionados con los borradores de campañas, casos y pasos.
Todos los modelos heredan EnvironmentMixin y Base para coherencia con el ORM.
"""

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
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


# ---- EJECUCIÓN DE CAMPAÑAS ---- #
class CampaignRun(EnvironmentMixin, Base):
    """Modelo que representa la ejecución de una campaña de pruebas."""

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


class CaseRun(Base):
    """Modelo que representa el estado de ejecución de un caso de prueba dentro de una campaña."""

    __tablename__ = "case_runs"
    campaign_run_id = Column(
        Integer, ForeignKey("campaign_runs.id", ondelete="RESTRICT"), nullable=False
    )
    case_id = Column(
        Integer, ForeignKey("cases.id", ondelete="RESTRICT"), nullable=False
    )
    notes = Column(Text)

    step_runs = relationship("StepRun", backref="case_run")


class StepRun(Base):
    """Modelo que representa la ejecución de un paso dentro de un caso de prueba en una campaña."""

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
