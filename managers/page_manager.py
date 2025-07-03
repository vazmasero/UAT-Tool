from typing import Dict, Callable, Optional
from PySide6.QtCore import QObject, Signal
from config.app_config import AppConfig
from config.forms_config import FORMS
from config.page_config import PAGES

class PageManager(QObject):

    page_changed = Signal(int)

    def __init__(self, stacked_widget, ui):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.ui = ui
        self.current_page = "bugs"

        # Page data loading callable
        self.data_loaders: Dict[str, Callable] = {}

    def register_data_loader(self, page_name: str, loader: Callable):
        self.data_loaders[page_name] = loader
    
    def change_page(self, page_name: str):      
        if page_name not in PAGES:
            return
        
        index = PAGES.get(page_name, {}).get("index")
        self.stacked_widget.setCurrentIndex(index)
        self.current_page = page_name

        self.ui.btn_start.setVisible(page_name == "campaigns")
        
        # Buscar la primera tabla asociada a la página (si existe)
        from config.table_config import TABLES
        tablas_pagina = [key for key, tinfo in TABLES.items() if tinfo.page == page_name]
        db_key = tablas_pagina[0] if tablas_pagina else None
        
        if page_name in self.data_loaders and db_key:
            self.data_loaders[page_name](db_key, None)
        
        self.page_changed.emit(index)

    def get_current_tab_index(self) -> Optional[int]:
        if self.current_page == "management":
            return self.ui.tab_widget_management.currentIndex()
        elif self.current_page == "assets":
            return self.ui.tab_widget_assets.currentIndex()
        return None