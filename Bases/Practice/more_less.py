import random

if __name__ == '__main__':

    # chose random number
    number_to_find = random.randint(1, 100)

    # until user find the number
    guess = -1
    while number_to_find != guess:

        # ask user for a guess
        guess = input('Choose number: ')
        if not guess.isdigit():
            print(f'{guess} is not a valid number.')
            continue

        guess = int(guess)
        if guess > number_to_find:
            # else tell user if > or <
            print('The number is smaller.')
        elif guess < number_to_find:
            print('The number is bigger.')

    # if guess is correct => won
    print('You won!')
