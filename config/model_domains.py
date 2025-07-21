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
class Email:
    id: int | None
    name: str
    email: str
    password: str

