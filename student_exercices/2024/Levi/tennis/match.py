
from player import Player


class Match:

    def __init__(self, player_a: Player, player_b: Player):
        self.match_sets = []
        self.player_a = player_a
        self.player_b = player_b

    def play_match(self):

        from match_set import MatchSet

        """
        Play 2 or 3 sets depending on the results and display the final score
        """

        # Set 1
        set_1 = MatchSet(match=self)
        self.match_sets.append(set_1)
        set_1.play_set()

        # Set 2
        set_2 = MatchSet(match=self)
        self.match_sets.append(set_2)
        set_2.play_set()

        # Set 3 if ex-eqo
        if set_1.get_set_winner() != set_2.get_set_winner():
            set_3 = MatchSet(match=self)
            self.match_sets.append(set_3)
            set_3.play_set()

    def get_result(self):
        results = []
        for match_set in self.match_sets:
            results.append(match_set.get_set_winner())

        if results.count('A') == 2:
            winner = 'A'
        else:
            winner = 'B'

        return results, winner

    def __str__(self):
        """
        Winner player A/B - Sets[A,B,A]
        """
        results, winner = self.get_result()

        return f"Winner {winner} - Sets {results}"
