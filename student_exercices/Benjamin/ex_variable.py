vokale = "aeiouy"
print(vokale)
print(vokale[3])

numbers = list(range(1, 11))
print(numbers)

numbers[4] = "dog"
print(numbers)

from string import ascii_lowercase as alphabet

wb = {
    1: alphabet[0],
    2: alphabet[1],
    3: alphabet[2],
    -1: alphabet,
    'sub_dict': {
        1: [
            {5: 1, 3: 2},
            {1, 2, 3}
        ]
    }
}
print(wb)
print(wb[-1][25])
print(wb["sub_dict"][1][0][3])
