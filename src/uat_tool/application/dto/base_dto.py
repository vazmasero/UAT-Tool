from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class BaseServiceDTO:
    """DTO base con campos comunes de AuditMixin y EnvironmentMixin."""

    # Campos requeridos (sin default)
    id: int
    environment_id: int
    modified_by: str
    created_at: datetime | None
    updated_at: datetime | None

    def to_dict(self) -> dict:
        """Convierte el DTO a un diccionario."""
        return asdict(self)


@dataclass
class BaseTableDTO:
    """DTO base para tablas con campos formateados comunes."""

    # Campos requeridos (sin default)
    id: int
    created_at: str  # Fecha formateada
    updated_at: str  # Fecha formateada
    modified_by: str

    @staticmethod
    def _format_date(date: datetime | None) -> str:
        """Formatea fecha para UI."""
        return date.strftime("%d/%m/%Y %H:%M") if date else "Not assigned"


@dataclass
class BaseFormDTO:
    """DTO base para formularios con validaciones comunes."""

    @staticmethod
    def _format_date(date: datetime | None) -> str:
        """Formatea fecha para UI."""
        return date.strftime("%d/%m/%Y %H:%M") if date else "Not assigned"
