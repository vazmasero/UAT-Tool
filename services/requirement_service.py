class RequirementService:
    """Servicio para manejar la lógica de negocio de requisitos."""

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_requirement(self, data):
        """Crea un nuevo requisito en la base de datos."""
        self.db_manager.create_register("requirements", data)

    def edit_requirement(self, requirement_id, data):
        """Edita un requisito existente en la base de datos."""
        self.db_manager.edit_register("requirements", requirement_id, data)
