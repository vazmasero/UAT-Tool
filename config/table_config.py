from PySide6.QtCore import Qt
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TableConfig:
    db_table: str
    headers: List[str]
    widget_name: str
    page: str
    tab: Optional[int] = None
    
class TableCommonConfig:
    @staticmethod
    def get_generic_table_config():
        return {
            'context_menu': False,
            'alternating_row_colors': True,
            'sort_enabled': True,
            'max_section_size': 250
        } 

TABLES = {
    "bugs": TableConfig(
        db_table="bugs",
        headers=[
            "Status", "System", "Version", "Creation Time", "Last Update",
            "ServiceNow ID", "Campaign", "Requirements", "Short Description",
            "Definition", "Urgency", "Impact", "Comments"
        ],
        widget_name="tbl_bugs",
        page="BUGS",
        tab=None
    ),
    "campaigns": TableConfig(
        db_table="campaigns",
        headers=[
            "Id", "Description", "System", "Version", "Test blocks", "Passed",
            "Success", "Creation Time", "Start date", "End date", "Last Update"
        ],
        widget_name="tbl_campaigns",
        page="CAMPAIGNS",
        tab=None
    ),
    "cases": TableConfig(
        db_table="cases",
        headers=["Id", "Name", "System", "Assets", "Steps"],
        widget_name="tbl_cases",
        page="MANAGEMENT",
        tab=0
    ),
    "blocks": TableConfig(
        db_table="blocks",
        headers=["Id", "Name", "System", "Cases", "Comments"],
        widget_name="tbl_blocks",
        page="MANAGEMENT",
        tab=1
    ),
    "requirements": TableConfig(
        db_table="requirements",
        headers=["Id", "System", "Section", "Definition", "Creation date", "Last update"],
        widget_name="tbl_requirements",
        page="REQUIREMENTS",
        tab=None
    ),
    "emails": TableConfig(
        db_table="emails",
        headers=["Name", "Email", "Password"],
        widget_name="tbl_emails",
        page="ASSETS",
        tab=0
    ),
    "operators": TableConfig(
        db_table="operators",
        headers=["Name", "EASA ID", "Verification code", "Email", "Password", "Phone"],
        widget_name="tbl_operators",
        page="ASSETS",
        tab=1
    ),
    "drones": TableConfig(
        db_table="drones",
        headers=["Operator", "Name", "SN", "Manufacturer", "Model", "Tracker", "Transponder Id"],
        widget_name="tbl_drones",
        page="ASSETS",
        tab=2
    ),
    "uas_zones": TableConfig(
        db_table="uas_zones",
        headers=["Name", "Reason", "Cause", "Restriction type", "Activation time", "Authority"],
        widget_name="tbl_uas_zones",
        page="ASSETS",
        tab=3
    ),
    "uhub_orgs": TableConfig(
        db_table="uhub_orgs",
        headers=["Name", "Role", "Jurisdiction", "AoI", "Email", "Phone"],
        widget_name="tbl_uhub_orgs",
        page="ASSETS",
        tab=4
    ),
    "uhub_users": TableConfig(
        db_table="uhub_users",
        headers=["Username", "Email", "Password", "Organization", "Role", "Jurisdiction", "AoI"],
        widget_name="tbl_uhub_users",
        page="ASSETS",
        tab=5
    ),
    "uspaces": TableConfig(
        db_table="uspaces",
        headers=["Id", "Name", "# of sectors", "File"],
        widget_name="tbl_uspaces",
        page="ASSETS",
        tab=6
    )
}