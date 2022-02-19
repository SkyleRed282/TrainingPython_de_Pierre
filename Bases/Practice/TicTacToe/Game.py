from Bases.Practice.TicTacToe import Player
from Bases.Practice.TicTacToe.Grid import Grid


class Game:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.grid = Grid()

        print(f'New game between {player1.name} and {player2.name}')

        # Tant que l'utilisateur veut continuer a jouer
        # initialiser la grille de 3x3
        # on demande à l'utilisateur s'il veut commencer ou laisser l'ordinateur

        # tant que personne n'à gagné ou que la grille n'est pas pleine
        # on demande au joueur actuel son prochain coup
        # on affiche la grille
        # on passe au joueur suivant

        # afficher le résultat
        # demander à l'utilisateur s'il veut rejouer
