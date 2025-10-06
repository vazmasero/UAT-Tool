"""
Paquete `application.services`

Contiene los servicios de aplicación con lógica de negocio:

- BugService: Gestión completa del ciclo de vida de bugs
- [Futuros]: CampaignService, RequirementService, etc.

Cada servicio encapsula la lógica de negocio para una entidad específica
y coordina las operaciones entre repositorios y DTOs.

Ejemplo:
    from application.services import BugService
    bugs = BugService(app_context).get_all_bugs_dto()
"""

from .base_service import BaseService
from .bug_service import BugService

__all__ = [
    "BugService",
    "BaseService",
]
