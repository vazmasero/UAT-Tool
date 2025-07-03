from .forms_config import FormType, PageType

PAGES = {
    PageType.BUGS: {
        "forms": ["bug"]
    },
    PageType.CAMPAIGNS: {
        "forms": ["campaign"]
    },
    PageType.MANAGEMENT: {
        "forms": ["cases", "blocks"]
    },
    PageType.REQUIREMENTS: {
        "forms": ["requirement"]
    },
    PageType.ASSETS: {
        "forms": [
            "emails", "operators", "drones",
            "uas_zones", "uhub_orgs", "uhub_users", "uspaces"
        ]
    }
}