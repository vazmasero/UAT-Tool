from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def get_or_create(session: Session, model, **kwargs):
    """Helper genérico para obtener o crear un registro en la base de datos
    de forma segura en entornos concurrentes.

    Args:
        session: instancia de SQLAlchemy Session
        model: clase del modelo
        **kwargs campos a buscar o crear

    Returns:
        instance: el objeto existente o recién creado
        created: True si se creó, False si ya existía
    """
    try:
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False

        instance = model(**kwargs)
        session.add(instance)
        session.flush()
        return instance, True

    except IntegrityError:
        session.rollback()
        instance = session.query(model).filter_by(**kwargs).first()
        if not instance:
            raise
        return instance, False
