-- Test cases table
CREATE TABLE IF NOT EXISTS cases (
    id INTEGER PRIMARY KEY,
    identifier TEXT,
    name TEXT,
    system TEXT,
    assets TEXT,
    steps TEXT
);

-- Test blocks table
CREATE TABLE IF NOT EXISTS blocks (
    id INTEGER PRIMARY KEY,
    identifier TEXT,
    name TEXT,
    system TEXT,
    cases TEXT,
    comments TEXT
);