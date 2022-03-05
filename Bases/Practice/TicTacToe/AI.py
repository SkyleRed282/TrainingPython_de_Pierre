from Bases.Practice.TicTacToe.Player import Player
import random


class AI(Player):
    def __init__(self, sign: str):
        ai_name = f'computer{random.randint(0, 1000)}'
        super().__init__(name=ai_name, sign=sign)
