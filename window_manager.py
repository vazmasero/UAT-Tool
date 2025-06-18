from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout

from ui.ui_main import Ui_MainWindow

# Home Page
class HomePage(QMainWindow):
    def __init__(self, manager=None,parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("UAT Tool")

# Window Manager
class WindowManager:
    def __init__(self):
        self.home = HomePage(manager=self)

    def show_home(self):
        self.home.show()


