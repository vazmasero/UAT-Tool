from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class BaseServiceDTO:
    """DTO base con campos comunes de AuditMixin y EnvironmentMixin."""

    # Campos requeridos (sin default)
    id: int | None
    environment_id: int
    modified_by: str
    created_at: datetime | None
    updated_at: datetime | None

    def to_dict(self) -> dict:
        """Convierte el DTO a un diccionario, excluyendo None values."""
        data = asdict(self)
        # Excluir campos None para que la BD asigne valores automáticos
        return {k: v for k, v in data.items() if v is not None}


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
        return date.strftime("%d/%m/%Y %H:%M") if date else "N/A"

    def _format_date_short(self, date_value: datetime | None) -> str:
        """Formatea una fecha en formato corto para la UI."""
        if not date_value:
            return "N/A"
        return date_value.strftime("%d/%m/%Y")


@dataclass
class BaseFormDTO:
    """DTO base para formularios con validaciones comunes."""

    @staticmethod
    def _format_date(date: datetime | None) -> str:
        """Formatea fecha para UI."""
        return date.strftime("%d/%m/%Y %H:%M") if date else "Not assigned"

    def _format_date_short(self, date_value: datetime | None) -> str:
        """Formatea una fecha en formato corto para la UI."""
        if not date_value:
            return "N/A"
        return date_value.strftime("%d/%m/%Y")
