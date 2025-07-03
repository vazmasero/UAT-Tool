import os
import sqlite3

DB_NAME = "uat_tool.db"
    
TABLE_DB_CONFIGS = {
    'bugs': {
        'table': 'bugs',
        'columns': '''status, system, version, creation_time, last_update,
            service_now_id, campaign, requirements, short_desc,
            definition, urgency, impact, comments'''
    },
    'campaigns': {
        'table': 'campaigns',
        'columns': '''id, identifier, description, system, version,
        test_blocks, passed, success, creation_time, start_date,
        end_date, last_update, comments'''
    },
    'cases': {
        'table': 'cases',
        'columns': '''id, identifier, name, system, assets, steps'''
    },
    'blocks': {
        'table': 'blocks',
        'columns': '''id, identifier, name, system, cases, comments'''
    },
    'requirements': {
        'table': 'requirements',
        'columns': '''id, system, section, definition, creation_date,
        last_update'''
    },
    'emails': {
        'table': 'emails',
        'columns': '''id, name, email, password'''
    },
    'operators': {
        'table': 'operators',
        'columns': '''id, name, easa_id, verification_code, email,
        password, phone'''
    },
    'drones': {
        'table': 'drones',
        'columns': '''id, operator, name, sn, manufacturer,
        model, tracker_type, transponder_id'''
    },
    'uas_zones': {
        'table': 'uas_zones',
        'columns': '''id, name, reason, cause, restriction_type, 
        activation_time, authority'''
    },
    'uhub_orgs': {
        'table': 'uhub_orgs',
        'columns': '''id, name, role, jurisdiction, aoi, email, phone'''
    },
    'uhub_users': {
        'table': 'uhub_users',
        'columns': '''id, username, email, password, organization, role,
        jurisdiction, aoi'''
    },
    'uspaces': {
        'table': 'uspaces',
        'columns': '''id, identification, name, sectors_number, file'''
    }
}

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    con = get_connection()
    cursor = con.cursor()
    
    # Create/Load tables
    schema_dir = os.path.join(os.path.dirname(__file__),"schemas")
    for filename in os.listdir(schema_dir):
        if filename.endswith(".sql"):
            with open(os.path.join(schema_dir, filename), "r", encoding="utf-8") as f:
                sql =f.read()
                cursor.executescript(sql)

    con.commit()
    con.close()

class DatabaseManager:
    
    def __init__(self):
        self.table_configs = TABLE_DB_CONFIGS
    
    def get_all_data(self, key, custom_columns=None):
        
        if key not in self.table_configs:
            available_keys = ', '.join(self.table_configs.keys())
            raise ValueError(f"Key '{key}' not found. Available keys: {available_keys}")
        
        config = self.table_configs[key]
        columns = custom_columns or config['columns']
        
        con = get_connection()
        cursor = con.cursor()
        
        try:
            cursor.execute(f"SELECT {columns} FROM {config['table']}")
            data = cursor.fetchall()
            return data
        finally:
            con.close()
    
