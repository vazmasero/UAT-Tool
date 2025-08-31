from services.assets_service import AssetsService
from config.assets_config import AssetConfig
from typing import Optional, Dict, Any


class AssetsController:
    
    def __init__(self, service: AssetsService, asset_config: AssetConfig):
        """Initizializes the asstes page controller.
        
        It communicates the users inputs with the actions performed by the service on
        the database.
        """
        self.service = service
        self.config = asset_config

    def get_item_by_id(self, db_id: int):
        """Fetches an item by its ID."""
        return self.service.get_item_by_id(db_id, self.config.table_name)

    def handle_form_submission(self, form_data: Dict,
                               db_id: Optional[int] = None) -> None:
        if db_id:
            return self.service.update_item(
                db_id, form_data, self.config.table_name)
        return self.service.create_item(form_data, self.config.table_name)

    def prepare_form_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.service.prepare_form_data(raw_data, self.config)
