from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from core.models import Requirement, Section, System

from .base import AuditEnvironmentMixinRepository


class RequirementRepository(AuditEnvironmentMixinRepository[Requirement]):
    """Repositorio especializado para el modelo Requirement."""

    def __init__(self, session: Session):
        super().__init__(session, Requirement)

    def _validate_related_objects(self, model_class, ids: list[int], error_message: str) -> list:
        """Valida que los objetos relacionados existan."""
        if not ids:
            return []
        
        objects = self.session.query(model_class).filter(model_class.id.in_(ids)).all()
        if len(objects) != len(ids):
            missing = set(ids) - {obj.id for obj in objects}
            raise ValueError(f"{error_message}: {missing}")
        return objects

    def create(self, data: dict, environment_id: int, modified_by: str) -> Requirement:
        """Crea un Requirement y lo asocia a sistemas y secciones"""
        system_ids = data.get("systems", [])
        section_ids = data.get("sections", [])

        if not system_ids:
            raise ValueError("Un requisito debe estar asociado a al menos un sistema.")
        if not section_ids:
            raise ValueError("Un requisito debe estar asociado a al menos una sección.")

        try:
            with self.session.begin_nested():
                # Validar objetos relacionados
                systems = self._validate_related_objects(
                    System, system_ids, "Sistemas no encontrados"
                )
                sections = self._validate_related_objects(
                    Section, section_ids, "Secciones no encontradas"
                )

                requirement = self.create_with_audit_env(data, environment_id, modified_by)

                # Establecer relaciones
                requirement.systems = systems
                requirement.sections = sections

                self.session.flush()
                return requirement

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_by_code(self, code: str, environment_id: int) -> Requirement | None:
        """Busca un requirement por su código único dentro del entorno."""
        return (
            self.query()
            .filter(
                Requirement.code == code, Requirement.environment_id == environment_id
            )
            .one_or_none()
        )

    def get_with_relations(
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

    def update(self, requirement_id: int, data: dict, environment_id: int, modified_by: str) -> Requirement:
        """Actualiza un requirement y sus relaciones."""
        requirement = self.get_by_id(requirement_id, raise_if_not_found=True)

        try:
            with self.session.begin_nested():
                # Actualizar campos básicos
                requirement = self.update_with_audit_env(requirement, data, modified_by)

                # Actualizar relaciones si se proporcionan
                if "systems" in data:
                    systems = self._validate_related_objects(
                        System, data["systems"], "Sistemas no encontrados"
                    )
                    requirement.systems = systems

                if "sections" in data:
                    sections = self._validate_related_objects(
                        Section, data["sections"], "Secciones no encontradas"
                    )
                    requirement.sections = sections

                self.session.flush()
                return requirement

        except SQLAlchemyError:
            self.session.rollback()
            raise
