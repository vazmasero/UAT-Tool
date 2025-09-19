from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from core.models import (
    Drone,
    Email,
    Operator,
    Reason,
    UasZone,
    UhubOrg,
    UhubUser,
    Uspace,
)

from .base import AuditEnvironmentMixinRepository, BaseRepository


class EmailRepository(BaseRepository[Email], AuditEnvironmentMixinRepository[Email]):
    def __init__(self, session: Session):
        super().__init__(session, Email)

    def create(self, **kwargs) -> Email:
        self._validate_audit_environment_data(kwargs)
        return super().create(**kwargs)

    def get_by_email(self, email: str, environment_id: int) -> Email | None:
        """Busca un email por dirección y environment_id."""
        return (
            self.query()
            .filter(Email.email == email, Email.environment_id == environment_id)
            .first()
        )


class OperatorRepository(
    BaseRepository[Operator], AuditEnvironmentMixinRepository[Operator]
):
    def __init__(self, session: Session):
        super().__init__(session, Operator)

    def create_with_relations(self, data: dict) -> Operator:
        self._validate_audit_environment_data(data)
        if "email_id" not in data:
            raise ValueError("Operator debe tener un email asociado (email_id).")
        return self.create(**data)

    def get_by_easa_id(self, easa_id: str, environment_id: int) -> Operator | None:
        """Busca un operador por EASA ID y environment_id."""
        return (
            self.query()
            .filter(
                Operator.easa_id == easa_id, Operator.environment_id == environment_id
            )
            .first()
        )


class DroneRepository(BaseRepository[Drone], AuditEnvironmentMixinRepository[Drone]):
    def __init__(self, session: Session):
        super().__init__(session, Drone)

    def create_with_operator(self, data: dict) -> Drone:
        self._validate_audit_environment_data(data)
        if "operator_id" not in data:
            raise ValueError("Un dron debe estar asociado a un operador (operator_id).")
        return self.create(**data)

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


class UhubOrgRepository(
    BaseRepository[UhubOrg], AuditEnvironmentMixinRepository[UhubOrg]
):
    def __init__(self, session: Session):
        super().__init__(session, UhubOrg)

    def create_with_relations(self, data: dict) -> UhubOrg:
        self._validate_audit_environment_data(data)

        return self.create(**data)

    def get_by_org_email(self, email: str, environment_id: int) -> UhubOrg | None:
        """Busca una organización por email y environment_id."""
        return (
            self.query()
            .filter(UhubOrg.email == email, UhubOrg.environment_id == environment_id)
            .first()
        )


class UhubUserRepository(
    BaseRepository[UhubUser], AuditEnvironmentMixinRepository[UhubUser]
):
    def __init__(self, session: Session):
        super().__init__(session, UhubUser)

    def create_with_org(self, data: dict) -> UhubUser:
        self._validate_audit_environment_data(data)
        if "organization_id" not in data:
            raise ValueError(
                "UhubUser debe estar asociado a una organización (organization_id)."
            )
        return self.create(**data)

    def get_by_username(self, username: str, environment_id: int) -> UhubUser | None:
        """Busca un usuario por username y environment_id."""
        return (
            self.query()
            .filter(
                UhubUser.username == username, UhubUser.environment_id == environment_id
            )
            .first()
        )


class UasZoneRepository(
    BaseRepository[UasZone], AuditEnvironmentMixinRepository[UasZone]
):
    def __init__(self, session: Session):
        super().__init__(session, UasZone)

    def create_with_relations(self, data: dict) -> UasZone:
        self._validate_audit_environment_data(data)

        required_fields = [
            "name",
            "area_type",
            "lower_limit",
            "upper_limit",
            "reference_lower",
            "reference_upper",
            "application",
            "restriction_type",
            "clearance_required",
        ]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para UasZone")

        try:
            # Crea la zona primero
            zone = self.create(**data)

            # Many-to-many relaciones opcionales
            if "organizations" in data:
                orgs = (
                    self.session.query(UhubOrg)
                    .filter(
                        UhubOrg.id.in_(data["organizations"]),
                        UhubOrg.environment_id == data["environment_id"],
                    )
                    .all()
                )
                zone.organizations = orgs

            if "reasons" in data:
                reasons = (
                    self.session.query(Reason)
                    .filter(Reason.id.in_(data["reasons"]))
                    .all()
                )
                zone.reasons = reasons

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


class UspaceRepository(BaseRepository[Uspace], AuditEnvironmentMixinRepository[Uspace]):
    def __init__(self, session: Session):
        super().__init__(session, Uspace)

    def create_with_file(self, data: dict) -> Uspace:
        """
        Crea un Uspace asociado a un file_id obligatorio.
        """
        self._validate_audit_environment_data(data)

        required_fields = ["code", "name", "sectors_count", "file_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para crear un Uspace")

        return self.create(**data)

    def get_by_code(self, code: str, environment_id: int) -> Uspace | None:
        """Busca un U-space por código y environment_id."""
        return (
            self.query()
            .filter(Uspace.code == code, Uspace.environment_id == environment_id)
            .first()
        )
