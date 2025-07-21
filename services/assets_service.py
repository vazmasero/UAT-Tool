from db.db import DatabaseManager
from config.model_domains import Email
from typing import Dict, Any, List, Optional
from config.assets_config import AssetConfig

class AssetsService:

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def get_item_by_id(self, db_id: int, table_name: str) -> Optional[Dict[str, Any]]:
        return self.db_manager.get_by_id(table_name, db_id)

    def create_item(self, data: Dict[str, Any], table_name: str) -> bool:
        try:
            self.db_manager.create_register(table_name, data)
            return True
        except Exception as e:
            print(f"Error creating {table_name}: {e}")
            return False
        
    def update_item(self, item_id: int, data: Dict[str, Any], table_name: str) -> bool:
        try:
            return self.db_manager.edit_register(table_name, item_id, data)
        except Exception as e:
            print(f"Error updating {table_name}: {e}")
            return False

    def get_systems(self):
        systems = self.db_manager.get_all_data("systems")
        return [system["name"] for system in systems] if systems else []

    def get_sections(self):
        sections = self.db_manager.get_all_data("sections")
        return [section["name"] for section in sections] if sections else []
    
    def prepare_form_data(self, raw_data: Dict[str, Any], config: AssetConfig) -> Dict[str, Any]:
        if not raw_data:
            return {}
        
        formatted_data = {}
        
        header_to_db_map = {
            'Id': 'id',
            'Name': 'name', 
            'Email': 'email',
            'Password': 'password',
            'Serial Number': 'serial_number',
            'Manufacturer': 'manufacturer',
            'Model': 'model',
            'Operator': 'operator',
            'Tracker Type': 'tracker_type',
            'Transponder ID': 'transponder_id',
            'EASA ID': 'easa_id',
            'Verification Code': 'verification_code',
            'Phone': 'phone',
            'Description': 'description'
        }
        
        for key, value in raw_data.items():
            db_key = header_to_db_map.get(key, key.lower())
            formatted_data[db_key] = value
        
        result = {}
        for field in config.fields:
            result[field] = formatted_data.get(field, "")
        
        return result
            
