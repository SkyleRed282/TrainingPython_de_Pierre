from string import ascii_lowercase as alphabet


my_list = ['zzzzz', 'aaa', 'uuuuuu']
print(
    sorted(
        my_list,
        key=lambda word: -len(word)
    )
)

print(
    sorted(
        my_list,
        key=lambda word: -alphabet.index(word[0])
    )
)
