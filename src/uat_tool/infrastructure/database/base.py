from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import declarative_base, declared_attr

Base = declarative_base()


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
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    modified_by = Column(String, nullable=False)
