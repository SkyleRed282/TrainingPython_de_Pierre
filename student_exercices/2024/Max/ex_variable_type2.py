from pprint import pprint

black_box = {
    '1': 1,  # int
    '2': 5 / 2,  # float
    '3': 5 < 4,  # bool
    '4': list(range(10)),  # list[int]
    '5': {9, 10, 11},  # set
    '6': ('D', 'E', 'F'),  # tuple[str]
    '7': ['A', 'B', ['C', 'F', {'a': 'b'}]],  # liste
}


black_box['7'][2][2]['a'] = 'c'
black_box['4'].remove(5)


pprint(black_box)

