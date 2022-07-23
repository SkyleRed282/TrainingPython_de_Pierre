if __name__ == '__main__':

    print(True)
    print(3 < 5)

    if 3 > 2:
        print('x')

    my_list = ['2']
    my_empty_list = []

    if my_empty_list:
        print('List is not empty')
    else:
        print('List is empty')

    # arithmetics
    print(' == Operateurs arithmetics ==')
    var = 1 * 2 / 2 - 3 + 5
    print(5 % 2)
    print(5 // 2)

    # assigement
    var1 = 1
    var1 = var1 + 2
    var1 += 2

    # comparison
    print(' == comparison operateurs  ==')
    print(1 == 2)
    print(1 != 2)

    # operateurs logiques
    print(' == logical ==')
    print(True and False)
    print(True or False)
    print(not False)

    # identity operators
    print(' == identity operators ==')
    print(type(var1) is int)
    print(isinstance(True, bool))  # classes

    # membership operator
    print(' == membership operator ==')
    print('x' in 'axc')
    print('x' in ['a', 'x', 'c'])

    print(len('axc'))
