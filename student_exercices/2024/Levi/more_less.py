import random

# Jemand muss sich eine Zahl überlegen
number_to_guess = random.randint(1, 100)

lives = 6
guess = 0
while guess != number_to_guess:

    # Eine Zahl raten
    guess = ''
    while not guess.isdigit():
        guess = input('Rate eine Zahl zwischen 1-100: ')
    guess = int(guess)

    # Entweder die Zahl ist grösser
    if guess < number_to_guess:
        print('Die Zahl die du suchst ist grösser.', lives, 'more lives')

    # Oder die Zahl ist kleiner
    elif guess > number_to_guess:
        print('Die Zahl die du suchst ist kleiner', lives, 'more lives')

    lives -= 1

# Ende Schleife
if lives == 0:
    print('Sorry you have 0 lives you lost')
else:
    print('Du hast gewonnen die Zahl ist richtig')
