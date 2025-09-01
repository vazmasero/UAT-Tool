
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

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

    instance = model(**kwargs)
    session.add(instance)
    try: 
        session.commit()
        return instance, True
    except IntegrityError:
        session.rollback()
        instance = session.query(model).filter_by(**kwargs).one()
        return instance, False