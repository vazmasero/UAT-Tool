import pytest

from data.repositories import (
    BlockRepository,
    BugRepository,
    CampaignRepository,
    CampaignRunRepository,
    CaseRepository,
    DroneRepository,
    FileRepository,
    OperatorRepository,
    ReasonRepository,
    SectionRepository,
    SystemRepository,
    UasZoneRepository,
    UhubOrgRepository,
    UhubUserRepository,
)


def test_bug_repository_create(db_session, model_test_data, sample_audit_data):
    """Test BugRepository.create"""
    # Primero crear un sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert bug.id is not None
    assert bug.status == "OPEN"
    assert bug.system_version == "1.0.0"
    assert bug.service_now_id == "SN123"
    assert bug.short_description == "Test bug"
    assert bug.system_id == system.id
    assert bug.modified_by == "test_user"
    assert bug.created_at is not None
    assert bug.updated_at is not None
    assert bug.environment_id == 1

    # Verificar que se creó el historial
    bug_with_history = repo.get_with_history(bug.id)
    assert bug_with_history is not None
    assert len(bug_with_history.history) == 1
    assert bug_with_history.history[0].change_summary == "Bug creado"
    assert bug_with_history.history[0].changed_by == "test_user"


def test_bug_repository_create_with_campaign_run_and_file(
    db_session, model_test_data, sample_audit_data
):
    """Test BugRepository.create con campaign_run y file"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear toda la estructura necesaria para campaign run
    operator_repo = OperatorRepository(db_session)
    operator_data = {
        **model_test_data["operator_data"],
        "email_id": 1,
    }
    operator = operator_repo.create(
        operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    drone_repo = DroneRepository(db_session)
    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }
    drone = drone_repo.create(
        drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    org_repo = UhubOrgRepository(db_session)
    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    user_repo = UhubUserRepository(db_session)
    user_data = {
        **model_test_data["uhub_user_data"],
        "organization_id": org.id,
    }
    user = user_repo.create(
        user_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    reason_repo = ReasonRepository(db_session)
    reason = reason_repo.create(**model_test_data["reason_data"])

    zone_repo = UasZoneRepository(db_session)
    zone_data = {
        **model_test_data["uas_zone_data"],
        "organizations": [org.id],
        "reasons": [reason.id],
    }
    zone = zone_repo.create(
        zone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    case_repo = CaseRepository(db_session)
    case_data = {
        **model_test_data["case_data"],
        "operators": [operator.id],
        "drones": [drone.id],
        "uhub_users": [user.id],
        "uas_zones": [zone.id],
        "systems": [system.id],
        "sections": [section.id],
    }
    case = case_repo.create(
        case_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    block_repo = BlockRepository(db_session)
    block_data = {
        **model_test_data["block_data"],
        "system_id": system.id,
        "cases": [case.id],
    }
    block = block_repo.create(
        block_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear campaign
    campaign_repo = CampaignRepository(db_session)
    campaign_data = {
        **model_test_data["campaign_data"],
        "system_id": system.id,
        "blocks": [block.id],
    }
    campaign = campaign_repo.create(
        campaign_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear campaign run
    campaign_run_repo = CampaignRunRepository(db_session)
    campaign_run_data = {
        **model_test_data["campaign_run_data"],
        "campaign_id": campaign.id,
        "modified_by": sample_audit_data["modified_by"],
    }
    campaign_run = campaign_run_repo.create(
        campaign_run_data,
        environment_id=1,
    )

    # Crear archivo
    file_repo = FileRepository(db_session)
    file_data = {
        **model_test_data["file_data"],
        "owner_type": "bug",
    }
    file = file_repo.create(**file_data)

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
        "campaign_run_id": campaign_run.id,
        "file_id": file.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert bug.id is not None
    assert bug.campaign_run_id == campaign_run.id
    assert bug.file_id == file.id
    assert bug.system_id == system.id


def test_bug_repository_create_without_system_should_fail(
    db_session, model_test_data, sample_audit_data
):
    """Test que BugRepository.create falla sin system_id"""
    repo = BugRepository(db_session)

    bug_data = model_test_data["bug_data"].copy()
    # system_id está omitido deliberadamente

    with pytest.raises(ValueError, match="system_id"):
        repo.create(
            bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
        )


def test_bug_repository_get_by_service_now_id(
    db_session, model_test_data, sample_audit_data
):
    """Test BugRepository.get_by_service_now_id"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Buscar por Service Now ID
    found = repo.get_by_service_now_id("SN123", 1)

    assert found is not None
    assert found.id == bug.id
    assert found.service_now_id == "SN123"


def test_bug_repository_get_with_history(
    db_session, model_test_data, sample_audit_data
):
    """Test BugRepository.get_with_history"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Agregar más historial
    repo.add_history(bug.id, "user2", "Bug revisado")
    repo.add_history(bug.id, "user3", "Bug asignado")

    # Obtener con historial
    bug_with_history = repo.get_with_history(bug.id)

    assert bug_with_history is not None
    assert bug_with_history.id == bug.id
    assert len(bug_with_history.history) == 3
    assert bug_with_history.history[0].change_summary == "Bug creado"
    assert bug_with_history.history[1].change_summary == "Bug revisado"
    assert bug_with_history.history[2].change_summary == "Bug asignado"


def test_bug_repository_update_status(db_session, model_test_data, sample_audit_data):
    """Test BugRepository.update_status"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Actualizar estado
    updated_bug = repo.update_status(
        bug.id, "CLOSED SOLVED", "status_updater", "Bug resuelto"
    )

    assert updated_bug.id == bug.id
    assert updated_bug.status == "CLOSED SOLVED"

    # Verificar historial
    bug_with_history = repo.get_with_history(bug.id)
    assert len(bug_with_history.history) == 2
    assert "OPEN->CLOSED SOLVED" in bug_with_history.history[1].change_summary
    assert bug_with_history.history[1].changed_by == "status_updater"


def test_bug_repository_update(db_session, model_test_data, sample_audit_data):
    """Test BugRepository.update"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear otro sistema para la actualización
    system2_data = {
        "name": "Test System 2",
    }

    system2 = sys_repo.create(**system2_data)

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )
    # Actualizar el bug
    update_data = {
        "short_description": "Updated bug description",
        "urgency": "1",
        "impact": "1",
        "system_id": system2.id,
        "status": "ON HOLD",
    }

    updated_bug = repo.update(
        bug.id,
        update_data,
        environment_id=1,
        modified_by="updated_user",
        change_summary="Bug modificado",
    )

    assert updated_bug.id == bug.id
    assert updated_bug.short_description == "Updated bug description"
    assert updated_bug.urgency == "1"
    assert updated_bug.impact == "1"
    assert updated_bug.system_id == system2.id
    assert updated_bug.status == "ON HOLD"
    assert updated_bug.modified_by == "updated_user"

    # Verificar historial
    bug_with_history = repo.get_with_history(bug.id)
    assert len(bug_with_history.history) == 2
    assert "Bug modificado" in bug_with_history.history[1].change_summary
    assert "OPEN->ON HOLD" in bug_with_history.history[1].change_summary
    assert bug_with_history.history[1].changed_by == "updated_user"


def test_bug_repository_update_with_campaign_run_and_file(
    db_session, model_test_data, sample_audit_data
):
    """Test BugRepository.create con campaign_run y file"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    # Crear toda la estructura necesaria para campaign run
    operator_repo = OperatorRepository(db_session)
    operator_data = {
        **model_test_data["operator_data"],
        "email_id": 1,
    }
    operator = operator_repo.create(
        operator_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    drone_repo = DroneRepository(db_session)
    drone_data = {
        **model_test_data["drone_data"],
        "operator_id": operator.id,
    }
    drone = drone_repo.create(
        drone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    org_repo = UhubOrgRepository(db_session)
    org = org_repo.create(
        model_test_data["uhub_org_data"],
        environment_id=1,
        modified_by=sample_audit_data["modified_by"],
    )

    user_repo = UhubUserRepository(db_session)
    user_data = {
        **model_test_data["uhub_user_data"],
        "organization_id": org.id,
    }
    user = user_repo.create(
        user_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    reason_repo = ReasonRepository(db_session)
    reason = reason_repo.create(**model_test_data["reason_data"])

    zone_repo = UasZoneRepository(db_session)
    zone_data = {
        **model_test_data["uas_zone_data"],
        "organizations": [org.id],
        "reasons": [reason.id],
    }
    zone = zone_repo.create(
        zone_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    case_repo = CaseRepository(db_session)
    case_data = {
        **model_test_data["case_data"],
        "operators": [operator.id],
        "drones": [drone.id],
        "uhub_users": [user.id],
        "uas_zones": [zone.id],
        "systems": [system.id],
        "sections": [section.id],
    }
    case = case_repo.create(
        case_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    block_repo = BlockRepository(db_session)
    block_data = {
        **model_test_data["block_data"],
        "system_id": system.id,
        "cases": [case.id],
    }
    block = block_repo.create(
        block_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear campaign
    campaign_repo = CampaignRepository(db_session)
    campaign_data = {
        **model_test_data["campaign_data"],
        "system_id": system.id,
        "blocks": [block.id],
    }
    campaign = campaign_repo.create(
        campaign_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear campaign run
    campaign_run_repo = CampaignRunRepository(db_session)
    campaign_run_data = {
        **model_test_data["campaign_run_data"],
        "campaign_id": campaign.id,
        "modified_by": sample_audit_data["modified_by"],
    }
    # Para simplificar, creamos un bug sin campaign_run primero y luego lo actualizamos
    campaign_run = campaign_run_repo.create(campaign_run_data, environment_id=1)

    file_repo = FileRepository(db_session)
    file_data = {
        **model_test_data["file_data"],
        "owner_type": "bug",
    }
    file = file_repo.create(**file_data)

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
        "campaign_run_id": campaign_run.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Para este test, solo probamos con file ya que campaign_run requiere mucho setup
    update_data = {
        "file_id": file.id,
    }

    updated_bug = repo.update(
        bug.id,
        update_data,
        environment_id=1,
        modified_by="updated_user",
        change_summary="Bug con archivo",
    )

    assert updated_bug.id == bug.id
    assert updated_bug.file_id == file.id

    # Verificar que se puede desasociar
    update_data2 = {
        "file_id": None,
    }

    updated_bug2 = repo.update(
        bug.id,
        update_data2,
        environment_id=1,
        modified_by="updated_user2",
        change_summary="Bug sin archivo",
    )

    assert updated_bug2.file_id is None


def test_bug_repository_get_bugs_by_system(
    db_session, model_test_data, sample_audit_data
):
    """Test BugRepository.get_bugs_by_system"""
    # Crear sistemas
    sys_repo = SystemRepository(db_session)
    system1 = sys_repo.create(**model_test_data["system_data"])
    system2 = sys_repo.create(
        **{**model_test_data["system_data"], "name": "Test System 2"}
    )

    repo = BugRepository(db_session)

    # Crear bugs para system1
    bug_data1 = {**model_test_data["bug_data"], "system_id": system1.id}
    bug1 = repo.create(
        bug_data1, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    bug_data2 = {
        **model_test_data["bug_data"],
        "system_id": system1.id,
        "short_description": "Bug 2",
    }
    bug2 = repo.create(
        bug_data2, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear bug para system2
    bug_data3 = {
        **model_test_data["bug_data"],
        "system_id": system2.id,
        "short_description": "Bug 3",
    }
    bug3 = repo.create(
        bug_data3, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Obtener bugs de system1
    system1_bugs = repo.get_bugs_by_system(system1.id, 1)

    # Obtener bugs de system2
    system2_bugs = repo.get_bugs_by_system(system2.id, 1)

    assert len(system1_bugs) == 2
    assert {bug.id for bug in system1_bugs} == {bug1.id, bug2.id}
    assert len(system2_bugs) == 1
    assert {bug.id for bug in system2_bugs} == {bug3.id}
    assert all(bug.system_id == system1.id for bug in system1_bugs)


def test_bug_repository_get_bugs_by_status(
    db_session, model_test_data, sample_audit_data
):
    """Test BugRepository.get_bugs_by_status"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    repo = BugRepository(db_session)

    # Crear bugs con diferentes estados
    bug_data1 = {
        **model_test_data["bug_data"],
        "system_id": system.id,
        "status": "OPEN",
    }
    bug1 = repo.create(
        bug_data1, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    bug_data2 = {
        **model_test_data["bug_data"],
        "system_id": system.id,
        "status": "CLOSED SOLVED",
    }
    bug2 = repo.create(
        bug_data2, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    bug_data3 = {
        **model_test_data["bug_data"],
        "system_id": system.id,
        "status": "OPEN",
    }
    bug3 = repo.create(
        bug_data3, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Obtener bugs OPEN
    open_bugs = repo.get_bugs_by_status("OPEN", 1)

    # Obtener bugs CLOSED SOLVED
    solved_bugs = repo.get_bugs_by_status("CLOSED SOLVED", 1)

    assert len(open_bugs) == 2
    assert len(solved_bugs) == 1
    assert {bug.id for bug in open_bugs} == {bug1.id, bug3.id}
    assert {bug.id for bug in solved_bugs} == {bug2.id}
    assert all(bug.status == "OPEN" for bug in open_bugs)


def test_bug_repository_add_history(db_session, model_test_data, sample_audit_data):
    """Test BugRepository.add_history"""
    # Crear sistema
    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    repo = BugRepository(db_session)

    bug_data = {
        **model_test_data["bug_data"],
        "system_id": system.id,
    }
    bug = repo.create(
        bug_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Agregar historial manualmente
    history = repo.add_history(
        bug.id, "history_user", "Entrada de historial personalizada"
    )

    assert history.id is not None
    assert history.bug_id == bug.id
    assert history.changed_by == "history_user"
    assert history.change_summary == "Entrada de historial personalizada"

    # Verificar que se agregó al bug
    bug_with_history = repo.get_with_history(bug.id)
    assert len(bug_with_history.history) == 2
    assert (
        bug_with_history.history[1].change_summary
        == "Entrada de historial personalizada"
    )
