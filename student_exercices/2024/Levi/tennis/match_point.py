from random import randint


class MatchPoint:

    def __init__(self):
        self.score_player_a = 0
        self.score_player_b = 0
        self.advantage = ''  # a / b
        self.winner = ''  # a / b

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

    # If winner? => 'Won by player X' / Else: 'A:pts - B:pts'
    def __str__(self):
        if self.winner:
            return f'Point won by player {self.winner}'
        else:

            result = f'A:{self.score_player_a}'
            if self.advantage == 'A':
                result += ' [ADV]'
            result += f' - B:{self.score_player_b}'
            if self.advantage == 'B':
                result += ' [ADV]'

            return result

    def is_finished(self):
        return bool(self.winner)

    def play_point(self):

        while not self.is_finished():
            player_points = randint(0, 1)
            player_name = ('A', 'B')[player_points]
            self.score_point(player_name)
            print(self)