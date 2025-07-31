from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class TableConfig:
    """Common configuration for tables."""
    db_table: str
    headers: List[str]
    widget_name: str
    column_map: Dict[str, str] = field(default_factory=dict)  
    
class TableCommonConfig:
    """Common configuration for all tables."""
    @staticmethod
    def get_generic_table_config():
        return {
            'context_menu': False,
            'alternating_row_colors': False,
            'sort_enabled': True,
            #'max_section_size': 250
        }

# Dictionary to hold table configurations for different entities
BLOCK_TABLES = {
    "cases": {
        "config": TableConfig(
            db_table="cases",
            headers=["Id", "Identification", "Name", "Section(s)", "Operator(s)", "Drone(s)", "U-hub user(s)", "Steps"],
            column_map={
                "Id": "id",
                "Identification": "identification",
                "Name": "name",
                "Section(s)": "sections",
                "Operator(s)": "operators",
                "Drone(s)": "drones",
                "U-hub user(s)": "uhub_users",
                "Steps": "steps"
            },
            widget_name="tbl_cases",
        )
    }
}