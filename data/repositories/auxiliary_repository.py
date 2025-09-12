from sqlalchemy.orm import Session

from core.models import Environment, File, Reason, Section, System

from .base import BaseRepository


class EnvironmentRepository(BaseRepository[Environment]):
    """Repositorio para la entidad Environment."""

    def __init__(self, session: Session):
        super().__init__(session, Environment)

    def get_by_name(self, name: str) -> Environment | None:
        """Busca un entorno por su nombre.

        Args:
            name (str): nombre del entorno que se quiere obtener

        Returns:
            System | None: entidad del entorno solicitado.
        """

        return self.session.query(Environment).filter(Environment.name == name).first()


class SystemRepository(BaseRepository[System]):
    """Repositorio para la entidad System."""

    def __init__(self, session: Session):
        super().__init__(session, System)

    def get_by_name(self, name: str) -> System | None:
        """Busca un sistema por su nombre."""
        return self.session.query(System).filter(System.name == name).first()


class SectionRepository(BaseRepository[Section]):
    """Repositorio para la entidad Section."""

    def __init__(self, session: Session):
        super().__init__(session, Section)

    def get_by_name(self, name: str) -> Section | None:
        """Busca una sección por su nombre."""
        return self.session.query(Section).filter(Section.name == name).first()


class FileRepository(BaseRepository[File]):
    """Repositorio para la entidad File."""

    def __init__(self, session: Session):
        super().__init__(session, File)

    def get_by_filename(self, filename: str) -> File | None:
        """Busca un archivo por su nombre."""
        return self.session.query(File).filter(File.filename == filename).first()


class ReasonRepository(BaseRepository[Reason]):
    """Repositorio para la entidad Reason."""

    def __init__(self, session: Session):
        super().__init__(session, Reason)

    def get_by_name(self, name: str) -> Reason | None:
        """Busca una razón por su nombre."""
        return self.session.query(Reason).filter(Reason.name == name).first()
