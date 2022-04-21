-- CREATE TABLE IF NOT EXISTS Users (
--     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     first_name TEXT NOT NULL,
--     last_name TEXT NOT NULL,
--     phone TEXT NOT NULL,
--     email TEXT UNIQUE NOT NULL,
--     password TEXT NOT NULL,
--     date_created TEXT NOT NULL,
--     hire_date TEXT NOT NULL,
--     user_type TEXT NOT NULL,
--     active INTEGER DEFAULT 1
-- );

-- CREATE TABLE IF NOT EXISTS Competency (
--     comp_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     date_created TEXT NOT NULL,
--     active INTEGER DEFAULT 1
-- );

-- CREATE TABLE IF NOT EXISTS Assessments (
--     assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     comp_type INTEGER NOT NULL,
--     name TEXT UNIQUE NOT NULL,
--     date_created TEXT NOT NULL,
--     active INTEGER DEFAULT 1,
--     FOREIGN KEY (comp_type)
--         REFERENCES Competency (comp_id)
-- );

CREATE TABLE IF NOT EXISTS Assessment_Results (
    user_id INTEGER NOT NULL,
    assessment_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    date_taken TEXT NOT NULL,
    manager_id INTEGER NOT NULL,
    active INTEGER DEFAULT 1,
    PRIMARY KEY (user_id, assessment_id)
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id)
        REFERENCES Assessments (assessment_id),
    FOREIGN KEY (manager_id)
        REFERENCES Users (user_id)
);