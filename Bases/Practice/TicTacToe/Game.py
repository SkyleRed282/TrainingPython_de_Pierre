import random
from Bases.Practice.TicTacToe import Player
from Bases.Practice.TicTacToe.Grid import Grid
from Bases.Practice.TicTacToe.Human import Human


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        # initialiser la grille de 3x3
        self.grid = Grid()
        self.starting_player = self.ask_who_start()

    def ask_who_start(self):
        # on demande à l'utilisateur s'il veut commencer ou laisser l'ordinateur
        if isinstance(self.player1, Human):
            answer = None
            while answer not in ['1', '2']:
                answer = input('Which player shall start first? (1/2)')
            starting_player = int(answer)
        else:
            starting_player = random.randint(0, 2)
        return starting_player

    def start(self):
        print(f'New game between {self.player1.name} and {self.player2.name}')

        # tant que personne n'à gagné
        while self.check_grid_result() == None:

            # on demande au joueur actuel son prochain coup


            # on affiche la grille
            # on passe au joueur suivant

        # afficher le résultat
        # demander à l'utilisateur s'il veut rejouer


    def check_grid_result(self):
        # return None if no result, False if draw, else the player who won
        grid_lines = self.grid.cells

        # Pour chacun des joueurs, on vérifie s'il a gagné
        for player in [self.player1, self.player2]:
            sign = player.sign

            # test lines
            player_sign_3 = sign*3

            line_1_as_str = ''.join(grid_lines[0])
            line_2_as_str = ''.join(grid_lines[1])
            line_3_as_str = ''.join(grid_lines[2])
            lines_as_list = [line_1_as_str, line_2_as_str,line_3_as_str]

            if player_sign_3 in lines_as_list:
                return player

            # test columns
            col_1_as_str = f'{grid_lines[0][0]}{grid_lines[1][0]}{grid_lines[2][0]}'
            col_2_as_str = f'{grid_lines[0][1]}{grid_lines[1][1]}{grid_lines[2][1]}'
            col_3_as_str = f'{grid_lines[0][2]}{grid_lines[1][2]}{grid_lines[2][2]}'
            cols_as_list = [col_1_as_str, col_2_as_str, col_3_as_str]

            if player_sign_3 in cols_as_list:
                return player

            # test diagonals
            diag_hgbd_str = f'{grid_lines[0][0]}{grid_lines[1][1]}{grid_lines[2][2]}'
            diag_hdbg_str = f'{grid_lines[0][2]}{grid_lines[1][1]}{grid_lines[2][0]}'

            if player_sign_3 in [diag_hdbg_str,diag_hgbd_str]:
                return player

        # Check if grid is full
        lines_as_list_str = ''.join(lines_as_list)
        if ' ' in lines_as_list_str:
            return None

        return False

