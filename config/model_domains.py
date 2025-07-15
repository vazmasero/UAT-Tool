from dataclasses import dataclass
from enum import Enum

@dataclass
class Requirement:
    id: int | None
    code: str
    definition: str
    systems: list[str]
    sections: list[str]

    @classmethod
    def from_db_dict(cls, data: dict) -> 'Requirement':
        return cls(
            id=data.get('id'),
            code=data['code'],
            definition=data['definition'],
            systems=data.get('systems', []),
            sections=data.get('sections', [])
        )   

