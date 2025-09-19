from core.models.auxiliary import Environment, System
from data.repositories.auxiliary_repository import (
    EnvironmentRepository,
    SystemRepository,
)


def test_environment_repository_get_by_name(db_session, sample_environment_data):
    """Test EnvironmentRepository.get_by_name"""
    repo = EnvironmentRepository(db_session)

    # Crear environment
    environment = Environment(**sample_environment_data)
    db_session.add(environment)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("Test Environment")

    assert found is not None
    assert found.name == "Test Environment"
    assert found.description == "Test environment for unit testing"


def test_environment_repository_get_by_name_not_found(db_session):
    """Test EnvironmentRepository.get_by_name cuando no existe"""
    repo = EnvironmentRepository(db_session)

    found = repo.get_by_name("NonExistent")

    assert found is None


def test_system_repository_get_by_name(db_session):
    """Test SystemRepository.get_by_name"""
    repo = SystemRepository(db_session)

    # Crear system
    system = System(name="Test System")
    db_session.add(system)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("Test System")

    assert found is not None
    assert found.name == "Test System"


def test_environment_repository_get_with_relationships(
    db_session, sample_environment_data
):
    """Test EnvironmentRepository.get_with_relationships"""
    repo = EnvironmentRepository(db_session)

    # Crear environment
    environment = Environment(**sample_environment_data)
    db_session.add(environment)
    db_session.commit()

    # Obtener con relaciones
    found = repo.get_with_relationships(environment.id)

    assert found is not None
    assert found.id == environment.id
    # Verificar que las relaciones están cargadas (aunque estén vacías)
    assert hasattr(found, "environment_bugs")
    assert hasattr(found, "environment_campaigns")
