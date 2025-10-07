from uat_tool.infrastructure import DB_URL, Session, engine


def test_engine_creation():
    """Test que verifica la creación del motor"""
    assert engine is not None
    assert str(engine.url) == DB_URL


def test_session_creation():
    """Test que verifica la creación de la sesión"""
    assert Session is not None
    assert hasattr(Session, "query")
