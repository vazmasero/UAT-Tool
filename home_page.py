import sys
import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Directorio donde está el archivo main de Python
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta al archivo .ui
    ui_file_route = os.path.join(base_dir, "ui", "home_page.ui")

    ui_file = QFile(ui_file_route)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_route}:{ui_file.errorString()}")
        sys.exit(-1)
    
    loader = QUiLoader()
    main_window = loader.load(ui_file)
    ui_file.close()
    if not main_window:
        print(loader.errorString())
        sys.exit(-1)

    main_window.show()

    sys.exit(app.exec())