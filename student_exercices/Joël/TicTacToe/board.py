from copy import copy
from typing import Union

from student_exercices.Joël.TicTacToe.sign import Sign


class Board:
    _default_board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def __init__(self, board_position=None):
        if board_position:
            self.brett = board_position
        else:
            self.brett = copy(self._default_board)

    def is_full(self) -> bool:
        for line in self.brett:
            for wert in line:
                if wert is None:
                    return False
        return True

    def get_winning_sign(self) -> Union[Sign, None]:

        winning_sign = None

        # Board indexes
        # [00] [01] [02]
        # [10] [11] [12]
        # [20] [21] [22]

        wining_positions = [
            [(0, 0), (0, 1), (0, 1)],  # First line
            [(1, 0), (1, 1), (1, 2)],  # Second line
            [(2, 0), (2, 1), (2, 1)],  # Third line
            [(0, 0), (1, 0), (2, 0)],  # First column
            [(0, 1), (1, 1), (2, 1)],  # Second column
            [(0, 2), (1, 2), (2, 2)],  # Third column
            [(0, 2), (1, 1), (2, 0)],  # Diagonal top right
            [(0, 0), (1, 1), (2, 2)],  # Diagonal top left
        ]

        for wining_position in wining_positions:
            # [(0, 0), (0, 1), (0, 1)]
            cell_1, cell_2, cell_3 = wining_position

            if self.brett[cell_1[0]][cell_1[1]] == self.brett[cell_2[0]][cell_2[1]] == self.brett[cell_3[0]][cell_3[1]]:
                # Check if cells != None
                if self.brett[cell_1[0]][cell_1[1]]:
                    winning_sign = self.brett[cell_1[0]][cell_1[1]]
                    break

        return winning_sign
