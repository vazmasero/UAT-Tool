from .base import Base


def init_models(engine):
    """
    Crea todas las tablas definidas en los modelos asociados a Base.
    No hace drops ni inserta datos iniciales.
    Útil para tests rápidos o bootstrap.
    """
    Base.metadata.create_all(bind=engine)
