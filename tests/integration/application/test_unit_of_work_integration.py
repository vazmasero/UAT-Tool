# Importar el módulo completo para poder hacer patch
from uat_tool.application.uow import UnitOfWork

PATH_TO_UOW_CLASS = "uat_tool.application.uow.UnitOfWork"
PATH_TO_SESSION_CLASS = "uat_tool.application.uow.Session"


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
