false_values = [0, '', False, None, [], {}, tuple(), set(), 0.0]

for false_value in false_values:
    print(f'{false_value} of type {type(false_value).__name__} => {bool(false_value)}')

if not []:
    print('\nThe list is empty')
