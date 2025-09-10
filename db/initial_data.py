from sqlalchemy.orm import Session

from db.models import Section, System

from .auxiliary import get_or_create


def load_initial_data(session: Session):
    """Puebla las tablas con datos predefinidos cuando el programa se lanza."""

    systems = ["USSP", "CISP", "AUDI", "EXCHANGE", "NA"]
    sections = [
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

    # Crea sistemas sin duplicados
    for system_name in systems:
        get_or_create(session, System, name=system_name)

    for section_name in sections:
        get_or_create(session, Section, name=section_name)
