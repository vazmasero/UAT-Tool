from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import Session as SQLAlchemySession
from sqlalchemy.orm import scoped_session

from data.database.engine import Session
from data.repositories import (
    BlockRepository,
    BugRepository,
    CampaignRepository,
    CampaignRunRepository,
    CaseRepository,
    CaseRunRepository,
    DroneRepository,
    EmailRepository,
    EnvironmentRepository,
    FileRepository,
    OperatorRepository,
    ReasonRepository,
    RequirementRepository,
    SectionRepository,
    StepRepository,
    StepRunRepository,
    SystemRepository,
    UasZoneRepository,
    UhubOrgRepository,
    UhubUserRepository,
    UspaceRepository,
)


class UnitOfWork:
    """Unidad de trabajo que agrupa todos los repositorios para transacciones
    atómicas.
    """

    def __init__(self, session: SQLAlchemySession | scoped_session):
        self.session = session

        # Repositorios de ejecución
        self.campaign_run_repo = CampaignRunRepository(session)
        self.case_run_repo = CaseRunRepository(session)
        self.step_run_repo = StepRunRepository(session)

        # Repositorios de gestión de tests
        self.campaign_repo = CampaignRepository(session)
        self.block_repo = BlockRepository(session)
        self.case_repo = CaseRepository(session)
        self.step_repo = StepRepository(session)

        # Repositorio de bugs
        self.bug_repo = BugRepository(session)

        # Repositorio de requisitos
        self.req_repo = RequirementRepository(session)

        # Repositorios auxiliares
        self.env_repo = EnvironmentRepository(session)
        self.sys_repo = SystemRepository(session)
        self.section_repo = SectionRepository(session)
        self.reason_repo = ReasonRepository(session)
        self.file_repo = FileRepository(session)

        # Repositorio de assets
        self.email_repo = EmailRepository(session)
        self.ope_repo = OperatorRepository(session)
        self.zone_repo = UasZoneRepository(session)
        self.org_repo = UhubOrgRepository(session)
        self.user_repo = UhubUserRepository(session)
        self.uspace_repo = UspaceRepository(session)
        self.drone_repo = DroneRepository(session)

    def commit(self):
        """Confirma todas las operaciones pendientes."""
        self.session.commit()

    def rollback(self):
        """Revierte todas las operaciones pendientes."""
        self.session.rollback()

    def close(self):
        """Cierra la sesión de forma segura para ambos tipos (scoped o no)."""
        try:
            if hasattr(self.session, "close"):
                self.session.close()
            elif hasattr(self.session, "remove"):
                self.session.remove()
        except Exception as e:
            print(f"Error cerrando sesión: {e}")


@contextmanager
def unit_of_work() -> Generator[UnitOfWork, None, None]:
    """Context manager para manejar la unidad de trabajo.

    Usage:
    with unit_of_work() as uow:
        uow.bug_repo.create(...)
        # Commit automático al salir si no hay erorres
    """
    session = Session()
    uow = UnitOfWork(session)
    try:
        yield uow
        uow.commit()

    except Exception:
        uow.rollback()
        raise
    finally:
        uow.close()
