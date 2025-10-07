from uat_tool.domain import (
    Environment,
    EnvironmentRepository,
    File,
    FileRepository,
    Reason,
    ReasonRepository,
    Section,
    SectionRepository,
    System,
    SystemRepository,
)


def test_environment_repository_get_by_name(db_session, model_test_data):
    """Test EnvironmentRepository.get_by_name."""
    repo = EnvironmentRepository(db_session)

    # Crear environment
    environment = Environment(**model_test_data["environment_data"])
    db_session.add(environment)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("Test Environment")

    assert found is not None
    assert found.name == "Test Environment"
    assert found.description == "Test environment for unit testing"


def test_environment_repository_get_by_name_not_found(db_session):
    """Test EnvironmentRepository.get_by_name cuando no existe."""
    repo = EnvironmentRepository(db_session)

    found = repo.get_by_name("NonExistent")

    assert found is None


def test_environment_repository_get_with_relationships(db_session, model_test_data):
    """Test EnvironmentRepository.get_with_relationships"""
    repo = EnvironmentRepository(db_session)

    # Crear environment
    environment = Environment(**model_test_data["environment_data"])
    db_session.add(environment)
    db_session.commit()

    # Obtener con relaciones
    found = repo.get_with_relationships(environment.id)

    assert found is not None
    assert found.id == environment.id
    # Verificar que las relaciones están cargadas (aunque estén vacías)
    assert hasattr(found, "environment_bugs")
    assert hasattr(found, "environment_campaigns")
    assert hasattr(found, "environment_campaign_runs")


def test_system_repository_get_by_name(db_session):
    """Test SystemRepository.get_by_name."""
    repo = SystemRepository(db_session)

    # Crear system
    system = System(name="Test System")
    db_session.add(system)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("Test System")

    assert found is not None
    assert found.name == "Test System"


def test_system_repository_get_by_name_not_found(db_session):
    """Test SystemRepository.get_by_name cuando no existe."""
    repo = SystemRepository(db_session)

    # Crear system
    system = System(name="Test System")
    db_session.add(system)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("NonExistent")

    assert found is None


def test_section_repository_get_by_name(db_session):
    """Test SectionRepository.get_by_name."""
    repo = SectionRepository(db_session)

    # Crear section
    section = Section(name="Test Section")
    db_session.add(section)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("Test Section")

    assert found is not None
    assert found.name == "Test Section"


def test_section_repository_get_by_name_not_found(db_session):
    """Test SectionRepository.get_by_name cuando no existe."""
    repo = SectionRepository(db_session)

    # Crear section
    section = Section(name="Test Section")
    db_session.add(section)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("NonExistent")

    assert found is None


def test_file_repository_get_by_filename(db_session, model_test_data):
    """Test FileRepository.get_by_filename."""
    repo = FileRepository(db_session)

    # Crear file
    file = File(**model_test_data["file_data"])
    db_session.add(file)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_filename("test.txt")

    assert found is not None
    assert found.filename == "test.txt"


def test_file_repository_get_by_filename_not_found(db_session, model_test_data):
    """Test FileRepository.get_by_name cuando no existe."""
    repo = FileRepository(db_session)

    # Crear file
    file = File(**model_test_data["file_data"])
    db_session.add(file)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_filename("NonExistent.txt")

    assert found is None


def test_reason_repository_get_by_filename(db_session):
    """Test ReasonRepository.get_by_filename."""
    repo = ReasonRepository(db_session)

    # Crear file
    reason = Reason(name="Test Reason")
    db_session.add(reason)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("Test Reason")

    assert found is not None
    assert found.name == "Test Reason"


def test_reason_repository_get_by_name_not_found(db_session):
    """Test ReasonRepository.get_by_name cuando no existe."""
    repo = ReasonRepository(db_session)

    # Crear file
    reason = Reason(name="Test Reason")
    db_session.add(reason)
    db_session.commit()

    # Buscar por nombre
    found = repo.get_by_name("NonExistent")

    assert found is None
