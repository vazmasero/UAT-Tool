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
        ui_module="ui.ui_form_email",    # Nombre exacto del archivo
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
        fields=["name", "serial_number", "manufacturer", "model", "operator", "tracker_type", "transponder_id"],
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
        fields=["name", "description"],
        validation_rules={
            "name": "Writing a name is mandatory"
        },
        form_key="uas_zones"
    )
}