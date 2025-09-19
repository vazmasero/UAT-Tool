from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.models import Requirement, Section, System

from .base import AuditEnvironmentMixinRepository, BaseRepository


class RequirementRepository(
    BaseRepository[Requirement], AuditEnvironmentMixinRepository[Requirement]
):
    """Repositorio especializado para el modelo Requirement."""

    def __init__(self, session: Session):
        super().__init__(session, Requirement)

    def create_with_relations(self, data: dict) -> Requirement:
        """Crea un Requirement y lo asocia a sistemas y secciones"""
        self._validate_audit_environment_data(data)
        system_ids = data.get("systems", [])
        section_ids = data.get("sections", [])

        if not system_ids:
            raise ValueError("Un requisito debe estar asociado a al menos un sistema.")
        if not section_ids:
            raise ValueError("Un requisito debe estar asociado a al menos una sección.")

        try:
            # Crear el requisito usando el método base
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
            self.query()
            .filter(
                Requirement.code == code, Requirement.environment_id == environment_id
            )
            .one_or_none()
        )

    def get_requirements_with_relations(
        self, requirement_id: int
    ) -> Requirement | None:
        """Obtiene un requisito con sus relaciones cargadas."""
        return (
            self.query()
            .options(
                joinedload(Requirement.bugs),
            )
            .filter(Requirement.id == requirement_id)
            .first()
        )

    def update_with_relations(self, requirement_id: int, data: dict) -> Requirement:
        """Actualiza un requirement y sus relaciones."""
        self._validate_audit_environment_data(data)

        requirement = self.get_by_id(requirement_id, raise_if_not_found=True)

        # Actualizar campos básicos
        if "code" in data:
            requirement.code = data["code"]
        if "definition" in data:
            requirement.definition = data["definition"]
        if "modified_by" in data:
            requirement.modified_by = data["modified_by"]

        # Actualizar relaciones si se proporcionan
        if "systems" in data:
            systems = (
                self.session.query(System).filter(System.id.in_(data["systems"])).all()
            )
            requirement.systems = systems

        if "sections" in data:
            sections = (
                self.session.query(Section)
                .filter(Section.id.in_(data["sections"]))
                .all()
            )
            requirement.sections = sections

        self.session.flush()
        return requirement
