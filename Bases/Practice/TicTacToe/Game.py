import random
from Bases.Practice.TicTacToe import Player
from Bases.Practice.TicTacToe.Grid import Grid
from Bases.Practice.TicTacToe.Human import Human


class Game:
    player_signs = ['o', 'x']

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


        # tant que personne n'à gagné ou que la grille n'est pas pleine
        # on demande au joueur actuel son prochain coup
        # on affiche la grille
        # on passe au joueur suivant

        # afficher le résultat

        # demander à l'utilisateur s'il veut rejouer

    def result(self):
        # return None if no result, else the player which won
        grid_lines = self.grid.cells

        # test lines
        # Pour chaque ligne
        for line_nbr in range(len(grid_lines)):

            # Pour chaque colonne
            first_element = grid_lines[line_nbr][0]
            same_element = True
            if first_element != ' ':
                for col in range(1, len(grid_lines[line_nbr])):
                    if first_element != grid_lines[line_nbr][col]:
                        same_element = False
                        break
            else:
                same_element = False

            if same_element:
                # someone won...
                pass


        # test columns

        # test diagonals
