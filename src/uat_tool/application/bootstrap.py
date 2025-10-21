from uat_tool.application import ApplicationContext
from uat_tool.infrastructure import get_engine, init_db
from uat_tool.shared import get_logger, setup_logging


def bootstrap(
    test_mode: bool = False, load_initial_data: bool = True
) -> ApplicationContext:
    """Inicializa el entorno completo de la aplicación de forma determinista.

    Args:
        test_mode (bool, optional): Si True, elimina tablas existentes y usa un engine aislado. Default en False.
        load_initial_data (bool, optional): Si True, carga datos iniciales. Default en True.
    Returns:
        ApplicationContext: Contexto de aplicación completamente inicializado.
    """
    setup_logging(verbose=test_mode)
    logger = get_logger(__name__)
    logger.info("Bootstrap de aplicación iniciado...")

    engine = get_engine(echo=test_mode)
    init_db(drop_existing=test_mode, engine=engine, load_initial_data=load_initial_data)

    app_context = ApplicationContext(
        test_mode=test_mode, test_engine=engine, load_initial_data=load_initial_data
    )
    app_context.initialize()

    logger.info("Bootstrap completado correctamente.")
    return app_context
