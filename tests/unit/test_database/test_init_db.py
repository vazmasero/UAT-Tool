from sqlalchemy import inspect

from data.database import Base
from data.database.init_db import init_db


def test_init_db_creates_tables(test_engine):
    """Test que verifica que init_db crea las tablas"""
    # Asegurarse de que no hay tablas inicialmente
    inspector = inspect(test_engine)
    tables_before = inspector.get_table_names()

    # Crear tablas
    init_db()

    # Verificar que se crearon tablas
    tables_after = inspector.get_table_names()
    assert len(tables_after) > len(tables_before)


def test_init_db_with_drop_existing(test_engine):
    """Test que verifica que drop_existing funciona correctamente"""
    # Crear tablas primero
    Base.metadata.create_all(test_engine)
    inspector = inspect(test_engine)
    tables_before = inspector.get_table_names()

    # Recrear tablas con drop_existing
    init_db(drop_existing=True)

    tables_after = inspector.get_table_names()
    assert len(tables_after) == len(tables_before)
