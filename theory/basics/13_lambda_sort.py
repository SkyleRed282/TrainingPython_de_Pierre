import random
from string import ascii_lowercase as alphabet

word_list = ['table', ' you ', 'castle', 'edge ']

print('Alphabetic sort', sorted(word_list))

print('Sort by length', sorted(word_list, key=len))


def len_without_space(value: str):
    return value.strip()


print('Sort by length without space', sorted(word_list, key=len_without_space))

print('Sort by length without space, with lambda', sorted(word_list, key=lambda word: word.strip()))

print('Sort by last letter without space, with lambda', sorted(word_list, key=lambda word: word.strip()[-1]))

print(
    'Sort by index sum, without space, with lambda',
    sorted(
        word_list, key=lambda word: sum([alphabet.index(letter) for letter in word.strip()])
    )
)

print('Sort randomly', sorted(word_list, key=lambda _: random.randint(0, len(word_list))))
