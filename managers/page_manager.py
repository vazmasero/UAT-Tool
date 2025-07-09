from typing import Dict, Callable, Optional
from PySide6.QtCore import QObject, Signal
from config.app_config import AppConfig
from config.form_config import FORMS
from config.page_config import PAGES

class PageManager(QObject):

    def __init__(self, stacked_widget, ui):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.ui = ui
    
    def change_page(self, page_name: str):      
        if page_name not in PAGES:
            return
        
        index = PAGES[page_name]["config"].index
        self.stacked_widget.setCurrentIndex(index)
        self.current_page = page_name

        # Makes "Start campaign" button visible if page = campaigns
        self.ui.btn_start.setVisible(page_name == "campaigns")
        
        # If page has tabs, set first tab as initial
        if page_name == "management":
            self.ui.tab_widget_management.setCurrentIndex(0)
        elif page_name == "assets":
            self.ui.tab_widget_assets.setCurrentIndex(0)
        
    def get_current_tab_index(self) -> Optional[int]:
        if self.current_page == "management":
            return self.ui.tab_widget_management.currentIndex()
        elif self.current_page == "assets":
            return self.ui.tab_widget_assets.currentIndex()
        return None