-- Requirements table
CREATE TABLE IF NOT EXISTS requirements (
    id INTEGER PRIMARY KEY,
    system TEXT,
    section TEXT,
    definition TEXT,
    creation_date TEXT,
    last_update TEXT
);