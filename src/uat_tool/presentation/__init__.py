"""
Paquete `presentation`

Contiene la interfaz de usuario y componentes de presentación:

- Controllers: Controladores MVVM para coordinar UI y servicios
- Views: Ventanas y componentes de interfaz de usuario
- Models: Modelos de datos específicos para Qt
- Dialogs: Diálogos y formularios de la aplicación
- UI: Archivos .ui generados por Qt Designer

Arquitectura MVVM con separación clara entre vista y lógica.
"""

# Exportar componentes principales a través de sus paquetes
from .models import (
    BugProxyModel,
    BugTableModel,
    RequirementProxyModel,
    RequirementTableModel,
)
from .views.main_window import MainWindow

__all__ = [
    "MainWindow",
    "BugTableModel",
    "BugProxyModel",
    "RequirementTableModel",
    "RequirementProxyModel",
]
