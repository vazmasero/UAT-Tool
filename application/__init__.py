"""
Módulo de aplicación - Contiene el contexto de aplicación y gestión de unidades de trabajo.
"""

from .app_context import ApplicationContext
from .unit_of_work import UnitOfWork, unit_of_work

__all__ = ["ApplicationContext", "UnitOfWork", "unit_of_work"]
