from sqlalchemy import inspect

from uat_tool.infrastructure import Base, init_db


def test_init_db_creates_tables(test_engine):
    """Test que verifica que init_db crea las tablas"""
    # Verificar que hay modelos registrados
    assert len(Base.metadata.tables) > 0

    inspector = inspect(test_engine)
    tables_before = inspector.get_table_names()
    assert tables_before == []

    init_db(engine=test_engine)

    inspector = inspect(test_engine)
    tables_after = inspector.get_table_names()

    assert len(tables_after) > 0


def test_init_db_with_drop_existing(test_engine):
    """Test que verifica que drop_existing funciona correctamente"""
    # Crear tablas primero
    Base.metadata.create_all(test_engine)
    inspector = inspect(test_engine)
    tables_before = inspector.get_table_names()

    # Recrear tablas con drop_existing
    init_db(drop_existing=True, engine=test_engine)

    tables_after = inspector.get_table_names()
    assert len(tables_after) == len(tables_before)
