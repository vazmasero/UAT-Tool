from uat_tool.domain import (
    DroneRepository,
    EmailRepository,
    FileRepository,
    OperatorRepository,
    ReasonRepository,
    UasZoneRepository,
    UhubOrgRepository,
    UhubUserRepository,
    UspaceRepository,
)


def test_email_repository_create(db_session, model_test_data, sample_audit_data):
    """Test EmailRepository.create"""
    repo = EmailRepository(db_session)

    email = repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    assert email.id is not None
    assert email.name == "Test Email"
    assert email.email == "test@example.com"
    assert email.password == "password123"
    assert email.modified_by == "test_user"
    assert email.created_at is not None
    assert email.updated_at is not None
    assert email.environment_id == 1


def test_email_repository_get_by_email(db_session, model_test_data, sample_audit_data):
    """Test EmailRepository.get_by_email"""
    repo = EmailRepository(db_session)

    email = repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Buscar por email
    found = repo.get_by_email("test@example.com", 1)

    assert found is not None
    assert found.id == email.id
    assert found.email == "test@example.com"


def test_email_repository_update(db_session, model_test_data, sample_audit_data):
    """Test EmailRepository.update"""
    repo = EmailRepository(db_session)

    email = repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Actualizar el email
    update_data = {
        "name": "Updated Email",
        "password": "newpassword456",
    }

    updated_email = repo.update(
        email.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_email.id == email.id
    assert updated_email.name == "Updated Email"
    assert updated_email.password == "newpassword456"
    assert updated_email.modified_by == "updated_user"
    assert updated_email.email == "test@example.com"


def test_operator_repository_create(db_session, model_test_data, sample_audit_data):
    """Test OperatorRepository.create"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)

    email = email_repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    repo = OperatorRepository(db_session)

    operator_data = {
        **model_test_data["operator_data"],
        "email_id": email.id,
    }
    operator = repo.create(
        operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert operator.id is not None
    assert operator.name == "Test Operator"
    assert operator.easa_id == "EASA123"
    assert operator.email_id == email.id


def test_operator_repository_get_by_easa_id(
    db_session, model_test_data, sample_audit_data
):
    """Test OperatorRepository.get_by_easa_id"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)

    email = email_repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    repo = OperatorRepository(db_session)

    operator_data = {
        **model_test_data["operator_data"],
        "email_id": email.id,
    }

    operator = repo.create(
        operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por EASA ID
    found = repo.get_by_easa_id("EASA123", 1)

    assert found is not None
    assert found.id == operator.id
    assert found.easa_id == "EASA123"


def test_operator_repository_update(db_session, model_test_data, sample_audit_data):
    """Test OperatorRepository.update"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)
    email = email_repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    repo = OperatorRepository(db_session)

    operator_data = {
        **model_test_data["operator_data"],
        "email_id": email.id,
    }
    operator = repo.create(
        operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Actualizar el operador
    update_data = {
        "name": "Updated Operator",
        "phone": "+987654321",
        "verification_code": "UPDATED123",
    }

    updated_operator = repo.update(
        operator.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_operator.id == operator.id
    assert updated_operator.name == "Updated Operator"
    assert updated_operator.phone == "+987654321"
    assert updated_operator.verification_code == "UPDATED123"
    assert updated_operator.modified_by == "updated_user"
    assert updated_operator.easa_id == "EASA123"


def test_drone_repository_create(db_session, model_test_data, sample_audit_data):
    """Test DroneRepository.create"""
    # Primero crear un operador
    ope_repo = OperatorRepository(db_session)

    ope_data = {
        **model_test_data["operator_data"],
        "email_id": 1,
    }
    operator = ope_repo.create(
        ope_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    repo = DroneRepository(db_session)

    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }

    drone = repo.create(
        drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert drone.id is not None
    assert drone.name == "Test Drone"
    assert drone.serial_number == "DRONE123"
    assert drone.operator_id == operator.id


def test_drone_repository_get_by_serial_number(
    db_session, model_test_data, sample_audit_data
):
    """Test DroneRepository.get_by_serial_number"""
    # Primero crear un operador
    ope_repo = OperatorRepository(db_session)

    ope_data = {
        **model_test_data["operator_data"],
        "email_id": 1,
    }
    operator = ope_repo.create(
        ope_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    repo = DroneRepository(db_session)

    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }

    drone = repo.create(
        drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por número de serie
    found = repo.get_by_serial_number("DRONE123", 1)

    assert found is not None
    assert found.id == drone.id
    assert found.serial_number == "DRONE123"


def test_drone_repository_update(db_session, model_test_data, sample_audit_data):
    """Test DroneRepository.update"""
    # Primero crear un operador
    ope_repo = OperatorRepository(db_session)

    # Primero crear email para el operador
    email_repo = EmailRepository(db_session)
    email = email_repo.create(
        model_test_data["email_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    ope_data = {
        **model_test_data["operator_data"],
        "email_id": email.id,
    }
    operator = ope_repo.create(
        ope_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    repo = DroneRepository(db_session)

    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }

    drone = repo.create(
        drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Actualizar el dron
    update_data = {
        "name": "Updated Drone",
        "manufacturer": "Updated Manufacturer",
        "model": "Updated Model",
    }

    updated_drone = repo.update(
        drone.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_drone.id == drone.id
    assert updated_drone.name == "Updated Drone"
    assert updated_drone.manufacturer == "Updated Manufacturer"
    assert updated_drone.model == "Updated Model"
    assert updated_drone.modified_by == "updated_user"
    assert updated_drone.serial_number == "DRONE123"


def test_uhub_org_repository_create(db_session, model_test_data, sample_audit_data):
    """Test EmailRepository.create"""
    repo = UhubOrgRepository(db_session)

    org = repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    assert org.id is not None
    assert org.name == "Test Org"
    assert org.email == "org@example.com"
    assert org.phone == "+987654321"
    assert org.modified_by == "test_user"
    assert org.type == "OPERATIVE"
    assert org.created_at is not None
    assert org.updated_at is not None
    assert org.environment_id == 1


def test_uhub_org_repository_get_by_org_email(
    db_session, model_test_data, sample_audit_data
):
    """Test UhubOrgRepository.get_by_org_email"""
    repo = UhubOrgRepository(db_session)

    org = repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Buscar por email
    found = repo.get_by_org_email("org@example.com", 1)

    assert found is not None
    assert found.id == org.id
    assert found.email == "org@example.com"


def test_uhub_org_repository_update(db_session, model_test_data, sample_audit_data):
    """Test UhubOrgRepository.update"""
    repo = UhubOrgRepository(db_session)

    org = repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Actualizar la organización
    update_data = {
        "name": "Updated Org",
        "phone": "+111111111",
        "role": "Updated Role",
        "type": "ADMINISTRATIVE",
    }

    updated_org = repo.update(
        org.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_org.id == org.id
    assert updated_org.name == "Updated Org"
    assert updated_org.phone == "+111111111"
    assert updated_org.role == "Updated Role"
    assert updated_org.type == "ADMINISTRATIVE"
    assert updated_org.modified_by == "updated_user"
    assert updated_org.email == "org@example.com"


def test_uhub_user_repository_create(db_session, model_test_data, sample_audit_data):
    """Test UhubUserRepository.create"""
    # Primero crear una organización
    org_repo = UhubOrgRepository(db_session)

    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    repo = UhubUserRepository(db_session)

    user_data = {
        **model_test_data["uhub_user_data"],
        "organization_id": org.id,
    }
    user = repo.create(
        user_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert user.id is not None
    assert user.type == "USER"
    assert user.username == "testuser"
    assert user.organization_id == org.id


def test_uhub_user_repository_get_by_username(
    db_session, model_test_data, sample_audit_data
):
    """Test UhubUserRepository.get_by_username"""
    # Primero crear una organización
    org_repo = UhubOrgRepository(db_session)

    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    repo = UhubUserRepository(db_session)

    user_data = {
        **model_test_data["uhub_user_data"],
        "organization_id": org.id,
    }
    user = repo.create(
        user_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por username
    found = repo.get_by_username("testuser", 1)

    assert found is not None
    assert found.id == user.id
    assert found.username == "testuser"


def test_uhub_user_repository_update(db_session, model_test_data, sample_audit_data):
    """Test UhubUserRepository.update"""
    # Primero crear una organización
    org_repo = UhubOrgRepository(db_session)
    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    repo = UhubUserRepository(db_session)

    user_data = {
        **model_test_data["uhub_user_data"],
        "organization_id": org.id,
    }
    user = repo.create(
        user_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Actualizar el usuario
    update_data = {
        "phone": "+999999999",
        "role": "Updated Role",
        "type": "ADMIN",
    }

    updated_user = repo.update(
        user.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_user.id == user.id
    assert updated_user.phone == "+999999999"
    assert updated_user.role == "Updated Role"
    assert updated_user.type == "ADMIN"
    assert updated_user.modified_by == "updated_user"
    assert updated_user.username == "testuser"


def test_uas_zone_repository_create(db_session, model_test_data, sample_audit_data):
    """Test UasZoneRepository.create"""
    # Primero crear una organización
    org_repo = UhubOrgRepository(db_session)

    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Crear una razon
    reason_repo = ReasonRepository(db_session)
    reason = reason_repo.create(**model_test_data["reason_data"])

    # Crear la zona
    repo = UasZoneRepository(db_session)

    zone_data = {
        **model_test_data["uas_zone_data"],
        "organizations": [org.id],
        "reasons": [reason.id],
    }
    zone = repo.create(
        zone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert zone.id is not None
    assert zone.name == "Test Zone"
    assert zone.lower_limit == 0
    assert len(zone.organizations) == 1
    assert len(zone.reasons) == 1
    assert zone.organizations[0].id == org.id
    assert zone.reasons[0].id == reason.id


def test_uas_zone_repository_get_by_zone_name(
    db_session, model_test_data, sample_audit_data
):
    """Test UasZoneRepository.get_by_zone_name"""
    # Primero crear una organización
    org_repo = UhubOrgRepository(db_session)

    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Crear una razon
    reason_repo = ReasonRepository(db_session)
    reason = reason_repo.create(**model_test_data["reason_data"])

    # Crear la zona
    repo = UasZoneRepository(db_session)

    zone_data = {
        **model_test_data["uas_zone_data"],
        "organizations": [org.id],
        "reasons": [reason.id],
    }
    zone = repo.create(
        zone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por EASA ID
    found = repo.get_by_zone_name("Test Zone", 1)

    assert found is not None
    assert found.id == zone.id
    assert found.name == "Test Zone"


def test_uas_zone_repository_update(db_session, model_test_data, sample_audit_data):
    """Test UasZoneRepository.update"""
    # Primero crear una organización
    org_repo = UhubOrgRepository(db_session)
    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Crear una segunda organización para la actualización
    org2 = org_repo.create(
        {
            **model_test_data["uhub_org_data"],
            "name": "Test Org 2",
            "email": "org2@example.com",
        },
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    # Crear razones
    reason_repo = ReasonRepository(db_session)
    reason = reason_repo.create(**model_test_data["reason_data"])
    reason2 = reason_repo.create(
        **{**model_test_data["reason_data"], "name": "Test Reason 2"}
    )

    # Crear la zona
    repo = UasZoneRepository(db_session)

    zone_data = {
        **model_test_data["uas_zone_data"],
        "organizations": [org.id],
        "reasons": [reason.id],
    }
    zone = repo.create(
        zone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Actualizar la zona
    update_data = {
        "name": "Updated Zone",
        "upper_limit": 200,
        "message": "Updated message",
        "organizations": [org2.id],
        "reasons": [reason2.id],
    }

    updated_zone = repo.update(
        zone.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_zone.id == zone.id
    assert updated_zone.name == "Updated Zone"
    assert updated_zone.upper_limit == 200
    assert updated_zone.message == "Updated message"
    assert updated_zone.modified_by == "updated_user"
    assert len(updated_zone.organizations) == 1
    assert len(updated_zone.reasons) == 1
    assert updated_zone.organizations[0].id == org2.id
    assert updated_zone.reasons[0].id == reason2.id


def test_uspace_repository_create(db_session, model_test_data, sample_audit_data):
    """Test UspaceRepository.create"""
    # Primero crear un archivo
    file_repo = FileRepository(db_session)
    file = file_repo.create(**model_test_data["file_data"])

    repo = UspaceRepository(db_session)

    uspace_data = {
        **model_test_data["uspace_data"],
        "file_id": file.id,
    }

    uspace = repo.create(
        uspace_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert uspace.id is not None
    assert uspace.name == "Test Uspace"
    assert uspace.code == "USPACE001"
    assert uspace.file_id == file.id
    assert uspace.sectors_count == 5


def test_uspace_repository_get_by_code(db_session, model_test_data, sample_audit_data):
    """Test UspaceRepository.get_by_code"""
    # Primero crear un archivo
    file_repo = FileRepository(db_session)
    file = file_repo.create(**model_test_data["file_data"])

    repo = UspaceRepository(db_session)

    uspace_data = {
        **model_test_data["uspace_data"],
        "file_id": file.id,
    }

    uspace = repo.create(
        uspace_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por número de serie
    found = repo.get_by_code("USPACE001", 1)

    assert found is not None
    assert found.id == uspace.id
    assert found.code == "USPACE001"


def test_uspace_repository_update(db_session, model_test_data, sample_audit_data):
    """Test UspaceRepository.update"""
    # Primero crear un archivo
    file_repo = FileRepository(db_session)
    file = file_repo.create(**model_test_data["file_data"])

    repo = UspaceRepository(db_session)

    uspace_data = {
        **model_test_data["uspace_data"],
        "file_id": file.id,
    }

    uspace = repo.create(
        uspace_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Actualizar el uspace
    update_data = {
        "name": "Updated Uspace",
        "sectors_count": 10,
    }

    updated_uspace = repo.update(
        uspace.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_uspace.id == uspace.id
    assert updated_uspace.name == "Updated Uspace"
    assert updated_uspace.sectors_count == 10
    assert updated_uspace.modified_by == "updated_user"
    assert updated_uspace.code == "USPACE001"
