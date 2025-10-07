from datetime import datetime

from uat_tool.domain import (
    BlockRepository,
    CampaignRepository,
    CampaignRunRepository,
    CaseRepository,
    DroneRepository,
    FileRepository,
    OperatorRepository,
    ReasonRepository,
    SectionRepository,
    StepRepository,
    StepRun,
    StepRunRepository,
    SystemRepository,
    UasZoneRepository,
    UhubOrgRepository,
    UhubUserRepository,
)


def test_campaign_run_repository_create(db_session, model_test_data, sample_audit_data):
    """Test CampaignRepository.create"""
    # Primero crear todas las relaciones (operator, drone, uhub_user, uas_zone, system, section)
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
        "organization_id": 1,
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

    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    case_data = {
        **model_test_data["case_data"],
        "operators": [operator.id],
        "drones": [drone.id],
        "uhub_users": [user.id],
        "uas_zones": [zone.id],
        "systems": [system.id],
        "sections": [section.id],
    }

    case_repo = CaseRepository(db_session)

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
    repo = CampaignRunRepository(db_session)

    campaign_run_data = {
        **model_test_data["campaign_run_data"],
        "campaign_id": campaign.id,
        "modified_by": sample_audit_data["modified_by"],
    }

    campaign_run = repo.create(
        campaign_run_data,
        environment_id=1,
    )

    assert campaign_run.id is not None
    assert campaign_run.notes == "Test campaign run"

    db_session.refresh(campaign)
    assert campaign.status == "RUNNING"


def test_campaign_run_repository_finalize(
    db_session, model_test_data, sample_audit_data
):
    """Test CampaignRepository.create"""
    # Primero crear todas las relaciones (operator, drone, uhub_user, uas_zone, system, section)
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
        "organization_id": 1,
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

    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    case_data = {
        **model_test_data["case_data"],
        "operators": [operator.id],
        "drones": [drone.id],
        "uhub_users": [user.id],
        "uas_zones": [zone.id],
        "systems": [system.id],
        "sections": [section.id],
    }

    case_repo = CaseRepository(db_session)

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
    repo = CampaignRunRepository(db_session)

    campaign_run_data = {
        **model_test_data["campaign_run_data"],
        "campaign_id": campaign.id,
        "modified_by": sample_audit_data["modified_by"],
    }

    campaign_run = repo.create(
        campaign_run_data,
        environment_id=1,
    )

    # Verificar que la campaña está en estado RUNNING después de crear la ejecución
    db_session.refresh(campaign)
    assert campaign.status == "RUNNING"

    final_notes = "Ejecución completada exitosamente"
    finalized_campaign_run = repo.finalize(
        campaign_run_id=campaign_run.id,
        modified_by=sample_audit_data["modified_by"],
        notes=final_notes,
    )

    assert finalized_campaign_run.id == campaign_run.id
    assert finalized_campaign_run.ended_at is not None
    assert finalized_campaign_run.notes == final_notes
    assert finalized_campaign_run.ended_at <= datetime.now()

    db_session.refresh(campaign)
    assert campaign.status == "FINISHED"


def test_campaign_run_repository_cancel(db_session, model_test_data, sample_audit_data):
    """Test CampaignRepository.create"""
    # Primero crear todas las relaciones (operator, drone, uhub_user, uas_zone, system, section)
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
        "organization_id": 1,
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

    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    case_data = {
        **model_test_data["case_data"],
        "operators": [operator.id],
        "drones": [drone.id],
        "uhub_users": [user.id],
        "uas_zones": [zone.id],
        "systems": [system.id],
        "sections": [section.id],
    }

    case_repo = CaseRepository(db_session)

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
    repo = CampaignRunRepository(db_session)

    campaign_run_data = {
        **model_test_data["campaign_run_data"],
        "campaign_id": campaign.id,
        "modified_by": sample_audit_data["modified_by"],
    }

    campaign_run = repo.create(
        campaign_run_data,
        environment_id=1,
    )

    # Verificar que la campaña está en estado RUNNING después de crear la ejecución
    db_session.refresh(campaign)
    assert campaign.status == "RUNNING"

    finalized_campaign_run = repo.cancel(
        campaign_run_id=campaign_run.id,
        modified_by=sample_audit_data["modified_by"],
    )

    assert finalized_campaign_run.id == campaign_run.id
    assert finalized_campaign_run.ended_at is not None
    assert finalized_campaign_run.ended_at <= datetime.now()

    db_session.refresh(campaign)
    assert campaign.status == "CANCELLED"


def test_step_run_repository_update_step_result(
    db_session, model_test_data, sample_audit_data
):
    """Test StepRunRepository.update_step_result"""
    # Setup igual al test anterior para crear toda la estructura
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
        "organization_id": 1,
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

    sys_repo = SystemRepository(db_session)
    system = sys_repo.create(**model_test_data["system_data"])

    sect_repo = SectionRepository(db_session)
    section = sect_repo.create(**model_test_data["section_data"])

    case_data = {
        **model_test_data["case_data"],
        "operators": [operator.id],
        "drones": [drone.id],
        "uhub_users": [user.id],
        "uas_zones": [zone.id],
        "systems": [system.id],
        "sections": [section.id],
    }

    case_repo = CaseRepository(db_session)

    case = case_repo.create(
        case_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear un step para el caso
    step_repo = StepRepository(db_session)
    step_data = {
        **model_test_data["step_data"],
        "case_id": case.id,
    }
    step = step_repo.create(step_data)

    block_repo = BlockRepository(db_session)
    block_data = {
        **model_test_data["block_data"],
        "system_id": system.id,
        "cases": [case.id],
    }

    block = block_repo.create(
        block_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    campaign_repo = CampaignRepository(db_session)
    campaign_data = {
        **model_test_data["campaign_data"],
        "system_id": system.id,
        "blocks": [block.id],
    }
    campaign = campaign_repo.create(
        campaign_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    # Crear campaign run (esto creará automáticamente los step runs)
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

    # Obtener el step run que se creó automáticamente
    step_run_repo = StepRunRepository(db_session)
    step_runs = (
        db_session.query(StepRun)
        .filter(StepRun.step_id == step.id, StepRun.campaign_run_id == campaign_run.id)
        .all()
    )

    assert len(step_runs) == 1
    step_run = step_runs[0]

    updated_step_run = step_run_repo.update_step_result(
        step_run_id=step_run.id,
        passed=True,
        notes="Paso ejecutado exitosamente",
        file_id=None,  # Podrías crear un file si necesitas probar esta funcionalidad
    )

    # Verificaciones
    assert updated_step_run.id == step_run.id
    assert updated_step_run.passed
    assert updated_step_run.notes == "Paso ejecutado exitosamente"
    assert updated_step_run.file_id is None

    # Verificar que los otros campos no cambiaron
    assert updated_step_run.step_id == step.id
    assert updated_step_run.campaign_run_id == campaign_run.id
    assert updated_step_run.case_run_id == step_run.case_run_id

    # Para esto necesitarías crear un file primero
    file_repo = FileRepository(db_session)
    file_data = {
        **model_test_data["file_data"],
        "owner_type": "step_run",  # Cambiar a step_run en lugar de bug
    }
    file = file_repo.create(**file_data)
    updated_with_file = step_run_repo.update_step_result(
        step_run_id=step_run.id,
        passed=False,
        notes="Paso fallido con evidencia",
        file_id=file.id,
    )
    assert updated_with_file.file_id == file.id
    assert not updated_with_file.passed
    assert updated_with_file.notes == "Paso fallido con evidencia"

    updated_minimal = step_run_repo.update_step_result(
        step_run_id=step_run.id, passed=False
    )
    assert not updated_minimal.passed
    assert updated_minimal.notes == "Paso fallido con evidencia"
