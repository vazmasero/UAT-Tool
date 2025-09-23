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
def sample_audit_data():
    """Datos de auditoría para testing"""
    return {"modified_by": "test_user"}


@pytest.fixture
def model_test_data():
    """
    Fixture que devuelve diccionarios con datos de ejemplo para todos los modelos.
    Los datos están organizados por modelo y listos para ser usados en tests.
    """
    return {
        # ---- Environment (no necesita audit_data) ----
        "environment_data": {
            "name": "Test Environment",
            "description": "Test environment for unit testing",
        },
        # ---- Auxiliary Models (no necesitan audit_data) ----
        "system_data": {"name": "Test System"},
        "section_data": {"name": "Test Section"},
        "reason_data": {"name": "Test Reason"},
        "file_data": {
            "owner_type": "bug",
            "filename": "test.txt",
            "filepath": "/uploads/test.txt",
            "mime_type": "text/plain",
            "size": "1024",
            "uploaded_by": "test_user",
        },
        # ---- Assets Models (sí necesitan audit_data) ----
        "email_data": {
            "name": "Test Email",
            "email": "test@example.com",
            "password": "password123",
        },
        "operator_data": {
            "name": "Test Operator",
            "easa_id": "EASA123",
            "verification_code": "VER123",
            "password": "op_password",
            "phone": "+123456789",
        },
        "drone_data": {
            "name": "Test Drone",
            "serial_number": "DRONE123",
            "manufacturer": "DJI",
            "model": "Mavic 3",
            "tracker_type": "SIMULATOR",
            "transponder_id": "TRANS123",
        },
        "uhub_org_data": {
            "name": "Test Org",
            "email": "org@example.com",
            "phone": "+987654321",
            "jurisdiction": "Spain",
            "aoi": "Madrid",
            "role": "Administrator",
            "type": "OPERATIVE",
        },
        "uhub_user_data": {
            "name": "Test User",
            "email": "user@example.com",
            "dni": "12345678A",
            "phone": "+1122334455",
            "username": "testuser",
            "password": "userpass",
            "type": "USER",
            "role": "Tester",
            "jurisdiction": "Spain",
            "aoi": "Barcelona",
        },
        "uas_zone_data": {
            "name": "Test Zone",
            "area_type": "POLYGON",
            "lower_limit": 0,
            "upper_limit": 100,
            "reference_lower": "AGL",
            "reference_upper": "AMSL",
            "application": "TEMPORAL",
            "restriction_type": "INFORMATIVE",
            "clearance_required": False,
            "message": "Test zone message",
        },
        "uspace_data": {
            "code": "USPACE001",
            "name": "Test Uspace",
            "sectors_count": 5,
        },
        # ---- Requirements ----
        "requirement_data": {
            "code": "REQ001",
            "definition": "Test requirement definition",
        },
        # ---- Test Management ----
        "step_data": {
            "action": "Test action",
            "expected_result": "Expected result",
            "comments": "Step comments",
        },
        "case_data": {
            "code": "CASE001",
            "name": "Test Case",
            "comments": "Test case comments",
        },
        "block_data": {
            "code": "BLOCK001",
            "name": "Test Block",
            "comments": "Block comments",
        },
        "campaign_data": {
            "code": "CAMPAIGN001",
            "description": "Test campaign description",
            "system_version": "1.0.0",
            "comments": "Campaign comments",
            "status": "DRAFT",
        },
        # ---- Executions ----
        "campaign_run_data": {
            "executed_by": "test_executor",
            "notes": "Test campaign run",
        },
        "case_run_data": {"notes": "Test case run"},
        "step_run_data": {"passed": True, "notes": "Test step run"},
        # ---- Bugs ----
        "bug_data": {
            "status": "OPEN",
            "system_version": "1.0.0",
            "service_now_id": "SN123",
            "short_description": "Test bug",
            "definition": "Bug definition",
            "urgency": "2",
            "impact": "2",
            "comments": "Bug comments",
        },
        "bug_history_data": {
            "changed_by": "test_user",
            "change_summary": "Bug created",
        },
    }
