from string import ascii_lowercase


if __name__ == '__main__':

    print('\nFor each')
    for lettre in ascii_lowercase[:3]:
        print(lettre, end=' ')

    print('\n\nFor ')
    for letter_number in range(3):  # [0, 1, 2]
        # ['a','b', ...]
        print(ascii_lowercase[letter_number], end=' ')

    print('\n\nWhile')
    letter_number = 0
    while letter_number < 3:
        print(ascii_lowercase[letter_number], end=' ')
        letter_number += 1

    print('\n\nBreak')
    for x in ascii_lowercase:
        print(x, end=' ')
        if x == 'c':
            break

    print('\n\nContinue')
    for number in range(11):
        if number % 2 == 0:
            continue
        print(number, end=' ')
