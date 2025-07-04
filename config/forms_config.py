from PySide6.QtWidgets import QWidget
from dataclasses import dataclass
from typing import Type, Optional, Dict
from enum import Enum

from pages.campaigns import FormCampaign
from pages.bugs import FormBug
from pages.test_management import FormCase, FormBlock
from pages.requirements import FormRequirement
from pages.assets import (FormDrone, FormEmail, FormOperator,
                   FormUASZone, FormUhubOrg, FormUhubUser, FormUspace)

@dataclass
class FormConfig:
    form_class: Type[QWidget]
    add_title: str
    edit_title: str
    add_label: Optional[str]
    edit_label: Optional[str]
    label_attr: Optional[str]
    menu_action_attr: Optional[str]

FORMS = {
    "bug": {
        "config": FormConfig(
            form_class=FormBug,
            add_title="Add bug",
            edit_title="Edit bug",
            add_label="New bug",
            edit_label="Edit bug",
            label_attr="lbl_bug",
            menu_action_attr="action_add_bug"
        )
    },
    "campaign": {
        "config": FormConfig(
            form_class=FormCampaign,
            add_title="Add campaign",
            edit_title="Edit campaign",
            add_label="New campaign",
            edit_label="Edit campaign",
            label_attr="lbl_campaign",
            menu_action_attr="action_new_campaign"
        )
    },
    "requirement": {
        "config": FormConfig(
            form_class=FormRequirement,
            add_title="Add requirement",
            edit_title="Edit requirement",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_requirement"
        )
    },
    "cases": {
        "config": FormConfig(
            form_class=FormCase,
            add_title="Add case",
            edit_title="Edit case",
            add_label="New test case",
            edit_label="Edit test case",
            label_attr="lbl_case",
            menu_action_attr="action_new_case"
        )
    },
    "blocks": {
        "config": FormConfig(
            form_class=FormBlock,
            add_title="Add block",
            edit_title="Edit block",
            add_label="New test block",
            edit_label="Edit test block",
            label_attr="lbl_block",
            menu_action_attr="action_new_block"
        )
    },
    "emails": {
        "config": FormConfig(
            form_class=FormEmail,
            add_title="Add email",
            edit_title="Edit email",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_email"
        )
    },
    "operators": {
        "config": FormConfig(
            form_class=FormOperator,
            add_title="Add operator",
            edit_title="Edit operator",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_operator"
        )
    },
    "drones": {
        "config": FormConfig(
            form_class=FormDrone,
            add_title="Add drone",
            edit_title="Edit drone",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_drone"
        )
    },
    "uas_zones": {
        "config": FormConfig(
            form_class=FormUASZone,
            add_title="Add UAS zone",
            edit_title="Edit UAS zone",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uas_zone"
        )
    },
    "uhub_orgs": {
        "config": FormConfig(
            form_class=FormUhubOrg,
            add_title="Add U-hub org",
            edit_title="Edit U-hub org",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uhub_organization"
        )
    },
    "uhub_users": {
        "config": FormConfig(
            form_class=FormUhubUser,
            add_title="Add U-hub user",
            edit_title="Edit U-hub user",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uhub_user"
        )
    },
    "uspaces": {
        "config": FormConfig(
            form_class=FormUspace,
            add_title="Add U-space",
            edit_title="Edit U-space",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uspace"
        )
    },
}