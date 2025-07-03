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
        page="bugs",
        tab=None
    ),
    "campaigns": TableConfig(
        db_table="campaigns",
        headers=[
            "Id", "Description", "System", "Version", "Test blocks", "Passed",
            "Success", "Creation Time", "Start date", "End date", "Last Update"
        ],
        widget_name="tbl_campaigns",
        page="campaigns",
        tab=None
    ),
    "cases": TableConfig(
        db_table="cases",
        headers=["Id", "Name", "System", "Assets", "Steps"],
        widget_name="tbl_cases",
        page="management",
        tab=0
    ),
    "blocks": TableConfig(
        db_table="blocks",
        headers=["Id", "Name", "System", "Cases", "Comments"],
        widget_name="tbl_blocks",
        page="management",
        tab=1
    ),
    "requirements": TableConfig(
        db_table="requirements",
        headers=["Id", "System", "Section", "Definition", "Creation date", "Last update"],
        widget_name="tbl_requirements",
        page="requirements",
        tab=None
    ),
    "emails": TableConfig(
        db_table="emails",
        headers=["Name", "Email", "Password"],
        widget_name="tbl_emails",
        page="assets",
        tab=0
    ),
    "operators": TableConfig(
        db_table="operators",
        headers=["Name", "EASA ID", "Verification code", "Email", "Password", "Phone"],
        widget_name="tbl_operators",
        page="assets",
        tab=1
    ),
    "drones": TableConfig(
        db_table="drones",
        headers=["Operator", "Name", "SN", "Manufacturer", "Model", "Tracker", "Transponder Id"],
        widget_name="tbl_drones",
        page="assets",
        tab=2
    ),
    "uas_zones": TableConfig(
        db_table="uas_zones",
        headers=["Name", "Reason", "Cause", "Restriction type", "Activation time", "Authority"],
        widget_name="tbl_uas_zones",
        page="assets",
        tab=3
    ),
    "uhub_orgs": TableConfig(
        db_table="uhub_orgs",
        headers=["Name", "Role", "Jurisdiction", "AoI", "Email", "Phone"],
        widget_name="tbl_uhub_orgs",
        page="assets",
        tab=4
    ),
    "uhub_users": TableConfig(
        db_table="uhub_users",
        headers=["Username", "Email", "Password", "Organization", "Role", "Jurisdiction", "AoI"],
        widget_name="tbl_uhub_users",
        page="assets",
        tab=5
    ),
    "uspaces": TableConfig(
        db_table="uspaces",
        headers=["Id", "Name", "# of sectors", "File"],
        widget_name="tbl_uspaces",
        page="assets",
        tab=6
    )
}