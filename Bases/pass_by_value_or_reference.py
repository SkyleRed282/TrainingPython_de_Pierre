
def add_5(some_int):
    some_int += 5
    return some_int


def add_list_5(list_int):
    list_int.append(5)
    return list_int


def add_tuple_5(some_tuple):
    new_tuple = some_tuple + (5,)
    return new_tuple


if __name__ == '__main__':

    print('int are immutable')
    base_int = 5
    print(add_5(base_int))
    print(base_int)

    print('list are mutable')
    base_list = [1, 2]
    print(add_list_5(base_list))
    print(base_list)

    print('tuple are immutable')
    base_some_tuple = (1, 2)
    print(add_tuple_5(base_some_tuple))
    print(base_some_tuple)
