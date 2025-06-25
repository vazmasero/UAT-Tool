-- Campaigns table
CREATE TABLE IF NOT EXISTS campaign (
    id INTEGER PRIMARY KEY,
    identifier TEXT
    description TEXT,
    system TEXT,
    version TEXT,
    test_blocks TEXT,
    passed, TEXT,
    success, TEXT,
    creation_time TEXT,
    start_date TEXT,
    end_date TEXT,
    last_update TEXT,
    comments TEXT,
);