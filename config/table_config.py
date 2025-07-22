from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class TableConfig:
    """Common configuration for tables."""
    db_table: str
    headers: List[str]
    widget_name: str
    page: str
    tab: Optional[int] = None
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
# Each key corresponds to a specific entity type, and the value is a TableConfig instance
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
                "ServiceNow ID": "servicenow_id",
                "Campaign": "campaign",
                "Requirements": "requirements",
                "Short Description": "short_description",
                "Definition": "definition",
                "Urgency": "urgency",
                "Impact": "impact",
                "Comments": "comments"
            },
            widget_name="tbl_bugs",
            page="bugs"
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
            headers=["Id", "Identification", "Name", "System(s)", "Section(s)", "Operator(s)", "Drone(s)", "U-hub user(s)", "Steps"],
            column_map={
                "Id": "id",
                "Identification": "identification",
                "Name": "name",
                "System(s)": "systems",
                "Section(s)": "sections",
                "Operator(s)": "operators",
                "Drone(s)": "drones",
                "U-hub user(s)": "uhub_users",
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
            headers=["Id", "Assigned code", "System(s)", "Section(s)", "Definition", "Creation date", "Last update"],
            column_map={
                "Id": "id",
                "Assigned code": "code",
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
            headers=["Id", "Name", "Email", "Password"],
            column_map={
                "Id": "id",
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
            headers=["Id", "Name", "EASA ID", "Verification code", "Email", "Password", "Phone"],
            column_map={
                "Id": "id",
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
            headers=["Id", "Operator", "Name", "SN", "Manufacturer", "Model", "Tracker", "Transponder Id"],
            column_map={
                "Id": "id",
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
            headers=["Id", "Name", "Reason", "Cause", "Restriction type", "Activation time", "Authority"],
            column_map={
                "Id": "id",
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
            headers=["Id", "Name", "Role", "Jurisdiction", "AoI", "Email", "Phone"],
            column_map={
                "Id": "id",
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
            headers=["Id", "Username", "Email", "Password", "Organization", "Role", "Jurisdiction", "AoI"],
            column_map={
                "Id": "id",
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
            headers=["Id", "Code", "Name", "# of sectors", "File"],
            column_map={
                "Id": "id",
                "Code": "identification",
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