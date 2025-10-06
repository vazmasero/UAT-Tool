"""
Paquete `shared`

Contiene utilidades compartidas entre todas las capas:

- Logging: Configuración centralizada de logging
- Constants: Constantes de la aplicación
- Helpers: Funciones utilitarias generales
- [Futuros]: Validators, decorators, etc.

Componentes reutilizables que no pertenecen a una capa específica.
"""

from .constants import *
from .logging import get_logger, setup_logging

__all__ = [
    "setup_logging",
    "get_logger",
]
