from core.models import Email


def test_email_creation_full(db_session, model_test_data):
    """Test completo de creación de email"""
    email = Email(**model_test_data["email_data"])
    email.environment_id = 1
    db_session.add(email)
    db_session.commit()

    assert email.id is not None
    assert email.name == "Test Email"
    assert email.email == "test@example.com"
    assert email.password == "password123"
    assert email.created_at is not None
    assert email.updated_at is not None
    assert email.modified_by == "test_user"
    #assert email.environment_rel == []
    #assert email.operators == []

# def test_email_unique_name_creation(db_session, sample_environment_data):
