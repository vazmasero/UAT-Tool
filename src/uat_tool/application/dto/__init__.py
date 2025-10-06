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

from .bug_dto import BugFormDTO, BugServiceDTO, BugTableDTO

__all__ = [
    "BugFormDTO",
    "BugTableDTO",
    "BugServiceDTO",
]
