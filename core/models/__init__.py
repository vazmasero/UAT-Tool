"""
Paquete `db.models`

Contiene todos los modelos de la base de datos y tablas de asociación
para el ORM de SQLAlchemy. Organizado por categorías:

- Assets: Entidades relacionadas con operadores, drones, usuarios, etc.
- Associations: Tablas many-to-many intermedias.
- Auxiliary: Tablas de soporte como Environment, File, System.
- Bugs: Gestión de bugs y su historial.
- Test Management: Cases, Steps, Blocks, Campaigns.
- Executions: CampaignRun, CaseRun, StepRun.
- Requirements: Requisitos y su relación con sistemas y secciones.

Todos los modelos y asociaciones están exportados en `__all__` para
importación directa:

    from db.models import Case, Step, Bug, zone_organization

"""

# ---- Assets ----
from .assets import Drone, Email, Operator, UasZone, UhubOrg, UhubUser, Uspace

# ---- Associations (Many-to-Many) ----
from .associations import (
    block_cases,
    bug_requirements,
    campaign_blocks,
    case_drones,
    case_operators,
    case_sections,
    case_systems,
    case_uas_zones,
    case_uhub_users,
    requirement_sections,
    requirement_systems,
    step_requirements,
    zone_organization,
    zone_reasons,
)

# ---- Auxiliary Tables ----
from .auxiliary import Environment, File, Reason, Section, System

# ---- Bugs ----
from .bugs import Bug, BugHistory

# ---- Test executions ----
from .executions import CampaignRun, CaseRun, StepRun

# ---- Requirements ----
from .requirements import Requirement

# ---- Test management ----
from .test_management import Block, Campaign, Case, Step

__all__ = [
    "Email",
    "Operator",
    "Drone",
    "UhubOrg",
    "UhubUser",
    "UasZone",
    "Uspace",
    "Requirement",
    "Step",
    "Case",
    "Block",
    "Campaign",
    "CampaignRun",
    "CaseRun",
    "StepRun",
    "Bug",
    "BugHistory",
    "File",
    "Environment",
    "System",
    "Section",
    "Reason",
    "zone_organization",
    "zone_reasons",
    "requirement_systems",
    "requirement_sections",
    "step_requirements",
    "case_systems",
    "case_sections",
    "case_operators",
    "case_drones",
    "case_uhub_users",
    "case_uas_zones",
    "block_cases",
    "campaign_blocks",
    "bug_requirements",
]
