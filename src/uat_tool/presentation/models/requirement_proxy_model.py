from PySide6.QtCore import QModelIndex, QSortFilterProxyModel, Qt


class RequirementProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        # Filtrado por múltiples columnas
        model = self.sourceModel()
        if not model:
            return False

        # Buscar en título y estado
        title_index = model.index(source_row, 1, source_parent)
        status_index = model.index(source_row, 2, source_parent)

        title = model.data(title_index, Qt.ItemDataRole.DisplayRole) or ""
        status = model.data(status_index, Qt.ItemDataRole.DisplayRole) or ""

        filter_text = self.filterRegularExpression().pattern().lower()
        return filter_text in title.lower() or filter_text in status.lower()
