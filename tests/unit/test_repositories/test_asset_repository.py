from data.repositories.asset_repository import EmailRepository, OperatorRepository, DroneRepository


def test_email_repository_create(db_session, model_test_data, sample_audit_data):
    """Test EmailRepository.create"""
    repo = EmailRepository(db_session)

    email = repo.create(model_test_data["email_data"], environment_id=1, modified_by=sample_audit_data["modified_by"])

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

    email = repo.create(model_test_data["email_data"], environment_id=1, modified_by=sample_audit_data["modified_by"])

    # Buscar por email
    found = repo.get_by_email("test@example.com", 1)

    assert found is not None
    assert found.id == email.id
    assert found.email == "test@example.com"


def test_operator_repository_create(db_session, model_test_data, sample_audit_data):
    """Test OperatorRepository.create"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)

    email = email_repo.create(model_test_data["email_data"], environment_id=1, modified_by=sample_audit_data["modified_by"])

    repo = OperatorRepository(db_session)

    operator_data = {
        **model_test_data["operator_data"],
        "email_id": email.id,
    }
    operator = repo.create(operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"])

    assert operator.id is not None
    assert operator.name == "Test Operator"
    assert operator.easa_id == "EASA123"
    assert operator.email_id == email.id


def test_operator_repository_get_by_easa_id(db_session, model_test_data, sample_audit_data):
    """Test OperatorRepository.get_by_easa_id"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)

    email = email_repo.create(model_test_data["email_data"], environment_id=1, modified_by=sample_audit_data["modified_by"])

    repo = OperatorRepository(db_session)

    operator_data = {
        **model_test_data["operator_data"],
        "email_id": email.id,
    }

    operator = repo.create(operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"])

    # Buscar por EASA ID
    found = repo.get_by_easa_id("EASA123", 1)

    assert found is not None
    assert found.id == operator.id
    assert found.easa_id == "EASA123"

def test_drone_repository_create(db_session, model_test_data, sample_audit_data):
    """Test DroneRepository.create"""
    # Primero crear un operador
    ope_repo = OperatorRepository(db_session)

    ope_data = {
        **model_test_data["operator_data"],
        "email_id": 1,

    }
    operator = ope_repo.create(ope_data, environment_id=1, modified_by=sample_audit_data["modified_by"])   

    repo = DroneRepository(db_session)

    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }

    drone = repo.create(drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"])

    assert drone.id is not None
    assert drone.name == "Test Drone"
    assert drone.serial_number == "DRONE123"
    assert drone.operator_id == operator.id


def test_operator_repository_get_by_serial_number(db_session, model_test_data, sample_audit_data):
    """Test OperatorRepository.get_by_serial_number"""
    # Primero crear un operador
    ope_repo = OperatorRepository(db_session)

    ope_data = {
        **model_test_data["operator_data"],
        "email_id": 1,

    }
    operator = ope_repo.create(ope_data, environment_id=1, modified_by=sample_audit_data["modified_by"])   

    repo = DroneRepository(db_session)

    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }

    drone = repo.create(drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"])

    # Buscar por número de serie
    found = repo.get_by_serial_number("DRONE123", 1)

    assert found is not None
    assert found.id == drone.id
    assert found.serial_number == "DRONE123"