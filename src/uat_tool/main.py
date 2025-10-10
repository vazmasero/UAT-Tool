"""Módulo principal de la aplicación.

Inicializa la base de datos, crea la ventana principal y lanza
el bucle de eventos de la interfaz gráfica.
"""

import sys

from PySide6.QtWidgets import QApplication

from uat_tool.application import ApplicationContext
from uat_tool.presentation import MainWindow
from uat_tool.presentation.controllers import MainController
from uat_tool.shared import get_logger, setup_logging

setup_logging(verbose=False)
logger = get_logger(__name__)


class ApplicationOrchestrator:
    """Orquestador principal de la aplicación."""

    def __init__(self):
        self.app = None
        self.app_context = None
        self.main_controller = None
        self.main_window = None

    def initialize_application(self):
        """Inicializa todos los componentes de la aplicación."""
        try:
            logger.info("Inicializando UAT Tool...")

            # Crear aplicación Qt
            self.app = QApplication(sys.argv)
            self.app.setApplicationName("ENAIRE U-space UAT Tool")
            self.app.setApplicationVersion("1.0.0")
            self.app.setOrganizationName("ENAIRE")

            # Inicializar contexto de la aplicación
            logger.info("Configurando capa de aplicación...")
            self.app_context = ApplicationContext.get_instance()
            self.app_context.initialize()

            # Configurar controlador principal
            logger.info("Configurando interfaz...")
            self.main_controller = MainController(self.app_context)
            self.main_controller.initialize()

            # Crear ventana principal
            self.main_window = MainWindow(self.main_controller)

            # Configurar manejo de excepciones global
            self._setup_global_exception_handling()

            logger.info("Aplicación lista")

        except Exception as e:
            logger.error(f"Error durante la inicialización: {e}")
            self._safe_shutdown()
            raise

    def _setup_global_exception_handling(self):
        """Configura el manejo global de excepciones."""

        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            logger.critical(
                "Excepción no capturada:", exc_info=(exc_type, exc_value, exc_traceback)
            )

        sys.excepthook = handle_exception

    def _safe_shutdown(self):
        """Cierre seguro de la aplicación."""
        try:
            if self.main_controller:
                self.main_controller.shutdown()
            if self.app:
                self.app.quit()
            if self.app_context:
                self.app_context.shutdown()
        except Exception as e:
            logger.error(f"Error durante el cierre: {e}")

    def run(self):
        """Ejecuta la aplicación principal."""
        if not all([self.app, self.main_controller, self.main_window]):
            raise RuntimeError("La aplicación no está inicializada correctamente")

        try:
            logger.info("Mostrando ventana principal...")
            self.main_window.show()

            # Ejecutar aplicación
            return_code = self.app.exec()

            logger.info("Aplicación finalizada")
            return return_code

        except Exception as e:
            logger.error(f"Error durante la ejecución: {e}")
            return 1
        finally:
            self._safe_shutdown()


def main():
    """Punto de entrada principal."""
    orchestrator = ApplicationOrchestrator()

    try:
        orchestrator.initialize_application()
        return orchestrator.run()

    except Exception as e:
        logger.error(f"Error fatal: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
