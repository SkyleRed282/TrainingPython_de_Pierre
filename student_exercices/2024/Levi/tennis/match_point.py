from random import randint
from match_set import MatchSet


class MatchPoint:
    point_id = 0

    def __init__(self, match_set: MatchSet):
        self.score_player_a = 0
        self.score_player_b = 0
        self.advantage = ''  # A / B
        self.winner = ''  # A / B
        self.match_set = match_set

        MatchPoint.point_id += 1

        if MatchPoint.point_id != 1:
            self.match_set.match.toggle_serving_player()

        print(f'New match point, server: {self.match_set.match.serving_player.name}')

    def score_point(self, player: str):

        # If the scored is player a
        if player == 'A':
            self.score_player_a += 15

            # If score already max
            if self.score_player_a > 45:

                # If player a has advantage => Won
                if self.advantage == 'A':
                    self.winner = 'A'
                    self.advantage = ''

                elif self.advantage == 'B':
                    self.advantage = ''

                # False 45-45 without advantage
                elif self.score_player_b == 45:
                    self.advantage = 'A'

                else:
                    self.winner = 'A'
                    self.advantage = ''

                self.score_player_a = 45

        else:
            self.score_player_b += 15

            # If score already max
            if self.score_player_b > 45:

                # If player a has advantage => Won
                if self.advantage == 'B':
                    self.winner = 'B'
                    self.advantage = ''

                elif self.advantage == 'A':
                    self.advantage = ''

                # False 45-45 without advantage
                elif self.score_player_a == 45:
                    self.advantage = 'B'

                else:
                    self.winner = 'B'
                    self.advantage = ''

                self.score_player_b = 45

