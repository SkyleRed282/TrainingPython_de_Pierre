import random

if __name__ == '__main__':

    leben = 10
    zahl = random.randint(0, 101)

    user_input = -1

    while user_input != zahl and leben != 0:

        print(f'Du hast noch {leben} Leben ')

        user_input = int(input('Welche nummer?'))

        if zahl == user_input:
            print("You win!")
        elif zahl > user_input:
            print("Zahl ist grösser")
        else:
            print("Zahl ist kleiner")

        leben -= 1

        if leben == 0:
            print("You loose!")