import os
import sqlite3

DB_NAME = "uat_tool.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    con = get_connection()
    cursor = con.cursor()
    
    # Load tables
    schema_dir = os.path.join(os.path.dirname(__file__),"schemas")
    for filename in os.listdir(schema_dir):
        if filename.endswith(".sql"):
            with open(os.path.join(schema_dir, filename), "r", encoding="utf-8") as f:
                sql =f.read()
                cursor.executescript(sql)

    con.commit()
    con.close()

def get_all_bugs():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute('''
        SELECT status, system, version, creation_time, last_update,
            service_now_id, campaign, requirements, short_desc,
            definition, urgency, impact, comments
        FROM bugs
    ''')
    data = cursor.fetchall()
    con.close()
    return data

def get_all_campaigns():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute('''
        SELECT id, identifier, description, system, version,
        test_blocks, passed, success, creation_time, start_date,
        end_date, last_update, comments
        FROM campaigns
    ''')
    data = cursor.fetchall()
    con.close()
    return data
