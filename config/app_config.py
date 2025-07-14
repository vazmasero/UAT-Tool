from typing import Protocol, Any
from PySide6.QtWidgets import QStackedWidget, QPushButton, QTableView, QTabWidget

class BaseUI(Protocol):
    stacked_widget: QStackedWidget
    btn_add: QPushButton
    btn_edit: QPushButton
    btn_remove: QPushButton
    btn_start: QPushButton
    tab_widget_management: QTabWidget
    tab_widget_assets: QTabWidget



class AppConfig:
    """Centralized configuration for the application. """
