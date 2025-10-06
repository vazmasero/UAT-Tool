from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from uat_tool.domain import (
    Drone,
    Email,
    Operator,
    Reason,
    UasZone,
    UhubOrg,
    UhubUser,
    Uspace,
)

from .base import AuditEnvironmentMixinRepository


class EmailRepository(AuditEnvironmentMixinRepository[Email]):
    def __init__(self, session: Session):
        super().__init__(session, Email)

    def create(self, data: dict, environment_id: int, modified_by: str) -> Email:
        """Crea un email usando el método centralizado del mixin."""
        return self.create_with_audit_env(data, environment_id, modified_by)

    def get_by_email(self, email: str, environment_id: int) -> Email | None:
        """Busca un email por dirección y environment_id."""
        return (
            self.query()
            .filter(Email.email == email, Email.environment_id == environment_id)
            .first()
        )

    def update(
        self, email_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Operator:
        """Actualiza un operador."""
        email = self.get_by_id(email_id, raise_if_not_found=True)
        return self.update_with_audit_env(email, data, modified_by, environment_id)


class OperatorRepository(AuditEnvironmentMixinRepository[Operator]):
    def __init__(self, session: Session):
        super().__init__(session, Operator)

    def create(self, data: dict, environment_id: int, modified_by: str) -> Operator:
        """Crea operador validando email_id."""
        if not data.get("email_id"):
            raise ValueError("Operator debe tener un email asociado (email_id).")

        return self.create_with_audit_env(data, environment_id, modified_by)

    def get_by_easa_id(self, easa_id: str, environment_id: int) -> Operator | None:
        """Busca un operador por EASA ID y environment_id."""
        return (
            self.query()
            .filter(
                Operator.easa_id == easa_id, Operator.environment_id == environment_id
            )
            .first()
        )

    def update(
        self, operator_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Operator:
        """Actualiza un operador."""
        operator = self.get_by_id(operator_id, raise_if_not_found=True)
        return self.update_with_audit_env(operator, data, modified_by, environment_id)


class DroneRepository(AuditEnvironmentMixinRepository[Drone]):
    def __init__(self, session: Session):
        super().__init__(session, Drone)

    def create(self, data: dict, environment_id: int, modified_by: str) -> Drone:
        """Crea dron validando operator_id."""
        if not data.get("operator_id"):
            raise ValueError("Un dron debe estar asociado a un operador (operator_id).")

        return self.create_with_audit_env(data, environment_id, modified_by)

    def get_by_serial_number(
        self, serial_number: str, environment_id: int
    ) -> Drone | None:
        """Busca un dron por número de serie y environment_id."""
        return (
            self.query()
            .filter(
                Drone.serial_number == serial_number,
                Drone.environment_id == environment_id,
            )
            .first()
        )

    def update(
        self, drone_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Drone:
        """Actualiza un dron."""
        drone = self.get_by_id(drone_id, raise_if_not_found=True)
        return self.update_with_audit_env(drone, data, modified_by, environment_id)


class UhubOrgRepository(AuditEnvironmentMixinRepository[UhubOrg]):
    def __init__(self, session: Session):
        super().__init__(session, UhubOrg)

    def create(self, data: dict, environment_id: int, modified_by: str) -> UhubOrg:
        """Crea organización usando método centralizado."""
        return self.create_with_audit_env(data, environment_id, modified_by)

    def get_by_org_email(self, email: str, environment_id: int) -> UhubOrg | None:
        """Busca una organización por email y environment_id."""
        return (
            self.query()
            .filter(UhubOrg.email == email, UhubOrg.environment_id == environment_id)
            .first()
        )

    def update(
        self, org_id: int, data: dict, environment_id: int, modified_by: str
    ) -> UhubUser:
        """Actualiza un usuario Uhub."""
        org = self.get_by_id(org_id, raise_if_not_found=True)
        return self.update_with_audit_env(org, data, modified_by, environment_id)


class UhubUserRepository(AuditEnvironmentMixinRepository[UhubUser]):
    def __init__(self, session: Session):
        super().__init__(session, UhubUser)

    def create(self, data: dict, environment_id: int, modified_by: str) -> UhubUser:
        """Crea usuario validando organization_id."""
        if not data.get("organization_id"):
            raise ValueError(
                "UhubUser debe estar asociado a una organización (organization_id)."
            )

        return self.create_with_audit_env(data, environment_id, modified_by)

    def get_by_username(self, username: str, environment_id: int) -> UhubUser | None:
        """Busca un usuario por username y environment_id."""
        return (
            self.query()
            .filter(
                UhubUser.username == username, UhubUser.environment_id == environment_id
            )
            .first()
        )

    def update(
        self, user_id: int, data: dict, environment_id: int, modified_by: str
    ) -> UhubUser:
        """Actualiza un usuario Uhub."""
        user = self.get_by_id(user_id, raise_if_not_found=True)
        return self.update_with_audit_env(user, data, modified_by, environment_id)


class UasZoneRepository(AuditEnvironmentMixinRepository[UasZone]):
    def __init__(self, session: Session):
        super().__init__(session, UasZone)

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

    def create(self, data: dict, environment_id: int, modified_by: str) -> UasZone:
        """Crea zona UAS con relaciones."""
        try:
            # Configuración de relaciones
            relations_config = {
                "organizations": (
                    UhubOrg,
                    "organizations",
                    "Organizaciones no encontradas",
                ),
                "reasons": (Reason, "reasons", "Razones no encontradas"),
            }

            # Extraer relaciones antes de crear la instancia
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, [])

            # Usar transacción para operación atómica
            with self.session.begin_nested():
                # Crear zona base
                zone = self.create_with_audit_env(data, environment_id, modified_by)

                # Manejar relaciones many-to-many
                for relation_key, (
                    model_class,
                    attr_name,
                    error_msg,
                ) in relations_config.items():
                    ids = extracted_relations[relation_key]
                    if ids:
                        objects = self._validate_related_objects(
                            model_class, ids, error_msg
                        )
                        setattr(zone, attr_name, objects)

                self.session.flush()
                return zone

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def get_by_zone_name(self, name: str, environment_id: int) -> UasZone | None:
        """Busca una zona UAS por nombre y environment_id."""
        return (
            self.query()
            .filter(UasZone.name == name, UasZone.environment_id == environment_id)
            .first()
        )

    def update(
        self, zone_id: int, data: dict, environment_id: int, modified_by: str
    ) -> UasZone:
        """Actualiza una zona UAS con relaciones."""
        try:
            zone = self.get_by_id(zone_id, raise_if_not_found=True)

            # Configuración de relaciones
            relations_config = {
                "organizations": (
                    UhubOrg,
                    "organizations",
                    "Organizaciones no encontradas",
                ),
                "reasons": (Reason, "reasons", "Razones no encontradas"),
            }

            # Extraer relaciones primero
            extracted_relations = {}
            for relation_key in relations_config.keys():
                extracted_relations[relation_key] = data.pop(relation_key, None)

            with self.session.begin_nested():
                # Actualizar campos básicos
                zone = self.update_with_audit_env(
                    zone, data, modified_by, environment_id
                )

                # Actualizar relaciones si se proporcionan
                for relation_key, (
                    model_class,
                    attr_name,
                    error_msg,
                ) in relations_config.items():
                    ids = extracted_relations[relation_key]
                    if ids is not None:
                        objects = self._validate_related_objects(
                            model_class, ids, error_msg
                        )
                        setattr(zone, attr_name, objects)

                self.session.flush()
                return zone

        except SQLAlchemyError:
            self.session.rollback()
            raise


class UspaceRepository(AuditEnvironmentMixinRepository[Uspace]):
    def __init__(self, session: Session):
        super().__init__(session, Uspace)

    def create(self, data: dict, environment_id: int, modified_by: str) -> Uspace:
        """Crea Uspace validando file_id."""
        if not data.get("file_id"):
            raise ValueError("file_id es obligatorio para crear un Uspace")

        return self.create_with_audit_env(data, environment_id, modified_by)

    def get_by_code(self, code: str, environment_id: int) -> Uspace | None:
        """Busca un U-space por código y environment_id."""
        return (
            self.query()
            .filter(Uspace.code == code, Uspace.environment_id == environment_id)
            .first()
        )

    def update(
        self, uspace_id: int, data: dict, environment_id: int, modified_by: str
    ) -> Uspace:
        """Actualiza un Uspace."""
        uspace = self.get_by_id(uspace_id, raise_if_not_found=True)
        return self.update_with_audit_env(uspace, data, modified_by, environment_id)
