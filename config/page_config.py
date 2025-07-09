from dataclasses import dataclass
from typing import List
from config.form_config import FormConfig

@dataclass
class PageConfig:
    index: int
    forms: List[str]
    tables: List[str]

PAGES = {
    "bugs": {
        "config": PageConfig(
            index=0,
            forms=["bugs"],
            tables=["bugs"]
        )
    },
    "campaigns": {
        "config": PageConfig(
            index=1,
            forms=["campaigns"],
            tables=["campaigns"]
        )
    },
    "management": {
        "config": PageConfig(
            index=2,
            forms=["cases", "blocks"],
            tables=["cases", "blocks"]
        )
    },
    "requirements": {
        "config": PageConfig(
            index=3,
            forms=["requirements"],
            tables=["requirements"]
        )
    },
    "assets": {
        "config": PageConfig(
            index=4,
            forms=[
                "emails", "operators", "drones",
                "uas_zones", "uhub_orgs", "uhub_users", "uspaces"
            ],
            tables=[
                "emails", "operators", "drones",
                "uas_zones", "uhub_orgs", "uhub_users", "uspaces"
            ]
        )
    }
}