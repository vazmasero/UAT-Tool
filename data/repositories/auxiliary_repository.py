from sqlalchemy.orm import Session, joinedload

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
            Environment | None: entidad del entorno solicitado.
        """

        results = self.filter_by(name=name)
        return results[0] if results else None

    def get_with_relationships(self, environment_id: int) -> Environment | None:
        """Obtiene un entorno con todas sus relaciones cargadas."""
        return (
            self.session.query(Environment)
            .options(
                joinedload(Environment.environment_bugs),
                joinedload(Environment.environment_campaign_runs),
                joinedload(Environment.environment_campaigns),
            )
            .filter(Environment.id == environment_id)
            .first()
        )


class SystemRepository(BaseRepository[System]):
    """Repositorio para la entidad System."""

    def __init__(self, session: Session):
        super().__init__(session, System)

    def get_by_name(self, name: str) -> System | None:
        """Busca un sistema por su nombre.

        Args:
            name (str): nombre del sistema a buscar

        Returns:
            System | None: entidad del sistema solicitado.
        """
        return self.session.query(System).filter(System.name == name).first()


class SectionRepository(BaseRepository[Section]):
    """Repositorio para la entidad Section."""

    def __init__(self, session: Session):
        super().__init__(session, Section)

    def get_by_name(self, name: str) -> Section | None:
        """Busca una sección por su nombre.

        Args:
            name (str): nombre de la sección a buscar

        Returns:
            Section | None: entidad de la sección solicitada.
        """
        return self.session.query(Section).filter(Section.name == name).first()


class FileRepository(BaseRepository[File]):
    """Repositorio para la entidad File."""

    def __init__(self, session: Session):
        super().__init__(session, File)

    def get_by_filename(self, filename: str) -> File | None:
        """Busca un archivo por su nombre.

        Args:
            name (str): nombre del archivo a buscar

        Returns:
            File | None: entidad del archivo solicitada.
        """
        return self.session.query(File).filter(File.filename == filename).first()


class ReasonRepository(BaseRepository[Reason]):
    """Repositorio para la entidad Reason."""

    def __init__(self, session: Session):
        super().__init__(session, Reason)

    def get_by_name(self, name: str) -> Reason | None:
        """Busca una razón por su nombre.

        Args:
            name (str): nombre de la razón a buscar

        Returns:
            Reason | None: entidad de la razón solicitada.
        """
        return self.session.query(Reason).filter(Reason.name == name).first()
