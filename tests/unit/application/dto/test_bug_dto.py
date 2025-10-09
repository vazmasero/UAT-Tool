from datetime import datetime

import pytest

from uat_tool.application.dto import (
    BugDetailDTO,
    BugFormDTO,
    BugHistoryServiceDTO,
    BugHistoryTableDTO,
    BugServiceDTO,
    BugTableDTO,
)


def test_bug_service_dto_creation():
    """Test creación de BugServiceDTO con datos completos y opcionales en None"""
    # BugServiceDTO con datos completos
    created_at = datetime.now()
    updated_at = datetime.now()

    bug_service_dto1 = BugServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=created_at,
        updated_at=updated_at,
        status="OPEN",
        system_id=1,
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="2",
        impact="2",
        campaign_run_id="CR001",
        service_now_id="SN001",
        requirements=[1, 2, 3],
        comments="Test comments",
        file_id=1,
        history=[],
    )

    assert bug_service_dto1.id == 1
    assert bug_service_dto1.status == "OPEN"
    assert bug_service_dto1.system_id == 1
    assert bug_service_dto1.urgency == "2"
    assert bug_service_dto1.impact == "2"
    assert bug_service_dto1.requirements == [1, 2, 3]
    assert bug_service_dto1.campaign_run_id == "CR001"
    assert bug_service_dto1.service_now_id == "SN001"

    # BugServiceDTO con datos opcionales en None
    bug_service_dto2 = BugServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        status="CLOSED SOLVED",
        system_id=2,
        system_version="2.0.0",
        short_description="Another test bug",
        definition="Another test definition",
        urgency="1",
        impact="3",
        campaign_run_id=None,
        service_now_id=None,
        requirements=[],
        comments=None,
        file_id=None,
        history=[],
    )

    assert bug_service_dto2.created_at is None
    assert bug_service_dto2.updated_at is None
    assert bug_service_dto2.campaign_run_id is None
    assert bug_service_dto2.service_now_id is None
    assert bug_service_dto2.comments is None
    assert bug_service_dto2.file_id is None


def test_bug_table_dto_from_service_dto(sample_bug_service_dto):
    """Test creación de BugTableDTO desde BugServiceDTO"""
    bug_service_dto = sample_bug_service_dto

    bug_table_dto = BugTableDTO.from_service_dto(
        bug_service_dto,
        system_name="Test System",
        requirement_codes=["REQ001", "REQ002", "REQ003"],
        file_name="bug_attachment.txt",
    )

    assert bug_table_dto.id == bug_service_dto.id
    assert bug_table_dto.status == "Open"  # Capitalizado
    assert bug_table_dto.system == "Test System"
    assert bug_table_dto.system_version == bug_service_dto.system_version
    assert bug_table_dto.short_description == bug_service_dto.short_description
    assert bug_table_dto.definition == bug_service_dto.definition
    assert bug_table_dto.urgency == "Media"  # Mapeado de "2" a "Media"
    assert bug_table_dto.impact == "Media"  # Mapeado de "2" a "Media"
    assert bug_table_dto.created_at != "Not assigned"
    assert bug_table_dto.updated_at != "Not assigned"
    assert bug_table_dto.modified_by == bug_service_dto.modified_by
    assert bug_table_dto.requirements == "REQ001, REQ002, REQ003"
    assert bug_table_dto.file_name == "bug_attachment.txt"
    assert bug_table_dto.history_count == 0


def test_bug_table_dto_from_service_dto_no_enrichments(sample_bug_service_dto):
    """Test creación de BugTableDTO sin datos enriquecidos"""
    bug_service_dto = sample_bug_service_dto

    bug_table_dto = BugTableDTO.from_service_dto(bug_service_dto)

    assert bug_table_dto.system == "Unknown"
    assert bug_table_dto.requirements == "N/A"
    assert bug_table_dto.file_name == "No file attached"
    assert bug_table_dto.service_now_id == "N/A"
    assert bug_table_dto.campaign_run == "N/A"


def test_bug_table_dto_creation():
    """Test creación directa de BugTableDTO"""
    table_dto = BugTableDTO(
        id=1,
        created_at="01/01/2024 10:00",
        updated_at="01/01/2024 11:00",
        modified_by="test_user",
        status="Open",
        system="Test System",
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="Media",
        impact="Media",
        service_now_id="SN001",
        campaign_run="Test Campaign",
        requirements="REQ001, REQ002",
        comments="Test comments",
        file_name="test.txt",
        file_id=1,
        history_count=3,
    )

    assert table_dto.id == 1
    assert table_dto.status == "Open"
    assert table_dto.system == "Test System"
    assert table_dto.urgency == "Media"
    assert table_dto.impact == "Media"
    assert table_dto.history_count == 3
    assert table_dto.requirements == "REQ001, REQ002"


def test_bug_form_dto_creation_and_validation():
    """Test creación y validación de BugFormDTO"""
    # Test creación exitosa
    form_dto = BugFormDTO(
        cb_status="OPEN",
        cb_system="1",
        le_version="1.0.0",
        cb_urgency=2,
        cb_impact=2,
        le_short_desc="Descripción corta válida",
        le_definition="Definición válida con más de 10 caracteres",
    )

    assert form_dto.cb_status == "OPEN"
    assert form_dto.cb_system == "1"
    assert form_dto.le_version == "1.0.0"
    assert form_dto.cb_urgency == 2
    assert form_dto.cb_impact == 2

    # Test con campos opcionales
    form_dto_with_optional = BugFormDTO(
        cb_status="IN PROGRESS",
        cb_system="2",
        le_version="2.0.0",
        cb_urgency=1,
        cb_impact=3,
        le_short_desc="Otra descripción válida",
        le_definition="Otra definición con más de 10 caracteres también",
        cb_campaign=1,
        lw_requirements=[1, 2, 3],
        le_service_now_id="SN123",
        comments="Comentarios de prueba",
        existing_file_id=5,
    )

    assert form_dto_with_optional.cb_campaign == 1
    assert form_dto_with_optional.lw_requirements == [1, 2, 3]
    assert form_dto_with_optional.le_service_now_id == "SN123"
    assert form_dto_with_optional.comments == "Comentarios de prueba"
    assert form_dto_with_optional.existing_file_id == 5


def test_bug_form_dto_validation_errors():
    """Test validaciones fallidas en BugFormDTO"""
    # Test descripción corta muy corta
    with pytest.raises(
        ValueError, match="La descripción corta debe tener al menos 5 caracteres"
    ):
        BugFormDTO(
            cb_status="OPEN",
            cb_system="1",
            le_version="1.0.0",
            cb_urgency=2,
            cb_impact=2,
            le_short_desc="a",
            le_definition="Definición válida con más de 10 caracteres",
        )

    # Test definición muy corta
    with pytest.raises(
        ValueError, match="La definición debe tener al menos 10 caracteres"
    ):
        BugFormDTO(
            cb_status="OPEN",
            cb_system="1",
            le_version="1.0.0",
            cb_urgency=2,
            cb_impact=2,
            le_short_desc="Descripción válida",
            le_definition="corta",
        )

    # Test versión vacía
    with pytest.raises(ValueError, match="La versión del sistema es requerida"):
        BugFormDTO(
            cb_status="OPEN",
            cb_system="1",
            le_version="",
            cb_urgency=2,
            cb_impact=2,
            le_short_desc="Descripción válida",
            le_definition="Definición con más de 10 caracteres",
        )

    # Test versión solo espacios
    with pytest.raises(ValueError, match="La versión del sistema es requerida"):
        BugFormDTO(
            cb_status="OPEN",
            cb_system="1",
            le_version="   ",
            cb_urgency=2,
            cb_impact=2,
            le_short_desc="Descripción válida",
            le_definition="Definición con más de 10 caracteres",
        )


def test_bug_form_dto_to_service_dto():
    """Test conversión de BugFormDTO a BugServiceDTO"""
    form_dto = BugFormDTO(
        cb_status="OPEN",
        cb_system="1",
        le_version="1.0.0",
        cb_urgency=2,
        cb_impact=2,
        le_short_desc="Descripción corta",
        le_definition="Definición con más de 10 caracteres",
        cb_campaign=1,
        lw_requirements=[1, 2],
        le_service_now_id="SN001",
        comments="Test comments",
        existing_file_id=1,
    )

    context_data = {"modified_by": "test_user", "environment_id": 1}

    service_dto = form_dto.to_service_dto(context_data)

    assert service_dto.id == 0
    assert service_dto.status == "OPEN"
    assert service_dto.system_id == 1
    assert service_dto.system_version == "1.0.0"
    assert service_dto.urgency == "2"  # Convertido a string
    assert service_dto.impact == "2"  # Convertido a string
    assert service_dto.requirements == [1, 2]
    assert service_dto.campaign_run_id == 1
    assert service_dto.service_now_id == "SN001"
    assert service_dto.comments == "Test comments"
    assert service_dto.file_id == 1
    assert service_dto.modified_by == "test_user"
    assert service_dto.environment_id == 1
    assert service_dto.created_at is None
    assert service_dto.updated_at is None
    assert service_dto.history == []


def test_bug_form_dto_to_service_dto_with_none_values():
    """Test conversión de BugFormDTO a BugServiceDTO con valores None"""
    form_dto = BugFormDTO(
        cb_status="CLOSED",
        cb_system="2",
        le_version="2.0.0",
        cb_urgency=1,
        cb_impact=3,
        le_short_desc="Descripción válida",
        le_definition="Definición válida con caracteres suficientes",
        # Campos opcionales vacíos/None
        cb_campaign=None,
        lw_requirements=[],
        le_service_now_id="",
        comments="",
        existing_file_id=None,
    )

    context_data = {"modified_by": "another_user", "environment_id": 2}

    service_dto = form_dto.to_service_dto(context_data)

    assert service_dto.campaign_run_id is None
    assert service_dto.requirements == []
    assert service_dto.service_now_id is None
    assert service_dto.comments is None
    assert service_dto.file_id is None


def test_bug_form_from_service_dto(sample_bug_service_dto):
    """Test conversión de BugServiceDTO a BugFormDTO"""
    bug_service_dto = sample_bug_service_dto

    form_dto = BugFormDTO.from_service_dto(bug_service_dto)

    assert form_dto.cb_status == bug_service_dto.status
    assert form_dto.cb_system == str(bug_service_dto.system_id)  # Convertido a string
    assert form_dto.le_version == bug_service_dto.system_version
    assert form_dto.cb_urgency == int(bug_service_dto.urgency)  # Convertido a int
    assert form_dto.cb_impact == int(bug_service_dto.impact)  # Convertido a int
    assert form_dto.le_short_desc == bug_service_dto.short_description
    assert form_dto.le_definition == bug_service_dto.definition
    assert form_dto.cb_campaign == bug_service_dto.campaign_run_id
    assert form_dto.lw_requirements == bug_service_dto.requirements
    assert form_dto.le_service_now_id == (bug_service_dto.service_now_id or "")
    assert form_dto.comments == (bug_service_dto.comments or "")
    assert form_dto.existing_file_id == bug_service_dto.file_id


def test_bug_history_service_dto_creation():
    """Test creación de BugHistoryServiceDTO"""
    timestamp = datetime.now()

    history_service_dto = BugHistoryServiceDTO(
        id=1,
        bug_id=1,
        changed_by="user1",
        change_timestamp=timestamp,
        change_summary="Bug creado inicialmente",
    )

    assert history_service_dto.id == 1
    assert history_service_dto.bug_id == 1
    assert history_service_dto.changed_by == "user1"
    assert history_service_dto.change_timestamp == timestamp
    assert history_service_dto.change_summary == "Bug creado inicialmente"


def test_bug_history_table_dto_from_service_dto():
    """Test creación de BugHistoryTableDTO desde BugHistoryServiceDTO"""
    timestamp = datetime.now()

    history_service_dto = BugHistoryServiceDTO(
        id=1,
        bug_id=1,
        changed_by="user1",
        change_timestamp=timestamp,
        change_summary="Bug creado inicialmente",
    )

    history_table_dto = BugHistoryTableDTO.from_service_dto(history_service_dto)

    assert history_table_dto.changed_by == "user1"
    assert history_table_dto.change_timestamp == timestamp.strftime("%d/%m/%Y %H:%M")
    assert history_table_dto.change_summary == "Bug creado inicialmente"


def test_bug_history_table_dto_from_service_dto_none_timestamp():
    """Test BugHistoryTableDTO con timestamp None"""
    history_service_dto = BugHistoryServiceDTO(
        id=1,
        bug_id=1,
        changed_by="user1",
        change_timestamp=None,
        change_summary="Sin timestamp",
    )

    history_table_dto = BugHistoryTableDTO.from_service_dto(history_service_dto)

    assert history_table_dto.change_timestamp == "Not assigned"


def test_bug_detail_dto_creation():
    """Test creación de BugDetailDTO"""
    bug_table_dto = BugTableDTO(
        id=1,
        created_at="01/01/2024 10:00",
        updated_at="01/01/2024 11:00",
        modified_by="test_user",
        status="Open",
        system="Test System",
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="Media",
        impact="Media",
    )

    history_items = [
        BugHistoryTableDTO(
            changed_by="user1",
            change_timestamp="01/01/2024 10:00",
            change_summary="Bug creado",
        ),
        BugHistoryTableDTO(
            changed_by="user2",
            change_timestamp="01/01/2024 11:00",
            change_summary="Estado cambiado a In Progress",
        ),
    ]

    detail_dto = BugDetailDTO(bug=bug_table_dto, history=history_items)

    assert detail_dto.bug.id == 1
    assert len(detail_dto.history) == 2
    assert detail_dto.history[0].changed_by == "user1"
    assert detail_dto.history[1].changed_by == "user2"


def test_bug_detail_dto_from_service_dto(sample_bug_service_dto):
    """Test creación de BugDetailDTO desde BugServiceDTO"""
    # Añadir historial al service DTO
    history_item = BugHistoryServiceDTO(
        id=1,
        bug_id=1,
        changed_by="test_user",
        change_timestamp=datetime.now(),
        change_summary="Bug created for testing",
    )

    bug_service_dto_with_history = sample_bug_service_dto
    bug_service_dto_with_history.history = [history_item]

    detail_dto = BugDetailDTO.from_service_dto(
        bug_service_dto_with_history,
        system_name="Test System",
        requirement_codes=["REQ001", "REQ002"],
        file_name="test_file.txt",
    )

    assert detail_dto.bug.id == bug_service_dto_with_history.id
    assert detail_dto.bug.system == "Test System"
    assert len(detail_dto.history) == 1
    assert detail_dto.history[0].changed_by == "test_user"
    assert "created for testing" in detail_dto.history[0].change_summary


def test_bug_table_dto_urgency_impact_mapping():
    """Test mapeo correcto de urgencia e impacto en BugTableDTO"""
    bug_service_dto = BugServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status="OPEN",
        system_id=1,
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="1",  # Baja
        impact="3",  # Alta
        requirements=[],
        history=[],
    )

    bug_table_dto = BugTableDTO.from_service_dto(bug_service_dto)

    assert bug_table_dto.urgency == "Baja"
    assert bug_table_dto.impact == "Alta"

    # Test valores desconocidos
    bug_service_dto_unknown = BugServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        status="OPEN",
        system_id=1,
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="5",  # Valor desconocido
        impact="0",  # Valor desconocido
        requirements=[],
        history=[],
    )

    bug_table_dto_unknown = BugTableDTO.from_service_dto(bug_service_dto_unknown)

    assert bug_table_dto_unknown.urgency == "Unknown"
    assert bug_table_dto_unknown.impact == "Unknown"


def test_bug_table_dto_date_formatting():
    """Test formateo correcto de fechas en BugTableDTO"""
    # Test con fechas None
    bug_service_dto_none_dates = BugServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        status="OPEN",
        system_id=1,
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="2",
        impact="2",
        requirements=[],
        history=[],
    )

    bug_table_dto = BugTableDTO.from_service_dto(bug_service_dto_none_dates)

    assert bug_table_dto.created_at == "Not assigned"
    assert bug_table_dto.updated_at == "Not assigned"

    # Test con fechas válidas
    test_date = datetime(2024, 1, 15, 14, 30, 0)
    bug_service_dto_with_dates = BugServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=test_date,
        updated_at=test_date,
        status="OPEN",
        system_id=1,
        system_version="1.0.0",
        short_description="Test bug",
        definition="Test definition",
        urgency="2",
        impact="2",
        requirements=[],
        history=[],
    )

    bug_table_dto_with_dates = BugTableDTO.from_service_dto(bug_service_dto_with_dates)

    assert bug_table_dto_with_dates.created_at == "15/01/2024 14:30"
    assert bug_table_dto_with_dates.updated_at == "15/01/2024 14:30"
