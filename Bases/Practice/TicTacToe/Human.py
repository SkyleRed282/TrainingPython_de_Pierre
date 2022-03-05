from Bases.Practice.TicTacToe.Grid import Grid
from Bases.Practice.TicTacToe.Player import Player


class Human(Player):
    def __init__(self, sign: str):
        super().__init__(name=input('Please choose a name: '), sign=sign)

    def get_next_play(self, grid: Grid):

        user_choice = []
        while not user_choice:
            user_input = input('In which cell do you want to put your next move? (line_nbr col_nbr)')
            splitted_input = user_input.split()
            if len(splitted_input) != 2:
                print('Invalid value! ')
                continue

            if not splitted_input[0].isdigit() or not splitted_input[1].isdigit():
                print('Invalid value! ')
                continue

            if not splitted_input[0] not in ['1', '2', '3'] or splitted_input[1] not in ['1', '2', '3']:
                print('Invalid value! ')
                continue

            index_line = int(splitted_input[0]) - 1
            index_col = int(splitted_input[1]) - 1

            if grid.cells[index_line][index_col] != ' ':
                print(f'The cell {splitted_input[0]}{splitted_input[1]} is already filled!')

            return [index_line, index_col]
