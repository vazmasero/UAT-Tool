from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from uat_tool.domain import Requirement, Section, System

from .base import AuditEnvironmentMixinRepository


class RequirementRepository(AuditEnvironmentMixinRepository[Requirement]):
    """Repositorio especializado para el modelo Requirement."""

    def __init__(self, session: Session):
        super().__init__(session, Requirement)

    def _validate_related_objects(
        self, model_class, ids: list[int], error_message: str
    ) -> list:
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
        try:
            # Separar relaciones antes de crear la instancia
            system_ids = data.pop("systems", [])
            section_ids = data.pop("sections", [])

            with self.session.begin_nested():
                requirement = self.create_with_audit_env(
                    data, environment_id, modified_by
                )

                # Manejar relaciones many-to-many
                if system_ids:
                    systems = self._validate_related_objects(
                        System, system_ids, "Sistemas no encontrados"
                    )
                    requirement.systems = systems
                else:
                    raise ValueError(
                        "Un requisito debe estar asociado a al menos un sistema."
                    )

                if section_ids:
                    sections = self._validate_related_objects(
                        Section, section_ids, "Secciones no encontradas"
                    )
                    requirement.sections = sections
                else:
                    raise ValueError(
                        "Un requisito debe estar asociado a al menos una sección."
                    )

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

    def get_with_relations(self, requirement_id: int) -> Requirement | None:
        """Obtiene un requisito con sus relaciones cargadas."""
        return (
            self.query()
            .options(
                joinedload(Requirement.bugs),
                joinedload(Requirement.systems),
                joinedload(Requirement.sections),
            )
            .filter(Requirement.id == requirement_id)
            .first()
        )

    def get_all_with_relations(self) -> list[Requirement]:
        """Obtiene todos los requisitos con sistemas y secciones cargadas."""
        return (
            self.query()
            .options(
                joinedload(Requirement.systems),
                joinedload(Requirement.sections),
                joinedload(Requirement.bugs),
            )
            .all()
        )

    def update(
        self, requirement_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Requirement:
        """Actualiza un requirement y sus relaciones."""

        try:
            requirement = self.get_by_id(requirement_id, raise_if_not_found=True)

            # Separar relaciones antes de crear la instancia
            system_ids = data.pop("systems", [])
            section_ids = data.pop("sections", [])

            with self.session.begin_nested():
                # Actualizar campos básicos
                requirement = self.update_with_audit_env(
                    requirement, data, modified_by, environment_id
                )

                # Manejar relaciones many-to-many
                if system_ids:
                    systems = self._validate_related_objects(
                        System, system_ids, "Sistemas no encontrados"
                    )
                    requirement.systems = systems
                else:
                    raise ValueError(
                        "Un requisito debe estar asociado a al menos un sistema."
                    )

                if section_ids:
                    sections = self._validate_related_objects(
                        Section, section_ids, "Secciones no encontradas"
                    )
                    requirement.sections = sections
                else:
                    raise ValueError(
                        "Un requisito debe estar asociado a al menos una sección."
                    )

                self.session.flush()
                return requirement

        except SQLAlchemyError:
            self.session.rollback()
            raise
