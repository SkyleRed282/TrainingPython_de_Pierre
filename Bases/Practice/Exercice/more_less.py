import random

if __name__ == '__main__':

    # generate a random number between min and max values
    MAX_VALUE = 100
    MIN_VALUE = 0

    random_number = random.randint(# TODO)

    # until user has not find the number
    guess = -1
    while # TODO:

        # ask user for a guess
        # TODO

        # check answer is a number
        if not # TODO:
            print(f'{guess} is not a valid number.')
            continue

        # convert answer to int
        guess = # TODO
        if # TODO:
            # else tell user if > or <
            print('The number is smaller.')
        elif # TODO:
            print('The number is bigger.')

    # if guess is correct => won
    print('You won!')