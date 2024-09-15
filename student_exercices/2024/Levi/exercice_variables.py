# {'cat':'black', ... }
from pprint import pprint

black_box = {  # Dict
    '1': 1,
    '2': 5 / 2,
    '3': 5 < 4,
    '4': list(range(10)),  # Liste
    '5': {9, 10, 11},  # Set
    '6': ('D', 'E', 'F'),  # Tuple
    '7': ['A', 'B', ['C', 'F', {'a': 'b'}]],
}

# []
# black_box['3'] = not black_box['3']
# pprint(black_box)
#
# x = 1,
# print(type(x))

# len()

print(len(black_box['7'][2]))

# black_box['7'][2][2]['a'] = 'c'
# del black_box['4'][6]
# black_box['6'] = ('D', 'F')
#
# del black_box['3']
#
# black_box2 = {}
# for key, value in black_box.items():
#     black_box2[int(key)] = value
#
# pprint(black_box2)
