from typing import Optional, Dict

from db.db import DatabaseManager
from utils.dict_utils import get_base_table_config
from config.table_config import TableCommonConfig


class TableService:
    def __init__(self):
        self.db_manager = DatabaseManager()
        
    def get_table_data(self, table_name):
        return self.db_manager.get_all_data(table_name)
    
    @staticmethod
    def merge_table_config(name:str, custom_config: Optional[Dict] = None) -> Dict:
        base_config = get_base_table_config(name)
        generic_config = TableCommonConfig.get_generic_table_config()
        return {**generic_config, **vars(base_config), **(custom_config or {})}