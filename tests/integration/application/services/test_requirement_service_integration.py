import pytest

from uat_tool.application.dto import (
    RequirementFormDTO,
    RequirementServiceDTO,
    RequirementTableDTO,
)
from uat_tool.application.services import RequirementService
from uat_tool.domain import Section, System


def test_create_requirement_from_form_integration(db_session, app_context):
    """Test de integración completo: FormDTO -> Service -> BD -> ServiceDTO"""

    # Verificar que tenemos datos iniciales
    from uat_tool.domain import Section, System

    systems = db_session.query(System).all()
    sections = db_session.query(Section).all()

    assert len(systems) >= 2, "Se necesitan al menos 2 sistemas en datos iniciales"
    assert len(sections) >= 2, "Se necesitan al menos 2 secciones en datos iniciales"

    # 1. Crear FormDTO desde la UI
    form_dto = RequirementFormDTO(
        le_code="REQ-INT-001",
        le_definition="This is a test requirement definition for integration testing",
        lw_systems=[systems[0].id, systems[1].id],
        lw_sections=[sections[0].id, sections[1].id],
    )

    # 2. Contexto de la aplicación
    context = {
        "modified_by": "integration_test_user",
        "environment_id": 1,
    }

    # 3. Ejecutar el servicio
    service = RequirementService(app_context)
    result_dto = service.create_requirement_from_form(form_dto, context)

    # 4. Verificaciones
    assert isinstance(result_dto, RequirementServiceDTO)
    assert result_dto.code == "REQ-INT-001"
    assert (
        result_dto.definition
        == "This is a test requirement definition for integration testing"
    )
    assert result_dto.modified_by == "integration_test_user"
    assert result_dto.environment_id == 1
    assert set(result_dto.systems) == {systems[0].id, systems[1].id}
    assert set(result_dto.sections) == {sections[0].id, sections[1].id}
    assert result_dto.id is not None
    assert result_dto.created_at is not None
    assert result_dto.updated_at is not None

    # 5. Verificar que se guardó en BD
    with app_context.get_unit_of_work_context() as uow:
        saved_requirement = uow.req_repo.get_with_relations(result_dto.id)
        assert saved_requirement is not None
        assert saved_requirement.code == "REQ-INT-001"
        assert len(saved_requirement.systems) == 2
        assert len(saved_requirement.sections) == 2


def test_update_requirement_from_form_integration(db_session, app_context):
    """Test de integración para actualización completa"""
    # Setup - crear datos iniciales
    system1 = System(name="USSP")
    system2 = System(name="CISP")
    system3 = System(name="AUDI")
    section1 = Section(name="Operational Requirements")
    section2 = Section(name="Technical Requirements")

    db_session.add_all([system1, system2, system3, section1, section2])
    db_session.commit()

    # Crear requisito inicial
    initial_form = RequirementFormDTO(
        le_code="REQ-INT-UPDATE",
        le_definition="Initial requirement definition for update testing",
        lw_systems=[system1.id],
        lw_sections=[section1.id],
    )

    context = {"modified_by": "integration_test_user", "environment_id": 1}

    service = RequirementService(app_context)
    initial_result = service.create_requirement_from_form(initial_form, context)
    requirement_id = initial_result.id

    # 1. Obtener para edición
    edit_form = service.get_requirement_for_edit(requirement_id)
    assert edit_form is not None
    assert edit_form.le_code == "REQ-INT-UPDATE"
    assert (
        edit_form.le_definition == "Initial requirement definition for update testing"
    )
    assert edit_form.lw_systems == [system1.id]
    assert edit_form.lw_sections == [section1.id]

    # 2. Modificar el FormDTO (como haría la UI)
    edit_form.le_definition = "Updated requirement definition with more details"
    edit_form.lw_systems = [system2.id, system3.id]  # Cambiar sistemas
    edit_form.lw_sections = [section1.id, section2.id]  # Añadir sección

    # 3. Actualizar
    update_context = {
        "modified_by": "integration_test_user_updated",
        "environment_id": 2,
    }

    updated_result = service.update_requirement_from_form(
        requirement_id, edit_form, update_context
    )

    # 4. Verificaciones
    assert updated_result.code == "REQ-INT-UPDATE"
    assert (
        updated_result.definition == "Updated requirement definition with more details"
    )
    assert updated_result.modified_by == "integration_test_user_updated"
    assert set(updated_result.systems) == {system2.id, system3.id}
    assert set(updated_result.sections) == {section1.id, section2.id}

    # 5. Verificar en BD
    with app_context.get_unit_of_work_context() as uow:
        updated_requirement = uow.req_repo.get_with_relations(requirement_id)
        assert (
            updated_requirement.definition
            == "Updated requirement definition with more details"
        )
        assert updated_requirement.modified_by == "integration_test_user_updated"
        assert len(updated_requirement.systems) == 2
        assert len(updated_requirement.sections) == 2


def test_get_all_requirements_for_table_integration(db_session, app_context):
    """Test de integración para obtener requisitos en formato tabla"""
    # Setup - crear datos de prueba
    system1 = System(name="USSP")
    system2 = System(name="CISP")
    section1 = Section(name="Operational")
    section2 = Section(name="Technical")

    db_session.add_all([system1, system2, section1, section2])
    db_session.commit()

    # Crear varios requisitos
    service = RequirementService(app_context)
    context = {"modified_by": "table_test_user", "environment_id": 1}

    form1 = RequirementFormDTO(
        le_code="REQ-TABLE-1",
        le_definition="First requirement for table testing with sufficient length",
        lw_systems=[system1.id],
        lw_sections=[section1.id],
    )

    form2 = RequirementFormDTO(
        le_code="REQ-TABLE-2",
        le_definition="Second requirement for table testing with sufficient length",
        lw_systems=[system2.id],
        lw_sections=[section2.id],
    )

    service.create_requirement_from_form(form1, context)
    service.create_requirement_from_form(form2, context)

    # Ejecutar
    table_dtos = service.get_all_requirements_for_table()

    # Verificaciones
    assert len(table_dtos) >= 2  # Puede haber más si otros tests crearon datos

    # Encontrar nuestros requisitos
    req1 = next((dto for dto in table_dtos if dto.code == "REQ-TABLE-1"), None)
    req2 = next((dto for dto in table_dtos if dto.code == "REQ-TABLE-2"), None)

    assert req1 is not None
    assert req2 is not None

    # Verificar formato de tabla
    assert isinstance(req1, RequirementTableDTO)
    assert req1.systems == "USSP"  # Nombres formateados
    assert req1.sections == "Operational"
    assert req1.created_at is not None  # Fecha formateada como string
    assert isinstance(req1.created_at, str)

    assert req2.systems == "CISP"
    assert req2.sections == "Technical"


def test_delete_requirement_integration(db_session, app_context, model_test_data):
    """Test de integración para eliminar requisito"""
    # Setup
    system = System(name="USSP")
    section = Section(name="Operational")
    db_session.add_all([system, section])
    db_session.commit()

    service = RequirementService(app_context)
    context = {"modified_by": "delete_test_user", "environment_id": 1}

    form = RequirementFormDTO(
        le_code="REQ-DELETE",
        le_definition="Requirement to be deleted in integration test",
        lw_systems=[system.id],
        lw_sections=[section.id],
    )

    created_dto = service.create_requirement_from_form(form, context)
    requirement_id = created_dto.id

    # Verificar que existe
    with app_context.get_unit_of_work_context() as uow:
        existing = uow.req_repo.get_by_id(requirement_id)
        assert existing is not None

    # Ejecutar eliminación
    delete_result = service.delete_requirement(requirement_id)
    assert delete_result is True

    # Verificar que ya no existe
    with app_context.get_unit_of_work_context() as uow:
        deleted = uow.req_repo.get_by_id(requirement_id)
        assert deleted is None


def test_requirement_code_uniqueness_integration(
    db_session, app_context, model_test_data
):
    """Test que verifica la unicidad del código de requisito por entorno"""
    # Setup
    system = System(name="USSP")
    section = Section(name="Operational")
    db_session.add_all([system, section])
    db_session.commit()

    service = RequirementService(app_context)
    context_env1 = {"modified_by": "uniqueness_test", "environment_id": 1}
    context_env2 = {"modified_by": "uniqueness_test", "environment_id": 2}

    form = RequirementFormDTO(
        le_code="REQ-UNIQUE",
        le_definition="Requirement for uniqueness testing with sufficient length",
        lw_systems=[system.id],
        lw_sections=[section.id],
    )

    # Crear primer requisito en entorno 1
    result1 = service.create_requirement_from_form(form, context_env1)
    assert result1 is not None

    # Debería poder crear otro con mismo código en entorno diferente
    result2 = service.create_requirement_from_form(form, context_env2)
    assert result2 is not None
    assert result2.code == "REQ-UNIQUE"
    assert result2.environment_id == 2

    # Verificar que son diferentes registros
    assert result1.id != result2.id


def test_requirement_without_systems_validation(
    db_session, app_context, model_test_data
):
    """Test que verifica la validación de sistemas requeridos"""
    # Setup
    section = Section(name="Operational")
    db_session.add(section)
    db_session.commit()

    service = RequirementService(app_context)
    context = {"modified_by": "validation_test", "environment_id": 1}

    # Intentar crear requisito sin sistemas (debería fallar)
    invalid_form = RequirementFormDTO(
        le_code="REQ-NO-SYSTEMS",
        le_definition="Requirement without systems should fail validation",
        lw_systems=[],  # Sin sistemas - INVALIDO
        lw_sections=[section.id],
    )

    # Esto debería lanzar una excepción del repositorio
    with pytest.raises(ValueError, match="al menos un sistema"):
        service.create_requirement_from_form(invalid_form, context)


def test_requirement_without_sections_validation(
    db_session, app_context, model_test_data
):
    """Test que verifica la validación de secciones requeridas"""
    # Setup
    system = System(name="USSP")
    db_session.add(system)
    db_session.commit()

    service = RequirementService(app_context)
    context = {"modified_by": "validation_test", "environment_id": 1}

    # Intentar crear requisito sin secciones (debería fallar)
    invalid_form = RequirementFormDTO(
        le_code="REQ-NO-SECTIONS",
        le_definition="Requirement without sections should fail validation",
        lw_systems=[system.id],
        lw_sections=[],  # Sin secciones - INVALIDO
    )

    # Esto debería lanzar una excepción del repositorio
    with pytest.raises(ValueError, match="al menos una sección"):
        service.create_requirement_from_form(invalid_form, context)


def test_debug_sessions(db_session, app_context):
    """Debug para ver las sesiones y tablas"""
    from sqlalchemy import inspect

    print("=== DEBUG SESSIONS ===")

    # 1. Verificar sesión del fixture
    print(f"1. db_session: {db_session}")
    print(f"   Engine: {db_session.get_bind()}")

    inspector1 = inspect(db_session.get_bind())
    tables1 = inspector1.get_table_names()
    print(f"   Tablas en db_session: {tables1}")
    print(f"   ¿requirements existe?: {'requirements' in tables1}")

    # 2. Verificar sesión del ApplicationContext
    print(f"2. app_context session factory: {app_context._session_factory}")

    # 3. Verificar sesión del UnitOfWork
    with app_context.get_unit_of_work_context() as uow:
        print(f"3. UnitOfWork session: {uow.session}")
        print(f"   Engine: {uow.session.get_bind()}")
        print(f"   ¿Misma sesión que db_session?: {uow.session is db_session}")
        print(f"   ¿Mismo engine?: {uow.session.get_bind() is db_session.get_bind()}")

        inspector2 = inspect(uow.session.get_bind())
        tables2 = inspector2.get_table_names()
        print(f"   Tablas en UnitOfWork: {tables2}")
        print(f"   ¿requirements existe?: {'requirements' in tables2}")

    print("=== FIN DEBUG ===")

    # Verificación crítica
    assert "requirements" in tables1, (
        f"Tabla requirements no en db_session. Tablas: {tables1}"
    )
