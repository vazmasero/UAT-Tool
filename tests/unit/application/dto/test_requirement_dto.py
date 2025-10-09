from datetime import datetime

import pytest

from uat_tool.application.dto import (
    RequirementFormDTO,
    RequirementServiceDTO,
    RequirementTableDTO,
)


def test_requirement_service_dto_creation():
    """Test creación de RequirementServiceDTO con datos completos y opcionales en None"""
    # RequirementServiceDTO con datos completos
    created_at = datetime.now()
    updated_at = datetime.now()

    requirement_service_dto1 = RequirementServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=created_at,
        updated_at=updated_at,
        code="REQ001",
        definition="Test requirement definition with enough characters",
        systems=[1, 2, 3],
        sections=[1, 2],
    )

    assert requirement_service_dto1.id == 1
    assert requirement_service_dto1.code == "REQ001"
    assert (
        requirement_service_dto1.definition
        == "Test requirement definition with enough characters"
    )
    assert requirement_service_dto1.systems == [1, 2, 3]
    assert requirement_service_dto1.sections == [1, 2]

    # RequirementServiceDTO con datos opcionales en None
    requirement_service_dto2 = RequirementServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        code="REQ002",
        definition="Another test requirement definition",
        systems=[],
        sections=[],
    )

    assert requirement_service_dto2.created_at is None
    assert requirement_service_dto2.updated_at is None
    assert requirement_service_dto2.systems == []
    assert requirement_service_dto2.sections == []


def test_requirement_table_dto_from_service_dto(sample_requirement_service_dto):
    """Test creación de RequirementTableDTO desde RequirementServiceDTO"""
    requirement_service_dto = sample_requirement_service_dto

    requirement_table_dto = RequirementTableDTO.from_service_dto(
        requirement_service_dto,
        system_names=["System A", "System B", "System C"],
        section_names=["Section 1", "Section 2"],
    )

    assert requirement_table_dto.id == requirement_service_dto.id
    assert requirement_table_dto.code == requirement_service_dto.code
    assert requirement_table_dto.definition == requirement_service_dto.definition
    assert requirement_table_dto.systems == "System A, System B, System C"
    assert requirement_table_dto.sections == "Section 1, Section 2"
    assert requirement_table_dto.created_at != "Not assigned"
    assert requirement_table_dto.updated_at != "Not assigned"
    assert requirement_table_dto.modified_by == requirement_service_dto.modified_by


def test_requirement_table_dto_from_service_dto_no_enrichments(
    sample_requirement_service_dto,
):
    """Test creación de RequirementTableDTO sin datos enriquecidos"""
    requirement_service_dto = sample_requirement_service_dto

    requirement_table_dto = RequirementTableDTO.from_service_dto(
        requirement_service_dto
    )

    assert requirement_table_dto.systems == "N/A"
    assert requirement_table_dto.sections == "N/A"


def test_requirement_table_dto_from_service_dto_empty_lists(
    sample_requirement_service_dto,
):
    """Test creación de RequirementTableDTO con listas vacías en enriquecimientos"""
    requirement_service_dto = sample_requirement_service_dto

    requirement_table_dto = RequirementTableDTO.from_service_dto(
        requirement_service_dto, system_names=[], section_names=[]
    )

    assert requirement_table_dto.systems == "N/A"
    assert requirement_table_dto.sections == "N/A"


def test_requirement_table_dto_from_service_dto_none_enrichments(
    sample_requirement_service_dto,
):
    """Test creación de RequirementTableDTO con enriquecimientos None"""
    requirement_service_dto = sample_requirement_service_dto

    requirement_table_dto = RequirementTableDTO.from_service_dto(
        requirement_service_dto, system_names=None, section_names=None
    )

    assert requirement_table_dto.systems == "N/A"
    assert requirement_table_dto.sections == "N/A"


def test_requirement_table_dto_creation():
    """Test creación directa de RequirementTableDTO"""
    table_dto = RequirementTableDTO(
        id=1,
        created_at="01/01/2024 10:00",
        updated_at="01/01/2024 11:00",
        modified_by="test_user",
        code="REQ001",
        definition="Test requirement definition",
        systems="System A, System B",
        sections="Section 1",
    )

    assert table_dto.id == 1
    assert table_dto.code == "REQ001"
    assert table_dto.definition == "Test requirement definition"
    assert table_dto.systems == "System A, System B"
    assert table_dto.sections == "Section 1"


def test_requirement_form_dto_creation_and_validation():
    """Test creación y validación de RequirementFormDTO"""
    # Test creación exitosa
    form_dto = RequirementFormDTO(
        le_code="REQ001", le_definition="Definición válida con más de 10 caracteres"
    )

    assert form_dto.le_code == "REQ001"
    assert form_dto.le_definition == "Definición válida con más de 10 caracteres"

    # Test con campos opcionales
    form_dto_with_optional = RequirementFormDTO(
        le_code="REQ002",
        le_definition="Otra definición válida con más de 10 caracteres también",
        lw_systems=[1, 2, 3],
        lw_sections=[4, 5],
    )

    assert form_dto_with_optional.lw_systems == [1, 2, 3]
    assert form_dto_with_optional.lw_sections == [4, 5]


def test_requirement_form_dto_validation_errors():
    """Test validaciones fallidas en RequirementFormDTO"""
    # Test definición muy corta
    with pytest.raises(
        ValueError, match="La definición debe tener al menos 10 caracteres"
    ):
        RequirementFormDTO(le_code="REQ001", le_definition="corta")

    # Test código vacío
    with pytest.raises(ValueError, match="La versión del sistema es requerida"):
        RequirementFormDTO(
            le_code="", le_definition="Definición válida con más de 10 caracteres"
        )

    # Test código solo espacios
    with pytest.raises(ValueError, match="La versión del sistema es requerida"):
        RequirementFormDTO(
            le_code="   ", le_definition="Definición válida con más de 10 caracteres"
        )

    # Test definición solo espacios
    with pytest.raises(
        ValueError, match="La definición debe tener al menos 10 caracteres"
    ):
        RequirementFormDTO(le_code="REQ001", le_definition="   ")


def test_requirement_form_dto_to_service_dto():
    """Test conversión de RequirementFormDTO a RequirementServiceDTO"""
    form_dto = RequirementFormDTO(
        le_code="REQ001",
        le_definition="Definición con más de 10 caracteres para ser válida",
        lw_systems=[1, 2],
        lw_sections=[3, 4],
    )

    context_data = {"modified_by": "test_user", "environment_id": 1}

    service_dto = form_dto.to_service_dto(context_data)

    assert service_dto.id == 0
    assert service_dto.code == "REQ001"
    assert (
        service_dto.definition == "Definición con más de 10 caracteres para ser válida"
    )
    assert service_dto.systems == [1, 2]
    assert service_dto.sections == [3, 4]
    assert service_dto.modified_by == "test_user"
    assert service_dto.environment_id == 1
    assert service_dto.created_at is None
    assert service_dto.updated_at is None


def test_requirement_form_dto_to_service_dto_empty_lists():
    """Test conversión de RequirementFormDTO a RequirementServiceDTO con listas vacías"""
    form_dto = RequirementFormDTO(
        le_code="REQ002",
        le_definition="Otra definición válida con suficientes caracteres",
        lw_systems=[],
        lw_sections=[],
    )

    context_data = {"modified_by": "another_user", "environment_id": 2}

    service_dto = form_dto.to_service_dto(context_data)

    assert service_dto.systems == []
    assert service_dto.sections == []


def test_requirement_form_from_service_dto(sample_requirement_service_dto):
    """Test conversión de RequirementServiceDTO a RequirementFormDTO"""
    requirement_service_dto = sample_requirement_service_dto

    form_dto = RequirementFormDTO.from_service_dto(requirement_service_dto)

    assert form_dto.le_code == requirement_service_dto.code
    assert form_dto.le_definition == requirement_service_dto.definition
    assert form_dto.lw_systems == requirement_service_dto.systems
    assert form_dto.lw_sections == requirement_service_dto.sections


def test_requirement_table_dto_date_formatting():
    """Test formateo correcto de fechas en RequirementTableDTO"""
    # Test con fechas None
    requirement_service_dto_none_dates = RequirementServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=None,
        updated_at=None,
        code="REQ001",
        definition="Test requirement definition",
        systems=[],
        sections=[],
    )

    table_dto = RequirementTableDTO.from_service_dto(requirement_service_dto_none_dates)

    assert table_dto.created_at == "Not assigned"
    assert table_dto.updated_at == "Not assigned"

    # Test con fechas válidas
    test_date = datetime(2024, 1, 15, 14, 30, 0)
    requirement_service_dto_with_dates = RequirementServiceDTO(
        id=2,
        environment_id=1,
        modified_by="test_user",
        created_at=test_date,
        updated_at=test_date,
        code="REQ002",
        definition="Another test requirement definition",
        systems=[],
        sections=[],
    )

    table_dto_with_dates = RequirementTableDTO.from_service_dto(
        requirement_service_dto_with_dates
    )

    assert table_dto_with_dates.created_at == "15/01/2024 14:30"
    assert table_dto_with_dates.updated_at == "15/01/2024 14:30"


def test_requirement_service_dto_to_dict():
    """Test conversión de RequirementServiceDTO a diccionario"""
    created_at = datetime.now()
    updated_at = datetime.now()

    service_dto = RequirementServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=created_at,
        updated_at=updated_at,
        code="REQ001",
        definition="Test requirement definition",
        systems=[1, 2],
        sections=[3, 4],
    )

    dto_dict = service_dto.to_dict()

    assert dto_dict["id"] == 1
    assert dto_dict["code"] == "REQ001"
    assert dto_dict["definition"] == "Test requirement definition"
    assert dto_dict["systems"] == [1, 2]
    assert dto_dict["sections"] == [3, 4]
    assert dto_dict["modified_by"] == "test_user"
    assert dto_dict["environment_id"] == 1


def test_requirement_form_dto_edge_cases():
    """Test casos edge en RequirementFormDTO"""
    # Test con definición exactamente en el límite (10 caracteres)
    form_dto_exact = RequirementFormDTO(
        le_code="REQ001",
        le_definition="1234567890",  # Exactamente 10 caracteres
    )

    assert form_dto_exact.le_definition == "1234567890"

    # Test con muchos sistemas y secciones
    form_dto_many_items = RequirementFormDTO(
        le_code="REQ999",
        le_definition="Definición con muchos sistemas y secciones asignadas",
        lw_systems=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        lw_sections=[11, 12, 13, 14, 15],
    )

    assert len(form_dto_many_items.lw_systems) == 10
    assert len(form_dto_many_items.lw_sections) == 5


def test_requirement_table_dto_single_items():
    """Test RequirementTableDTO con un solo sistema y sección"""
    requirement_service_dto = RequirementServiceDTO(
        id=1,
        environment_id=1,
        modified_by="test_user",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        code="REQ001",
        definition="Test requirement definition",
        systems=[1],
        sections=[2],
    )

    table_dto = RequirementTableDTO.from_service_dto(
        requirement_service_dto,
        system_names=["Single System"],
        section_names=["Single Section"],
    )

    assert table_dto.systems == "Single System"
    assert table_dto.sections == "Single Section"
