import sys
from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow
from db.db import init_db

if __name__ == "__main__":
    app = QApplication(sys.argv)

    init_db()

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())