from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from uat_tool.application.dto import BugTableDTO


class BugTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.bugs: list[BugTableDTO] = []
        self.headers = [
            "Id",
            "Status",
            "System",
            "Version",
            "Creation Time",
            "Last Update",
            "Modified By",
            "ServiceNow ID",
            "Campaign",
            "Requirements",
            "Short Description",
            "Definition",
            "Urgency",
            "Impact",
            "Comments",
            "Associated files",
        ]

    def rowCount(self, parent: QModelIndex = None) -> int:
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return 0
        return len(self.bugs)

    def columnCount(self, parent: QModelIndex = None) -> int:
        if parent is None:
            parent = QModelIndex()
        if parent.isValid():
            return 0
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self.bugs):
            return None

        bug = self.bugs[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == 0:
                return str(bug.id)
            elif col == 1:
                return bug.status
            elif col == 2:
                return bug.system
            elif col == 3:
                return bug.system_version
            elif col == 4:
                return bug.created_at
            elif col == 5:
                return bug.updated_at
            elif col == 6:
                return bug.modified_by
            elif col == 7:
                return bug.service_now_id
            elif col == 8:
                return bug.campaign_run
            elif col == 9:
                return bug.requirements
            elif col == 10:
                return bug.short_description
            elif col == 11:
                return bug.definition
            elif col == 12:
                return bug.urgency
            elif col == 13:
                return bug.impact
            elif col == 14:
                return bug.comments
            elif col == 15:
                return bug.file_names

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

    def update_data(self, bugs: list[BugTableDTO]):
        """Actualiza los datos del modelo con una lista de BugDTOs."""
        self.beginResetModel()
        self.bugs = bugs
        self.endResetModel()
