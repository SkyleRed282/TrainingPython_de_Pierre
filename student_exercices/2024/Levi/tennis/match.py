from random import randint
from player import Player


class Match:

    def __init__(self, player_a: Player, player_b: Player):
        self.match_sets = []
        self.player_a = player_a
        self.player_b = player_b

        print(f'Match starting between : {self.player_a.name} and {self.player_b.name}.')

        self.serving_player = (player_a, player_b)[randint(0, 1)]
        print(f'{self.serving_player.name} will start serving.')

    def toggle_serving_player(self):
        # <some_variable> = <value if true> if <condition> else <value if false>
        self.serving_player = self.player_b if self.serving_player == self.player_a else self.player_a


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

        sum_points_a, sum_points_b = 0, 0
        for match_set in self.match_sets:
            player_a_points, player_b_points = match_set.get_points()  # [3,6]
            results.append(f'{player_a_points}:{player_b_points}')
            sum_points_a += player_a_points
            sum_points_b += player_b_points

        # Results [['3:6'],['2:6']]
        winner = self.player_a if sum_points_a > sum_points_b else self.player_b

        return results, winner

    def print_result(self):

        results, winner = self.get_result()
        print(f"Winner: {winner.name} - Sets {results}")
