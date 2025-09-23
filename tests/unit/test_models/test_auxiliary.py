import pytest
from sqlalchemy.exc import IntegrityError

from core.models.auxiliary import Environment, File, Reason, Section, System


def test_environment_creation(db_session, model_test_data):
    """Test creación de Environment"""
    environment = Environment(**model_test_data["environment_data"])
    db_session.add(environment)
    db_session.commit()

    assert environment.id is not None
    assert environment.name == "Test Environment"
    assert environment.description == "Test environment for unit testing"
    assert environment.created_at is not None


def test_environment_unique_name_creation(db_session, model_test_data):
    """Test que verifica la constraint de nombre único en Environment"""
    environment = Environment(**model_test_data["environment_data"])
    db_session.add(environment)
    db_session.commit()

    environment2 = Environment(name="Test Environment")
    db_session.add(environment2)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_environment_required_fields(db_session):
    """Test que verifica que los campos obligatorios fallen si faltan"""
    environment = Environment(name="Test")
    db_session.add(environment)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_environment_relationships(db_session, model_test_data):
    """Test básico de relaciones de Environment"""
    environment = Environment(**model_test_data["environment_data"])
    db_session.add(environment)
    db_session.commit()

    # Verificar que las relaciones están disponibles
    assert environment.environment_emails == []
    assert environment.environment_operators == []
    assert environment.environment_drones == []
    assert environment.environment_uhub_orgs == []
    assert environment.environment_uhub_users == []
    assert environment.environment_uas_zones == []
    assert environment.environment_uspaces == []
    assert environment.environment_bugs == []
    assert environment.environment_campaigns == []
    assert environment.environment_campaign_runs == []
    assert environment.environment_requirements == []


def test_system_creation(db_session):
    """Test creación de System"""
    system = System(name="Test System")
    db_session.add(system)
    db_session.commit()

    assert system.id is not None
    assert system.name == "Test System"


def test_system_unique_name_constraint(db_session):
    """Test que verifica la constraint de nombre único en System"""
    system1 = System(name="Unique System")
    db_session.add(system1)
    db_session.commit()

    system2 = System(name="Unique System")
    db_session.add(system2)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_system_relationships(db_session):
    """Test básico de relaciones de System"""
    system = System(name="Sample System")
    db_session.add(system)
    db_session.commit()

    # Verificar que las relaciones están disponibles
    assert system.cases == []
    assert system.bugs == []
    assert system.campaigns == []


def test_section_creation(db_session):
    """Test creación de Section"""
    section = Section(name="Test Section")
    db_session.add(section)
    db_session.commit()

    assert section.id is not None
    assert section.name == "Test Section"


def test_section_unique_name_constraint(db_session):
    """Test que verifica la constraint de nombre único en Section"""
    section1 = Section(name="Unique Section")
    db_session.add(section1)
    db_session.commit()

    section2 = Section(name="Unique Section")
    db_session.add(section2)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_section_relationships(db_session):
    """Test básico de relaciones de Section"""
    section = Section(name="Sample Section")
    db_session.add(section)
    db_session.commit()

    # Verificar que las relaciones están disponibles
    assert section.cases == []


def test_reason_creation(db_session):
    """Test creación de Reason"""
    reason = Reason(name="Test Reason")
    db_session.add(reason)
    db_session.commit()

    assert reason.id is not None
    assert reason.name == "Test Reason"


def test_reason_unique_name_constraint(db_session):
    """Test que verifica la constraint de nombre único en Reason"""
    reason1 = Reason(name="Unique Reason")
    db_session.add(reason1)
    db_session.commit()

    reason2 = Reason(name="Unique Reason")
    db_session.add(reason2)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_reason_relationships(db_session):
    """Test básico de relaciones de Reason"""
    reason = Reason(name="Sample Reason")
    db_session.add(reason)
    db_session.commit()

    # Verificar que las relaciones están disponibles
    assert reason.uas_zones == []


def test_file_creation(db_session):
    """Test creación de File"""
    file_data = {
        "owner_type": "bug",
        "filename": "test.txt",
        "filepath": "/uploads/test.txt",
        "mime_type": "text/plain",
        "size": "1024",
        "uploaded_by": "test_user",
    }
    file = File(**file_data)
    db_session.add(file)
    db_session.commit()

    assert file.id is not None
    assert file.filename == "test.txt"
    assert file.uploaded_at is not None


def test_file_required_fields(db_session):
    """Test campos obligatorios de File"""
    file = File()
    db_session.add(file)

    with pytest.raises(IntegrityError):
        db_session.commit()


def test_file_relationships(db_session):
    """Test básico de relaciones de File"""
    file_data = {
        "owner_type": "bug",
        "filename": "test.txt",
        "filepath": "/uploads/test.txt",
        "mime_type": "text/plain",
        "size": "1024",
        "uploaded_by": "test_user",
    }
    file = File(**file_data)
    db_session.add(file)
    db_session.commit()

    # Verificar que las relaciones están disponibles
    assert file.uspace == []
    assert file.bug_files == []
    assert file.step_runs_files == []
