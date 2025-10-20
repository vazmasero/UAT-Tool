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

        if role == Qt.ItemDataRole.DisplayRole:
            columns = (
                str(bug.id),
                bug.status,
                bug.system,
                bug.system_version,
                bug.created_at,
                bug.updated_at,
                bug.modified_by,
                bug.service_now_id,
                bug.campaign_run,
                bug.requirements,
                bug.short_description,
                bug.definition,
                bug.urgency,
                bug.impact,
                bug.comments,
                bug.file_names,
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

    def update_data(self, bugs: list[BugTableDTO]):
        """Actualiza los datos del modelo con una lista de BugDTOs."""
        self.beginResetModel()
        self.bugs = bugs
        self.endResetModel()
