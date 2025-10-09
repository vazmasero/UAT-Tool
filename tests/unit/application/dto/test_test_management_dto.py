from datetime import datetime

import pytest

from uat_tool.application.dto import (
    BlockFormDTO,
    BlockServiceDTO,
    BlockTableDTO,
    CampaignFormDTO,
    CampaignServiceDTO,
    CampaignTableDTO,
    CaseFormDTO,
    CaseServiceDTO,
    CaseTableDTO,
    StepFormDTO,
    StepServiceDTO,
    StepTableDTO,
)


# ===== STEP TESTS =====
def test_step_service_dto_creation():
    """Test creación de StepServiceDTO con datos completos y opcionales"""
    # StepServiceDTO con datos completos
    step_service_dto1 = StepServiceDTO(
        id=1,
        action="Click on button",
        expected_result="Modal opens",
        comments="Test step comments",
        case_id=1,
        requirements=[1, 2, 3],
    )

    assert step_service_dto1.id == 1
    assert step_service_dto1.action == "Click on button"
    assert step_service_dto1.expected_result == "Modal opens"
    assert step_service_dto1.comments == "Test step comments"
    assert step_service_dto1.case_id == 1
    assert step_service_dto1.requirements == [1, 2, 3]

    # StepServiceDTO con datos opcionales por defecto
    step_service_dto2 = StepServiceDTO(
        id=0,
        action="Another action",
        expected_result="Another result",
        comments="",
        case_id=0,
        requirements=[],
    )

    assert step_service_dto2.id == 0
    assert step_service_dto2.comments == ""
    assert step_service_dto2.requirements == []


def test_step_table_dto_from_service_dto():
    """Test creación de StepTableDTO desde StepServiceDTO"""
    step_service_dto = StepServiceDTO(
        id=1,
        action="Test action",
        expected_result="Expected result",
        comments="Step comments",
        requirements=[1, 2],
    )

    step_table_dto = StepTableDTO.from_service_dto(
        step_service_dto, requirement_codes=["REQ001", "REQ002"]
    )

    assert step_table_dto.id == step_service_dto.id
    assert step_table_dto.action == step_service_dto.action
    assert step_table_dto.expected_result == step_service_dto.expected_result
    assert step_table_dto.comments == step_service_dto.comments
    assert step_table_dto.requirements == "REQ001, REQ002"


def test_step_table_dto_from_service_dto_no_requirements():
    """Test StepTableDTO sin requisitos"""
    step_service_dto = StepServiceDTO(
        id=1,
        action="Test action",
        expected_result="Expected result",
        comments="Step comments",
        requirements=[],
    )

    step_table_dto = StepTableDTO.from_service_dto(step_service_dto)

    assert step_table_dto.requirements == "N/A"


def test_step_form_dto_creation_and_validation():
    """Test creación y validación de StepFormDTO"""
    # Test creación exitosa
    step_form_dto = StepFormDTO(
        le_action="Valid action",
        le_expected_result="Valid expected result",
        le_comments="Optional comments",
        lw_requirements=[1, 2],
    )

    assert step_form_dto.le_action == "Valid action"
    assert step_form_dto.le_expected_result == "Valid expected result"
    assert step_form_dto.le_comments == "Optional comments"
    assert step_form_dto.lw_requirements == [1, 2]


def test_step_form_dto_validation_errors():
    """Test validaciones fallidas en StepFormDTO"""
    # Test acción vacía
    with pytest.raises(ValueError, match="La acción es requerida"):
        StepFormDTO(
            le_action="",
            le_expected_result="Valid result",
            le_comments="Comments",
        )

    # Test resultado esperado vacío
    with pytest.raises(ValueError, match="El resultado esperado es requerido"):
        StepFormDTO(
            le_action="Valid action",
            le_expected_result="",
            le_comments="Comments",
        )

    # Test solo espacios
    with pytest.raises(ValueError, match="La acción es requerida"):
        StepFormDTO(
            le_action="   ",
            le_expected_result="Valid result",
            le_comments="Comments",
        )


def test_step_form_dto_to_service_dto():
    """Test conversión de StepFormDTO a StepServiceDTO"""
    step_form_dto = StepFormDTO(
        le_action="Test action",
        le_expected_result="Test result",
        le_comments="Test comments",
        lw_requirements=[1, 2, 3],
    )

    service_dto = step_form_dto.to_service_dto()

    assert service_dto.action == "Test action"
    assert service_dto.expected_result == "Test result"
    assert service_dto.comments == "Test comments"
    assert service_dto.requirements == [1, 2, 3]
    assert service_dto.id == 0
    assert service_dto.case_id == 0


def test_step_form_from_service_dto():
    """Test conversión de StepServiceDTO a StepFormDTO"""
    step_service_dto = StepServiceDTO(
        id=1,
        action="Test action",
        expected_result="Test result",
        comments="Test comments",
        case_id=5,
        requirements=[1, 2],
    )

    step_form_dto = StepFormDTO.from_service_dto(step_service_dto)

    assert step_form_dto.le_action == step_service_dto.action
    assert step_form_dto.le_expected_result == step_service_dto.expected_result
    assert step_form_dto.le_comments == step_service_dto.comments
    assert step_form_dto.lw_requirements == step_service_dto.requirements


# ===== CASE TESTS =====
def test_case_service_dto_creation():
    """Test creación de CaseServiceDTO con datos completos y opcionales"""
    created_at = datetime.now()
    updated_at = datetime.now()

    # CaseServiceDTO con datos completos
    case_service_dto1 = CaseServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=created_at,
        updated_at=updated_at,
        code="CASE001",
        name="Test Case",
        comments="Case comments",
        operators=[1, 2],
        drones=[3, 4],
        uhub_users=[5, 6],
        uas_zones=[7, 8],
        systems=[9, 10],
        sections=[11, 12],
        steps=[StepServiceDTO(id=1, action="Step 1", expected_result="Result 1")],
    )

    assert case_service_dto1.id == 1
    assert case_service_dto1.code == "CASE001"
    assert case_service_dto1.name == "Test Case"
    assert case_service_dto1.operators == [1, 2]
    assert case_service_dto1.drones == [3, 4]
    assert len(case_service_dto1.steps) == 1

    # CaseServiceDTO con datos opcionales en None/vacío
    case_service_dto2 = CaseServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        code="CASE002",
        name="Another Case",
        comments="",
        operators=[],
        drones=[],
        uhub_users=[],
        uas_zones=[],
        systems=[],
        sections=[],
        steps=[],
    )

    assert case_service_dto2.created_at is None
    assert case_service_dto2.updated_at is None
    assert case_service_dto2.comments == ""
    assert case_service_dto2.steps == []


def test_case_table_dto_from_service_dto():
    """Test creación de CaseTableDTO desde CaseServiceDTO"""
    case_service_dto = CaseServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="CASE001",
        name="Test Case",
        comments="Case comments",
        steps=[StepServiceDTO(), StepServiceDTO()],  # 2 steps
    )

    case_table_dto = CaseTableDTO.from_service_dto(
        case_service_dto,
        system_names=["System A", "System B"],
        section_names=["Section 1"],
    )

    assert case_table_dto.id == case_service_dto.id
    assert case_table_dto.code == case_service_dto.code
    assert case_table_dto.name == case_service_dto.name
    assert case_table_dto.comments == case_service_dto.comments
    assert case_table_dto.systems == "System A, System B"
    assert case_table_dto.sections == "Section 1"
    assert case_table_dto.steps_count == 2
    assert case_table_dto.created_at != "Not assigned"
    assert case_table_dto.updated_at != "Not assigned"


def test_case_table_dto_from_service_dto_no_enrichments():
    """Test CaseTableDTO sin datos enriquecidos"""
    case_service_dto = CaseServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="CASE001",
        name="Test Case",
        comments="Comments",
        steps=[],
    )

    case_table_dto = CaseTableDTO.from_service_dto(case_service_dto)

    assert case_table_dto.systems == "N/A"
    assert case_table_dto.sections == "N/A"
    assert case_table_dto.steps_count == 0


def test_case_form_dto_creation_and_validation():
    """Test creación y validación de CaseFormDTO"""
    # Test creación exitosa
    step_form = StepFormDTO(
        le_action="Step action",
        le_expected_result="Step result",
        le_comments="Step comments",
    )

    case_form_dto = CaseFormDTO(
        le_code="CASE001",
        le_name="Test Case",
        le_comments="Case comments",
        lw_systems=[1, 2],
        lw_sections=[3],
        lw_operators=[4, 5],
        lw_drones=[6],
        lw_uhub_users=[7],
        lw_uas_zones=[8, 9],
        steps=[step_form],
    )

    assert case_form_dto.le_code == "CASE001"
    assert case_form_dto.le_name == "Test Case"
    assert len(case_form_dto.steps) == 1
    assert case_form_dto.lw_systems == [1, 2]


def test_case_form_dto_validation_errors():
    """Test validaciones fallidas en CaseFormDTO"""
    # Test código vacío
    with pytest.raises(ValueError, match="El código es requerido"):
        CaseFormDTO(
            le_code="",
            le_name="Valid name",
            le_comments="Comments",
        )

    # Test nombre vacío
    with pytest.raises(ValueError, match="El nombre es requerido"):
        CaseFormDTO(
            le_code="CASE001",
            le_name="",
            le_comments="Comments",
        )


def test_case_form_dto_to_service_dto():
    """Test conversión de CaseFormDTO a CaseServiceDTO"""
    step_form = StepFormDTO(
        le_action="Step action",
        le_expected_result="Step result",
        le_comments="Step comments",
        lw_requirements=[1, 2],
    )

    case_form_dto = CaseFormDTO(
        le_code="CASE001",
        le_name="Test Case",
        le_comments="Case comments",
        lw_systems=[1, 2],
        lw_sections=[3, 4],
        lw_operators=[5],
        lw_drones=[6, 7],
        lw_uhub_users=[8],
        lw_uas_zones=[9],
        steps=[step_form],
    )

    context_data = {"modified_by": "test_user", "environment_id": 1}
    service_dto = case_form_dto.to_service_dto(context_data)

    assert service_dto.id == 0
    assert service_dto.code == "CASE001"
    assert service_dto.name == "Test Case"
    assert service_dto.systems == [1, 2]
    assert service_dto.sections == [3, 4]
    assert service_dto.operators == [5]
    assert service_dto.drones == [6, 7]
    assert len(service_dto.steps) == 1
    assert service_dto.modified_by == "test_user"
    assert service_dto.environment_id == 1
    assert service_dto.created_at is None
    assert service_dto.updated_at is None


def test_case_form_from_service_dto():
    """Test conversión de CaseServiceDTO a CaseFormDTO"""
    step_service = StepServiceDTO(
        id=1,
        action="Step action",
        expected_result="Step result",
        comments="Step comments",
        requirements=[1, 2],
    )

    case_service_dto = CaseServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="CASE001",
        name="Test Case",
        comments="Case comments",
        systems=[1, 2],
        sections=[3],
        operators=[4],
        drones=[5],
        uhub_users=[6],
        uas_zones=[7],
        steps=[step_service],
    )

    case_form_dto = CaseFormDTO.from_service_dto(case_service_dto)

    assert case_form_dto.le_code == case_service_dto.code
    assert case_form_dto.le_name == case_service_dto.name
    assert case_form_dto.le_comments == case_service_dto.comments
    assert case_form_dto.lw_systems == case_service_dto.systems
    assert case_form_dto.lw_sections == case_service_dto.sections
    assert case_form_dto.lw_operators == case_service_dto.operators
    assert case_form_dto.lw_drones == case_service_dto.drones
    assert len(case_form_dto.steps) == 1
    assert case_form_dto.steps[0].le_action == "Step action"


# ===== BLOCK TESTS =====
def test_block_service_dto_creation():
    """Test creación de BlockServiceDTO"""
    created_at = datetime.now()
    updated_at = datetime.now()

    block_service_dto = BlockServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=created_at,
        updated_at=updated_at,
        code="BLOCK001",
        name="Test Block",
        system_id=1,
        comments="Block comments",
        cases=[1, 2, 3],
    )

    assert block_service_dto.id == 1
    assert block_service_dto.code == "BLOCK001"
    assert block_service_dto.name == "Test Block"
    assert block_service_dto.system_id == 1
    assert block_service_dto.cases == [1, 2, 3]


def test_block_table_dto_from_service_dto():
    """Test creación de BlockTableDTO desde BlockServiceDTO"""
    block_service_dto = BlockServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="BLOCK001",
        name="Test Block",
        system_id=1,
        comments="Block comments",
        cases=[1, 2, 3],
    )

    block_table_dto = BlockTableDTO.from_service_dto(
        block_service_dto, system_name="Test System"
    )

    assert block_table_dto.id == block_service_dto.id
    assert block_table_dto.code == block_service_dto.code
    assert block_table_dto.name == block_service_dto.name
    assert block_table_dto.system == "Test System"
    assert block_table_dto.comments == block_service_dto.comments
    assert block_table_dto.cases_count == 3


def test_block_table_dto_from_service_dto_no_system():
    """Test BlockTableDTO sin nombre de sistema"""
    block_service_dto = BlockServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="BLOCK001",
        name="Test Block",
        system_id=1,
        comments="Comments",
        cases=[],
    )

    block_table_dto = BlockTableDTO.from_service_dto(block_service_dto)

    assert block_table_dto.system == "Unknown"
    assert block_table_dto.cases_count == 0


def test_block_form_dto_creation_and_validation():
    """Test creación y validación de BlockFormDTO"""
    block_form_dto = BlockFormDTO(
        le_code="BLOCK001",
        le_name="Test Block",
        cb_system="1",
        le_comments="Block comments",
        lw_cases=[1, 2],
    )

    assert block_form_dto.le_code == "BLOCK001"
    assert block_form_dto.le_name == "Test Block"
    assert block_form_dto.cb_system == "1"
    assert block_form_dto.lw_cases == [1, 2]


def test_block_form_dto_validation_errors():
    """Test validaciones fallidas en BlockFormDTO"""
    # Test código vacío
    with pytest.raises(ValueError, match="El código es requerido"):
        BlockFormDTO(
            le_code="",
            le_name="Valid name",
            cb_system="1",
            le_comments="Comments",
        )

    # Test sistema vacío
    with pytest.raises(ValueError, match="El sistema es requerido"):
        BlockFormDTO(
            le_code="BLOCK001",
            le_name="Valid name",
            cb_system="",
            le_comments="Comments",
        )


def test_block_form_dto_to_service_dto():
    """Test conversión de BlockFormDTO a BlockServiceDTO"""
    block_form_dto = BlockFormDTO(
        le_code="BLOCK001",
        le_name="Test Block",
        cb_system="5",
        le_comments="Block comments",
        lw_cases=[1, 2, 3],
    )

    context_data = {"modified_by": "test_user", "environment_id": 1}
    service_dto = block_form_dto.to_service_dto(context_data)

    assert service_dto.id == 0
    assert service_dto.code == "BLOCK001"
    assert service_dto.name == "Test Block"
    assert service_dto.system_id == 5  # Convertido a int
    assert service_dto.comments == "Block comments"
    assert service_dto.cases == [1, 2, 3]
    assert service_dto.modified_by == "test_user"
    assert service_dto.environment_id == 1


def test_block_form_from_service_dto():
    """Test conversión de BlockServiceDTO a BlockFormDTO"""
    block_service_dto = BlockServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="BLOCK001",
        name="Test Block",
        system_id=5,
        comments="Block comments",
        cases=[1, 2],
    )

    block_form_dto = BlockFormDTO.from_service_dto(block_service_dto)

    assert block_form_dto.le_code == block_service_dto.code
    assert block_form_dto.le_name == block_service_dto.name
    assert block_form_dto.cb_system == "5"  # Convertido a string
    assert block_form_dto.le_comments == block_service_dto.comments
    assert block_form_dto.lw_cases == block_service_dto.cases


# ===== CAMPAIGN TESTS =====
def test_campaign_service_dto_creation():
    """Test creación de CampaignServiceDTO"""
    created_at = datetime.now()
    updated_at = datetime.now()

    campaign_service_dto = CampaignServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=created_at,
        updated_at=updated_at,
        code="CAMPAIGN001",
        description="Test campaign description",
        system_id=1,
        system_version="1.0.0",
        comments="Campaign comments",
        status="DRAFT",
        blocks=[1, 2],
    )

    assert campaign_service_dto.id == 1
    assert campaign_service_dto.code == "CAMPAIGN001"
    assert campaign_service_dto.description == "Test campaign description"
    assert campaign_service_dto.system_id == 1
    assert campaign_service_dto.system_version == "1.0.0"
    assert campaign_service_dto.status == "DRAFT"
    assert campaign_service_dto.blocks == [1, 2]


def test_campaign_table_dto_from_service_dto():
    """Test creación de CampaignTableDTO desde CampaignServiceDTO"""
    campaign_service_dto = CampaignServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="CAMPAIGN001",
        description="Test campaign",
        system_id=1,
        system_version="1.0.0",
        comments="Comments",
        status="DRAFT",
        blocks=[1, 2, 3],
    )

    campaign_table_dto = CampaignTableDTO.from_service_dto(
        campaign_service_dto, system_name="Test System"
    )

    assert campaign_table_dto.id == campaign_service_dto.id
    assert campaign_table_dto.code == campaign_service_dto.code
    assert campaign_table_dto.description == campaign_service_dto.description
    assert campaign_table_dto.system == "Test System"
    assert campaign_table_dto.system_version == campaign_service_dto.system_version
    assert campaign_table_dto.status == "DRAFT"
    assert campaign_table_dto.blocks_count == 3


def test_campaign_form_dto_creation_and_validation():
    """Test creación y validación de CampaignFormDTO"""
    campaign_form_dto = CampaignFormDTO(
        le_code="CAMPAIGN001",
        le_description="Test campaign description",
        cb_system="1",
        le_version="1.0.0",
        le_comments="Campaign comments",
        lw_blocks=[1, 2, 3],
    )

    assert campaign_form_dto.le_code == "CAMPAIGN001"
    assert campaign_form_dto.le_description == "Test campaign description"
    assert campaign_form_dto.cb_system == "1"
    assert campaign_form_dto.le_version == "1.0.0"
    assert campaign_form_dto.lw_blocks == [1, 2, 3]


def test_campaign_form_dto_validation_errors():
    """Test validaciones fallidas en CampaignFormDTO"""
    # Test código vacío
    with pytest.raises(ValueError, match="El código es requerido"):
        CampaignFormDTO(
            le_code="",
            le_description="Valid description",
            cb_system="1",
            le_version="1.0.0",
            le_comments="Comments",
            lw_blocks=[1],
        )

    # Test descripción vacía
    with pytest.raises(ValueError, match="La descripción es requerida"):
        CampaignFormDTO(
            le_code="CAMPAIGN001",
            le_description="",
            cb_system="1",
            le_version="1.0.0",
            le_comments="Comments",
            lw_blocks=[1],
        )

    # Test sistema vacío
    with pytest.raises(ValueError, match="El sistema es requerido"):
        CampaignFormDTO(
            le_code="CAMPAIGN001",
            le_description="Valid description",
            cb_system="",
            le_version="1.0.0",
            le_comments="Comments",
            lw_blocks=[1],
        )

    # Test versión vacía
    with pytest.raises(ValueError, match="La versión del sistema es requerida"):
        CampaignFormDTO(
            le_code="CAMPAIGN001",
            le_description="Valid description",
            cb_system="1",
            le_version="",
            le_comments="Comments",
            lw_blocks=[1],
        )

    # Test sin bloques
    with pytest.raises(ValueError, match="Debe seleccionar al menos un bloque de test"):
        CampaignFormDTO(
            le_code="CAMPAIGN001",
            le_description="Valid description",
            cb_system="1",
            le_version="1.0.0",
            le_comments="Comments",
            lw_blocks=[],
        )


def test_campaign_form_dto_to_service_dto():
    """Test conversión de CampaignFormDTO a CampaignServiceDTO"""
    campaign_form_dto = CampaignFormDTO(
        le_code="CAMPAIGN001",
        le_description="Test campaign",
        cb_system="5",
        le_version="2.0.0",
        le_comments="Campaign comments",
        lw_blocks=[1, 2],
    )

    context_data = {"modified_by": "test_user", "environment_id": 1}
    service_dto = campaign_form_dto.to_service_dto(context_data)

    assert service_dto.id == 0
    assert service_dto.code == "CAMPAIGN001"
    assert service_dto.description == "Test campaign"
    assert service_dto.system_id == 5
    assert service_dto.system_version == "2.0.0"
    assert service_dto.comments == "Campaign comments"
    assert service_dto.status == "DRAFT"  # Siempre DRAFT al crear
    assert service_dto.blocks == [1, 2]
    assert service_dto.modified_by == "test_user"
    assert service_dto.environment_id == 1


def test_campaign_form_from_service_dto():
    """Test conversión de CampaignServiceDTO a CampaignFormDTO"""
    campaign_service_dto = CampaignServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="CAMPAIGN001",
        description="Test campaign",
        system_id=5,
        system_version="2.0.0",
        comments="Campaign comments",
        status="IN_PROGRESS",
        blocks=[1, 2],
    )

    campaign_form_dto = CampaignFormDTO.from_service_dto(campaign_service_dto)

    assert campaign_form_dto.le_code == campaign_service_dto.code
    assert campaign_form_dto.le_description == campaign_service_dto.description
    assert campaign_form_dto.cb_system == "5"  # Convertido a string
    assert campaign_form_dto.le_version == campaign_service_dto.system_version
    assert campaign_form_dto.le_comments == campaign_service_dto.comments
    assert campaign_form_dto.lw_blocks == campaign_service_dto.blocks


def test_campaign_table_dto_date_formatting():
    """Test formateo correcto de fechas en CampaignTableDTO"""
    # Test con fechas None
    campaign_service_dto_none_dates = CampaignServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        code="CAMPAIGN001",
        description="Test campaign",
        system_id=1,
        system_version="1.0.0",
        comments="Comments",
        status="DRAFT",
        blocks=[],
    )

    table_dto = CampaignTableDTO.from_service_dto(campaign_service_dto_none_dates)

    assert table_dto.created_at == "Not assigned"
    assert table_dto.updated_at == "Not assigned"

    # Test con fechas válidas
    test_date = datetime(2024, 1, 15, 14, 30, 0)
    campaign_service_dto_with_dates = CampaignServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=test_date,
        updated_at=test_date,
        code="CAMPAIGN002",
        description="Another campaign",
        system_id=1,
        system_version="1.0.0",
        comments="Comments",
        status="DRAFT",
        blocks=[],
    )

    table_dto_with_dates = CampaignTableDTO.from_service_dto(
        campaign_service_dto_with_dates
    )

    assert table_dto_with_dates.created_at == "15/01/2024 14:30"
    assert table_dto_with_dates.updated_at == "15/01/2024 14:30"
