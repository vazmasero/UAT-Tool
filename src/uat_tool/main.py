"""Módulo principal de la aplicación.

Inicializa la base de datos, contexto de aplicación, controlador principal y
crea la ventana principal y lanza el bucle de eventos de la interfaz gráfica.
"""

import sys

from PySide6.QtWidgets import QApplication

from uat_tool.application import bootstrap
from uat_tool.presentation import MainWindow
from uat_tool.presentation.controllers import MainController
from uat_tool.shared import get_logger, setup_logging

setup_logging(verbose=False)
logger = get_logger(__name__)


class ApplicationOrchestrator:
    """Orquestador principal de la aplicación."""

    def __init__(self):
        """Inicializa ApplicationOrchestrator con placeholders.

        Configura los atributos de instancia de applicación, contexto, controlador y ventana principal
        a None. Estos serán incializados más tarde durante el ciclo de la aplicación.

        Esta inicialización diferida permite una gestión de dependencias y un manejo de errores correcto
        durante la inicialización de la aplicación.
        """
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
            self.app_context = bootstrap()

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
            logger.error("Error durante la inicialización: %s", e)
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
        shutdown_actions = [
            (self.main_controller, "shutdown"),
            (self.app, "quit"),
            (self.app_context, "shutdown"),
        ]

        for component, shutdown_method in shutdown_actions:
            self._safe_component_shutdown(component, shutdown_method)

    def _safe_component_shutdown(self, component, method_name):
        """Apaga un componente individual de forma segura."""
        if component is None:
            return

        try:
            method = getattr(component, method_name)
            method()
        except Exception as e:
            component_name = type(component).__name__
            logger.error("Error cerrando %s: %s", component_name, e)

    def _safe_component_shutdown(self, component, method_name):
        """Apaga un componente individual de forma segura."""
        if component is None:
            return

        try:
            method = getattr(component, method_name)
            method()
        except Exception as e:
            component_name = type(component).__name__
            logger.error("Error cerrando %s: %s", component_name, e)

    def run(self):
        """Ejecuta la aplicación principal."""
        if not all([self.app, self.main_controller, self.main_window]):
            raise RuntimeError("La aplicación no está inicializada correctamente")

        try:
            logger.info("Mostrando ventana principal...")
            self.main_window.show()
            return_code = self.app.exec()
            logger.info("Aplicación finalizada")
            return return_code

        except Exception as e:
            logger.error("Error durante la ejecución: %s", e)
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
        logger.error("Error fatal: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
