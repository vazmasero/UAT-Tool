import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from data.database import Base


@pytest.fixture(scope="session")
def test_engine():
    """Motor de base de datos para testing."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    return engine


@pytest.fixture(scope="session")
def test_session_factory(test_engine):
    """Factory de sesiones para testing"""
    return scoped_session(sessionmaker(bind=test_engine))


@pytest.fixture(scope="function")
def db_session(test_engine, test_session_factory):
    """Sesión de base de datos para cada test"""
    # Crear todas las tablas
    Base.metadata.create_all(test_engine)

    # Crear una nueva sesión
    session = test_session_factory()

    yield session

    # Limpiar después del test
    session.rollback()
    session.close()
    # Eliminar todas las tablas
    Base.metadata.drop_all(test_engine)


@pytest.fixture
def sample_environment_data():
    """Datos de ejemplo para Environment"""
    return {
        "name": "Test Environment",
        "description": "Test environment for unit testing",
    }


@pytest.fixture
def sample_audit_data():
    """Datos de auditoría para testing"""
    return {"modified_by": "test_user"}
