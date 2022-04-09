class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f'{self.num}/{self.den}'

    def multi(self, fract):
        multi_num = self.num * fract.num  # 2 * 3 = 6
        multi_den = self.den * fract.den  # 3 * 4 = 12
        return Fraction(multi_num, multi_den)

    def add(self, fract):
        den_com = self.den * fract.den
        new_num = self.num * fract.den + fract.num * self.den
        return Fraction(new_num, den_com)

    def multi_scal(self, scal):
        return Fraction(self.num * scal, self.den)

    @staticmethod
    def multi_list(list_frac: list):
        new_fract = list_frac[0]
        for fract in list_frac[1:]:
            new_fract = new_fract.multi(fract)
        return new_fract
