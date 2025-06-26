from PySide6.QtWidgets import QWidget

from dataclasses import dataclass
from typing import Dict, Type, Optional, Any
from enum import Enum

@dataclass
class FormConfig:
    """Specific form configuration"""
    form_class: Type[QWidget]
    add_title: str
    edit_title: str
    add_label: Optional[str]
    edit_label: Optional[str]
    label_attr: Optional[str]
    menu_action_attr: Optional[str]

class PageType(Enum):
    BUGS = "bugs"
    CAMPAIGNS = "campaigns"
    CASES = "cases"
    REQUIREMENTS = "requirements"
    ASSETS = "assets"

class FormType(Enum):
    # Test management
    CASE = "case"
    BLOCK = "block"
    
    # Assets
    EMAIL = "email"
    OPERATOR = "operator"
    DRONE = "drone"
    UAS_ZONE = "uas_zone"
    UHUB_ORG = "uhub_org"
    UHUB_USER = "uhub_user"
    USPACE = "uspace"

