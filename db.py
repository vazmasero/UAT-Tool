import sqlite3
import os

DB_NAME = "uat_tool.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    con = get_connection()
    cursor = con.cursor()

    # Tabla Bugs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bugs(
            id,
            status,
            system,
            version,
            creation_time,
            last_update,
            service_now_id,
            campaign,
            requirements,
            short_desc,
            definition,
            urgency,
            impact,
            comments
        )
    ''')
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
