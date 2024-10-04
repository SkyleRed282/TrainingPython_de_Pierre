def get_number_from_position(list_of_number, asked_position):
    return list_of_number[asked_position]


if __name__ == '__main__':

    number_list = [23, 45, 234, 67, 98, 45, 234, 79, 23]

    # ask the user for a position
    valid_number = False

    while not valid_number:

        position = input(f'Gib eine Zahl unter {len(number_list)} als Position ein: ')

        if not position.isdigit():
            print('Deine Eingabe ist keine Nummer')
        elif int(position) > len(number_list) - 1:
            print(f'Deine Eingabe ist grösser als {len(number_list) - 1}')
        else:
            valid_number = True

    number = get_number_from_position(number_list, int(position))

    print(number)
