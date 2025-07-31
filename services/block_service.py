from db.db import DatabaseManager
from config.model_domains import Block, Case
from config.block_table_config import BLOCK_TABLES
from typing import Any, Dict, Optional, List

class BlockService:
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.active_forms = {}

    def save_block(self, block: Block) -> None:
        data = {
            'identification': block.identification,
            'name': block.name,
            'systems': block.systems,
            'sections': block.sections,
            'operators': block.operators,
            'drones': block.drones,
            'uhub_users': block.uhub_users,
            'comments': block.comments
        }

        if block.id:
            self.db_manager.edit_register("blocks", block.id, data)
        else:
            block_id = self.db_manager.create_register("blocks", data)

        return block_id

    def save_case(self, case_data: Dict[str, Any]) -> int:
        case_fields = {
            'action': case_data.get('action'),
            'expected_result': case_data.get('expected_result'),
            'affected_requirements': case_data.get('affected_requirements'),
            'comments': case_data.get('comments'),
            'case_id': case_data.get('case_id')
        }

        case_id = self.db_manager.create_register("cases", case_fields)
        return case_id
            
    def setup_tables(self, ui):
        for table_name, table_dict in BLOCK_TABLES.items():
            table_info = table_dict["config"]
            table_widget = getattr(ui, table_info.widget_name, None)
            if not table_widget:
                print(f"Widget for table '{table_name}' not found. ")
                continue
            data = self.db_manager.get_all_data(table_info.db_table)
            self.table_manager.setup_table(table_widget, table_name, data, register=True)
    
    def _on_form_closed(self, form_key: str):
        self.active_forms.pop(form_key, None)

    def get_block(self, block_id: int) -> Block:
        data = self.db_manager.get_by_id("blocks", block_id)
        return data
    
    def get_case_by_id(self, case_id):
        return self.db_manager.get_by_id("cases", case_id)
    
    def get_cases_by_system(self, system_name: str) -> list:
        """ Retrieves all cases associated with a specific system """
        all_cases = self.db_manager.get_all_data("cases")
        filtered = []
        for case in all_cases:
            systems = case.get('systems', [])
            if isinstance(systems, str):
                systems = [s.strip() for s in systems.split(',')]
            if system_name in systems:
                filtered.append(case)
        return filtered

    def save_block_and_cases(self, block: Block, case_ids: List[int]) -> None:
        """
        Guarda un bloque y asocia los casos seleccionados (por id).
        """
        data = {
            'identification': block.identification,
            'name': block.name,
            'system': block.system,
            'comments': block.comments,
            'cases': case_ids  # Solo IDs, no diccionarios ni objetos
        }

        if block.id:
            # Editar bloque y asociar casos
            self.db_manager.edit_register("blocks", block.id, data)
        else:
            # Crear bloque y asociar casos
            self.db_manager.create_register("blocks", data)