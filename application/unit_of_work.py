from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import Session as SQLAlchemySession
from sqlalchemy.orm import scoped_session

from data.database.engine import Session
from data.repositories import BugRepository  # falta añadir todos los repositorios


class UnitOfWork:
    """Unidad de trabajo que agrupa todos los repositorios para transacciones
    atómicas.
    """

    def __init__(self, session: SQLAlchemySession | scoped_session):
        self.session = session
        self.bug_repo = BugRepository(session)
        # Añadir otros repositorios aquí

    def commit(self):
        """Confirma todas las operaciones pendientes."""
        self.session.commit()

    def rollback(self):
        """Revierte todas las operaciones pendientes."""
        self.session.rollback()

    def close(self):
        """Cierra la sesión de forma segura para ambos tipos (scoped o no)."""
        try:
            if hasattr(self.session, 'close'):
                self.session.close()
            elif hasattr(self.session, 'remove'):
                self.session.remove()
        except Exception as e:
            print(f"Error cerrando sesión: {e}")


@contextmanager
def unit_of_work() -> Generator[UnitOfWork, None, None]:
    """Context manager para manejar la unidad de trabajo.

    Usage:
    with unit_of_work() as uow:
        uow.bug_repo.create(...)
        # Commit automático al salir si no hay erorres
    """
    session = Session()
    uow = UnitOfWork(session)
    try:
        yield uow
        uow.commit()

    except Exception:
        uow.rollback()
        raise
    finally:
        uow.close()
