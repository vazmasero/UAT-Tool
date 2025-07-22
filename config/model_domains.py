from dataclasses import dataclass
from enum import Enum

@dataclass
class Requirement:
    id: int | None
    code: str
    definition: str
    systems: list[str]
    sections: list[str]

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
    case_id: int | None