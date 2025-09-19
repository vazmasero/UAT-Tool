from data.database.base import AuditMixin, Base, EnvironmentMixin


def test_audit_mixin_structure():
    """Test que verifica la estructura de AuditMixin"""
    assert hasattr(AuditMixin, "id")
    assert hasattr(AuditMixin, "created_at")
    assert hasattr(AuditMixin, "updated_at")
    assert hasattr(AuditMixin, "modified_by")


def test_environment_mixin_structure():
    """Test que verifica la estructura de EnvironmentMixin"""
    assert hasattr(EnvironmentMixin, "environment_id")


def test_base_declarative():
    """Test que verifica que Base es una base declarativa"""
    assert hasattr(Base, "metadata")
    assert hasattr(Base, "query")
