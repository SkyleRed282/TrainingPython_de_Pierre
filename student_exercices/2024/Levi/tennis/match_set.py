class MatchSet:

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
                # If the oter play had advantage => deuce
                elif self.advantage == 'B':
                    self.advantage = ''

                # Advantage to player A
                else:
                    self.advantage = 'A'

                self.score_player_a = 45

        else:
            self.score_player_b += 15

            # If score already max
            if self.score_player_b > 45:

                # If player a has advantage => Won
                if self.advantage == 'B':
                    self.winner = 'B'
                # If the oter play had advantage => deuce
                elif self.advantage == 'A':
                    self.advantage = ''

                # Advantage to player b
                else:
                    self.advantage = 'B'

                self.score_player_b = 45

    # If winner? => 'Won by player X' / Else: 'A:pts - B:pts'
    def __str__(self):
        if self.winner:
            return f'Won by player {self.winner}'
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
