from uat_tool.domain import (
    BlockRepository,
    CampaignRepository,
    CaseRepository,
    DroneRepository,
    OperatorRepository,
    ReasonRepository,
    RequirementRepository,
    SectionRepository,
    StepRepository,
    SystemRepository,
    UasZoneRepository,
    UhubOrgRepository,
    UhubUserRepository,
)


def test_case_repository_create(db_session, model_test_data, sample_audit_data):
    """Test CaseRepository.create"""
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

    repo = CaseRepository(db_session)

    case = repo.create(
        case_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert case.id is not None
    assert case.code == "CASE001"
    assert case.name == "Test Case"
    assert len(case.operators) == 1
    assert len(case.uas_zones) == 1
    assert len(case.uhub_users) == 1
    assert len(case.drones) == 1
    assert len(case.systems) == 1
    assert len(case.sections) == 1
    assert case.operators[0].id == operator.id
    assert case.uas_zones[0].id == zone.id
    assert case.uhub_users[0].id == user.id
    assert case.drones[0].id == drone.id
    assert case.systems[0].id == system.id
    assert case.sections[0].id == section.id


def test_step_repository_create(db_session, model_test_data, sample_audit_data):
    """Test StepRepository.create"""
    # Primero crear todas las relaciones (operator, drone, uhub_user, uas_zone, system, section)
    # necesarias para crear un case, ya que case_id es necesario para el step y es verificada su existencia.
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

    # Crear un requisito
    req_repo = RequirementRepository(db_session)
    req_data = {
        **model_test_data["requirement_data"],
        "systems": [system.id],
        "sections": [section.id],
    }
    requirement = req_repo.create(
        req_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    repo = StepRepository(db_session)
    step_data = {
        **model_test_data["step_data"],
        "case_id": case.id,
        "requirements": [requirement.id],
    }
    step = repo.create(step_data)

    assert step.id is not None
    assert step.action == "Test action"
    assert step.expected_result == "Expected result"
    assert step.case_id == case.id
    assert len(step.requirements) == 1
    assert step.requirements[0].id == requirement.id


def test_block_repository_create(db_session, model_test_data, sample_audit_data):
    """Test BlockRepository.create"""
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

    repo = BlockRepository(db_session)
    block_data = {
        **model_test_data["block_data"],
        "system_id": system.id,
        "cases": [case.id],
    }

    block = repo.create(
        block_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert block.id is not None
    assert block.code == "BLOCK001"
    assert block.name == "Test Block"
    assert block.system_id == system.id
    assert len(block.cases) == 1
    assert block.cases[0].id == case.id


def test_campaign_repository_create(db_session, model_test_data, sample_audit_data):
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

    repo = CampaignRepository(db_session)
    campaign_data = {
        **model_test_data["campaign_data"],
        "system_id": system.id,
        "blocks": [block.id],
    }
    campaign = repo.create(
        campaign_data, environment_id=1, modified_by=sample_audit_data["modified_by"]
    )

    assert campaign.id is not None
    assert campaign.code == "CAMPAIGN001"
    assert campaign.description == "Test campaign description"
    assert campaign.status == "DRAFT"
    assert campaign.system_id == system.id
    assert len(campaign.blocks) == 1
    assert campaign.blocks[0].id == block.id
