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

from .base import BaseRepository, EnvironmentMixinRepository


class EmailRepository(BaseRepository[Email], EnvironmentMixinRepository[Email]):
    def __init__(self, session: Session):
        super().__init__(session, Email)
        EnvironmentMixinRepository.__init__(session, Email)

    def create(self, **kwargs) -> Email:
        self._validate_environment_data(kwargs)
        return super().create(**kwargs)


class OperatorRepository(
    BaseRepository[Operator], EnvironmentMixinRepository[Operator]
):
    def __init__(self, session: Session):
        super().__init__(session, Operator)
        EnvironmentMixinRepository.__init__(session, Operator)

    def create_with_relations(self, data: dict) -> Operator:
        self._validate_environment_data(data)
        if "email_id" not in data:
            raise ValueError("Operator debe tener un email asociado (email_id).")

        operator_data = {
            "name": data["name"],
            "surname": data.get("surname"),
            "email_id": data["email_id"],
            "environment_id": data["environment_id"],
            "modified_by": data["modified_by"],
        }
        return self.create(**operator_data)


class DroneRepository(BaseRepository[Drone], EnvironmentMixinRepository[Drone]):
    def __init__(self, session: Session):
        super().__init__(session, Drone)
        EnvironmentMixinRepository.__init__(session, Drone)

    def create_with_operator(self, data: dict) -> Drone:
        self._validate_environment_data(data)
        if "operator_id" not in data:
            raise ValueError("Drone debe estar asociado a un operador (operator_id).")

        drone_data = {
            "name": data["name"],
            "model": data.get("model"),
            "serial_number": data.get("serial_number"),
            "operator_id": data["operator_id"],
            "environment_id": data["environment_id"],
            "modified_by": data["modified_by"],
        }
        return self.create(**drone_data)


class UhubOrgRepository(BaseRepository[UhubOrg], EnvironmentMixinRepository[UhubOrg]):
    def __init__(self, session: Session):
        super().__init__(session, UhubOrg)
        EnvironmentMixinRepository.__init__(session, UhubOrg)

    def create_with_relations(self, data: dict) -> UhubOrg:
        self._validate_environment_data(data)

        org_data = {
            "name": data["name"],
            "description": data.get("description"),
            "environment_id": data["environment_id"],
            "modified_by": data["modified_by"],
        }
        return self.create(**org_data)


class UhubUserRepository(
    BaseRepository[UhubUser], EnvironmentMixinRepository[UhubUser]
):
    def __init__(self, session: Session):
        super().__init__(session, UhubUser)
        EnvironmentMixinRepository.__init__(session, UhubUser)

    def create_with_org(self, data: dict) -> UhubUser:
        self._validate_environment_data(data)
        if "organization_id" not in data:
            raise ValueError(
                "UhubUser debe estar asociado a una organización (organization_id)."
            )

        user_data = {
            "name": data["name"],
            "surname": data.get("surname"),
            "email": data["email"],
            "organization_id": data["organization_id"],
            "environment_id": data["environment_id"],
            "modified_by": data["modified_by"],
        }
        return self.create(**user_data)


class UasZoneRepository(BaseRepository[UasZone], EnvironmentMixinRepository[UasZone]):
    def __init__(self, session: Session):
        super().__init__(session, UasZone)
        EnvironmentMixinRepository.__init__(session, UasZone)

    def create_with_relations(self, data: dict) -> UasZone:
        self._validate_environment_data(data)

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
            zone_data = {
                "name": data["name"],
                "area_type": data["area_type"],
                "lower_limit": data["lower_limit"],
                "upper_limit": data["upper_limit"],
                "reference_lower": data["reference_lower"],
                "reference_upper": data["reference_upper"],
                "application": data["application"],
                "restriction_type": data["restriction_type"],
                "clearance_required": data["clearance_required"],
                "comments": data.get("comments"),
                "environment_id": data["environment_id"],
                "modified_by": data["modified_by"],
            }
            zone = self.create(**zone_data)

            # Many-to-many relaciones opcionales
            if "organizations" in data:
                orgs = (
                    self.session.query(UhubOrg)
                    .filter(UhubOrg.id.in_(data["organizations"]))
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


class UspaceRepository(BaseRepository[Uspace], EnvironmentMixinRepository[Uspace]):
    def __init__(self, session: Session):
        super().__init__(session, Uspace)
        EnvironmentMixinRepository.__init__(session, Uspace)

    def create_with_file(self, data: dict) -> Uspace:
        """
        Crea un Uspace asociado a un file_id obligatorio.
        """
        self._validate_environment_data(data)

        required_fields = ["code", "name", "sectors_count", "file_id"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} es obligatorio para crear un Uspace")

        uspace_data = {
            "code": data["code"],
            "name": data["name"],
            "sectors_count": data["sectors_count"],
            "file_id": data["file_id"],
            "comments": data.get("comments"),
            "environment_id": data["environment_id"],
            "modified_by": data["modified_by"],
        }
        return self.create(**uspace_data)
