# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from window_manager import HomePage
# Important:
# You need to run the following command to generate the ui_xxx.py file
# pyside6-uic xxx.ui -o ui_xxx.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec())
