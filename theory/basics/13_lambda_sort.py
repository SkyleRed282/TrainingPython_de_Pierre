liste_chiffre = ['table', ' car ', 'dog', 'rainbow ']

# alphabetic sort
print(sorted(liste_chiffre))

# sort by length
print(sorted(liste_chiffre, key=len))

# sort by length without space
print(sorted(liste_chiffre, key=len))

def len_without_space(value:str):
    return value.strip()

print(sorted(liste_chiffre, key=len_without_space))