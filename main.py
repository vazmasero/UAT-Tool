"""Módulo principal de la aplicación.

Inicializa la base de datos, crea la ventana principal y lanza
el bucle de eventos de la interfaz gráfica.
"""

import sys

from PySide6.QtWidgets import QApplication

from db import db
from views.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Inicializa la base de datos
    db.init_db()

    # Crear y mostrar la ventana principal
    main_window = MainWindow()
    main_window.show()

    # Ejecuta el bucle de eventos de la app
    sys.exit(app.exec())
