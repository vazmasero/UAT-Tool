"""
Paquete `presentation.models`

Contiene los modelos de datos específicos para Qt:

- BugTableModel: Modelo de tabla para mostrar bugs en QTableView
- BugProxyModel: Modelo proxy para filtrado y ordenación de bugs
- [Futuros]: CampaignTableModel, RequirementTableModel, etc.

Estos modelos adaptan los DTOs de aplicación al formato requerido
por los componentes de vista de Qt.

Ejemplo:
    from presentation.models import BugTableModel, BugProxyModel
"""

from .bug_proxy_model import BugProxyModel
from .bug_table_model import BugTableModel
from .requirement_proxy_model import RequirementProxyModel
from .requirement_table_model import RequirementTableModel

__all__ = [
    "BugTableModel",
    "BugProxyModel",
    "RequirementTableModel",
    "RequirementProxyModel",
]
