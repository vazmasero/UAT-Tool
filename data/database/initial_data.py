from sqlalchemy.orm import Session

from core.models import Reason, Section, System

from .utils import get_or_create

# ---- Datos iniciales ----
SYSTEMS = ["USSP", "CISP", "AUDI", "EXCHANGE", "NA"]
SECTIONS = [
    "General",
    "Regulation",
    "Testing environment",
    "HMI",
    "GCS API",
    "User management",
    "NID",
    "Geo-awareness",
    "UAS flight authorization",
    "Traffic info",
    "DAIM",
    "Weather",
    "Conformance monitoring",
    "Tracking",
    "Conflict management",
    "ATM/U-space",
    "Billing",
    "Emergency management",
    "NA",
]
REASONS = [
    "AIR TRAFFIC",
    "SENSIBLE",
    "PRIVACY",
    "POPULATION",
    "NOISE",
    "EMERGENCY",
    "OTHER",
    "NATURE",
]


def load_initial_data(session: Session) -> None:
    """Puebla las tablas con datos predefinidos cuando el programa se lanza."""
    mapping = {
        System: SYSTEMS,
        Section: SECTIONS,
        Reason: REASONS,
    }

    for model, values in mapping.items():
        for value in values:
            get_or_create(session, model, name=value)
