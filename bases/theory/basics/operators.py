if __name__ == '__main__':

    # arithmetics
    print(' == arithmetic ==')
    var = 1 * 2 / 2 - 3 + 5
    print(5 % 2)
    print(5 // 2)

    # assigement
    var1 = 1
    var1 = var1 + 2
    var1 += 2

    # comparison
    print(' == comparison ==')
    print(1 == 2)
    print(1 != 2)

    # logical operators
    print(' == logical ==')
    print(True and False)
    print(True or False)
    print(not False)

    # identity operators
    print(' == identity operators ==')
    print(type(var1) is int)

    # membership operator
    print(' == membership operator ==')
    print('x' in 'axc')
    print('x' in ['a', 'x', 'c'])
    print('axc' in ['a', 'x', 'c'])
