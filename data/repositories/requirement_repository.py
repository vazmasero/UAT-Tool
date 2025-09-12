from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from core.models import Requirement, Section, System

from .base import BaseRepository, EnvironmentMixinRepository


class RequirementRepository(BaseRepository[Requirement], EnvironmentMixinRepository[Requirement]):
    """Repositorio especializado para el modelo Requirement."""

    def __init__(self, session: Session):
        super().__init__(session, Requirement)
        EnvironmentMixinRepository.__init__(session, Requirement)

    def create_with_relations(self, data: dict) -> Requirement:
        """Crea un Requirement y lo asocia a sistemas y secciones"""
        self._validate_environment_data(data)
        system_ids = data.get("systems", [])
        section_ids = data.get("sections", [])

        if not system_ids:
            raise ValueError("Un Requirement debe estar asociado a al menos un sistema.")
        if not section_ids:
            raise ValueError(
                "Un Requirement debe estar asociado a al menos una sección."
            )

        try:
            # Crear el requirement usando el método base
            requirement_data = {
                "code": data["code"],
                "definition": data["definition"],
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],

            }
            requirement = self.create(**requirement_data)

            # Relaciones obligatorias
            systems = self.session.query(System).filter(System.id.in_(system_ids)).all()
            sections = (
                self.session.query(Section).filter(Section.id.in_(section_ids)).all()
            )

            if len(systems) != len(system_ids):
                missing = set(system_ids) - {s.id for s in systems}
                raise ValueError(f"Sistemas no encontrados: {missing}")
            if len(sections) != len(section_ids):
                missing = set(section_ids) - {s.id for s in sections}
                raise ValueError(f"Secciones no encontradas: {missing}")

            requirement.systems = systems
            requirement.sections = sections

            self.session.flush()
            return requirement

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def find_by_code(self, code: str, environment_id: int) -> Requirement | None:
        """Busca un requirement por su código único dentro del entorno."""
        return (
            self.session.query(Requirement)
            .filter(Requirement.code == code, Requirement.environment_id == environment_id)
            .one_or_none()
        )
