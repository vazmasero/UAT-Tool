from dataclasses import dataclass

from uat_tool.domain import File, Section, System


@dataclass
class SystemServiceDTO:
    """DTO 1:1 con el modelo de dominio para operaciones CRUD y lógica de negocio.
    Propósito: comunicación entre servicios y con repositorios.
    Debe reflejar fielmente la entidad de dominio"""

    # Campos requeridos (sin default)
    id: int
    name: str

    @classmethod
    def from_model(cls, system: "System") -> "SystemServiceDTO":
        """Conversión directa modelo -> DTO (sin enriquecimiento).

        Args:
            system (System): modelo SQLAlchemy de la entidad a transformar.

        Returns:
            SystemServiceDTO: modelo DTO de la entidad transformada.
        """
        return cls(
            id=system.id,
            name=system.name,
        )


@dataclass
class SectionServiceDTO:
    """DTO 1:1 con el modelo de dominio para operaciones CRUD y lógica de negocio.
    Propósito: comunicación entre servicios y con repositorios.
    Debe reflejar fielmente la entidad de dominio"""

    # Campos requeridos (sin default)
    id: int
    name: str

    @classmethod
    def from_model(cls, section: "Section") -> "SectionServiceDTO":
        """Conversión directa modelo -> DTO (sin enriquecimiento).

        Args:
            section (Section): modelo SQLAlchemy de la entidad a transformar.

        Returns:
            SectionServiceDTO: modelo DTO de la entidad transformada.
        """
        return cls(
            id=section.id,
            name=section.name,
        )


@dataclass
class FileServiceDTO:
    id: int | None
    owner_type: str
    filename: str
    filepath: str
    mime_type: str
    size: str
    uploaded_by: str
    uploaded_at: str

    @classmethod
    def from_model(cls, file: "File") -> "FileServiceDTO":
        """Conversión directa modelo -> DTO (sin enriquecimiento).

        Args:
            section (Section): modelo SQLAlchemy de la entidad a transformar.

        Returns:
            SectionServiceDTO: modelo DTO de la entidad transformada.
        """
        return cls(
            id=file.id,
            owner_type=file.owner_type,
            filename=file.filename,
            filepath=file.filepath,
            mime_type=file.mime_type,
            size=file.size,
            uploaded_by=file.uploaded_by,
            uploaded_at=file.uploaded_at,
        )
