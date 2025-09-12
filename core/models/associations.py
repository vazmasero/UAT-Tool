"""
db.models.associations
----------------

Tablas intermedias para las relaciones de muchos a muchos (Many-to-Many).
"""

from sqlalchemy import Column, ForeignKey, Integer, Table

from data.database import Base

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
    "zone_reasons",
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
