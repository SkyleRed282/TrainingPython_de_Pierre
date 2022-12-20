import random

def get_random_value_from(data:list):
    # wenn liste leer ist
    if len(data) == 0:
        return None

    # wenn liste > 0 ist: zufälliges Element ausgeben
    index = random.randint(0, len(data)-1)
    return data[index]


if __name__ == '__main__':
    print(get_random_value_from(['a', 1, 3, 4]))
    print(get_random_value_from([]))
