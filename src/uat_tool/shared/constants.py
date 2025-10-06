"""
Constantes compartidas de la aplicación.

Contiene valores constantes utilizados en múltiples capas
para mantener la consistencia y facilitar el mantenimiento.
"""

# Estados de bugs
BUG_STATUS_OPEN = "OPEN"
BUG_STATUS_CLOSED_SOLVED = "CLOSED SOLVED"
BUG_STATUS_CLOSED_UNSOLVED = "CLOSED UNSOLVED"
BUG_STATUS_PENDING = "PENDING"
BUG_STATUS_ON_HOLD = "ON HOLD"

BUG_STATUS_CHOICES = [
    BUG_STATUS_OPEN,
    BUG_STATUS_CLOSED_SOLVED,
    BUG_STATUS_CLOSED_UNSOLVED,
    BUG_STATUS_PENDING,
    BUG_STATUS_ON_HOLD,
]

# Niveles de urgencia e impacto
URGENCY_LEVELS = ["1", "2", "3"]
IMPACT_LEVELS = ["1", "2", "3"]

# Nombres de pestañas
TAB_BUGS = "bugs"
TAB_CAMPAIGNS = "campaigns"
TAB_TEST_MANAGEMENT = "test_management"
TAB_REQUIREMENTS = "requirements"
TAB_ASSETS = "assets"

TAB_NAMES = {
    TAB_BUGS: "Bugs",
    TAB_CAMPAIGNS: "Campaigns",
    TAB_TEST_MANAGEMENT: "Test Management",
    TAB_REQUIREMENTS: "Requirements",
    TAB_ASSETS: "Assets",
}
