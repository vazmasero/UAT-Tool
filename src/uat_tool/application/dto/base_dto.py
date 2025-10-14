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
        """Convierte a dict para el repositorio, excluyendo None values y campos de solo lectura."""
        data = asdict(self)

        # Campos a excluir (solo lectura/calculados)
        excluded_fields = {
            "system_names",
            "section_names",
            "requirement_codes",
            "system_name",
            "file_name",
            # Añadir más campos de lectura si es necesario
        }

        return {
            key: value
            for key, value in data.items()
            if value is not None and key not in excluded_fields
        }


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
