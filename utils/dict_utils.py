from typing import Optional, Dict
from config.page_config import PAGES
from config.table_config import TABLES
from config.case_table_config import CASE_TABLES

def get_base_table_config(name: str) -> Optional[Dict]:
    if name == 'steps':
        base_config = CASE_TABLES.get(name, {}).get("config", {})
    else:
        base_config = TABLES.get(name, {}).get("config", {})
    return base_config

def get_form_key(current_page: str, tab_index: Optional[int]) -> Optional[str]:
    page_config = PAGES.get(current_page, {}).get("config")
    page_forms = page_config.forms if page_config else []
    if not page_forms:
        return None
    return page_forms[tab_index] if tab_index is not None and tab_index < len(
        page_forms) else page_forms[0]
