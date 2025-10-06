"""
Paquete `domain.repositories`

Contiene todas las interfaces de repositorio para el patrón Repository.
Organizado por entidades de dominio:

- Asset Repositories: Operadores, drones, usuarios, etc.
- Bug Repositories: Gestión de bugs.
- Test Management Repositories: Cases, Steps, Blocks, Campaigns.
- Execution Repositories: CampaignRun, CaseRun, StepRun.
- Requirement Repositories: Requisitos.
- Auxiliary Repositories: Environment, File, System, etc.

Todas las interfaces de repositorio están exportadas en `__all__` para
importación directa:

    from domain.repositories import BugRepository, CampaignRepository

Cada repositorio define las operaciones CRUD básicas y consultas específicas
para su entidad correspondiente.
"""

# ---- Asset Repositories ----
from .asset_repository import (
    DroneRepository,
    EmailRepository,
    OperatorRepository,
    UasZoneRepository,
    UhubOrgRepository,
    UhubUserRepository,
    UspaceRepository,
)

# ---- Auxiliary Repositories ----
from .auxiliary_repository import (
    EnvironmentRepository,
    FileRepository,
    ReasonRepository,
    SectionRepository,
    SystemRepository,
)
from .base import BaseRepository

# ---- Bug Repositories ----
from .bug_repository import BugRepository

# ---- Execution Repositories ----
from .executions_repository import (
    CampaignRunRepository,
    CaseRunRepository,
    StepRunRepository,
)

# ---- Requirement Repositories ----
from .requirement_repository import RequirementRepository

# ---- Test Management Repositories ----
from .test_management_repository import (
    BlockRepository,
    CampaignRepository,
    CaseRepository,
    StepRepository,
)

__all__ = [
    "BaseRepository",
    # Asset Repositories
    "DroneRepository",
    "EmailRepository",
    "OperatorRepository",
    "UasZoneRepository",
    "UhubOrgRepository",
    "UhubUserRepository",
    "UspaceRepository",
    # Bug Repositories
    "BugRepository",
    # Test Management Repositories
    "BlockRepository",
    "CampaignRepository",
    "CaseRepository",
    "StepRepository",
    # Execution Repositories
    "CampaignRunRepository",
    "CaseRunRepository",
    "StepRunRepository",
    # Requirement Repositories
    "RequirementRepository",
    # Auxiliary Repositories
    "EnvironmentRepository",
    "FileRepository",
    "ReasonRepository",
    "SectionRepository",
    "SystemRepository",
]
