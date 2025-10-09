from unittest.mock import MagicMock, patch

import pytest

from uat_tool.application import ApplicationContext


def test_initialize_calls_internal_methods_once():
    """Verifica que la inicialización de AppContext funciona y que solo ocurre una vez."""
    ctx = ApplicationContext()
    with (
        patch.object(ctx, "_initialize_database") as mock_db,
        patch.object(ctx, "_initialize_services") as mock_services,
    ):
        ctx.initialize()

        mock_db.assert_called_once()
        mock_services.assert_called_once()
        assert ctx.is_initialized()

        # Segunda llamada no vuelve a ejecutar
        ctx.initialize()
        mock_db.assert_called_once()
        mock_services.assert_called_once()


def test_get_uow_with_custom_session_factory():
    """Verifica la función get_uow() para garantizar que proporciona un uow"""
    mock_session = MagicMock()
    mock_uow = MagicMock()
    ctx = ApplicationContext()
    ctx._session_factory = lambda: mock_session  # inyectamos factory

    # patch UnitOfWork
    with patch(
        "uat_tool.application.app_context.UnitOfWork", return_value=mock_uow
    ) as MockUnitOfWork:
        uow = ctx.get_uow()

    assert uow is mock_uow
    MockUnitOfWork.assert_called_once_with(mock_session)


def test_register_and_get_service():
    """Prueba la funcionalidad de registro y obtención de un servicio."""
    ctx = ApplicationContext()
    service = object()
    ctx._is_initialized = True  # simular inicialización previa

    ctx.register_service("test_service", service)
    assert ctx.get_service("test_service") is service


def test_get_service_raises_if_not_initialized():
    """Garantiza que se produzca un error si se intenta obtener un servicio antes de la inicialización."""
    ctx = ApplicationContext()
    with pytest.raises(RuntimeError, match="no está inicializado"):
        ctx.get_service("something")


def test_shutdown_calls_service_shutdown_and_clears():
    """Mockea un servicio con método shutdown() y verifica que se llame."""
    ctx = ApplicationContext()
    mock_service = MagicMock()
    ctx._services = {"bug_service": mock_service}
    ctx._is_initialized = True

    ctx.shutdown()

    mock_service.shutdown.assert_called_once()
    assert ctx._services == {}
    assert not ctx._is_initialized


def test_get_instance_returns_singleton():
    """Verifica el patrón singleton de get_instance()."""
    instance1 = ApplicationContext.get_instance()
    instance2 = ApplicationContext.get_instance()
    assert instance1 is instance2


@patch(
    "uat_tool.application.app_context.init_db", side_effect=Exception("DB init error")
)
def test_initialize_database_raises_and_logs(mock_init_db):
    """Verifica que _initialize_database propaga excepciones de init_db."""
    ctx = ApplicationContext(test_mode=True)

    with pytest.raises(Exception, match="DB init error"):
        ctx._initialize_database()

    mock_init_db.assert_called_once_with(drop_existing=True)


@patch(
    "uat_tool.application.services.bug_service.BugService",
    side_effect=Exception("Service init failed"),
)
@patch("uat_tool.application.app_context.init_db")
def test_initialize_services_raises_and_logs(mock_init_db, mock_bug_service):
    """Verifica que initialize() propaga excepciones si un servicio falla."""
    ctx = ApplicationContext(test_mode=True)

    with pytest.raises(Exception, match="Service init failed"):
        ctx.initialize()

    mock_init_db.assert_called_once_with(drop_existing=True)
    mock_bug_service.assert_called_once_with(ctx)
    assert not ctx.is_initialized()


def test_initialize_twice_warns(monkeypatch):
    """Verifica que se muestra un warning si initialize() se llama dos veces."""
    ctx = ApplicationContext()
    ctx._is_initialized = True

    mock_logger = MagicMock()
    monkeypatch.setattr("uat_tool.application.app_context.logger", mock_logger)

    ctx.initialize()
    mock_logger.warning.assert_called_once_with(
        "ApplicationContext ya está inicializado"
    )


def test_shutdown_logs_error_on_exception(monkeypatch):
    """Verifica que shutdown registra errores pero no lanza excepciones."""
    ctx = ApplicationContext()
    ctx._is_initialized = True

    bad_service = MagicMock()
    bad_service.shutdown.side_effect = Exception("Failed to close service")

    ctx._services = {"bug_service": bad_service}

    mock_logger = MagicMock()
    monkeypatch.setattr("uat_tool.application.app_context.logger", mock_logger)

    ctx.shutdown()

    bad_service.shutdown.assert_called_once()
    mock_logger.error.assert_any_call(
        "Error cerrando servicio bug_service: Failed to close service"
    )
    mock_logger.error.assert_any_call(
        "Error(es) cerrando ApplicationContext: bug_service: Failed to close service"
    )

    assert not ctx._services
    assert ctx._is_initialized is False
