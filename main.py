"""Módulo principal de la aplicación.

Inicializa la base de datos, crea la ventana principal y lanza
el bucle de eventos de la interfaz gráfica.
"""

# import sys

# from PySide6.QtWidgets import QApplication

#from application.application_controller import ApplicationController
from data.database import Session, init_db

# from views.main_window import MainWindow


def main():
    # Inicializa la base de datos y carga datos iniciales
    init_db()

    # Crea la sesión para los repositorios
    #session = Session()

    # Inicializa el ApplicationController con la sesión
    #app_controller = ApplicationController(session)

    """# Inicializa la aplicación Qt
    app = QApplication(sys.argv)

    # Pasa el controller a la ventana principal
    main_window = MainWindow(controller=app_controller)
    main_window.show()

    sys.exit(app.exec())"""


if __name__ == "__main__":
    main()
