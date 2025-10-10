from dataclasses import is_dataclass
from datetime import datetime

from uat_tool.application.dto import (
    BugServiceDTO,
    BugTableDTO,
    RequirementServiceDTO,
    RequirementTableDTO,
)


class TestBaseDTOs:
    """Tests para DTOs base"""

    def test_base_dto_dataclasses(self):
        """Verifica que todos los DTOs base son dataclasses"""
        from uat_tool.application.dto.base_dto import (
            BaseFormDTO,
            BaseServiceDTO,
            BaseTableDTO,
        )

        assert is_dataclass(BaseServiceDTO)
        assert is_dataclass(BaseTableDTO)
        assert is_dataclass(BaseFormDTO)


class TestDTOConversions:
    """Tests para conversiones entre DTOs"""

    def test_bug_service_to_table_conversion(self):
        """Test conversión de BugServiceDTO a BugTableDTO"""
        service_dto = BugServiceDTO(
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
            urgency="2",
            impact="2",
            requirements=[1, 2],
        )

        table_dto = BugTableDTO.from_service_dto(
            service_dto,
            system_name="Test System",
            requirement_codes=["REQ001", "REQ002"],
            file_name="test.txt",
        )

        assert table_dto.id == 1
        assert table_dto.status == "Open"  # Capitalizado
        assert table_dto.system == "Test System"
        assert table_dto.urgency == "Media"  # Mapeado
        assert table_dto.impact == "Media"  # Mapeado
        assert table_dto.requirements == "REQ001, REQ002"
        assert table_dto.file_name == "test.txt"

    def test_requirement_service_to_table_conversion(self):
        """Test conversión de RequirementServiceDTO a RequirementTableDTO"""
        service_dto = RequirementServiceDTO(
            id=1,
            environment_id=1,
            modified_by="test_user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            code="REQ001",
            definition="Test definition",
            systems=[1, 2],
            sections=[1, 2],
        )

        table_dto = RequirementTableDTO.from_service_dto(
            service_dto,
            system_names=["System A", "System B"],
            section_names=["Section A", "Section B"],
        )

        assert table_dto.code == "REQ001"
        assert table_dto.systems == "System A, System B"
        assert table_dto.sections == "Section A, Section B"

    def test_step_service_to_table_conversion(self):
        """Test conversión de StepServiceDTO a StepTableDTO"""
        from uat_tool.application.dto.test_management_dto import (
            StepServiceDTO,
            StepTableDTO,
        )

        service_dto = StepServiceDTO(
            id=1,
            action="Test action",
            expected_result="Expected result",
            comments="Test comments",
            case_id=1,
            requirements=[1, 2],
        )

        table_dto = StepTableDTO.from_service_dto(
            service_dto, requirement_codes=["REQ001", "REQ002"]
        )

        assert table_dto.action == "Test action"
        assert table_dto.expected_result == "Expected result"
        assert table_dto.requirements == "REQ001, REQ002"


class TestDTOFormatting:
    """Tests para formateo de datos en DTOs"""

    def test_date_formatting(self):
        """Test formateo de fechas en DTOs"""
        from uat_tool.application.dto.base_dto import BaseTableDTO

        test_date = datetime(2024, 1, 1, 10, 30, 0)
        formatted_date = BaseTableDTO._format_date(test_date)

        assert formatted_date == "01/01/2024 10:30"

        # Test con fecha None
        formatted_none = BaseTableDTO._format_date(None)
        assert formatted_none == "N/A"

    def test_urgency_impact_mapping(self):
        """Test mapeo de urgencia e impacto"""
        service_dto = BugServiceDTO(
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
        )

        table_dto = BugTableDTO.from_service_dto(service_dto, system_name="Test System")

        assert table_dto.urgency == "Baja"
        assert table_dto.impact == "Alta"

        # Test con valores desconocidos
        service_dto_unknown = BugServiceDTO(
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
            urgency="5",  # Desconocido
            impact="0",  # Desconocido
            requirements=[],
        )

        table_dto_unknown = BugTableDTO.from_service_dto(
            service_dto_unknown, system_name="Test System"
        )

        assert table_dto_unknown.urgency == "Unknown"
        assert table_dto_unknown.impact == "Unknown"
