from PySide6.QtCore import Qt
from sqlalchemy import table
from managers.table_manager import TableManager
from services.block_service import BlockService
from config.model_domains import Block, Case
from config.block_table_config import BLOCK_TABLES
from typing import Optional, Dict

from utils.form_mode import FormMode

class BlockController:
    def __init__(self, service: BlockService, table_manager: TableManager = None):
        self.service = service
        self.table_manager = table_manager

    def setup_tables(self, ui, mode, db_id):
        table_name = 'cases'
        table_info = BLOCK_TABLES[table_name]["config"]
        table_widget = getattr(ui, table_info.widget_name, None)
        if not table_widget:
            print(f"Widget for table '{table_name}' not found. ")
            return

        self.table_manager.setup_table(table_widget, table_name, data=None, register=True)

    def get_cases_by_system(self, system_name: str) -> list:
        """Fetches all cases associated with a system."""
        return self.service.get_cases_by_system(system_name)

    def handle_form_submission(self, form_data: Dict, db_id: Optional[int], cases_table=None) -> None:
        # Crea el bloque con los datos del formulario
        block = Block(
            id=db_id,
            identification=form_data['identification'],
            name=form_data['name'],
            system=form_data['system'],
            comments=form_data['comments']
        )

        # Obtiene los IDs de los casos seleccionados (ya vienen en form_data['cases'])
        selected_case_ids = form_data.get('cases', [])

        # Guardar el bloque y asociar los casos seleccionados
        if db_id:
            # EDIT: actualizar bloque y casos asociados
            self.service.save_block_and_cases(block, selected_case_ids)
        else:
            # CREATE: crear bloque y asociar casos
            self.service.save_block_and_cases(block, selected_case_ids)

    def handle_new_step(self, edit: bool, table_name: str, row_data: Dict):
        from managers.form_manager import FormManager

        form_manager = FormManager()
        form_key = table_name

        # Obtain row index if editing
        row_index = None
        if edit and row_data and 'steps' in self.table_manager.tables:
            steps_table = self.table_manager.tables['steps']
            row_index = self.table_manager.get_selected_row_indices(steps_table)

        # Opens the form using FormManager and returns the form instance
        form_instance = form_manager.open_form(form_key, edit, row_data, data_instead_id=True, row_index=row_index)

        # Returned form instance is used to handle event of updated data in db 
        # (to refresh the appropriate table)
        if form_instance and hasattr(form_instance, 'new_step_data'):
            form_instance.new_step_data.connect(self._handle_new_step_data)
            
    def _handle_new_step_data(self, step_data:Dict):
        if not self.table_manager or 'steps' not in self.table_manager.tables:
            print("Error: Steps table not available")
            return

        steps_table = self.table_manager.tables['steps']

        formatted_data = self._format_step_for_table(step_data)

        if 'id' in step_data and 'row_index' in step_data:
            self.table_manager.update_row(steps_table, formatted_data, step_data['row_index'])
        else:
            # CREATE: add new row
            self.table_manager.add_row(steps_table, formatted_data)

    def _format_step_for_table(self, step_data:Dict) -> Dict:
        return {
            'action': step_data.get('action', ''),
            'expected_result': step_data.get('expected_result', ''),
            'affected_requirements': ', '.join(step_data.get('affected_requirements', [])),
            'comments': step_data.get('comments', '')
        }
    
    def _handle_remove_step(self):   
        """Handles the removal of a step from the table."""   
        table = self.table_manager.tables.get('steps') 
        row_index = self.table_manager.get_selected_row_indices(table)
        if not row_index:
            return
        
        try:
            self.table_manager.delete_row(table, row_index[0])

        except Exception as e:
            print(f"Error deleting register {row_index} from table: {e}")

    def get_item_by_id(self, db_id):
        """Fetches a block item by its ID."""
        return self.service.get_block(db_id)
    
    def get_case_by_id(self, case_id):
        return self.service.get_case_by_id(case_id)

    def get_steps_by_block_id(self, block_id):
        """Fetches all steps associated with a block ID."""
        return self.service.get_steps_by_block_id(block_id)
    
    def prepare_form_data(self, data: Dict) -> Dict:
        if not data:
            return None
        
        if 'Id' in data:
            # Header as key:
            return {
                'id': data['Id'],
                'identification': data['Identification'],
                'name': data['Name'],
                'system': data['System'],
                'comments': data['Comments']
            }
        else:
            return data

    def is_case_in_table(self, case_id):
        model = self.table_manager.tables["cases"].model()
        if not model:
            return False
        for row in range(model.rowCount()):
            idx = model.index(row, 0)
            if str(model.data(idx)) == str(case_id):
                return True
        return False
    
    def add_case_to_table(self, case_data):
        table = self.table_manager.tables.get('cases')
        if table is None:
            self.table_manager.setup_table(self.ui.tbl_cases, 'cases', [], config=BLOCK_TABLES['cases']['config'], register=True)
            return
        # Usa tu TableManager para añadir la fila correctamente
        self.table_manager.add_row(table, case_data, config_module=BLOCK_TABLES)

    def remove_case_from_table(self, case_id):
        table = self.table_manager.tables.get('cases')
        model = table.model()
        if not model:
            return

        # Buscar el índice de la columna 'id'
        id_col = None
        for col in range(model.columnCount()):
            header = model.headerData(col, Qt.Orientation.Horizontal)
            if str(header).lower() == "id":
                id_col = col
                break
        if id_col is None:
            # Si no hay columna id, no se puede eliminar correctamente
            return

        # Buscar la fila con ese id
        for row in range(model.rowCount()):
            idx = model.index(row, id_col)
            if str(model.data(idx)) == str(case_id):
                self.table_manager.delete_row(table, row)
                break
