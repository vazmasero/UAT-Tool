"""
Paquete `infrastructure.database`

Contiene la configuración y acceso a base de datos:

- Engine: Configuración del motor de base de datos
- Base: Clase base para todos los modelos SQLAlchemy
- InitDB: Utilidades para inicialización de base de datos
- Session: Gestión de sesiones de base de datos

Configuración centralizada para PostgreSQL + SQLAlchemy.
"""

from .base import AuditMixin, Base, EnvironmentMixin
from .engine import DB_URL, Session, engine
from .init_db import init_db
from .utils import get_or_create

__all__ = [
    "AuditMixin",
    "EnvironmentMixin",
    "Base",
    "Session",
    "engine",
    "init_db",
    "get_or_create",
    "DB_URL",
]
