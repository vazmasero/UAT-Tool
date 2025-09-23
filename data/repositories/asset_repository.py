from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from core.models import Drone, Email, Operator, Reason, UasZone, UhubOrg, UhubUser, Uspace
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


class UhubUserRepository(AuditEnvironmentMixinRepository[UhubUser]):
    def __init__(self, session: Session):
        super().__init__(session, UhubUser)

    def create(self, data: dict, environment_id: int, modified_by: str) -> UhubUser:
        """Crea usuario validando organization_id."""
        if not data.get("organization_id"):
            raise ValueError("UhubUser debe estar asociado a una organización (organization_id).")
        
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


class UasZoneRepository(AuditEnvironmentMixinRepository[UasZone]):
    def __init__(self, session: Session):
        super().__init__(session, UasZone)

    def _validate_related_objects(self, model_class, ids: list[int], error_message: str) -> list:
        """Valida que los objetos relacionados existan."""
        if not ids:
            return []
        
        objects = self.query(model_class).filter(model_class.id.in_(ids)).all()
        if len(objects) != len(ids):
            missing = set(ids) - {obj.id for obj in objects}
            raise ValueError(f"{error_message}: {missing}")
        return objects

    def create(self, data: dict, environment_id: int, modified_by: str) -> UasZone:
        """Crea zona UAS con relaciones."""
        try:
            # Usar transacción para operación atómica
            with self.session.begin_nested():
                # Crear zona base 
                zone = self.create_with_audit_env(data, environment_id, modified_by)

                # Manejar relaciones many-to-many
                if "organizations" in data:
                    orgs = self._validate_related_objects(
                        UhubOrg, data["organizations"], "Organizaciones no encontradas"
                    )
                    zone.organizations = orgs

                if "reasons" in data:
                    reasons = self._validate_related_objects(
                        Reason, data["reasons"], "Razones no encontradas"
                    )
                    zone.reasons = reasons

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
