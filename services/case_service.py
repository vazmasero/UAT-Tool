from db.db import DatabaseManager
from config.model_domains import Case

class CaseService:
    def __init__(self, db_manager: DatabaseManager, table_manager=None):
        self.db_manager = db_manager
        self.table_manager = table_manager

    def get_systems(self):
        systems = self.db_manager.get_all_data("systems")
        return [system["name"] for system in systems] if systems else []

    def get_sections(self):
        sections = self.db_manager.get_all_data("sections")
        return [section["name"] for section in sections] if sections else []

    def get_operators(self):
        operators = self.db_manager.get_all_data("operators")
        return [operator["name"] for operator in operators] if operators else []

    def get_drones(self):
        drones = self.db_manager.get_all_data("drones")
        return [drone["name"] for drone in drones] if drones else []

    def get_uhub_users(self):
        uhub_users = self.db_manager.get_all_data('uhub_users')
        return [uhub_user["username"] for uhub_user in uhub_users] if uhub_users else []