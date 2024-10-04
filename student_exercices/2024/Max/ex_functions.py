import string


def half(nummer):
    return nummer / 2


def is_even(nummer: int) -> bool:
    return nummer % 2 == 0


def count_letter(text: str, counted_letter: str) -> int:
    counter = 0
    for letter in text:
        if letter == counted_letter:
            counter += 1

    return counter

for letter in string.ascii_lowercase:
    print(f'How many time is the letter {letter} in this text:? {count_letter("sdfjskdjfbkjsdfaaaa", letter)}')  # 3
