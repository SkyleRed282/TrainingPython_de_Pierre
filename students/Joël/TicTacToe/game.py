from students.Joël.TicTacToe.board import Board
from students.Joël.TicTacToe.sign import Sign
from students.Joël.TicTacToe.spieler import Spieler


class Game:
    def __init__(self):
        self.spieler1 = Spieler(Sign.o)
        self.spieler2 = Spieler(Sign.x)
        self.board = Board()

    def board_full(self):
        return self.board.is_full()

    def get_winner(self):
        return self.board.get_winner()

    def play(self):

        # Das Spiel geht solange bis ein Spieler gewonnen hat oder das Board ist voll
        pass