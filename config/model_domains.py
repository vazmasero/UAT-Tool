from dataclasses import dataclass


@dataclass
class Requirement:
    id: int | None
    code: str
    definition: str
    systems: list[str]
    sections: list[str]


@dataclass
class Block:
    id: int | None
    identification: str
    name: str
    system: str
    comments: str


@dataclass
class Bug:
    id: int | None
    status: str
    system_id: str
    campaign_id: str
    requirements: list[str]
    version: str
    service_now_id: str
    short_desc: str
    definition: str
    urgency: str
    impact: str
    file: str


@dataclass
class Case:
    id: int | None
    identification: str
    name: str
    systems: list[str]
    sections: list[str]
    operators: list[str]
    drones: list[str]
    uhub_users: list[str]
    comments: str


@dataclass
class Step:
    id: int | None
    action: str
    expected_result: str
    affected_requirements: list[str]
    comments: str
    
@dataclass
class Campaign:
    id: int | None
    identification: str
    description: str
    system: list[str]
    version: list[str]
    blocks: list[str]
