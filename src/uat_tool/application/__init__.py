"""
Paquete `application`

Contiene la lógica de aplicación y orquestación del sistema:

- AppContext: Contenedor de dependencias y contexto global
- UnitOfWork: Patrón unidad de trabajo para transacciones
- Services: Servicios con lógica de negocio
- DTOs: Objetos de transferencia de datos type-safe

Todos los componentes están exportados para importación directa:

    from application import ApplicationContext, BugService, BugDTO
"""

from .app_context import ApplicationContext
from .bootstrap import bootstrap
from .services.auxiliary_service import AuxiliaryService

# Services
# DTOs
from .services.base_service import BaseService
from .services.bug_service import BugService
from .services.requirement_service import RequirementService
from .uow import unit_of_work

__all__ = [
    "AuxiliaryService",
    "ApplicationContext",
    "bootstrap",
    "BugService",
    "RequirementService",
    "BaseService",
    "unit_of_work",
]
