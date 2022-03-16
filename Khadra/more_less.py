import random

if __name__ == '__main__':

    # chose random number
    MAX_VALUE = 100
    MIN_VALUE = 0
    random_number = random.randint(MIN_VALUE, MAX_VALUE)


    # until user did not find the number
    guess = -1
    while guess != random_number:

        # ask user for a guess
        guess = input('Choose a number ')

        # check answer is a number
        if not guess.isdigit():
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
