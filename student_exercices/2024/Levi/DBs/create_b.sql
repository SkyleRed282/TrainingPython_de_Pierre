-- Create Player table
CREATE TABLE Player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    serving_skill REAL DEFAULT 1
);

-- Create Match table
CREATE TABLE Match (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_a_id INTEGER NOT NULL,
    player_b_id INTEGER NOT NULL,
    serving_player_id INTEGER NOT NULL,
    FOREIGN KEY (player_a_id) REFERENCES Player (id),
    FOREIGN KEY (player_b_id) REFERENCES Player (id),
    FOREIGN KEY (serving_player_id) REFERENCES Player (id)
);

-- Create MatchSet table
CREATE TABLE MatchSet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    FOREIGN KEY (match_id) REFERENCES Match (id)
);

-- Create MatchPoint table
CREATE TABLE MatchPoint (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_set_id INTEGER NOT NULL,
    score_player_a INTEGER DEFAULT 0,
    score_player_b INTEGER DEFAULT 0,
    advantage TEXT DEFAULT '',
    winner TEXT DEFAULT '',
    FOREIGN KEY (match_set_id) REFERENCES MatchSet (id)
);
