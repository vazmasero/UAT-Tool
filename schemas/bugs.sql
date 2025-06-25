-- Bugs table
CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY,
    status TEXT
    system TEXT,
    version TEXT,
    creation_time TEXT,
    last_update TEXT,
    service_now_id TEXT,
    campaign TEXT,
    requirements TEXT,
    short_desc TEXT,
    definition TEXT,
    urgency TEXT,
    impact TEXT,
    comments TEXT
);