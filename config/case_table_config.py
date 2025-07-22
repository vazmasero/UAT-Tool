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
CASE_TABLES = {
    "steps": {
        "config": TableConfig(
            db_table="steps",
            headers=[
                "Id", "Action", "Expected result", "Affected requirements", "Comments"
            ],
            column_map={
                "Id": "id",
                "Action": "action",
                "Expected result": "expected_result",
                "Affected requirements": "affected_requirements",
                "Comments": "comments"
            },
            widget_name="tbl_steps",
        )
    },
}