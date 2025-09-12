from . import Base
from .engine import Session, engine
from .initial_data import load_initial_data


def init_db(drop_existing: bool = False):
    """Inicializa la base de datos.

    Esta función crea la base de datos y todas las tablas definidas en los modelos y
    la pobla con los datos iniciales.

    """
    if drop_existing:
        Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)

    session = Session()
    try:
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
