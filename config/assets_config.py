from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class AssetConfig:
    table_name: str
    ui_module: str
    ui_class: str 
    fields: List[str]
    validation_rules: Dict[str, str]
    form_key: str

ASSET_CONFIGS = {
    "emails": AssetConfig(
        table_name="emails",
        ui_module="ui.ui_form_email",
        ui_class="Ui_form_email",
        fields=["name", "email", "password"],
        validation_rules={
            "name": "Writing a name is mandatory",
            "email": "Writing an email is mandatory", 
            "password": "Writing a password is mandatory"
        },
        form_key="emails"
    ),
    "operators": AssetConfig(
        table_name="operators",
        ui_module="ui.ui_form_operator",
        ui_class="Ui_form_operator",
        fields=["name", "easa_id", "verification_code", "email", "password", "phone"],
        validation_rules={
            "name": "Writing a name is mandatory",
            "easa_id": "Writing an EASA ID is mandatory",
            "verification_code": "Writing a verification code is mandatory",
            "email": "Writing an email is mandatory",
            "password": "Writing a password is mandatory",
            "phone": "Writing a phone number is mandatory"
        },
        form_key="operators"
    ),
    "drones": AssetConfig(
        table_name="drones",
        ui_module="ui.ui_form_drone",
        ui_class="Ui_form_drone",
        fields=["name", "sn", "manufacturer", "model", "operator", "tracker", "transponder"],
        validation_rules={
            "name": "Writing a name is mandatory",
            "serial_number": "Writing a serial number is mandatory"
        },
        form_key="drones"
    ),
    "uas_zones": AssetConfig(
        table_name="uas_zones", 
        ui_module="ui.ui_form_uas_zone",
        ui_class="Ui_form_uas_zone",
        fields=["name", "reason", "cause", "restriction", "authority", "activation", "description"],
        validation_rules={
            "name": "Writing a name is mandatory"
        },
        form_key="uas_zones"
    ),
    "uhub_orgs": AssetConfig(
        table_name="uhub_orgs", 
        ui_module="ui.ui_form_uhub_org",
        ui_class="Ui_form_uhub_org",
        fields=["name", "email", "phone", "role", "jurisdiction", "aoi"],
        validation_rules={
            "name": "Writing a name is mandatory"
        },
        form_key="uhub_orgs"
    ),
    "uhub_users": AssetConfig(
        table_name="uhub_users", 
        ui_module="ui.ui_form_uhub_user",
        ui_class="Ui_form_uhub_user",
        fields=["username", "email", "password", "organization", "role", "jurisdiction", "aoi"],
        validation_rules={
            "name": "Writing a name is mandatory"
        },
        form_key="uhub_users"
    ),
    "uspaces": AssetConfig(
        table_name="uspaces", 
        ui_module="ui.ui_form_uspace",
        ui_class="Ui_form_uspace",
        fields=["identification", "name", "password", "sectors_number", "file"],
        validation_rules={
            "name": "Writing a name is mandatory"
        },
        form_key="uspaces"
    )
}