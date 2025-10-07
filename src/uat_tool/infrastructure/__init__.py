"""
Paquete `infrastructure`

Proporciona acceso a la capa de infraestructura:
- Configuración de base de datos
- Sesiones y motor SQLAlchemy
- Utilidades de persistencia
- [Futuros]: APIs externas, sistemas de archivos, etc.
"""

from .database import (
    DB_URL,
    AuditMixin,
    Base,
    EnvironmentMixin,
    Session,
    engine,
    get_or_create,
    init_db,
)

__all__ = [
    # Configuración BD
    "DB_URL",
    "engine",
    "Session",
    # Base y Mixins para modelos
    "Base",
    "AuditMixin",
    "EnvironmentMixin",
    # Funciones públicas
    "init_db",
    "get_or_create",
]
