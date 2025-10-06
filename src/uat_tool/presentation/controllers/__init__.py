"""
Paquete `presentation.controllers`

Contiene los controladores MVVM para la interfaz de usuario:

- MainController: Controlador principal que coordina las pestañas
- BaseTabController: Clase base para controladores de pestañas
- BugTabController: Controlador específico para la pestaña de bugs
- [Futuros]: CampaignTabController, RequirementTabController, etc.

Cada controlador maneja la lógica de presentación para una pestaña
y actúa como intermediario entre la UI y los servicios.

Ejemplo:
    from presentation.controllers import MainController, BugTabController
"""

from .base_tab_controller import BaseTabController
from .bug_tab_controller import BugTabController
from .main_controller import MainController

__all__ = [
    "MainController",
    "BaseTabController",
    "BugTabController",
]
