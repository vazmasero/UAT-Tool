import pytest
from sqlalchemy.exc import IntegrityError

from core.models.auxiliary import Environment, Reason, Section, System


def test_environment_creation(db_session, sample_environment_data):
    """Test creación de Environment"""
    environment = Environment(**sample_environment_data)
    db_session.add(environment)
    db_session.commit()

    assert environment.id is not None
    assert environment.name == "Test Environment"
    assert environment.description == "Test environment for unit testing"


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


def test_section_creation(db_session):
    """Test creación de Section"""
    section = Section(name="Test Section")
    db_session.add(section)
    db_session.commit()

    assert section.id is not None
    assert section.name == "Test Section"


def test_reason_creation(db_session):
    """Test creación de Reason"""
    reason = Reason(name="Test Reason")
    db_session.add(reason)
    db_session.commit()

    assert reason.id is not None
    assert reason.name == "Test Reason"
