from managers.table_manager import TableManager
from typing import List, Dict, Any, Optional


class StepTableManager(TableManager):
    
    def __init__(self):
        super().__init__()
        self.temp_steps = [] #Provisional steps