from sqlalchemy.orm import sessionmaker

from .base import Base
from .engine import Session
from .engine import engine as default_engine


def init_db(drop_existing: bool = False, engine=None):
    """Inicializa la base de datos.

    Esta función crea la base de datos y todas las tablas definidas en los modelos y
    la pobla con los datos iniciales.

    Args:
        drop_existing: Si True, elimina las tablas existentes primero
        engine: Motor de base de datos opcional (para testing)

    """
    db_engine = engine if engine is not None else default_engine

    if drop_existing:
        Base.metadata.drop_all(db_engine)

    Base.metadata.create_all(db_engine)

    # Crear sesión apropiada según el engine
    if engine is not None:
        # Testing: crear una nueva sesión con el engine de test
        TestSession = sessionmaker(bind=engine)
        session = TestSession()
    else:
        # Producción: usar la sesión por defcto (scoped)
        session = Session()

    try:
        from .initial_data import load_initial_data

        load_initial_data(session)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada y poblada con datos iniciales.")
