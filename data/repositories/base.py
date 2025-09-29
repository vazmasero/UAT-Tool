import logging
from typing import Any, Generic, TypeVar

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Query, Session

# Configurar logging
logger = logging.getLogger(__name__)

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """Repositorio base genérico para operaciones CRUD con manejo de errores
    y funcionalidades extendidas.
    """

    def __init__(self, session: Session, model_class: type[T]):
        self.session = session
        self.model_class = model_class

    def get_by_id(self, id: int, raise_if_not_found: bool = False) -> T | None:
        """Obtiene un registro por su ID.

        Args:
            id: ID del registro a buscar
            raise_if_not_found: Si True, lanza excepción si no se encuentra

        Returns:
            Instancia del modelo o None si no se encuentra

        Raises:
            ValueError: Si raise_if_not_found es True y no se encuentra el registro
        """
        instance = self.session.get(self.model_class, id)
        if raise_if_not_found and instance is None:
            raise ValueError(f"{self.model_class.__name__} con id {id} no encontrado")
        return instance

    def get_all(self, limit: int | None = None, offset: int | None = None) -> list[T]:
        """Obtiene todos los registros del modelo con opciones de paginación.

        Args:
            limit: Límite de registros a devolver
            offset: Offset para paginación

        Returns:
            Lista de instancias del modelo
        """
        query = self.session.query(self.model_class)
        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)
        return query.all()

    def filter_by(self, **kwargs) -> list[T]:
        """Filtra registros según los criterios proporcionados.

        Args:
            **kwargs: Criterios de filtrado (campo=valor)

        Returns:
            Lista de instancias que coinciden con los criterios
        """
        return self.session.query(self.model_class).filter_by(**kwargs).all()

    def query(self) -> Query:
        """Devuelve una query base para construir consultas personalizadas.

        Returns:
            Query de SQLAlchemy para el modelo
        """
        return self.session.query(self.model_class)

    def exists(self, **kwargs) -> bool:
        """Verifica si existe al menos un registro que cumpla los criterios.

        Args:
            **kwargs: Criterios de búsqueda

        Returns:
            True si existe al menos un registro, False otherwise
        """
        return self.session.query(
            self.session.query(self.model_class).filter_by(**kwargs).exists()
        ).scalar()

    def count(self, **kwargs) -> int:
        """Cuenta el número de registros que cumplen los criterios.

        Args:
            **kwargs: Criterios de filtrado (opcional)

        Returns:
            Número de registros que coinciden
        """
        query = self.session.query(self.model_class)
        if kwargs:
            query = query.filter_by(**kwargs)
        return query.count()

    def create(self, **kwargs) -> T:
        """Crea un nuevo registro en la base de datos.

        Args:
            **kwargs: Atributos del nuevo registro

        Returns:
            Instancia creada

        Raises:
            IntegrityError: Si viola constraints de la base de datos
            SQLAlchemyError: Para otros errores de base de datos
        """
        try:
            instance = self.model_class(**kwargs)
            self.session.add(instance)
            self.session.flush()
            logger.info(f"Creado {self.model_class.__name__}: {instance.id}")
            return instance
        except IntegrityError as e:
            self.session.rollback()
            logger.error(
                f"Error de integridad creando {self.model_class.__name__}: {e}"
            )
            raise
        except SQLAlchemyError as e:
            self.session.rollback()
            logger.error(
                f"Error en base de datos creando {self.model_class.__name__}: {e}"
            )
            raise

    def bulk_create(self, instances_data: list[dict]) -> list[T]:
        """Crea múltiples registros en una sola operación.

        Args:
            instances_data: Lista de diccionarios con datos para crear instancias

        Returns:
            Lista de instancias creadas
        """
        try:
            instances = [self.model_class(**data) for data in instances_data]
            self.session.bulk_save_objects(instances)
            self.session.flush()
            logger.info(
                f"Registros en bulk creados {len(instances)} {self.model_class.__name__}"
            )
            return instances
        except SQLAlchemyError as e:
            self.session.rollback()
            logger.error(f"Error de base de datos en creación en bulk: {e}")
            raise

    def update(self, instance: T, **kwargs) -> T | None:
        """Actualiza un registro existente.

        Args:
            instance: Instancia a actualizar
            **kwargs: Campos a actualizar

        Returns:
            Instancia actualizada o None si no se encuentra

        Raises:
            IntegrityError: Si viola constraints de la base de datos
        """
        try:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.session.flush()
            instance_id = getattr(instance, "id", "NA")
            logger.info(f"Actualizado {self.model_class.__name__} {instance_id}")
            return instance
        except IntegrityError as e:
            self.session.rollback()
            instance_id = getattr(instance, "id", "NA")
            logger.error(
                f"Error de integridad actualizando {self.model_class.__name__} {instance_id}: {e}"
            )
            raise

    def delete(self, id: int) -> bool:
        """Elimina un registro por su ID.

        Args:
            id: ID del registro a eliminar

        Returns:
            True si se eliminó, False si no se encontró

        Raises:
            SQLAlchemyError: Si hay error de base de datos
        """
        instance = self.get_by_id(id)
        if not instance:
            logger.warning(
                f"{self.model_class.__name__} con id {id} no encontrado para eliminar"
            )
            return False

        try:
            self.session.delete(instance)
            self.session.flush()
            logger.info(f"Borrado {self.model_class.__name__} {id}")
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            logger.error(
                f"Error de base de datos borrando {self.model_class.__name__} {id}: {e}"
            )
            raise

    def refresh(self, instance: T) -> T:
        """Refresca una instancia desde la base de datos.

        Args:
            instance: Instancia a refrescar

        Returns:
            Instancia refrescada
        """
        self.session.refresh(instance)
        return instance

    def get_or_create(
        self, defaults: dict[str, Any] | None = None, **kwargs
    ) -> tuple[T, bool]:
        """Obtiene un registro o lo crea si no existe.

        Args:
            defaults: Valores por defecto si hay que crear el registro
            **kwargs: Criterios de búsqueda

        Returns:
            Tupla (instancia, created) donde created es True si se creó nuevo
        """
        instance = self.session.query(self.model_class).filter_by(**kwargs).first()
        if instance:
            return instance, False

        create_data = kwargs.copy()
        if defaults:
            create_data.update(defaults)

        instance = self.create(**create_data)
        return instance, True


class AuditMixinRepository(BaseRepository[T]):
    """Mixin para repositorios que manejan modelos con AuditMixin."""

    def _validate_audit_data(self, data: dict) -> None:
        """Valida que los datos contengan modified_by."""
        if "modified_by" not in data:
            raise ValueError("Se debe indicar quién ha modificado el modelo")

    def create_with_audit(self, data: dict, modified_by: str) -> T:
        """Crea un registro validando los campos de AuditMixin."""
        create_data = data.copy()
        create_data["modified_by"] = modified_by
        self._validate_audit_data(create_data)
        return super().create(**create_data)

    def update_with_audit(self, instance: T, data: dict, modified_by: str) -> T:
        """Actualiza un registro con campos de AuditMixin."""
        update_data = data.copy()
        update_data["modified_by"] = modified_by
        self._validate_audit_data(update_data)
        return super().update(instance, **update_data)


class EnvironmentMixinRepository(BaseRepository[T]):
    """Mixin para repositorios que manejan modelos con EnvironmentMixin."""

    def _validate_environment_data(self, data: dict) -> None:
        """Valida que los datos contengan environment_id."""
        if "environment_id" not in data:
            raise ValueError("Es obligatiorio definir un entorno para este modelo")

    def create_with_environment(self, data: dict, environment_id: int) -> T:
        """Crea un registro validando los campos de EnvironmentMixin."""
        create_data = data.copy()
        create_data["environment_id"] = environment_id
        self._validate_environment_data(create_data)
        return super().create(**create_data)


class AuditEnvironmentMixinRepository(BaseRepository[T]):
    """Mixin combinado para modelos con AMBOS mixins."""

    def _validate_audit_environment_data(self, data: dict) -> None:
        """Valida ambos campos requeridos."""
        if "environment_id" not in data:
            raise ValueError("environment_id requerido")
        if "modified_by" not in data:
            raise ValueError("modified_by requerido")

    def create_with_audit_env(
        self, data: dict, environment_id: int, modified_by: str
    ) -> T:
        """Crea registro con validación de ambos mixins."""
        create_data = data.copy()
        create_data["environment_id"] = environment_id
        create_data["modified_by"] = modified_by

        self._validate_audit_environment_data(create_data)
        return super().create(**create_data)

    def update_with_audit_env(self, instance: T, data: dict, modified_by: str, environment_id: int) -> T:
        """Actualiza registro con campos de ambos mixins."""
        update_data = data.copy()
        update_data["modified_by"] = modified_by
        update_data["environment_id"] = environment_id

        self._validate_audit_environment_data(update_data)
        return super().update(instance, **update_data)
