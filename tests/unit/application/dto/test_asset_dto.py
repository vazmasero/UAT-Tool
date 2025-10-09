from datetime import datetime

import pytest

from uat_tool.application.dto import (
    EmailFormDTO,
    EmailServiceDTO,
    OperatorFormDTO,
    OperatorServiceDTO,
    OperatorTableDTO,
)
from uat_tool.application.dto.assets_dto import (
    DroneFormDTO,
    DroneServiceDTO,
    DroneTableDTO,
    EmailTableDTO,
    UasZoneFormDTO,
    UasZoneServiceDTO,
    UasZoneTableDTO,
    UhubOrgFormDTO,
    UhubOrgServiceDTO,
    UhubOrgTableDTO,
    UhubUserFormDTO,
    UhubUserServiceDTO,
    UhubUserTableDTO,
    UspaceFormDTO,
    UspaceServiceDTO,
    UspaceTableDTO,
)


def test_email_service_dtos():
    """Test DTOs de Email (creación con datos obligatorios y opcionales en None)"""
    # EmailServiceDTO con datos completos
    email_service_dto1 = EmailServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        email="test@example.com",
        name="Test Email",
        password="testpassword",
    )

    assert email_service_dto1.email == "test@example.com"
    assert email_service_dto1.password == "testpassword"

    # EmailServiceDTO con datos opcionales en None
    email_service_dto2 = EmailServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        email="test@example.com",
        name="Test Email",
        password="testpassword",
    )

    assert email_service_dto2.created_at is None
    assert email_service_dto2.updated_at is None


def test_email_table_from_service_dto(sample_email_service_dto):
    """Test creación de EmailTableDTO desde EmailServiceDTO"""
    email_service_dto = sample_email_service_dto

    email_table_dto = EmailTableDTO.from_service_dto(email_service_dto)

    assert email_table_dto.id == email_service_dto.id
    assert email_table_dto.name == email_service_dto.name
    assert email_table_dto.email == email_service_dto.email
    assert email_table_dto.created_at != "Not assigned"
    assert email_table_dto.updated_at != "Not assigned"
    assert email_table_dto.modified_by == email_service_dto.modified_by


def test_email_form_dto_validation():
    """Test validaciones en EmailFormDTO"""
    # EmailFormDTO con validación
    with pytest.raises(ValueError, match="Email válido es requerido"):
        EmailFormDTO(
            le_name="Test Email",
            le_email="invalid-email",
            le_password="password123",
        )

    with pytest.raises(ValueError, match="El nombre es requerido"):
        EmailFormDTO(
            le_name="",
            le_email="test@example.com",
            le_password="password123",
        )

    with pytest.raises(ValueError, match="La contraseña es requerida"):
        EmailFormDTO(
            le_name="Test Email",
            le_email="test@example.com",
            le_password="",
        )


def test_email_form_to_service_dto():
    """Test conversión de EmailFormDTO a EmailServiceDTO"""
    email_form_dto = EmailFormDTO(
        le_name="Test Email",
        le_email="test@example.com",
        le_password="password123",
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    email_service_dto = email_form_dto.to_service_dto(context_data)

    assert email_service_dto.id == 0
    assert email_service_dto.created_at is None
    assert email_service_dto.updated_at is None
    assert email_service_dto.modified_by == context_data["modified_by"]
    assert email_service_dto.environment_id == context_data["environment_id"]


def test_email_form_from_service_dto(sample_email_service_dto):
    """Test conversión de EmailServiceDTO a EmailFormDTO"""
    email_service_dto = sample_email_service_dto

    email_form_dto = EmailFormDTO.from_service_dto(email_service_dto)

    assert email_form_dto.le_name == email_service_dto.name
    assert email_form_dto.le_email == email_service_dto.email
    assert email_form_dto.le_password == email_service_dto.password


def test_operator_service_dtos():
    """Test DTOs de Operator (Creación con datos obligatorios y opcionales en None)"""
    # OperatorFormDTO con datos completos
    operator_service_dto1 = OperatorServiceDTO(
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

    assert operator_service_dto1.name == "Test Name"
    assert operator_service_dto1.easa_id == "EASA123"
    assert operator_service_dto1.verification_code == "VERIF123"
    assert operator_service_dto1.password == "testpassword"
    assert operator_service_dto1.phone == "123456789"
    assert operator_service_dto1.email_id == 1

    # OperatorServiceDTO con datos opcionales en None
    operator_service_dto2 = OperatorServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        name="Test Name",
        easa_id="EASA123",
        verification_code="VERIF123",
        password="testpassword",
        phone="123456789",
        email_id=1,
    )

    assert operator_service_dto2.created_at is None
    assert operator_service_dto2.updated_at is None


def test_operator_table_from_service_dto(sample_operator_service_dto):
    """Test creación de OperatorTableDTO desde OperatorServiceDTO"""
    operator_service_dto = sample_operator_service_dto

    operator_table_dto = OperatorTableDTO.from_service_dto(
        operator_service_dto, email_email="test@example.com"
    )

    assert operator_table_dto.id == operator_service_dto.id
    assert operator_table_dto.name == operator_service_dto.name
    assert operator_table_dto.email == "test@example.com"
    assert operator_table_dto.created_at != "Not assigned"
    assert operator_table_dto.updated_at != "Not assigned"
    assert operator_table_dto.modified_by == operator_service_dto.modified_by


def test_operator_form_dto_validation():
    """Test validaciones en OperatorFormDTO"""
    with pytest.raises(ValueError, match="Nombre, EASA ID y teléfono son requeridos"):
        OperatorFormDTO(
            le_name="",
            le_easa_id="",
            le_verification_code="123",
            le_password="pass",
            le_phone="",
            cb_email=1,
        )


def test_operator_form_to_service_dto():
    """Test conversión de OperatorFormDTO a OperatorServiceDTO"""
    operator_form_dto = OperatorFormDTO(
        le_name="Test Operator",
        le_easa_id="EASA123",
        le_verification_code="VERIF123",
        le_password="password123",
        le_phone="123456789",
        cb_email=1,
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    operator_service_dto = operator_form_dto.to_service_dto(context_data)

    assert operator_service_dto.id == 0
    assert operator_service_dto.created_at is None
    assert operator_service_dto.updated_at is None
    assert operator_service_dto.modified_by == context_data["modified_by"]
    assert operator_service_dto.environment_id == context_data["environment_id"]


def test_operator_form_from_service_dto(sample_operator_service_dto):
    """Test conversión de OperatorServiceDTO a OperatorFormDTO"""
    operator_service_dto = sample_operator_service_dto

    operator_form_dto = OperatorFormDTO.from_service_dto(operator_service_dto)

    assert operator_form_dto.le_name == operator_service_dto.name
    assert operator_form_dto.le_easa_id == operator_service_dto.easa_id
    assert (
        operator_form_dto.le_verification_code == operator_service_dto.verification_code
    )
    assert operator_form_dto.le_password == operator_service_dto.password
    assert operator_form_dto.le_phone == operator_service_dto.phone
    assert operator_form_dto.cb_email == operator_service_dto.email_id


def test_drone_service_dtos():
    """Test DTOs de Drone (Creación con datos obligatorios y opcionales en None)"""
    # DroneServiceDTO con datos completos
    drone_service_dto1 = DroneServiceDTO(
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

    assert drone_service_dto1.name == "Test Drone"
    assert drone_service_dto1.serial_number == "SN123456"
    assert drone_service_dto1.manufacturer == "Test Manufacturer"
    assert drone_service_dto1.model == "Test Model"
    assert drone_service_dto1.tracker_type == "SIMULATOR"
    assert drone_service_dto1.transponder_id == "TP123456"
    assert drone_service_dto1.operator_id == 1

    # DroneServiceDTO con datos opcionales en None
    drone_service_dto2 = DroneServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        name="Test Drone",
        serial_number="SN123456",
        manufacturer="Test Manufacturer",
        model="Test Model",
        tracker_type="SIMULATOR",
        transponder_id="TP123456",
        operator_id=1,
    )

    assert drone_service_dto2.created_at is None
    assert drone_service_dto2.updated_at is None


def test_drone_table_from_service_dto(sample_drone_service_dto):
    """Test creación de DroneTableDTO desde DroneServiceDTO"""
    drone_service_dto = sample_drone_service_dto

    drone_table_dto = DroneTableDTO.from_service_dto(
        drone_service_dto, operator_name="Test Operator"
    )

    assert drone_table_dto.id == drone_service_dto.id
    assert drone_table_dto.name == drone_service_dto.name
    assert drone_table_dto.created_at != "Not assigned"
    assert drone_table_dto.updated_at != "Not assigned"
    assert drone_table_dto.modified_by == drone_service_dto.modified_by
    assert drone_table_dto.operator == "Test Operator"


def test_drone_form_dto_validation():
    """Test validaciones en DroneFormDTO"""
    with pytest.raises(ValueError, match="Nombre y número de serie son requeridos"):
        DroneFormDTO(
            le_name="",
            le_sn="",
            cb_operator=1,
            le_manufacturer="Test Manufacturer",
            le_model="Test Model",
            le_transponder_id="TP123456",
            cb_tracker_type="SIMULATOR",
        )


def test_drone_form_to_service_dto():
    """Test conversión de DroneFormDTO a DroneServiceDTO"""
    drone_form_dto = DroneFormDTO(
        le_name="Test Drone",
        le_sn="SN123456",
        le_manufacturer="Test Manufacturer",
        le_model="Test Model",
        le_transponder_id="TP123456",
        cb_tracker_type="SIMULATOR",
        cb_operator=1,
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    drone_service_dto = drone_form_dto.to_service_dto(context_data)

    assert drone_service_dto.id == 0
    assert drone_service_dto.created_at is None
    assert drone_service_dto.updated_at is None
    assert drone_service_dto.modified_by == context_data["modified_by"]
    assert drone_service_dto.environment_id == context_data["environment_id"]


def test_drone_form_from_service_dto(sample_drone_service_dto):
    """Test conversión de DroneServiceDTO a DroneFormDTO"""
    drone_service_dto = sample_drone_service_dto

    drone_form_dto = DroneFormDTO.from_service_dto(drone_service_dto)

    assert drone_form_dto.le_name == drone_service_dto.name
    assert drone_form_dto.le_sn == drone_service_dto.serial_number
    assert drone_form_dto.le_manufacturer == drone_service_dto.manufacturer
    assert drone_form_dto.le_model == drone_service_dto.model
    assert drone_form_dto.le_transponder_id == drone_service_dto.transponder_id
    assert drone_form_dto.cb_tracker_type == drone_service_dto.tracker_type
    assert drone_form_dto.cb_operator == drone_service_dto.operator_id


def test_org_service_dtos():
    """Test DTOs de Uhub Org (Creación con datos obligatorios y opcionales en None)"""
    # UhubOrgServiceDTO con datos completos
    org_service_dto1 = UhubOrgServiceDTO(
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

    assert org_service_dto1.name == "Test Organization"
    assert org_service_dto1.email == "test@example.com"
    assert org_service_dto1.phone == "123456789"
    assert org_service_dto1.jurisdiction == "Test Jurisdiction"
    assert org_service_dto1.aoi == "Test AOI"
    assert org_service_dto1.role == "Test Role"
    assert org_service_dto1.type == "INFORMATIVE"

    # UhubOrgServiceDTO con datos opcionales en None
    org_service_dto2 = UhubOrgServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        name="Test Organization",
        email="test@example.com",
        phone="123456789",
        jurisdiction="Test Jurisdiction",
        aoi="Test AOI",
        role="Test Role",
        type="INFORMATIVE",
    )

    assert org_service_dto2.created_at is None
    assert org_service_dto2.updated_at is None


def test_org_table_from_service_dto(sample_org_service_dto):
    """Test creación de UhubOrgTableDTO desde UhubOrgServiceDTO"""
    org_service_dto = sample_org_service_dto

    org_table_dto = UhubOrgTableDTO.from_service_dto(org_service_dto)

    assert org_table_dto.id == org_service_dto.id
    assert org_table_dto.name == org_service_dto.name
    assert org_table_dto.created_at != "Not assigned"
    assert org_table_dto.updated_at != "Not assigned"
    assert org_table_dto.modified_by == org_service_dto.modified_by
    assert org_table_dto.email == "test@example.com"
    assert org_table_dto.phone == "123456789"
    assert org_table_dto.jurisdiction == "Test Jurisdiction"
    assert org_table_dto.aoi == "Test AOI"
    assert org_table_dto.role == "Test Role"
    assert org_table_dto.type == "INFORMATIVE"


def test_org_form_dto_validation():
    """Test validaciones en UhubOrgFormDTO"""
    with pytest.raises(ValueError, match="Nombre y email son requeridos"):
        UhubOrgFormDTO(
            le_name="",
            le_email="",
            le_phone="123456789",
            le_jurisdiction="Test Jurisdiction",
            le_aoi="Test AOI",
            le_role="Test Role",
            cb_type="INFORMATIVE",
        )


def test_org_form_to_service_dto():
    """Test conversión de UhubOrgFormDTO a UhubOrgServiceDTO"""
    org_form_dto = UhubOrgFormDTO(
        le_name="Test Organization",
        le_email="test@example.com",
        le_phone="123456789",
        le_jurisdiction="Test Jurisdiction",
        le_aoi="Test AOI",
        le_role="Test Role",
        cb_type="INFORMATIVE",
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    org_service_dto = org_form_dto.to_service_dto(context_data)

    assert org_service_dto.id == 0
    assert org_service_dto.created_at is None
    assert org_service_dto.updated_at is None
    assert org_service_dto.modified_by == context_data["modified_by"]
    assert org_service_dto.environment_id == context_data["environment_id"]


def test_org_form_from_service_dto(sample_org_service_dto):
    """Test conversión de UhubOrgServiceDTO a UhubOrgFormDTO"""
    org_service_dto = sample_org_service_dto

    org_form_dto = UhubOrgFormDTO.from_service_dto(org_service_dto)

    assert org_form_dto.le_name == org_service_dto.name
    assert org_form_dto.le_email == org_service_dto.email
    assert org_form_dto.le_phone == org_service_dto.phone
    assert org_form_dto.le_jurisdiction == org_service_dto.jurisdiction
    assert org_form_dto.le_aoi == org_service_dto.aoi
    assert org_form_dto.le_role == org_service_dto.role
    assert org_form_dto.cb_type == org_service_dto.type


# Añadir estas pruebas al final del archivo test_asset_dto.py


def test_uhub_user_service_dtos():
    """Test DTOs de UhubUser (Creación con datos obligatorios y opcionales en None)"""
    # UhubUserServiceDTO con datos completos
    user_service_dto1 = UhubUserServiceDTO(
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

    assert user_service_dto1.username == "testuser"
    assert user_service_dto1.password == "testpassword"
    assert user_service_dto1.email == "user@example.com"
    assert user_service_dto1.dni == "12345678A"
    assert user_service_dto1.phone == "123456789"
    assert user_service_dto1.type == "USER"
    assert user_service_dto1.role == "Test Role"
    assert user_service_dto1.jurisdiction == "Test Jurisdiction"
    assert user_service_dto1.aoi == "Test AOI"
    assert user_service_dto1.organization_id == 1

    # UhubUserServiceDTO con datos opcionales en None
    user_service_dto2 = UhubUserServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
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

    assert user_service_dto2.created_at is None
    assert user_service_dto2.updated_at is None


def test_uhub_user_table_from_service_dto(sample_uhub_user_service_dto):
    """Test creación de UhubUserTableDTO desde UhubUserServiceDTO"""
    user_service_dto = sample_uhub_user_service_dto

    user_table_dto = UhubUserTableDTO.from_service_dto(
        user_service_dto, org_name="Test Organization"
    )

    assert user_table_dto.id == user_service_dto.id
    assert user_table_dto.username == user_service_dto.username
    assert user_table_dto.email == user_service_dto.email
    assert user_table_dto.created_at != "Not assigned"
    assert user_table_dto.updated_at != "Not assigned"
    assert user_table_dto.modified_by == user_service_dto.modified_by
    assert user_table_dto.organization == "Test Organization"


def test_uhub_user_form_dto_validation():
    """Test validaciones en UhubUserFormDTO"""
    with pytest.raises(ValueError, match="Email y username son requeridos"):
        UhubUserFormDTO(
            le_email="",
            le_dni="12345678A",
            le_phone="123456789",
            le_username="",
            le_password="password123",
            cb_type="USER",
            le_role="Test Role",
            le_jurisdiction="Test Jurisdiction",
            le_aoi="Test AOI",
            cb_organization=1,
        )


def test_uhub_user_form_to_service_dto():
    """Test conversión de UhubUserFormDTO a UhubUserServiceDTO"""
    user_form_dto = UhubUserFormDTO(
        le_email="user@example.com",
        le_dni="12345678A",
        le_phone="123456789",
        le_username="testuser",
        le_password="password123",
        cb_type="USER",
        le_role="Test Role",
        le_jurisdiction="Test Jurisdiction",
        le_aoi="Test AOI",
        cb_organization=1,
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    user_service_dto = user_form_dto.to_service_dto(context_data)

    assert user_service_dto.id == 0
    assert user_service_dto.created_at is None
    assert user_service_dto.updated_at is None
    assert user_service_dto.modified_by == context_data["modified_by"]
    assert user_service_dto.environment_id == context_data["environment_id"]


def test_uhub_user_form_from_service_dto(sample_uhub_user_service_dto):
    """Test conversión de UhubUserServiceDTO a UhubUserFormDTO"""
    user_service_dto = sample_uhub_user_service_dto

    user_form_dto = UhubUserFormDTO.from_service_dto(user_service_dto)

    assert user_form_dto.le_email == user_service_dto.email
    assert user_form_dto.le_dni == user_service_dto.dni
    assert user_form_dto.le_phone == user_service_dto.phone
    assert user_form_dto.le_username == user_service_dto.username
    assert user_form_dto.le_password == user_service_dto.password
    assert user_form_dto.cb_type == user_service_dto.type
    assert user_form_dto.le_role == user_service_dto.role
    assert user_form_dto.le_jurisdiction == user_service_dto.jurisdiction
    assert user_form_dto.le_aoi == user_service_dto.aoi
    assert user_form_dto.cb_organization == user_service_dto.organization_id


def test_uas_zone_service_dtos():
    """Test DTOs de UasZone (Creación con datos obligatorios y opcionales en None)"""
    # UasZoneServiceDTO con datos completos
    zone_service_dto1 = UasZoneServiceDTO(
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

    assert zone_service_dto1.name == "Test Zone"
    assert zone_service_dto1.area_type == "POLYGON"
    assert zone_service_dto1.lower_limit == 0
    assert zone_service_dto1.upper_limit == 120
    assert zone_service_dto1.reference_lower == "AGL"
    assert zone_service_dto1.reference_upper == "AGL"
    assert zone_service_dto1.application == "TEMPORAL"
    assert zone_service_dto1.restriction_type == "INFORMATIVE"
    assert zone_service_dto1.message == "Test message"
    assert zone_service_dto1.clearance_required is False
    assert zone_service_dto1.reasons == [1, 2]
    assert zone_service_dto1.organizations == [1, 3]

    # UasZoneServiceDTO con datos opcionales en None
    zone_service_dto2 = UasZoneServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        name="Test Zone",
        area_type="CIRCLE",
        circle_radius=500,
        corridor_width=None,
        lower_limit=0,
        upper_limit=120,
        reference_lower="AGL",
        reference_upper="AGL",
        application="TEMPORAL",
        restriction_type="INFORMATIVE",
        message=None,
        clearance_required=True,
        reasons=[],
        organizations=[],
    )

    assert zone_service_dto2.created_at is None
    assert zone_service_dto2.updated_at is None
    assert zone_service_dto2.circle_radius == 500
    assert zone_service_dto2.message is None


def test_uas_zone_table_from_service_dto(sample_uas_zone_service_dto):
    """Test creación de UasZoneTableDTO desde UasZoneServiceDTO"""
    zone_service_dto = sample_uas_zone_service_dto

    zone_table_dto = UasZoneTableDTO.from_service_dto(
        zone_service_dto, reasons=["Security", "Event"], organizations=["Org1", "Org2"]
    )

    assert zone_table_dto.id == zone_service_dto.id
    assert zone_table_dto.name == zone_service_dto.name
    assert zone_table_dto.area_type == zone_service_dto.area_type
    assert zone_table_dto.restriction_type == zone_service_dto.restriction_type
    assert zone_table_dto.application == zone_service_dto.application
    assert zone_table_dto.created_at != "Not assigned"
    assert zone_table_dto.updated_at != "Not assigned"
    assert zone_table_dto.modified_by == zone_service_dto.modified_by
    assert "0-120 ft AGL" in zone_table_dto.limits
    assert "Security, Event" == zone_table_dto.reasons
    assert "Org1, Org2" == zone_table_dto.organizations


def test_uas_zone_table_from_service_dto_no_data(sample_uas_zone_service_dto):
    """Test creación de UasZoneTableDTO sin razones ni organizaciones"""
    zone_service_dto = sample_uas_zone_service_dto

    zone_table_dto = UasZoneTableDTO.from_service_dto(
        zone_service_dto, reasons=None, organizations=None
    )

    assert zone_table_dto.reasons == "N/A"
    assert zone_table_dto.organizations == "N/A"


def test_uas_zone_form_dto_validation():
    """Test validaciones en UasZoneFormDTO"""
    # Test nombre requerido
    with pytest.raises(ValueError, match="El nombre es requerido"):
        UasZoneFormDTO(
            le_name="",
            cb_area_type="POLYGON",
            le_lower_limit=0,
            le_upper_limit=120,
        )

    # Test radio requerido para área circular
    with pytest.raises(ValueError, match="Radio requerido para área circular"):
        UasZoneFormDTO(
            le_name="Test Zone",
            cb_area_type="CIRCLE",
            le_radius=None,
            le_lower_limit=0,
            le_upper_limit=120,
        )

    # Test ancho requerido para corredor
    with pytest.raises(ValueError, match="Ancho requerido para corredor"):
        UasZoneFormDTO(
            le_name="Test Zone",
            cb_area_type="CORRIDOR",
            le_width=None,
            le_lower_limit=0,
            le_upper_limit=120,
        )


def test_uas_zone_form_to_service_dto():
    """Test conversión de UasZoneFormDTO a UasZoneServiceDTO"""
    zone_form_dto = UasZoneFormDTO(
        le_name="Test Zone",
        cb_area_type="POLYGON",
        le_lower_limit=0,
        le_upper_limit=120,
        cb_reference_lower="AGL",
        cb_reference_upper="AGL",
        cb_application="TEMPORAL",
        cb_restriction_type="INFORMATIVE",
        le_message="Test message",
        cb_clearance=True,
        lw_reasons=[1, 2],
        lw_orgs=[3, 4],
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    zone_service_dto = zone_form_dto.to_service_dto(context_data)

    assert zone_service_dto.id == 0
    assert zone_service_dto.created_at is None
    assert zone_service_dto.updated_at is None
    assert zone_service_dto.modified_by == context_data["modified_by"]
    assert zone_service_dto.environment_id == context_data["environment_id"]
    assert zone_service_dto.clearance_required is True
    assert zone_service_dto.reasons == [1, 2]
    assert zone_service_dto.organizations == [3, 4]


def test_uas_zone_form_from_service_dto(sample_uas_zone_service_dto):
    """Test conversión de UasZoneServiceDTO a UasZoneFormDTO"""
    zone_service_dto = sample_uas_zone_service_dto

    zone_form_dto = UasZoneFormDTO.from_service_dto(zone_service_dto)

    assert zone_form_dto.le_name == zone_service_dto.name
    assert zone_form_dto.cb_area_type == zone_service_dto.area_type
    assert zone_form_dto.le_radius == zone_service_dto.circle_radius
    assert zone_form_dto.le_width == zone_service_dto.corridor_width
    assert zone_form_dto.le_lower_limit == zone_service_dto.lower_limit
    assert zone_form_dto.le_upper_limit == zone_service_dto.upper_limit
    assert zone_form_dto.cb_reference_lower == zone_service_dto.reference_lower
    assert zone_form_dto.cb_reference_upper == zone_service_dto.reference_upper
    assert zone_form_dto.cb_application == zone_service_dto.application
    assert zone_form_dto.cb_restriction_type == zone_service_dto.restriction_type
    assert zone_form_dto.le_message == (zone_service_dto.message or "")
    assert zone_form_dto.cb_clearance == zone_service_dto.clearance_required
    assert zone_form_dto.lw_reasons == zone_service_dto.reasons
    assert zone_form_dto.lw_orgs == zone_service_dto.organizations


def test_uspace_service_dtos():
    """Test DTOs de Uspace (Creación con datos obligatorios y opcionales en None)"""
    # UspaceServiceDTO con datos completos
    uspace_service_dto1 = UspaceServiceDTO(
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

    assert uspace_service_dto1.code == "USPACE001"
    assert uspace_service_dto1.name == "Test Uspace"
    assert uspace_service_dto1.sectors_count == 5
    assert uspace_service_dto1.file_id == 1

    # UspaceServiceDTO con datos opcionales en None
    uspace_service_dto2 = UspaceServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        code="USPACE002",
        name="Test Uspace 2",
        sectors_count=3,
        file_id=2,
    )

    assert uspace_service_dto2.created_at is None
    assert uspace_service_dto2.updated_at is None


def test_uspace_table_from_service_dto(sample_uspace_service_dto):
    """Test creación de UspaceTableDTO desde UspaceServiceDTO"""
    uspace_service_dto = sample_uspace_service_dto

    uspace_table_dto = UspaceTableDTO.from_service_dto(
        uspace_service_dto, file_name="test_file.xml"
    )

    assert uspace_table_dto.id == uspace_service_dto.id
    assert uspace_table_dto.code == uspace_service_dto.code
    assert uspace_table_dto.name == uspace_service_dto.name
    assert uspace_table_dto.sectors_count == uspace_service_dto.sectors_count
    assert uspace_table_dto.file_name == "test_file.xml"
    assert uspace_table_dto.file_id == uspace_service_dto.file_id
    assert uspace_table_dto.created_at != "Not assigned"
    assert uspace_table_dto.updated_at != "Not assigned"
    assert uspace_table_dto.modified_by == uspace_service_dto.modified_by


def test_uspace_table_from_service_dto_no_file(sample_uspace_service_dto):
    """Test creación de UspaceTableDTO sin nombre de archivo"""
    uspace_service_dto = sample_uspace_service_dto

    uspace_table_dto = UspaceTableDTO.from_service_dto(uspace_service_dto)

    assert uspace_table_dto.file_name == "N/A"


def test_uspace_form_dto_validation():
    """Test validaciones en UspaceFormDTO"""
    with pytest.raises(ValueError, match="Código y nombre son requeridos"):
        UspaceFormDTO(
            le_code="",
            le_name="",
            le_sectors_count=5,
        )


def test_uspace_form_to_service_dto():
    """Test conversión de UspaceFormDTO a UspaceServiceDTO"""
    uspace_form_dto = UspaceFormDTO(
        le_code="USPACE001",
        le_name="Test Uspace",
        le_sectors_count=5,
        existing_file_id=1,
    )

    context_data = {
        "modified_by": "test_user",
        "environment_id": 1,
    }

    uspace_service_dto = uspace_form_dto.to_service_dto(context_data)

    assert uspace_service_dto.id == 0
    assert uspace_service_dto.created_at is None
    assert uspace_service_dto.updated_at is None
    assert uspace_service_dto.modified_by == context_data["modified_by"]
    assert uspace_service_dto.environment_id == context_data["environment_id"]
    assert uspace_service_dto.file_id == 1


def test_uspace_form_from_service_dto(sample_uspace_service_dto):
    """Test conversión de UspaceServiceDTO a UspaceFormDTO"""
    uspace_service_dto = sample_uspace_service_dto

    uspace_form_dto = UspaceFormDTO.from_service_dto(uspace_service_dto)

    assert uspace_form_dto.le_code == uspace_service_dto.code
    assert uspace_form_dto.le_name == uspace_service_dto.name
    assert uspace_form_dto.le_sectors_count == uspace_service_dto.sectors_count
    assert uspace_form_dto.existing_file_id == uspace_service_dto.file_id
