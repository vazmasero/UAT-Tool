from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from uat_tool.application.dto import RequirementTableDTO


class RequirementTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.requirements: list[RequirementTableDTO] = []
        self.headers = [
            "Id",
            "Code",
            "Definition",
            "Systems",
            "Sections",
            "Creation Time",
            "Last Update",
            "Last Modified By",
        ]

    def rowCount(self, parent: QModelIndex = None) -> int:
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return 0
        return len(self.requirements)

    def columnCount(self, parent: QModelIndex = None) -> int:
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return 0
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self.requirements):
            return None

        requirement = self.requirements[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            columns = (
                str(requirement.id),
                requirement.code,
                requirement.definition,
                requirement.systems,
                requirement.sections,
                requirement.created_at,
                requirement.updated_at,
                requirement.modified_by,
            )
            if 0 <= index.column() < len(columns):
                return columns[index.column()]

        return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self.headers[section] if section < len(self.headers) else None
        return None

    def update_data(self, requirements: list[RequirementTableDTO]):
        """Actualiza los datos del modelo con una lista de RequirementTableDTOs."""
        self.beginResetModel()
        self.requirements = requirements
        self.endResetModel()
