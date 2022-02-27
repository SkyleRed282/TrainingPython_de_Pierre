
if __name__ == '__main__':

    # Ceci est un commentaire
    print('b')

    # Assignation
    var1 = 123
    var2 = var1 + 2
    print(var2)

    # Assignation multiple
    x, y, z = "Orange", "Banana", "Cherry"

    # Types de données
    print(' === types de données === ')
    my_string = 'abc'
    print(my_string[1])
    my_multiline_string = ''' 
    aaaasd 
    asdasd
    asdasd
    asdasd
    '''

    my_int = 23
    my_float = 2.4
    my_bool = True

    # casting
    print(' === casting === ')
    var3 = '100'
    print(type(var3))
    print(int(var3) + 5)
    print(var3 + str(5))

    # Structures
    print(' === structures === ')
    my_list = ['a', 1, 'test', 'toto']
    print(my_list)

    my_list[1] = 'gg'
    print(my_list)

    my_list.append('asd')
    print(my_list)

    print(' === tuple === ')
    my_tuple = ('abc', 1)

    print(' === set === ')
    # set = pas de doublons
    my_set = {'a', 'a', 'b'}
    print(my_set)

    print(' === range === ')
    my_range = range(0, 15, 2)
    for x in my_range:
        print(x, end=' ')
    print(my_range)

    print(' === dict === ')
    my_dict = {
        'cle1': 'valeur1',
        2: 34
    }
    print(my_dict)
    my_dict.update(
        {
            'cle1': 11,
        }
    )
    print(my_dict)
    my_dict[456] = 'abc'
    print(my_dict)

    print(my_dict.get('324'))




