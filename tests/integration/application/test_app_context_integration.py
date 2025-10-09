from unittest.mock import patch

import pytest


@patch("uat_tool.application.services.bug_service.BugService")
@patch("uat_tool.application.app_context.init_db")
def test_initialize_and_shutdown_integration(mock_init_db, MockBugService, app_context):
    """Verifica que ApplicationContext inicializa correctamente la BD y los servicios reales."""
    mock_bug_service_instance = MockBugService.return_value

    # --- Ejecutar ---
    app_context.initialize()

    # --- Verificar base de datos inicializada ---
    mock_init_db.assert_called_once_with(drop_existing=True)

    # --- Verificar que BugService fue creado y registrado ---
    MockBugService.assert_called_once_with(app_context)
    assert "bug_service" in app_context._services
    assert app_context._services["bug_service"] is mock_bug_service_instance
    assert app_context.is_initialized()

    # --- Ejecutar shutdown ---
    app_context.shutdown()

    # --- Verificar limpieza ---
    assert not app_context._services
    assert not app_context.is_initialized()


def test_get_unit_of_work_context_real(app_context):
    """Verifica que get_unit_of_work_context devuelve un context manager funcional."""
    from uat_tool.application.uow import UnitOfWork

    with app_context.get_unit_of_work_context() as uow:
        assert isinstance(uow, UnitOfWork)
        assert hasattr(uow, "commit")
        assert hasattr(uow, "rollback")


@patch("uat_tool.application.app_context.init_db", side_effect=Exception("DB broken"))
def test_initialize_raises_and_logs_integration(mock_init_db, app_context):
    """Verifica que ApplicationContext.initialize relanza errores de init_db."""
    with pytest.raises(Exception, match="DB broken"):
        app_context.initialize()

    mock_init_db.assert_called_once()
    assert not app_context.is_initialized()
