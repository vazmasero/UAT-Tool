from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from core.models import Environment
from data.database import AuditMixin, Base, EnvironmentMixin


# Modelo de ejemplo para test
class DummyModel(AuditMixin, EnvironmentMixin, Base):
    __tablename__ = "dummy"
    environment_id = Column(Integer, ForeignKey("environments.id"))
    environment = relationship("Environment")


# -------------------
# Tests de estructura
# -------------------


def test_audit_mixin_structure():
    """Verifica que los modelos que heredan de AuditMixin tienen las debidas columnas"""
    assert hasattr(AuditMixin, "id")
    assert hasattr(AuditMixin, "created_at")
    assert hasattr(AuditMixin, "updated_at")
    assert hasattr(AuditMixin, "modified_by")
    columns = DummyModel.__table__.columns.keys()
    assert "id" in columns
    assert "created_at" in columns
    assert "updated_at" in columns
    assert "modified_by" in columns


def test_environment_mixin_structure():
    """Verifica que los modelos que heredan de EnvironmentMixin tienen environment_id"""
    columns = DummyModel.__table__.columns.keys()
    assert "environment_id" in columns


def test_base_declarative():
    """Test que verifica que Base es una base declarativa"""
    assert hasattr(Base, "metadata")
    assert isinstance(Base, type)
    assert hasattr(Base, "registry")


# -----------------------
# Tests de persistencia
# -----------------------


def test_dummy_model_insert_and_query(db_session, sample_audit_data):
    """Crea y consulta un DummyModel en la base de datos."""
    dummy = DummyModel(**sample_audit_data)
    db_session.add(dummy)
    db_session.commit()

    result = db_session.query(DummyModel).first()
    assert result is not None
    assert result.modified_by == "test_user"


def test_dummy_model_with_environment(
    db_session, sample_audit_data, model_test_data
):
    """Comprueba que environment_id puede asignarse."""
    env = Environment(**model_test_data["environment_data"])
    db_session.add(env)
    db_session.commit()

    dummy = DummyModel(**sample_audit_data, environment_id=env.id)
    db_session.add(dummy)
    db_session.commit()

    result = db_session.query(DummyModel).first()
    assert result.environment_id == env.id
    assert result.modified_by == "test_user"
    assert result.environment.name == "Test Environment"
