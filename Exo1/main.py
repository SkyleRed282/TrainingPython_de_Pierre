from Exo1.fraction import Fraction
from Exo1.operation import Operation

if __name__ == '__main__':
    f1 = Fraction(2, 3)
    f2 = Fraction(3, 4)

    f3 = f1.add(f2)
    print(f3)

    op1 = Operation(frac2=f2, frac1=f1, op='+')
    print(op1)
    op1.calculer()
    print(op1)

    # print(f1, f2)
    #
    # f3 = f1.multi(f2)
    # print(f3)
    #
    # f4 = f3.multi_scal(-4)
    # print(f4)
    #
    # print(Fraction.multi_list([f1, f2, f3]))
    #
