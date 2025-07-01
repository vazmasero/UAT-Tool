import sys
from PySide6.QtWidgets import QApplication

from pages.home import HomePage
from db import init_db

if __name__ == "__main__":
    app = QApplication(sys.argv)

    init_db()

    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec())
