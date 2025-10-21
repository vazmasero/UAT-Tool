from sqlalchemy.orm import sessionmaker

from .base import Base
from .engine import get_engine


def init_db(drop_existing: bool = False, engine=None, load_initial_data: bool = True):
    """Inicializa la base de datos.

    Esta función crea la base de datos y todas las tablas definidas en los modelos y
    la pobla con los datos iniciales.

    Args:
        drop_existing (bool): Si True, elimina las tablas existentes primero
        engine: Motor de base de datos opcional (para testing)
        load_initial_data (bool): Si True, carga los datos iniciales.

    """
    actual_engine = engine or get_engine()

    if drop_existing:
        Base.metadata.drop_all(actual_engine)

    Base.metadata.create_all(actual_engine)

    SessionLocal = sessionmaker(
        bind=actual_engine, autoflush=False, autocommit=False, future=True
    )
    session = SessionLocal()

    try:
        if load_initial_data:
            from .initial_data import load_initial_data as load_data

            load_data(session)

        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

    return actual_engine  # Se devuelve el engine únicamente por si es útil en tests


if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada y poblada con datos iniciales.")
