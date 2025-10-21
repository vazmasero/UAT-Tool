"""
Paquete `infrastructure`

Proporciona acceso a la capa de infraestructura:
- Configuración de base de datos
- Sesiones y motor SQLAlchemy
- Utilidades de persistencia
- [Futuros]: APIs externas, sistemas de archivos, etc.
"""

from .database import (
    AuditMixin,
    Base,
    EnvironmentMixin,
    get_engine,
    get_or_create,
    get_session_factory,
    init_db,
)

__all__ = [
    # Configuración BD
    "get_engine",
    "get_session_factory",
    "Session",
    # Base y Mixins para modelos
    "Base",
    "AuditMixin",
    "EnvironmentMixin",
    # Funciones públicas
    "init_db",
    "get_or_create",
]
