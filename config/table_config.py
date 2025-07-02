from PySide6.QtCore import Qt
from dataclasses import dataclass
from typing import List

# Predefined configurations for tables

@dataclass
class TableData:
    """Table common data model"""
    headers: List[str]
    
class TableSpecificConfig:
    """Specific configuration for each table"""
    
    BUGS_TABLE_CONFIG = TableData(
        headers=[
            "Status", "System", "Version", "Creation Time", "Last Update",
            "ServiceNow ID", "Campaign", "Requirements", "Short Description",
            "Definition", "Urgency", "Impact", "Comments"
        ]
    )
    
    CAMPAIGNS_TABLE_CONFIG = TableData(
        headers=[
            "Id", "Description", "System", "Version", "Test blocks", "Passed",
            "Success", "Creation Time", "Start date", "End date", "Last Update"
        ]
    )
    
    CASES_TABLE_CONFIG = TableData(
        headers=[
            "Id", "Name", "System", "Assets", "Steps"
        ]
    )
    
    BLOCKS_TABLE_CONFIG = TableData(
        headers=[
            "Id", "Name", "System", "Cases", "Comments"
        ]
    )
    
    REQUIREMENTS_TABLE_CONFIG = TableData(
        headers=[
            "Id", "System", "Section", "Definition", "Creation date", "Last update"
        ]
    )
    
    EMAILS_TABLE_CONFIG = TableData(
        headers=[
            "Name", "Email", "Password"
        ]
    )
        
    OPERATORS_TABLE_CONFIG = TableData(
        headers=[
            "Name", "EASA ID", "Verification code", "Email", "Password", "Phone"
        ]
    )
            
    DRONES_TABLE_CONFIG = TableData(
        headers=[
            "Operator", "Name", "SN", "Manufacturer", "Model", "Tracker", "Transponder Id"
        ]
    )
                
    ZONES_TABLE_CONFIG = TableData(
        headers=[
            "Name", "Reason", "Cause", "Restriction type", "Activation time", "Authority"
        ]
    )
    
    ORGS_TABLE_CONFIG = TableData(
        headers=[
            "Name", "Role", "Jurisdiction", "AoI", "Email", "Phone"
        ]
    )
                        
    USERS_TABLE_CONFIG = TableData(
        headers=[
            "Username", "Email", "Password", "Organization", "Role", "Jurisdiction", "AoI"
        ]
    )
                            
    USPACES_TABLE_CONFIG = TableData(
        headers=[
            "Id", "Name", "# of sectors", "File"
        ]
    )    
    

class TableCommonConfig:
    """Configuraciones predefinidas para diferentes tipos de tablas."""
      
    @staticmethod
    def get_generic_table_config():
        """Configuración genérica para tablas."""
        return {
            'context_menu': False,
            'alternating_row_colors': True,
            'sort_enabled': True,
            'max_section_size': 250
        }