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
    code: str
    definition: str
    systems: list[str]
    sections: list[str]