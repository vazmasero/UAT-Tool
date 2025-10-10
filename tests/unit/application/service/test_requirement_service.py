from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from uat_tool.application.dto import (
    RequirementFormDTO,
    RequirementServiceDTO,
    RequirementTableDTO,
)
from uat_tool.application.services import RequirementService
from uat_tool.domain import Requirement


@pytest.fixture
def mock_app_context():
    """Mock de ApplicationContext"""
    return Mock()


@pytest.fixture
def mock_uow():
    """Mock de UnitOfWork"""
    uow = Mock()
    uow.req_repo = Mock()
    return uow


@pytest.fixture
def requirement_service(mock_app_context):
    """Instancia del servicio con mocks"""
    mock_app_context.get_unit_of_work_context.return_value.__enter__ = Mock(
        return_value=Mock()
    )
    mock_app_context.get_unit_of_work_context.return_value.__exit__ = Mock(
        return_value=None
    )
    return RequirementService(mock_app_context)


@pytest.fixture
def sample_requirement_model():
    """Modelo Requirement de ejemplo"""
    requirement = Mock(spec=Requirement)
    requirement.id = 1
    requirement.code = "REQ001"
    requirement.definition = "Test requirement definition"
    requirement.environment_id = 1
    requirement.modified_by = "test_user"
    requirement.created_at = datetime.now()
    requirement.updated_at = datetime.now()

    # Mock de relaciones
    system1 = Mock()
    system1.id = 1
    system1.name = "System A"
    system2 = Mock()
    system2.id = 2
    system2.name = "System B"
    requirement.systems = [system1, system2]

    section1 = Mock()
    section1.id = 1
    section1.name = "Section X"
    section2 = Mock()
    section2.id = 2
    section2.name = "Section Y"
    requirement.sections = [section1, section2]

    return requirement


@pytest.fixture
def sample_form_dto():
    """FormDTO de ejemplo"""
    return RequirementFormDTO(
        le_code="REQ001",
        le_definition="Test requirement definition",
        lw_systems=[1, 2],
        lw_sections=[1, 2],
    )


@pytest.fixture
def sample_context():
    """Contexto de ejemplo"""
    return {"modified_by": "test_user", "environment_id": 1}


def test_get_all_requirements(
    requirement_service, mock_app_context, mock_uow, sample_requirement_model
):
    """Test para obtener todos los requisitos"""
    # Setup
    mock_uow.req_repo.get_all_with_relations.return_value = [sample_requirement_model]
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.get_all_requirements()

    # Assert
    mock_uow.req_repo.get_all_with_relations.assert_called_once()
    assert result == [sample_requirement_model]


def test_get_requirement_by_id_found(
    requirement_service, mock_app_context, mock_uow, sample_requirement_model
):
    """Test para obtener requisito por ID (encontrado)"""
    # Setup
    mock_uow.req_repo.get_with_relations.return_value = sample_requirement_model
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.get_requirement_by_id(1)

    # Assert
    mock_uow.req_repo.get_with_relations.assert_called_once_with(1)
    assert result == sample_requirement_model


def test_get_requirement_by_id_not_found(
    requirement_service, mock_app_context, mock_uow
):
    """Test para obtener requisito por ID (no encontrado)"""
    # Setup
    mock_uow.req_repo.get_with_relations.return_value = None
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.get_requirement_by_id(999)

    # Assert
    mock_uow.req_repo.get_with_relations.assert_called_once_with(999)
    assert result is None


def test_get_all_requirements_for_table(
    requirement_service, mock_app_context, mock_uow, sample_requirement_model
):
    """Test para obtener requisitos enriquecidos para tabla"""
    # Setup
    mock_uow.req_repo.get_all_with_relations.return_value = [sample_requirement_model]
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.get_all_requirements_for_table()

    # Assert
    assert len(result) == 1
    assert isinstance(result[0], RequirementTableDTO)
    assert result[0].code == "REQ001"
    assert result[0].systems == "System A, System B"
    assert result[0].sections == "Section X, Section Y"


def test_enrich_requirement_for_table_success(
    requirement_service, sample_requirement_model
):
    """Test para enriquecimiento exitoso de requisito"""
    # Execute
    result = requirement_service._enrich_requirement_for_table(sample_requirement_model)

    # Assert
    assert isinstance(result, RequirementTableDTO)
    assert result.code == "REQ001"
    assert result.systems == "System A, System B"
    assert result.sections == "Section X, Section Y"


def test_enrich_requirement_for_table_exception(
    requirement_service, sample_requirement_model
):
    """Test para enriquecimiento con excepción (fallback)"""
    # Setup - hacer que from_model falle
    with patch(
        "uat_tool.application.dto.RequirementServiceDTO.from_model"
    ) as mock_from_model:
        mock_from_model.side_effect = Exception("Test error")

        # Execute
        result = requirement_service._enrich_requirement_for_table(
            sample_requirement_model
        )

    # Assert - debería devolver un TableDTO básico incluso con error
    assert isinstance(result, RequirementTableDTO)
    assert result.code == "REQ001"  # Aún debería tener los datos básicos


def test_create_requirement_from_form(
    requirement_service,
    mock_app_context,
    mock_uow,
    sample_form_dto,
    sample_context,
    sample_requirement_model,
):
    """Test para crear requisito desde FormDTO"""
    # Setup
    created_requirement = Mock()
    created_requirement.id = 2

    mock_uow.req_repo.create.return_value = created_requirement
    mock_uow.req_repo.get_with_relations.return_value = sample_requirement_model
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.create_requirement_from_form(
        sample_form_dto, sample_context
    )

    # Assert
    mock_uow.req_repo.create.assert_called_once()
    mock_uow.req_repo.get_with_relations.assert_called_once_with(2)
    assert isinstance(result, RequirementServiceDTO)


def test_update_requirement_from_form(
    requirement_service,
    mock_app_context,
    mock_uow,
    sample_form_dto,
    sample_context,
    sample_requirement_model,
):
    """Test para actualizar requisito desde FormDTO"""
    # Setup
    updated_requirement = Mock()
    updated_requirement.id = 1

    mock_uow.req_repo.update.return_value = updated_requirement
    mock_uow.req_repo.get_with_relations.return_value = sample_requirement_model
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.update_requirement_from_form(
        1, sample_form_dto, sample_context
    )

    # Assert
    mock_uow.req_repo.update.assert_called_once()
    mock_uow.req_repo.get_with_relations.assert_called_once_with(1)
    assert isinstance(result, RequirementServiceDTO)


def test_get_requirement_for_edit_found(
    requirement_service, mock_app_context, mock_uow, sample_requirement_model
):
    """Test para obtener requisito para edición (encontrado)"""
    # Setup
    mock_uow.req_repo.get_with_relations.return_value = sample_requirement_model
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.get_requirement_for_edit(1)

    # Assert
    assert isinstance(result, RequirementFormDTO)
    assert result.le_code == "REQ001"


def test_get_requirement_for_edit_not_found(
    requirement_service, mock_app_context, mock_uow
):
    """Test para obtener requisito para edición (no encontrado)"""
    # Setup
    mock_uow.req_repo.get_with_relations.return_value = None
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.get_requirement_for_edit(999)

    # Assert
    assert result is None


def test_delete_requirement_success(requirement_service, mock_app_context, mock_uow):
    """Test para eliminar requisito exitoso"""
    # Setup
    mock_uow.req_repo.delete.return_value = True
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.delete_requirement(1)

    # Assert
    mock_uow.req_repo.delete.assert_called_once_with(1)
    assert result is True


def test_delete_requirement_failure(requirement_service, mock_app_context, mock_uow):
    """Test para eliminar requisito fallido"""
    # Setup
    mock_uow.req_repo.delete.return_value = False
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Execute
    result = requirement_service.delete_requirement(999)

    # Assert
    mock_uow.req_repo.delete.assert_called_once_with(999)
    assert result is False

    # --- Tests para logging ---


def test_log_operation_called(requirement_service, mock_app_context, mock_uow):
    """Test que verifica que se llama al logging de operaciones"""
    # Setup
    mock_uow.req_repo.get_all_with_relations.return_value = []
    mock_app_context.get_unit_of_work_context.return_value.__enter__.return_value = (
        mock_uow
    )

    # Mock del logger de BaseService
    with patch("uat_tool.application.services.base_service.logger") as mock_logger:
        # Execute
        requirement_service.get_all_requirements()

        # Assert - verificar el mensaje específico
        mock_logger.info.assert_called_once()
        call_args = mock_logger.info.call_args
        message = call_args[0][0]  # Primer argumento del primer call

        assert "get_all" in message
        assert "Requirement" in message

    # --- Tests para validación de datos ---


def test_create_with_invalid_form_dto(requirement_service, sample_context):
    """Test que verifica comportamiento con FormDTO inválido"""
    # La validación ocurre al crear el FormDTO, no en to_service_dto
    with pytest.raises(ValueError, match="La definición debe tener al menos 10 caracteres"):
        # Crear FormDTO inválido (definición muy corta) - esto lanzará la excepción
        RequirementFormDTO(
            le_code="REQ001",
            le_definition="Short",  # Menos de 10 caracteres
            lw_systems=[1],
            lw_sections=[1],
        )
