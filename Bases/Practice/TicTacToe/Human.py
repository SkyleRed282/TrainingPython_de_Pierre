from Bases.Practice.TicTacToe.Player import Player


class Human(Player):
    def __init__(self):
        super().__init__(name=input('Please choose a name: '))

