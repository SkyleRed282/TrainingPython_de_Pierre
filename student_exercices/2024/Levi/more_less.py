import random
from datetime import datetime



if __name__ == '__main__':
    pass


# Jemand muss sich eine Zahl überlegen
number_to_guess = random.randint(1,100)


guess = 0
while guess != number_to_guess:

    # Eine Zahl raten
    guess = int(input('Rate eine Zahl zwischen 1-100: '))

    # Entweder die Zahl ist grösser
    if guess < number_to_guess:
        print('Die Zahl die du suchst ist grösser.')

    # Oder die Zahl ist kleiner
    elif guess > number_to_guess:
        print('Die Zahl die du suchst ist kleiner')


# Es kann richtig sein
print('Du hast gewonnen die Zahl ist richtig')

# hausaufabe
# Add lives to game => 6 lives to win