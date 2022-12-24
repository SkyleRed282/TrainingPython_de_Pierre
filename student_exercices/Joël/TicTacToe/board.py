rom
students.Joël.TicTacToe.spieler
import Spieler
from typing import Union


class Board:

    def __init__(self):
        self.brett = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def is_full(self) -> bool:
        for line in self.brett:
            for wert in line:
                if wert is None:
                    return False
        return True

    def get_winner(self) -> Union[Spieler, None]:
        if self.brett[0][0] == self.brett[0][1] == self.brett[0][2]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[1][0] == self.brett[1][1] == self.brett[1][2]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[2][0] == self.brett[2][1] == self.brett[2][2]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[0][0] == self.brett[1][0] == self.brett[2][0]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[0][1] == self.brett[1][1] == self.brett[2][1]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[0][2] == self.brett[1][2] == self.brett[2][2]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[0][0] == self.brett[1][1] == self.brett[2][2]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o

        elif self.brett[2][0] == self.brett[1][1] == self.brett[0][2]:
            if self.brett == self.Sign.x:
                return self.Sign.x
            elif self.brett == self.Sign.o:
                return self.Sign.o
        return None