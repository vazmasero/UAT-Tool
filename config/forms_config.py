from PySide6.QtWidgets import QWidget

from dataclasses import dataclass
from typing import Dict, Type, Optional, Any
from enum import Enum

@dataclass
class FormConfig:
    """Specific form configuration according to definition in .ui files"""
    form_class: Type[QWidget]
    add_title: str
    edit_title: str
    add_label: Optional[str]
    edit_label: Optional[str]
    label_attr: Optional[str]
    menu_action_attr: Optional[str]

class PageType(Enum):
    """Enumeration of pages in the home page's stacked widget"""
    BUGS = "bugs"
    CAMPAIGNS = "campaigns"
    MANAGEMENT = "management"
    REQUIREMENTS = "requirements"
    ASSETS = "assets"
    
class FormType(Enum):
    """Enumeration of tabs in test management and assets pages"""
    # Test management tabs
    CASE = "test_cases"
    BLOCK = "test_blocks"
    
    # Assets tabs
    EMAIL = "emails"
    OPERATOR = "operators"
    DRONE = "drones"
    UAS_ZONE = "uas_zones"
    UHUB_ORG = "uhub_orgs"
    UHUB_USER = "uhub_users"
    USPACE = "uspaces"