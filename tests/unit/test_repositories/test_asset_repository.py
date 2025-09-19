from data.repositories.asset_repository import EmailRepository, OperatorRepository


def test_email_repository_create(db_session, sample_audit_data):
    """Test EmailRepository.create"""
    repo = EmailRepository(db_session)

    email_data = {
        "name": "Test Email",
        "email": "test@example.com",
        "password": "password123",
        "environment_id": 1,
        **sample_audit_data,
    }

    email = repo.create(**email_data)

    assert email.id is not None
    assert email.name == "Test Email"
    assert email.email == "test@example.com"


def test_email_repository_get_by_email(db_session, sample_audit_data):
    """Test EmailRepository.get_by_email"""
    repo = EmailRepository(db_session)

    email_data = {
        "name": "Test Email",
        "email": "test@example.com",
        "password": "password123",
        "environment_id": 1,
        **sample_audit_data,
    }

    email = repo.create(**email_data)

    # Buscar por email
    found = repo.get_by_email("test@example.com", 1)

    assert found is not None
    assert found.id == email.id
    assert found.email == "test@example.com"


def test_operator_repository_create_with_relations(db_session, sample_audit_data):
    """Test OperatorRepository.create_with_relations"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)
    email = email_repo.create(
        name="Test Email",
        email="test@example.com",
        password="password123",
        environment_id=1,
        modified_by="test_user",
    )

    repo = OperatorRepository(db_session)

    operator_data = {
        "name": "Test Operator",
        "easa_id": "EASA123",
        "verification_code": "VER123",
        "password": "op_password",
        "phone": "+123456789",
        "email_id": email.id,
        "environment_id": 1,
        **sample_audit_data,
    }

    operator = repo.create_with_relations(operator_data)

    assert operator.id is not None
    assert operator.name == "Test Operator"
    assert operator.easa_id == "EASA123"
    assert operator.email_id == email.id


def test_operator_repository_get_by_easa_id(db_session, sample_audit_data):
    """Test OperatorRepository.get_by_easa_id"""
    # Primero crear un email
    email_repo = EmailRepository(db_session)
    email = email_repo.create(
        name="Test Email",
        email="test@example.com",
        password="password123",
        environment_id=1,
        modified_by="test_user",
    )

    repo = OperatorRepository(db_session)

    operator_data = {
        "name": "Test Operator",
        "easa_id": "EASA123",
        "verification_code": "VER123",
        "password": "op_password",
        "phone": "+123456789",
        "email_id": email.id,
        "environment_id": 1,
        **sample_audit_data,
    }

    operator = repo.create_with_relations(operator_data)

    # Buscar por EASA ID
    found = repo.get_by_easa_id("EASA123", 1)

    assert found is not None
    assert found.id == operator.id
    assert found.easa_id == "EASA123"
