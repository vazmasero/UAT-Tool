"""
db.models.test_management
----------------

Modelos relacionados con la gestión de pruebas. Contiene los borradores de pruebas, casos y pasos.
Todos los modelos heredan EnvironmentMixin y Base para coherencia con el ORM.
"""

from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import (
    relationship,
)

from uat_tool.infrastructure import AuditMixin, Base, EnvironmentMixin


# ---- TEST MANAGEMENT ---- #
class Step(Base):
    __tablename__ = "steps"
    id = Column(Integer, primary_key=True, autoincrement=True)
    action = Column(Text, nullable=False)
    expected_result = Column(Text, nullable=False)
    comments = Column(Text, nullable=False)

    case_id = Column(
        Integer, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False
    )
    step_runs = relationship("StepRun", back_populates="step")
    requirements = relationship(
        "Requirement", secondary="step_requirements", back_populates="steps"
    )
    case = relationship("Case", back_populates="steps")


class Case(AuditMixin, EnvironmentMixin, Base):
    __tablename__ = "cases"
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    comments = Column(Text, nullable=False)

    operators = relationship(
        "Operator", secondary="case_operators", back_populates="cases"
    )
    drones = relationship("Drone", secondary="case_drones", back_populates="cases")
    uhub_users = relationship(
        "UhubUser", secondary="case_uhub_users", back_populates="cases"
    )
    uas_zones = relationship(
        "UasZone", secondary="case_uas_zones", back_populates="cases"
    )
    systems = relationship("System", secondary="case_systems", back_populates="cases")
    sections = relationship(
        "Section", secondary="case_sections", back_populates="cases"
    )

    steps = relationship("Step", back_populates="case")
    blocks = relationship("Block", secondary="block_cases", back_populates="cases")
    case_runs = relationship("CaseRun", back_populates="case")

    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_case_code_env"),
    )


class Block(AuditMixin, EnvironmentMixin, Base):
    __tablename__ = "blocks"
    code = Column(String, nullable=False)
    name = Column(String)
    system_id = Column(
        Integer, ForeignKey("systems.id", ondelete="RESTRICT"), nullable=False
    )
    comments = Column(Text)

    cases = relationship("Case", secondary="block_cases", back_populates="blocks")
    campaigns = relationship(
        "Campaign", secondary="campaign_blocks", back_populates="blocks"
    )
    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_block_code_env"),
    )


class Campaign(AuditMixin, EnvironmentMixin, Base):
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
        "Block", secondary="campaign_blocks", back_populates="campaigns"
    )
    __table_args__ = (
        UniqueConstraint("environment_id", "code", name="uq_campaign_code_env"),
    )

    campaign_runs = relationship("CampaignRun", back_populates="campaign")
    system = relationship("System", back_populates="campaigns")
    environment_rel = relationship(
        "Environment", back_populates="environment_campaigns"
    )
