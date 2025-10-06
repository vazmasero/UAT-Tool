"""
Paquete `presentation.views`

Contiene las ventanas principales y componentes de UI:

- MainWindow: Ventana principal de la aplicación
- [Futuros]: Dialogos, widgets personalizados, etc.

Las vistas contienen principalmente la configuración de UI
y delegan la lógica a los controladores.

Ejemplo:
    from presentation.views import MainWindow
"""

from .main_window import MainWindow

__all__ = [
    "MainWindow",
]
