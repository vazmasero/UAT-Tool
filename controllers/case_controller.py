from services.case_service import CaseService
from config.model_domains import Case
from typing import Optional, Dict

class CaseController:
    def __init__(self, service: CaseService):
            self.service = service

    def get_lw_data(self):
        systems = self.service.get_systems()
        sections = self.service.get_sections()
        operators = self.service.get_operators()
        drones = self.service.get_drones()
        uhub_users = self.service.get_uhub_users()
        return {
            "systems": systems,
            "sections": sections,
            "operators": operators,
            "drones": drones,
            "uhub_users": uhub_users
        }