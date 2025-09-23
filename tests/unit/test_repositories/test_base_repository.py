import pytest
from core.models.auxiliary import System
from data.repositories.base import BaseRepository

def test_base_repository_create(db_session, model_test_data):
    """Test creación básica con BaseRepository"""
    repo = BaseRepository(db_session, System)

    system = repo.create(**model_test_data["system_data"])

    assert system.id is not None
    assert system.name == "Test System"


def test_base_repository_get_by_id(db_session, model_test_data):
    """Test obtener por ID con BaseRepository"""
    repo = BaseRepository(db_session, System)

    system = repo.create(**model_test_data["system_data"])
    retrieved = repo.get_by_id(system.id)

    assert retrieved is not None
    assert retrieved.id == system.id
    assert retrieved.name == "Test System"

def test_base_repository_get_by_id_value_error(db_session, model_test_data):
    """Test obtener por ID erróneo con BaseRepository (ValueError)"""
    repo = BaseRepository(db_session, System)

    system = repo.create(**model_test_data["system_data"])
    
    with pytest.raises(ValueError):
        repo.get_by_id(2, raise_if_not_found=True)

def test_base_repository_get_all(db_session):
    """Test obtener todos los registros con BaseRepository"""
    repo = BaseRepository(db_session, System)

    # Crear varios sistemas
    repo.create(name="System 1")
    repo.create(name="System 2")

    systems = repo.get_all()

    assert len(systems) == 2

def test_base_repository_get_all_limit(db_session):
    """Test obtener un número de registros concreto (limit) con BaseRepository"""
    repo = BaseRepository(db_session, System)

    # Crear varios sistemas
    repo.create(name="System 1")
    repo.create(name="System 2")

    systems = repo.get_all(limit=1)

    assert len(systems) == 1

def test_base_repository_get_all_offset(db_session):
    """Test obtener un registro concreto (offset) con BaseRepository"""
    repo = BaseRepository(db_session, System)

    # Crear varios sistemas
    repo.create(name="System 1")
    repo.create(name="System 2")

    retrieved = repo.get_all(limit=1, offset=1)

    assert retrieved[0] is not None
    assert retrieved[0].id == 2
    assert retrieved[0].name == "System 2"

def test_base_repository_filter_by(db_session):
    """Test filtrar registros con BaseRepository"""
    repo = BaseRepository(db_session, System)

    repo.create(name="System A")
    repo.create(name="System B")

    results = repo.filter_by(name="System A")

    assert len(results) == 1
    assert results[0].name == "System A"


def test_base_repository_update(db_session):
    """Test actualizar registro con BaseRepository"""
    repo = BaseRepository(db_session, System)

    system = repo.create(name="Old Name")
    updated = repo.update(system, name="New Name")

    assert updated.name == "New Name"


def test_base_repository_delete(db_session):
    """Test eliminar registro con BaseRepository"""
    repo = BaseRepository(db_session, System)

    system = repo.create(name="To Delete")
    result = repo.delete(system.id)

    assert result is True
    assert repo.get_by_id(system.id) is None

def test_base_repository_delete_false(db_session):
    """Test eliminar registro con BaseRepository"""
    repo = BaseRepository(db_session, System)

    system = repo.create(name="To Delete")
    result = repo.delete(2)

    assert result is False
    assert repo.get_by_id(system.id) is not None


def test_base_repository_get_or_create(db_session):
    """Test get_or_create con BaseRepository"""
    repo = BaseRepository(db_session, System)

    # Primera vez: crear
    system1, created1 = repo.get_or_create(name="Test System")
    assert created1 is True
    assert system1.name == "Test System"

    # Segunda vez: obtener existente
    system2, created2 = repo.get_or_create(name="Test System")
    assert created2 is False
    assert system2.id == system1.id