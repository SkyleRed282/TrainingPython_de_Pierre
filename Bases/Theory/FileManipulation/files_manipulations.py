import os
import random
import json

if __name__ == '__main__':

    # Generate dict of numbers and save it as JSON
    numbers = list(range(10))
    number_dict = {}
    for number in numbers:
        number_dict[number] = random.randint(50,100)

    for key, value in number_dict.items():
        print(key, value)

    with open('numbers.json', 'w') as file_pointer:
        file_pointer.write(json.dumps(number_dict))

    # read the file and display it as Python object
    with open('numbers.json') as file_pointer:
        content = json.loads(file_pointer.read())
    print(content,type(content))