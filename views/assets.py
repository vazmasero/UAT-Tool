from base.base_asset_form import BaseAssetForm
from utils.form_mode import FormMode
from typing import Optional

class FormEmail(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("emails", mode, db_id)

class FormOperator(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("operators", mode, db_id)

class FormDrone(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("drones", mode, db_id)

class FormUASZone(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("uas_zones", mode, db_id)

class FormUhubOrg(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("uhub_orgs", mode, db_id)

class FormUhubUser(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("uhub_users", mode, db_id)

class FormUspace(BaseAssetForm):
    def __init__(self, mode: FormMode, db_id: Optional[int] = None):
        super().__init__("uspaces", mode, db_id)