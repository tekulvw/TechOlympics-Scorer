CREATE TABLE Student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    school_code INTEGER,
    email TEXT,
    room INTEGER,
    score INTEGER
);

CREATE TABLE School (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Events (
    id INTEGER PRIMARY KEY,
    name TEXT,
    value INTEGER
);
