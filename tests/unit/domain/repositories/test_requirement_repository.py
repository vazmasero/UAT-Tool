from uat_tool.domain import (
    RequirementRepository,
    SectionRepository,
    SystemRepository,
)


def test_requirement_repository_create(db_session, model_test_data, sample_audit_data):
    """Test RequirementRepository.create"""
    # Primero crear un sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear una sección
    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    # Crear el requisito
    repo = RequirementRepository(db_session)

    req_data = {
        **model_test_data["requirement_data"],
        "systems": [system.id],
        "sections": [section.id],
    }
    requirement = repo.create(
        req_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert requirement.id is not None
    assert requirement.code == "REQ001"
    assert requirement.definition == "Test requirement definition"
    assert len(requirement.systems) == 1
    assert len(requirement.sections) == 1
    assert requirement.systems[0].id == system.id
    assert requirement.sections[0].id == section.id
    assert requirement.modified_by == "test_user"
    assert requirement.created_at is not None
    assert requirement.updated_at is not None
    assert requirement.environment_id == 1


def test_requirement_repository_get_by_code(
    db_session, model_test_data, sample_audit_data
):
    """Test RequirementRepository.get_by_code"""
    # Primero crear un sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear una sección
    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    # Crear el requisito
    repo = RequirementRepository(db_session)

    req_data = {
        **model_test_data["requirement_data"],
        "systems": [system.id],
        "sections": [section.id],
    }
    requirement = repo.create(
        req_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por código
    found = repo.get_by_code("REQ001", 1)

    assert found is not None
    assert found.id == requirement.id
    assert found.code == "REQ001"


def test_requirement_repository_get_by_code_not_found(db_session):
    """Test RequirementRepository.get_by_code cuando no existe"""
    repo = RequirementRepository(db_session)

    found = repo.get_by_code("NONEXISTENT", 1)

    assert found is None


def test_requirement_repository_get_with_relations(
    db_session, model_test_data, sample_audit_data
):
    """Test RequirementRepository.get_with_relations"""
    # Primero crear un sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear una sección
    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    # Crear el requisito
    repo = RequirementRepository(db_session)

    req_data = {
        **model_test_data["requirement_data"],
        "systems": [system.id],
        "sections": [section.id],
    }
    requirement = repo.create(
        req_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Obtener con relaciones
    found = repo.get_with_relations(requirement.id)

    assert found is not None
    assert found.id == requirement.id
    assert found.code == "REQ001"
    # Verificar que las relaciones están cargadas
    assert hasattr(found, "bugs")


def test_requirement_repository_update(db_session, model_test_data, sample_audit_data):
    """Test RequirementRepository.update"""
    # Primero crear un sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear una sección
    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    # Crear el requisito
    repo = RequirementRepository(db_session)

    req_data = {
        **model_test_data["requirement_data"],
        "systems": [system.id],
        "sections": [section.id],
    }
    requirement = repo.create(
        req_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear otro sistema y sección para la actualización
    system2 = sys_repo.create(
        **{**model_test_data["system_data"], "name": "Test System 2"}
    )
    section2 = sect_repo.create(
        **{**model_test_data["section_data"], "name": "Test Section 2"}
    )

    # Actualizar el requisito
    update_data = {
        "definition": "Updated requirement definition",
        "systems": [system2.id],
        "sections": [section2.id],
    }

    updated_requirement = repo.update(
        requirement.id, update_data, environment_id=1, modified_by="updated_user"
    )

    assert updated_requirement.id == requirement.id
    assert updated_requirement.definition == "Updated requirement definition"
    assert updated_requirement.modified_by == "updated_user"
    assert len(updated_requirement.systems) == 1
    assert len(updated_requirement.sections) == 1
    assert updated_requirement.systems[0].id == system2.id
    assert updated_requirement.sections[0].id == section2.id
