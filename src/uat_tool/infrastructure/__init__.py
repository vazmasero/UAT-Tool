"""
Paquete `infrastructure`

Contiene las implementaciones técnicas y acceso a recursos externos:

- Database: Configuración y conexión a base de datos
- Implementations: Implementaciones concretas de repositorios
- [Futuros]: APIs externas, sistemas de archivos, etc.

Esta capa contiene detalles de implementación que pueden variar
sin afectar al dominio de negocio.

Ejemplos de uso:
    from infrastructure.database import Session, init_db
    from infrastructure.implementations import SQLAlchemyBugRepository
"""

from .database import (
    DB_URL,
    AuditMixin,
    Base,
    EnvironmentMixin,
    Session,
    engine,
    init_db,
)

__all__ = [
    "AuditMixin",
    "Session",
    "engine",
    "init_db",
    "Base",
    "EnvironmentMixin",
    "DB_URL",
]
