from unittest.mock import MagicMock, Mock, patch

import pytest

# Importar el módulo completo para poder hacer patch
from uat_tool.application.uow import UnitOfWork, unit_of_work

PATH_TO_UOW_CLASS = "uat_tool.application.uow.UnitOfWork"
PATH_TO_SESSION_CLASS = "uat_tool.application.uow.Session"


class TestUnitOfWork:
    """Tests para Unit of Work"""

    def test_unit_of_work_initialization(self, db_session):
        """Test inicialización de UnitOfWork"""
        uow = UnitOfWork(db_session)

        # Verificar que todos los repositorios están inicializados
        assert uow.session == db_session
        assert uow.bug_repo is not None
        assert uow.req_repo is not None
        assert uow.campaign_repo is not None
        assert uow.block_repo is not None
        assert uow.case_repo is not None
        assert uow.step_repo is not None
        assert uow.env_repo is not None
        assert uow.sys_repo is not None
        assert uow.section_repo is not None
        assert uow.email_repo is not None
        assert uow.ope_repo is not None
        assert uow.drone_repo is not None
        assert uow.zone_repo is not None
        assert uow.org_repo is not None
        assert uow.user_repo is not None
        assert uow.uspace_repo is not None

    def test_unit_of_work_commit(self, db_session):
        """Test commit de UnitOfWork"""
        uow = UnitOfWork(db_session)

        # Mock de la sesión para verificar que se llama a commit
        with patch.object(db_session, "commit") as mock_commit:
            uow.commit()
            mock_commit.assert_called_once()

    def test_unit_of_work_rollback(self, db_session):
        """Test rollback de UnitOfWork"""
        uow = UnitOfWork(db_session)

        # Mock de la sesión para verificar que se llama a rollback
        with patch.object(db_session, "rollback") as mock_rollback:
            uow.rollback()
            mock_rollback.assert_called_once()

    def test_unit_of_work_close_scoped_session(self):
        """Test que llama a remove() cuando la sesión es scoped."""
        # Crear un mock que simule scoped_session (tiene remove pero no close)
        scoped_session_mock = Mock()

        # Nos aseguramos de que el mock no tenga close.
        if hasattr(scoped_session_mock, "close"):
            del scoped_session_mock.close

        # Instanciar el objeto a probar y ejecutar el método
        uow = UnitOfWork(scoped_session_mock)
        uow.close()

        # Verificar la interacción
        scoped_session_mock.remove.assert_called_once()

        # Asegurar que 'close' NO fue llamado (si el mock tiene el atributo)
        if hasattr(scoped_session_mock, "close"):
            scoped_session_mock.close.assert_not_called()

    def test_unit_of_work_close_regular_session(self):
        """Test que llama a close() cuando la sesión es regular."""
        # Crear un mock que simule una sesión regular
        regular_session_mock = Mock()

        # Forzar que el mock no tenga el método 'remove'
        if hasattr(regular_session_mock, "remove"):
            del regular_session_mock.remove

        uow = UnitOfWork(regular_session_mock)
        uow.close()

        regular_session_mock.close.assert_called_once()


class TestUnitOfWorkContextManager:
    """Tests para el context manager de Unit of Work"""

    def test_unit_of_work_context_success(self):
        """Test context manager exitoso"""
        with unit_of_work() as uow:
            assert isinstance(uow, UnitOfWork)
            assert uow.session is not None

            # Verificar que se puede acceder a los repositorios
            assert uow.bug_repo is not None
            assert uow.req_repo is not None

    def test_unit_of_work_context_with_exception(self):
        """Test context manager con excepción"""
        with pytest.raises(ValueError, match="Test error"):
            with unit_of_work() as uow:
                assert isinstance(uow, UnitOfWork)
                raise ValueError("Test error")

    @patch(PATH_TO_SESSION_CLASS)
    @patch(PATH_TO_UOW_CLASS)
    def test_uow_commits_on_success(
        self, MockUnitOfWork: MagicMock, MockSession: MagicMock
    ):
        """Verifica que se llama a commit() y close() si no hay excepciones."""
        # Configura el mock para que devuelva instancia simulada
        mock_uow_instance = MockUnitOfWork.return_value

        with unit_of_work() as uow:
            assert uow is mock_uow_instance

        # Verificamos las llamadas al salir del context manager
        MockSession.assert_called_once()
        MockUnitOfWork.assert_called_once_with(MockSession.return_value)
        mock_uow_instance.commit.assert_called_once()
        mock_uow_instance.rollback.assert_not_called()
        mock_uow_instance.close.assert_called_once()

    @patch(PATH_TO_SESSION_CLASS)
    @patch(PATH_TO_UOW_CLASS)
    def test_uow_rollbacks_on_exception(
        self, MockUnitOfWork: MagicMock, MockSession: MagicMock
    ):
        """Verifica que se llama a rollback() y close() si hay excepciones."""
        # Configura el mock para que devuelva instancia simulada
        mock_uow_instance = MockUnitOfWork.return_value

        with pytest.raises(ValueError, match="Test error"):
            with unit_of_work() as uow:
                assert uow is mock_uow_instance
                raise ValueError("Test error")

        # Verificamos las llamadas tras la excepción
        MockSession.assert_called_once()
        MockUnitOfWork.assert_called_once_with(MockSession.return_value)
        mock_uow_instance.commit.assert_not_called()
        mock_uow_instance.rollback.assert_called_once()
        mock_uow_instance.close.assert_called_once()

class TestUnitOfWorkErrorScenarios:
    """Tests para escenarios de error en Unit of Work"""

    def test_unit_of_work_close_with_errors(self, db_session):
        """Test cierre de UoW con errores"""
        uow = UnitOfWork(db_session)

        # Para una sesión regular, usamos close
        with patch.object(
            db_session, "close", side_effect=Exception("Close error")
        ) as mock_close:
            uow.close()
            mock_close.assert_called_once()
