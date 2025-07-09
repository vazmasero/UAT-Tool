from PySide6.QtCore import Qt
from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class TableConfig:
    db_table: str
    headers: List[str]
    widget_name: str
    page: str
    tab: Optional[int] = None
    column_map: Dict[str, str] = field(default_factory=dict)  
    
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
    "bugs": {
        "config": TableConfig(
            db_table="bugs",
            headers=[
                "Status", "System", "Version", "Creation Time", "Last Update",
                "ServiceNow ID", "Campaign", "Requirements", "Short Description",
                "Definition", "Urgency", "Impact", "Comments"
            ],
            column_map={
                "Status": "status",
                "System": "system",
                "Version": "version",
                "Creation Time": "creation_time",
                "Last Update": "last_update",
                "ServiceNow ID": "service_now_id",
                "Campaign": "campaign",
                "Requirements": "requirements",
                "Short Description": "short_desc",
                "Definition": "definition",
                "Urgency": "urgency",
                "Impact": "impact",
                "Comments": "comments"
            },
            widget_name="tbl_bugs",
            page="bugs",
            tab=None
        )
    },
    "campaigns": {
        "config": TableConfig(
            db_table="campaigns",
            headers=[
                "Id", "Description", "System", "Version", "Test blocks", "Passed",
                "Success", "Creation Time", "Start date", "End date", "Last Update", "Comments"
            ],
            column_map={
                "Id": "identifier",
                "Description": "description",
                "System": "system",
                "Version": "version",
                "Test blocks": "test_blocks",
                "Passed": "passed",
                "Success": "success",
                "Creation Time": "creation_time",
                "Start date": "start_date",
                "End date": "end_date",
                "Last Update": "last_update",
                "Comments": "comments"
            },
            widget_name="tbl_campaigns",
            page="campaigns",
            tab=None
        )
    },
    "cases": {
        "config": TableConfig(
            db_table="cases",
            headers=["Id", "Name", "System", "Assets", "Steps"],
            column_map={
                "Id": "identifier",
                "Name": "name",
                "System": "system",
                "Assets": "assets",
                "Steps": "steps"
            },
            widget_name="tbl_cases",
            page="management",
            tab=0
        )
    },
    "blocks": {
        "config": TableConfig(
            db_table="blocks",
            headers=["Id", "Name", "System", "Cases", "Comments"],
            column_map={
                "Id": "identifier",
                "Name": "name",
                "System": "system",
                "Cases": "cases",
                "Comments": "comments"
            },
            widget_name="tbl_blocks",
            page="management",
            tab=1
        )
    },
    "requirements": {
        "config": TableConfig(
            db_table="requirements",
            headers=["Id", "System(s)", "Section(s)", "Definition", "Creation date", "Last update"],
            column_map={
                "Id": "code",
                "System(s)": "systems",
                "Section(s)": "sections",
                "Definition": "definition",
                "Creation date": "creation_date",
                "Last update": "last_update"
            },
            widget_name="tbl_requirements",
            page="requirements",
            tab=None
        )
    },
    "emails": {
        "config": TableConfig(
            db_table="emails",
            headers=["Name", "Email", "Password"],
            column_map={
                "Name": "name",
                "Email": "email",
                "Password": "password"
            },
            widget_name="tbl_emails",
            page="assets",
            tab=0
        )
    },
    "operators": {
        "config": TableConfig(
            db_table="operators",
            headers=["Name", "EASA ID", "Verification code", "Email", "Password", "Phone"],
            column_map={
                "Name": "name",
                "EASA ID": "easa_id",
                "Verification code": "verification_code",
                "Email": "email",
                "Password": "password",
                "Phone": "phone"
            },
            widget_name="tbl_operators",
            page="assets",
            tab=1
        )
    },
    "drones": {
        "config": TableConfig(
            db_table="drones",
            headers=["Operator", "Name", "SN", "Manufacturer", "Model", "Tracker", "Transponder Id"],
            column_map={
                "Operator": "operator",
                "Name": "name",
                "SN": "sn",
                "Manufacturer": "manufacturer",
                "Model": "model",
                "Tracker": "tracker_type",
                "Transponder Id": "transponder_id"
            },
            widget_name="tbl_drones",
            page="assets",
            tab=2
        )
    },
    "uas_zones": {
        "config": TableConfig(
            db_table="uas_zones",
            headers=["Name", "Reason", "Cause", "Restriction type", "Activation time", "Authority"],
            column_map={
                "Name": "name",
                "Reason": "reason",
                "Cause": "cause",
                "Restriction type": "restriction_type",
                "Activation time": "activation_time",
                "Authority": "authority"
            },
            widget_name="tbl_uas_zones",
            page="assets",
            tab=3
        )
    },
    "uhub_orgs": {
        "config": TableConfig(
            db_table="uhub_orgs",
            headers=["Name", "Role", "Jurisdiction", "AoI", "Email", "Phone"],
            column_map={
                "Name": "name",
                "Role": "role",
                "Jurisdiction": "jurisdiction",
                "AoI": "aoi",
                "Email": "email",
                "Phone": "phone"
            },
            widget_name="tbl_uhub_orgs",
            page="assets",
            tab=4
        )
    },
    "uhub_users": {
        "config": TableConfig(
            db_table="uhub_users",
            headers=["Username", "Email", "Password", "Organization", "Role", "Jurisdiction", "AoI"],
            column_map={
                "Username": "username",
                "Email": "email",
                "Password": "password",
                "Organization": "organization",
                "Role": "role",
                "Jurisdiction": "jurisdiction",
                "AoI": "aoi"
            },
            widget_name="tbl_uhub_users",
            page="assets",
            tab=5
        )
    },
    "uspaces": {
        "config": TableConfig(
            db_table="uspaces",
            headers=["Id", "Name", "# of sectors", "File"],
            column_map={
                "Id": "identification",
                "Name": "name",
                "# of sectors": "sectors_number",
                "File": "file"
            },
            widget_name="tbl_uspaces",
            page="assets",
            tab=6
        )
    }
}