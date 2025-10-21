from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_NAME = "uat_tool.db"
_DEFAULT_DATABASE_URL = f"sqlite:///{DB_NAME}"

_engine = None


def get_engine(database_url: str = None, echo: bool = False):
    """Devuelve el engine global (o crea uno nuevo si no existe)."""
    global _engine
    if _engine is None:
        _engine = create_engine(
            database_url or _DEFAULT_DATABASE_URL, echo=echo, future=True
        )
    return _engine


def get_session_factory(engine=None, scoped: bool = True):
    """Devuelve la sesión scoped o normal ligada a un engine."""
    engine = engine or get_engine()
    factory = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    if scoped:
        return scoped_session(factory)
    return factory
