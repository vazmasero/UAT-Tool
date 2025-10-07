from unittest.mock import Mock, patch

import pytest

# Importar el módulo completo para poder hacer patch
from uat_tool.application.unit_of_work import UnitOfWork, unit_of_work


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
        """Test cierre de sesión scoped"""
        # Crear un mock que simule scoped_session (tiene remove pero no close)
        scoped_session_mock = Mock()
        scoped_session_mock.remove = Mock()
        # Forzar que no tenga close
        del scoped_session_mock.close

        uow = UnitOfWork(scoped_session_mock)
        uow.close()

        scoped_session_mock.remove.assert_called_once()


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


class TestUnitOfWorkIntegration:
    """Tests de integración para Unit of Work"""

    def test_unit_of_work_with_actual_operations(
        self, db_session, model_test_data, sample_audit_data
    ):
        """Test UnitOfWork con operaciones reales de repositorio"""
        uow = UnitOfWork(db_session)

        # Crear un sistema y sección usando el repositorio del UoW
        system = uow.sys_repo.create(**model_test_data["system_data"])
        section = uow.section_repo.create(**model_test_data["section_data"])

        # Crear un requisito
        requirement_data = {
            **model_test_data["requirement_data"],
            "systems": [system.id],
            "sections": [section.id],
        }

        requirement = uow.req_repo.create(
            requirement_data,
            environment_id=1,
            modified_by=sample_audit_data["modified_by"],
        )

        # Verificar que las operaciones se realizaron correctamente
        assert system.id is not None
        assert requirement.id is not None
        assert requirement.code == "REQ001"

        # Commit de las operaciones
        uow.commit()

        # Verificar que los datos persisten después del commit
        persisted_system = uow.sys_repo.get_by_id(system.id)
        persisted_requirement = uow.req_repo.get_by_id(requirement.id)

        assert persisted_system is not None
        assert persisted_requirement is not None
        assert persisted_requirement.code == "REQ001"

    def test_unit_of_work_rollback_operations(self, db_session, model_test_data):
        """Test que el rollback revierte las operaciones"""
        uow = UnitOfWork(db_session)

        # Contar sistemas antes de la operación
        initial_count = len(uow.sys_repo.get_all())

        # Crear un nuevo sistema
        system = uow.sys_repo.create(**model_test_data["system_data"])

        # Verificar que se creó en la sesión actual
        current_count = len(uow.sys_repo.get_all())
        assert current_count == initial_count + 1

        # Hacer rollback
        uow.rollback()

        # Verificar que el sistema no persiste después del rollback
        final_count = len(uow.sys_repo.get_all())
        assert final_count == initial_count

    def test_unit_of_work_multiple_repositories(
        self, db_session, model_test_data, sample_audit_data
    ):
        """Test uso de múltiples repositorios en el mismo UoW"""
        uow = UnitOfWork(db_session)

        # Usar varios repositorios
        system = uow.sys_repo.create(**model_test_data["system_data"])
        section = uow.section_repo.create(**model_test_data["section_data"])

        # Crear requirement relacionado
        requirement_data = {
            **model_test_data["requirement_data"],
            "systems": [system.id],
            "sections": [section.id],
        }

        requirement = uow.req_repo.create(
            requirement_data,
            environment_id=1,
            modified_by=sample_audit_data["modified_by"],
        )

        # Verificar relaciones
        assert requirement.systems[0].id == system.id
        assert requirement.sections[0].id == section.id

        uow.commit()

        # Verificar persistencia
        persisted_requirement = uow.req_repo.get_with_relations(requirement.id)
        assert persisted_requirement is not None
        assert len(persisted_requirement.systems) == 1
        assert len(persisted_requirement.sections) == 1


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
