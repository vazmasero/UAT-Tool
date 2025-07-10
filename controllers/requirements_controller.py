from services.requirement_service import RequirementService

class RequirementsController:
    def __init__(self, requirement_service: RequirementService):
        self.requirement_service = requirement_service

    def save_requirement(self, requirement_data):
        """Handles saving a requirement."""
        return self.requirement_service.save_requirement(requirement_data)

    def edit_requirement(self, requirement_id, new_data):
        """Handles editing a requirement."""
        try:
            self.requirement_service.edit_requirement(requirement_id, new_data)
        except ValueError as e:
            return f"Error: {str(e)}"

    def get_all_requirements(self):
        """Fetches all requirements."""
        return self.requirement_service.get_all_requirements()
