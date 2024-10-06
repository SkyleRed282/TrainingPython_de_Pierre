import random

from match_set import MatchSet

if __name__ == '__main__':

    # ball - rackets - net - field - spieler - referee - ball boy - match - set

    match_set = MatchSet()
    while not match_set.is_finished():
        player_points = random.randint(0, 1)
        player_name = ('A', 'B')[player_points]
        match_set.score_point(player_name)
        print(match_set)


