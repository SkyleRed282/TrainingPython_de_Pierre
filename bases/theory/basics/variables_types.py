
if __name__ == '__main__':

    # I'm a comment
    print('I\'m printing inside the terminal')

    # Attribute + Method call
    print('hello world'.capitalize())

    # Assignation
    var1 = 123
    var2 = var1 + 2
    print(var2)

    # Multiple assignation
    x, y, z = "Orange", "Banana", "Cherry"
    a, b, c = ["Orange", "Banana", "Cherry"]

    # Data type
    print(' === data type === ')
    my_string = 'abc' # my_string = ['a', 'b', 'c']
    print(my_string[0])

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
    print(5 * 'x')

    # Structures
    print(' === structures === ')
    my_list = ['a', 1, 'test', 'toto', 1]
    print(my_list)

    empty_list = []  # list()

    my_list[1] = 'dog'
    print(my_list)

    my_list.append('cat')
    print(my_list)

    my_list.insert(0, 'bird')
    print(my_list)

    print(' === tuple === ')
    my_tuple = ('abc', 1, [1, 2, 3])
    print(my_tuple[2][0])

    print(' === set === ')
    # set = no duplicates
    my_set = {'a', 'a', 'b'}
    empty_set = set()
    print(my_set)

    print(' === range === ')
    my_range = range(1, 15, 2)  # [2, 4, 6, ..]
    print(list(my_range))

    print(' === dict === ')
    empty_dict = {}
    my_dict = {
        'key1': 'value1',
        2: 34
    }
    print(my_dict)
    my_dict.update(
        {
            'key1': 11,
            'key33': 123
        }
    )
    print(my_dict)

    my_dict[456] = 'abc'
    print(my_dict)

    del my_dict[456]
    print(my_dict)

    print(my_dict.get(324, 'Nothing'))  # None
    # print(my_dict['324'])

    print(my_dict.keys())
