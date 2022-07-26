from string import ascii_lowercase as alphabet


if __name__ == '__main__':

    print('\nFor each')
    for letter in alphabet[:3]: # ['a','b','c']
        print(letter, end=' ')

    print('\n\nFor each - enumerate')
    for index, letter in enumerate(alphabet[:3]):
        print(index, letter, end=' ')

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
    for letter in alphabet:
        print(letter, end=' ')
        if letter == 'c':
            break

    print('\n\nContinue')
    for number in range(11):
        if number % 2 == 0:
            continue
        print(number, end=' ')

    print('\n\nLoop in loop')
    for letter1 in alphabet:
        if letter1 == 'd':
            break
        for letter2 in alphabet[::-1]:
            if letter2 == 'w':
                break
            print(f'{letter1}/{letter2}', end=' ')
