from enum import Enum
from typing import Dict, Callable, Optional
from PySide6.QtCore import QObject, Signal
from config.app_config import AppConfig
from config.forms_config import PageType, FormType

class PageManager(QObject):

    page_changed = Signal(int)

    def __init__(self, stacked_widget, ui):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.ui = ui
        self.current_page = PageType.BUGS

        # Index-page mapping
        self.page_indices ={
            PageType.BUGS: 0,
            PageType.CAMPAIGNS: 1,
            PageType.MANAGEMENT: 2,
            PageType.REQUIREMENTS: 3,
            PageType.ASSETS: 4
        }
        
        # PageType to database key mapping
        self.page_to_db_key = {
            PageType.BUGS: "bugs",
            PageType.CAMPAIGNS: "campaigns", 
            PageType.MANAGEMENT: "cases",
            PageType.REQUIREMENTS: "requirements",
            PageType.ASSETS: "emails"
        }

        # Page data loading callable
        self.data_loaders: Dict[PageType, Callable] = {}

    def register_data_loader(self, page_type: PageType, loader: Callable):
        self.data_loaders[page_type] = loader
    
    def change_page(self, page_type: PageType):      
        if page_type not in self.page_indices:
            return
        
        index = self.page_indices[page_type]
        self.stacked_widget.setCurrentIndex(index)
        self.current_page = page_type

        self.ui.btn_start.setVisible(page_type == PageType.CAMPAIGNS)
        
        db_key = self.page_to_db_key[page_type]
        
        if page_type in self.data_loaders:
            self.data_loaders[page_type](db_key, None)
        
        self.page_changed.emit(index)

    def get_current_tab_index(self) -> Optional[int]:
        if self.current_page == PageType.MANAGEMENT:
            return self.ui.tab_widget_management.currentIndex()
        elif self.current_page == PageType.ASSETS:
            return self.ui.tab_widget_assets.currentIndex()
        return None