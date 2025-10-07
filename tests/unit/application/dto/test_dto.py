from dataclasses import is_dataclass
from datetime import datetime

import pytest

from uat_tool.application.dto import (
    BugDetailDTO,
    BugFormDTO,
    BugHistoryServiceDTO,
    BugHistoryTableDTO,
    BugServiceDTO,
    BugTableDTO,
    EmailFormDTO,
    EmailServiceDTO,
    OperatorFormDTO,
    OperatorServiceDTO,
    OperatorTableDTO,
    RequirementFormDTO,
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


class TestBugDTOs:
    """Tests para DTOs de Bug"""

    def test_bug_service_dto_creation(self):
        """Test creación de BugServiceDTO"""
        created_at = datetime.now()
        updated_at = datetime.now()

        service_dto = BugServiceDTO(
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

        assert service_dto.id == 1
        assert service_dto.status == "OPEN"
        assert service_dto.system_id == 1
        assert service_dto.urgency == "2"
        assert service_dto.impact == "2"
        assert service_dto.requirements == [1, 2, 3]

    def test_bug_table_dto_creation(self):
        """Test creación de BugTableDTO"""
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

    def test_bug_form_dto_creation_and_validation(self):
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

        # Test validaciones fallidas
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

    def test_bug_form_dto_to_service_dto(self):
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
        assert service_dto.urgency == "2"
        assert service_dto.impact == "2"
        assert service_dto.requirements == [1, 2]
        assert service_dto.modified_by == "test_user"
        assert service_dto.environment_id == 1

    def test_bug_history_dtos(self):
        """Test DTOs de historial de bugs"""
        # BugHistoryServiceDTO
        history_service_dto = BugHistoryServiceDTO(
            id=1,
            bug_id=1,
            changed_by="user1",
            change_timestamp=datetime.now(),
            change_summary="Bug creado",
        )

        assert history_service_dto.id == 1
        assert history_service_dto.bug_id == 1
        assert history_service_dto.changed_by == "user1"

        # BugHistoryTableDTO
        history_table_dto = BugHistoryTableDTO(
            changed_by="user1",
            change_timestamp="01/01/2024 10:00",
            change_summary="Bug creado",
        )

        assert history_table_dto.changed_by == "user1"
        assert history_table_dto.change_summary == "Bug creado"

    def test_bug_detail_dto(self):
        """Test BugDetailDTO"""
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
            )
        ]

        detail_dto = BugDetailDTO(bug=bug_table_dto, history=history_items)

        assert detail_dto.bug.id == 1
        assert len(detail_dto.history) == 1
        assert detail_dto.history[0].changed_by == "user1"


class TestRequirementDTOs:
    """Tests para DTOs de Requirement"""

    def test_requirement_service_dto_creation(self):
        """Test creación de RequirementServiceDTO"""
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
            sections=[1, 2],
        )

        assert service_dto.id == 1
        assert service_dto.code == "REQ001"
        assert service_dto.definition == "Test requirement definition"
        assert service_dto.systems == [1, 2]
        assert service_dto.sections == [1, 2]

    def test_requirement_form_dto_validation(self):
        """Test validación de RequirementFormDTO"""
        # Test creación exitosa
        form_dto = RequirementFormDTO(
            le_code="REQ001", le_definition="Definición válida con más de 10 caracteres"
        )

        assert form_dto.le_code == "REQ001"

        # Test validaciones fallidas
        with pytest.raises(
            ValueError, match="La definición debe tener al menos 10 caracteres"
        ):
            RequirementFormDTO(le_code="REQ001", le_definition="corta")

        with pytest.raises(ValueError, match="La versión del sistema es requerida"):
            RequirementFormDTO(
                le_code="", le_definition="Definición válida con más de 10 caracteres"
            )


class TestAssetDTOs:
    """Tests para DTOs de Assets"""

    def test_email_dtos(self):
        """Test DTOs de Email"""
        # EmailFormDTO con validación
        with pytest.raises(ValueError, match="Email válido es requerido"):
            EmailFormDTO(
                le_name="Test Email",
                le_email="invalid-email",
                le_password="password123",
            )

        # EmailServiceDTO
        email_service_dto = EmailServiceDTO(
            id=1,
            environment_id=1,
            modified_by="test_user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            name="Test Email",
            email="test@example.com",
            password="password123",
        )

        assert email_service_dto.email == "test@example.com"
        assert email_service_dto.password == "password123"

    def test_operator_dtos(self):
        """Test DTOs de Operator"""
        # OperatorFormDTO con validación
        with pytest.raises(
            ValueError, match="Nombre, EASA ID y teléfono son requeridos"
        ):
            OperatorFormDTO(
                le_name="",
                le_easa_id="",
                le_verification_code="123",
                le_password="pass",
                le_phone="",
                cb_email="1",
            )

        # OperatorTableDTO con enriquecimiento
        operator_service_dto = OperatorServiceDTO(
            id=1,
            environment_id=1,
            modified_by="test_user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            name="Test Operator",
            easa_id="EASA123",
            verification_code="123",
            password="pass",
            phone="+123456789",
            email_id=1,
        )

        operator_table_dto = OperatorTableDTO.from_service_dto(
            operator_service_dto, email_email="test@example.com"
        )

        assert operator_table_dto.name == "Test Operator"
        assert operator_table_dto.email == "test@example.com"


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
        assert formatted_none == "Not assigned"

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
