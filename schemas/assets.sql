-- Emails table
CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT
);

-- Operators table
CREATE TABLE IF NOT EXISTS operators (
    id INTEGER PRIMARY KEY,
    name TEXT,
    easa_id TEXT,
    verification_code TEXT,
    email TEXT,
    password TEXT,
    phone TEXT
);

-- Drones table
CREATE TABLE IF NOT EXISTS drones (
    id INTEGER PRIMARY KEY,
    operator TEXT,
    name TEXT,
    sn TEXT,
    manufacturer TEXT,
    model TEXT,
    tracker_type TEXT,
    transponder_id TEXT
);

-- UAS zones table
CREATE TABLE IF NOT EXISTS uas_zones (
    id INTEGER PRIMARY KEY,
    name TEXT,
    reason TEXT,
    cause TEXT,
    restriction_type TEXT,
    activation_time TEXT,
    authority TEXT
);

-- U-hub organizations table
CREATE TABLE IF NOT EXISTS uhub_orgs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    jurisdiction TEXT,
    aoi TEXT,
    email TEXT,
    phone, TEXT
);

-- U-hub users table
CREATE TABLE IF NOT EXISTS uhub_users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT,
    organization TEXT,
    role TEXT,
    jurisdiction TEXT,
    aoi TEXT
);

-- U-spaces table
CREATE TABLE IF NOT EXISTS uspaces (
    id INTEGER PRIMARY KEY,
    identification TEXT,
    name TEXT,
    sectors_number TEXT,
    file TEXT
);