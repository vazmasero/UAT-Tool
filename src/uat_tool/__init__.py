"""UAT Tool - Sistema de gestión de pruebas UATs y seguimiento de bugs
sobre el sistema U-space de Enaire"""

__version__ = "1.0.0"
__author__ = "David Vázquez Masero"

from .application.app_context import ApplicationContext
from .main import main
from .shared.logging import get_logger, setup_logging

__version__ = "1.0.0"
__all__ = ["main", "ApplicationContext", "get_logger", "setup_logging"]
