from Exo1.fraction import Fraction


class Operation:

    def __init__(self, frac1: Fraction, op: str, frac2: Fraction):
        self.frac1 = frac1
        self.frac2 = frac2
        self.op = op
        self.result = None

    def calculer(self):
        if self.op == '*':
            self.result = self.frac1.multi(self.frac2)

        elif self.op == '+':
            self.result = self.frac1.add(self.frac2)

    def __str__(self):
        return f'{self.frac1} {self.op} {self.frac2} = {self.result}'
