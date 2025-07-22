from PySide6.QtWidgets import QWidget
from dataclasses import dataclass
from typing import Type, Optional

from views.steps import FormStep

@dataclass
class FormConfig:
    """Common configuration for forms."""
    form_class: Type[QWidget]
    add_title: str
    edit_title: str
    add_label: Optional[str]
    edit_label: Optional[str]
    label_attr: Optional[str]

# Dictionary to hold form configurations for different entities
STEP_FORMS = {
    "steps": {
        "config": FormConfig(
            form_class=FormStep,
            add_title="Add step",
            edit_title="Edit step",
            add_label=None,
            edit_label=None,
            label_attr=None,
        ),
    },
}