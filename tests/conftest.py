from datetime import datetime

import pytest

from uat_tool.application import ApplicationContext
from uat_tool.application.dto.assets_dto import (
    UasZoneServiceDTO,
    UhubUserServiceDTO,
    UspaceServiceDTO,
)


@pytest.fixture(scope="session")
def test_engine():
    from sqlalchemy import create_engine

    """Motor de base de datos para testing."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    return engine


@pytest.fixture(scope="session")
def test_session_factory(test_engine):
    from sqlalchemy.orm import scoped_session, sessionmaker

    """Factory de sesiones para testing"""
    return scoped_session(sessionmaker(bind=test_engine))


@pytest.fixture(scope="function")
def shared_test_session(test_engine, test_session_factory):
    from uat_tool.infrastructure import Base
    from uat_tool.infrastructure.database.initial_data import load_initial_data

    """Sesión compartida con datos iniciales para cada test."""
    # Crear todas las tablas
    Base.metadata.create_all(test_engine)

    # Crear una nueva sesión
    session = test_session_factory()

    # Cargar datos iniciales
    try:
        load_initial_data(session)
        session.commit()
        print("Datos iniciales cargados correctamente")
    except Exception as e:
        session.rollback()
        print(f"Error cargando datos iniciales: {e}")
        # Continuar aunque falle la carga de datos iniciales

    yield session

    # Limpiar después del test
    try:
        session.rollback()
    finally:
        session.close()


@pytest.fixture(scope="function")
def db_session(shared_test_session):
    """Alias para compatibilidad con tests existentes."""
    return shared_test_session


@pytest.fixture
def app_context(db_session):
    """Crea ApplicationContext usando la misma sesión de BD SIN inicializar."""

    # Usar el engine de la sesión compartida
    test_engine = db_session.get_bind()

    # Crear ApplicationContext pero NO inicializar
    # (las tablas ya fueron creadas por shared_test_session)
    ctx = ApplicationContext(test_mode=True, test_engine=test_engine)

    # NO llamar a initialize() - las tablas ya existen
    # ctx.initialize()

    yield ctx
    ctx.shutdown()


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


@pytest.fixture
def sample_email_service_dto():
    from uat_tool.application.dto import EmailServiceDTO

    """Fixture para EmailServiceDTO de ejemplo"""
    return EmailServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        email="test@example.com",
        name="Test Email",
        password="testpassword",
    )


@pytest.fixture
def sample_operator_service_dto():
    from uat_tool.application.dto import OperatorServiceDTO

    """Fixture para OperatorServiceDTO de ejemplo"""
    return OperatorServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        name="Test Name",
        easa_id="EASA123",
        verification_code="VERIF123",
        password="testpassword",
        phone="123456789",
        email_id=1,
    )


@pytest.fixture
def sample_drone_service_dto():
    from uat_tool.application.dto import DroneServiceDTO

    """Fixture para DroneServiceDTO de ejemplo"""
    return DroneServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        name="Test Drone",
        serial_number="SN123456",
        manufacturer="Test Manufacturer",
        model="Test Model",
        tracker_type="SIMULATOR",
        transponder_id="TP123456",
        operator_id=1,
    )


@pytest.fixture
def sample_org_service_dto():
    from uat_tool.application.dto import UhubOrgServiceDTO

    """Fixture para UhubOrgServiceDTO de ejemplo"""
    return UhubOrgServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        name="Test Organization",
        email="test@example.com",
        phone="123456789",
        jurisdiction="Test Jurisdiction",
        aoi="Test AOI",
        role="Test Role",
        type="INFORMATIVE",
    )


@pytest.fixture
def sample_uhub_user_service_dto():
    return UhubUserServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        username="testuser",
        password="testpassword",
        email="user@example.com",
        dni="12345678A",
        phone="123456789",
        type="USER",
        role="Test Role",
        jurisdiction="Test Jurisdiction",
        aoi="Test AOI",
        organization_id=1,
    )


@pytest.fixture
def sample_uas_zone_service_dto():
    return UasZoneServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        name="Test Zone",
        area_type="POLYGON",
        circle_radius=None,
        corridor_width=None,
        lower_limit=0,
        upper_limit=120,
        reference_lower="AGL",
        reference_upper="AGL",
        application="TEMPORAL",
        restriction_type="INFORMATIVE",
        message="Test message",
        clearance_required=False,
        reasons=[1, 2],
        organizations=[1, 3],
    )


@pytest.fixture
def sample_uspace_service_dto():
    return UspaceServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="USPACE001",
        name="Test Uspace",
        sectors_count=5,
        file_id=1,
    )


@pytest.fixture
def sample_bug_service_dto():
    from uat_tool.application.dto import BugServiceDTO

    """Fixture para BugServiceDTO de ejemplo"""
    return BugServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status="OPEN",
        system_id=1,
        system_version="1.0.0",
        short_description="Test bug description",
        definition="Test bug definition with enough characters",
        urgency="2",
        impact="2",
        requirements=[1, 2, 3],
        history=[],
    )


@pytest.fixture
def sample_requirement_service_dto():
    from uat_tool.application.dto import RequirementServiceDTO

    """Fixture para RequirementServiceDTO de ejemplo"""
    return RequirementServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="REQ001",
        definition="Test requirement definition with enough characters",
        systems=[1, 2],
        sections=[1, 2],
    )
