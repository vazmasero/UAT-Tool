from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import declarative_base, declared_attr

Base = declarative_base(name="Base")
metadata = Base.metadata


class EnvironmentMixin:
    @declared_attr
    def environment_id(cls):
        return Column(
            Integer,
            ForeignKey("environments.id", ondelete="RESTRICT"),
            nullable=False,
        )


class AuditMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

    modified_by = Column(String, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, name={getattr(self, 'name', None)})>"
