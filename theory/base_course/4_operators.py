import random
from pprint import pprint

# arithmetics
print(' == arithmetic ==')
print(1 * 2 / 2 - 3 + 5)
print(5 % 2)

# Ex of %: repartition of student in classrooms
class_rooms = [[], [], [], [], []]
for _ in range(1, 22):
    student_nbr = random.randint(0,100)
    class_rooms[student_nbr % 5].append(student_nbr)

pprint(class_rooms)
print(5 // 2)

# assignment
var1 = 1
var1 = var1 + 2
var1 += 2

# comparison
print(' == comparison ==')
print(1 == 2)
print(1 != 2)
print(1 <= 2)

# logical operators
print(' == logical ==')
print(True and False)
print(True or False)
print(not False)
print(any([False, False, False, False, True]))
print(all([False, False, False, False, True]))

# identity operators
print(' == identity operators ==')
print(type(IndexError) is LookupError)
print(isinstance(IndexError(), LookupError))
print(type('1') is int)

# membership operator
print(' == membership operator ==')
print('x' in 'axc')
print('x' in ['a', 'x', 'c'])
print('axc' in ['a', 'x', 'c'])
print(['a', 'x'] in ['a', 'x', 'c'])
