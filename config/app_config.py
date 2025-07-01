from .forms_config import FormConfig, FormType, PageType
from pages.campaigns import FormCampaign
from pages.bugs import FormBug
from pages.test_management import FormCase, FormBlock
from pages.requirements import FormRequirement
from pages.assets import (FormDrone, FormEmail, FormOperator,
                   FormUASZone, FormUhubOrg, FormUhubUser, FormUspace)

class AppConfig:
    """Centralized configuration for the application. """

    FORMS_CONFIG = {
        # Core forms
        "bug": FormConfig(
            form_class=FormBug,
            add_title="Add bug",
            edit_title="Edit bug",
            add_label="New bug",
            edit_label="Edit bug",
            label_attr="lbl_bug",
            menu_action_attr="action_add_bug"
        ),
        "campaign": FormConfig(
            form_class=FormCampaign,
            add_title="Add campaign", 
            edit_title="Edit campaign",
            add_label="New campaign",
            edit_label="Edit campaign",
            label_attr="lbl_campaign",
            menu_action_attr="action_new_campaign"
        ),
        "requirement": FormConfig(
            form_class=FormRequirement,
            add_title="Add requirement",
            edit_title="Edit requirement",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_requirement"
        ),
        
        # Test forms
        FormType.CASE.value: FormConfig(
            form_class=FormCase,
            add_title="Add case",
            edit_title="Edit case", 
            add_label="New test case",
            edit_label="Edit test case",
            label_attr="lbl_case",
            menu_action_attr="action_new_case"
        ),
        FormType.BLOCK.value: FormConfig(
            form_class=FormBlock,
            add_title="Add block",
            edit_title="Edit block",
            add_label="New test block", 
            edit_label="Edit test block",
            label_attr="lbl_block",
            menu_action_attr="action_new_block"
        ),
        
        # Asset forms
        FormType.EMAIL.value: FormConfig(
            form_class=FormEmail,
            add_title="Add email",
            edit_title="Edit email",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_email"
        ),
        FormType.OPERATOR.value: FormConfig(
            form_class=FormOperator,
            add_title="Add operator", 
            edit_title="Edit operator",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_operator"
        ),
        FormType.DRONE.value: FormConfig(
            form_class=FormDrone,
            add_title="Add drone",
            edit_title="Edit drone",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_drone"
        ),
        FormType.UAS_ZONE.value: FormConfig(
            form_class=FormUASZone,
            add_title="Add UAS zone",
            edit_title="Edit UAS zone", 
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uas_zone"
        ),
        FormType.UHUB_ORG.value: FormConfig(
            form_class=FormUhubOrg,
            add_title="Add U-hub org",
            edit_title="Edit U-hub org",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uhub_organization"
        ),
        FormType.UHUB_USER.value: FormConfig(
            form_class=FormUhubUser,
            add_title="Add U-hub user",
            edit_title="Edit U-hub user",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uhub_user"
        ),
        FormType.USPACE.value: FormConfig(
            form_class=FormUspace,
            add_title="Add U-space",
            edit_title="Edit U-space",
            add_label=None,
            edit_label=None,
            label_attr=None,
            menu_action_attr="action_new_uspace"
        ),
    }

    PAGE_FORM_MAPPING = {
        PageType.BUGS: ["bug"],
        PageType.CAMPAIGNS: ["campaign"], 
        PageType.MANAGEMENT: [FormType.CASE.value, FormType.BLOCK.value],
        PageType.REQUIREMENTS: ["requirement"],
        PageType.ASSETS: [
            FormType.EMAIL.value, FormType.OPERATOR.value, FormType.DRONE.value,
            FormType.UAS_ZONE.value, FormType.UHUB_ORG.value, 
            FormType.UHUB_USER.value, FormType.USPACE.value
        ]
    }
