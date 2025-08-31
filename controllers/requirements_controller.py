from services.requirement_service import RequirementService
from config.model_domains import Requirement
from typing import Optional, Dict


class RequirementController:
    
    def __init__(self, service: RequirementService):
        """Initizializes the requirements page controller.
        
        It communicates the users inputs with the actions performed by the service on
        the database.
        """
        self.service = service

    def get_lw_data(self):
        systems = self.service.get_systems()
        sections = self.service.get_sections()
        return {
            "systems": systems,
            "sections": sections
        }

    def handle_form_submission(self, form_data: Dict,
                               db_id: Optional[int]) -> None:
        requirement = Requirement(
            id=db_id,
            code=form_data['code'],
            definition=form_data['definition'],
            systems=form_data['systems'],
            sections=form_data['sections']
        )

        self.service.save_requirement(requirement)

    def prepare_form_data(self, data):
        return self.service.format_requirement_data(data)

    def save_requirement(self, requirement_data):
        """Handles saving a requirement."""
        return self.service.save_requirement(requirement_data)

    def edit_requirement(self, requirement_id, new_data):
        """Handles editing a requirement."""
        try:
            self.service.edit_requirement(requirement_id, new_data)
            return {"success": True, "message": "Requirement updated successfully"}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    def get_item_by_id(self, db_id):
        """Fetches a requirement item by its ID."""
        return self.service.get_requirement(db_id)

    def get_all_requirements(self):
        """Fetches all requirements."""
        return self.requirement_service.get_all_requirements()
