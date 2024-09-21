animals = []
birds = ('B1', 'B2', 'B3')

animals.extend(birds)
print(animals)

animals.append(birds)
print(animals)

del animals[3]
print(animals)

cats = {
    'C1': ['cat name 1', 4],
    'C2': ['cat name 2', 4],
    'C3': ['cat name 3', ['cat name 3', ['cat name 3', ['cat name 3', 4]]]],
    'C4': ['cat name 4', 5],
}

animals.append(cats['C3'][0])
print(animals)

animals[3] = animals[3].title()
print(animals)


