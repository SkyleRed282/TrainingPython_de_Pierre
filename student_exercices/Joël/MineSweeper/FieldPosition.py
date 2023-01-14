from enum import Enum


class FieldPosition:
    def __init__(self, mine):
        self.mine = mine
        self.status = Status.HIDDEN

    def __str__(self):
        return self.display_position()

    def display_position(self, reveal_all=False):

        if not reveal_all:
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
