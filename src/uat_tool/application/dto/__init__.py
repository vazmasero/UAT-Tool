"""
Paquete `application.dto`

Contiene los Data Transfer Objects (DTOs) para transferencia
type-safe entre capas:

- BugBugFormDTO, BugServiceDTO, BugTableDTO: Representación de Bug para servicios,
formularios y  tabla de UI
- [Futuros]: CampaignDTO, RequirementDTO, etc.

Los DTOs son inmutables y contienen solo datos, sin lógica de negocio.
Se utilizan para transferir datos entre la capa de aplicación y presentación.

Ejemplo:
    from application.dto import BugDTO
    bug_dto = BugDTO(id=1, status="OPEN", ...)
"""

from .assets_dto import (
    DroneFormDTO,
    DroneServiceDTO,
    DroneTableDTO,
    EmailFormDTO,
    EmailServiceDTO,
    EmailTableDTO,
    OperatorFormDTO,
    OperatorServiceDTO,
    OperatorTableDTO,
    UasZoneFormDTO,
    UasZoneServiceDTO,
    UasZoneTableDTO,
    UhubOrgFormDTO,
    UhubOrgServiceDTO,
    UhubOrgTableDTO,
    UhubUserFormDTO,
    UhubUserServiceDTO,
    UhubUserTableDTO,
    UspaceFormDTO,
    UspaceServiceDTO,
    UspaceTableDTO,
)
from .bug_dto import (
    BugDetailDTO,
    BugFormDTO,
    BugHistoryServiceDTO,
    BugHistoryTableDTO,
    BugServiceDTO,
    BugTableDTO,
)
from .requirement_dto import (
    RequirementFormDTO,
    RequirementServiceDTO,
    RequirementTableDTO,
)
from .test_management_dto import (
    BlockFormDTO,
    BlockServiceDTO,
    BlockTableDTO,
    CampaignFormDTO,
    CampaignServiceDTO,
    CampaignTableDTO,
    CaseFormDTO,
    CaseServiceDTO,
    CaseTableDTO,
    StepFormDTO,
    StepServiceDTO,
    StepTableDTO,
)

__all__ = [
    "BlockFormDTO",
    "BlockServiceDTO",
    "BlockTableDTO",
    "StepFormDTO",
    "StepServiceDTO",
    "StepTableDTO",
    "CaseFormDTO",
    "CaseServiceDTO",
    "CaseTableDTO",
    "CampaignFormDTO",
    "CampaignServiceDTO",
    "CampaignTableDTO",
    "BugDetailDTO",
    "BugFormDTO",
    "BugHistoryServiceDTO",
    "BugHistoryTableDTO",
    "BugHistoryServiceDTOBugFormDTO",
    "BugTableDTO",
    "BugServiceDTO",
    "RequirementFormDTO",
    "RequirementServiceDTO",
    "RequirementTableDTO",
    "EmailFormDTO",
    "EmailServiceDTO",
    "EmailTableDTO",
    "OperatorTableDTO",
    "OperatorFormDTO",
    "OperatorServiceDTO",
    "UhubOrgFormDTO",
    "UhubOrgServiceDTO",
    "UhubOrgTableDTO",
    "UhubUserFormDTO",
    "UhubUserServiceDTO",
    "UhubUserTableDTO",
    "DroneFormDTO",
    "DroneServiceDTO",
    "DroneTableDTO",
    "UasZoneFormDTO",
    "UasZoneServiceDTO",
    "UasZoneTableDTO",
    "UspaceFormDTO",
    "UspaceServiceDTO",
    "UspaceTableDTO",
]
