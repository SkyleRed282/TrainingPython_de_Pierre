from enum import Enum


class FieldPosition:
    def __init__(self, mine):
        self.mine = mine
        self.status = Status.HIDDEN

    def __str__(self):
        if self.status == Status.HIDDEN:
            return '?'

        if self.status == Status.MARKED:
            return 'X'

        if self.mine == Mine.BOMBE:
            return 'B'

        if self.mine == Mine.LEER:
            return ' '

class Mine(Enum):
    BOMBE = 1
    LEER = 2


class Status(Enum):
    VISIBLE = 1
    HIDDEN = 2
    MARKED = 3
