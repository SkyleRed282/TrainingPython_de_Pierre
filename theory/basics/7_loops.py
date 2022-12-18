from string import ascii_lowercase as alphabet

if __name__ == '__main__':

    print('\nFor each')

    for letter in alphabet[:3]:  # abc
        print(letter, end=' ')

    print('\n\nFor each - enumerate')

    for index, letter in enumerate(alphabet[:3]):
        print(index, letter, end=' ', sep='-')

    print('\n\nFor i')

    for letter_number in range(3):  # [0, 1, 2]
        # ['a','b', ...]
        print(alphabet[letter_number], end=' ')

    print('\n\nWhile')

    letter_number = 0
    while letter_number < 3:
        print(alphabet[letter_number], end=' ')
        letter_number += 1

    print('\n\nBreak')

    for letter in alphabet:  # ['a','b', ..., z]
        print(letter, end=' ')
        if letter == 'c':
            break

    print('\n\nElse')

    for letter in alphabet:
        pass
    else:
        print('The for loop did run on all elements')

    print('\n\nContinue')

    for letter_number in range(11):
        if letter_number % 2 == 1:
            continue
        print(alphabet[letter_number], end=' ')

    print('\n\nLoop in loop')

    for letter1 in alphabet:
        if letter1 == 'd':
            break

        for letter2 in alphabet[::-1]:
            if letter2 == 'w':
                break
            print(letter1, letter2, sep='/', end=' ')

    print('\n\nZip')

    for letter_a, letter_b in zip(alphabet[:3], alphabet[2::-1]):
        print(letter_a, letter_b, sep='/')
