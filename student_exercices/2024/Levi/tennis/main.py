from match import Match
from player import Player

if __name__ == '__main__':
    # ball - rackets - net - field - spieler - referee - ball boy - match - set

    roger = Player(name='Roger Federer')
    messi = Player(name='Lionel Messi', serving_skill=0.7)

    match = Match(player_a=roger, player_b=messi)
    match.play_match()
    match.print_result()
