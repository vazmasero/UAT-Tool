from services.requirement_service import RequirementService
from config.model_domains import Requirement

class RequirementsController:
    def __init__(self, service: RequirementService):
            self.service = service

    def get_lw_data(self):
        systems = self.service.get_systems()
        sections = self.service.get_sections()
        return {
            "systems": systems,
            "sections": sections
        }
    
    def handle_form_submission(self, form_data: dict, requirement_id: int | None = None) -> None:
        requirement = Requirement(
            id=requirement_id,
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
        except ValueError as e:
            return f"Error: {str(e)}"

    def get_all_requirements(self):
        """Fetches all requirements."""
        return self.requirement_service.get_all_requirements()
