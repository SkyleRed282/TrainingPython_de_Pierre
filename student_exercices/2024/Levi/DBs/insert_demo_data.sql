-- Insert demo players
INSERT INTO Player (name, serving_skill) VALUES ('Player A', 0.9);
INSERT INTO Player (name, serving_skill) VALUES ('Player B', 0.85);

-- Insert demo match
-- Assume Player A serves first
INSERT INTO Match (player_a_id, player_b_id, serving_player_id) VALUES (1, 2, 1);

-- Insert demo match sets
-- Match ID is 1 for this demo
INSERT INTO MatchSet (match_id) VALUES (1);
INSERT INTO MatchSet (match_id) VALUES (1);

-- Insert demo match points for the first set
-- Assume MatchSet ID 1 is for the first set
INSERT INTO MatchPoint (match_set_id, score_player_a, score_player_b, advantage, winner) VALUES (1, 15, 0, '', '');
INSERT INTO MatchPoint (match_set_id, score_player_a, score_player_b, advantage, winner) VALUES (1, 30, 15, '', '');
INSERT INTO MatchPoint (match_set_id, score_player_a, score_player_b, advantage, winner) VALUES (1, 40, 15, 'A', 'A');

-- Insert demo match points for the second set
-- Assume MatchSet ID 2 is for the second set
INSERT INTO MatchPoint (match_set_id, score_player_a, score_player_b, advantage, winner) VALUES (2, 15, 15, '', '');
INSERT INTO MatchPoint (match_set_id, score_player_a, score_player_b, advantage, winner) VALUES (2, 30, 40, '', 'B');
INSERT INTO MatchPoint (match_set_id, score_player_a, score_player_b, advantage, winner) VALUES (2, 40, 40, 'B', 'B');
