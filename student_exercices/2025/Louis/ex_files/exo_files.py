# 1) Créer le dossier data/ au besoin
from string import ascii_lowercase as alphabet
import os

if not os.path.exists('data'):
    os.mkdir(path='data')

# 2) Créer pour chaque lettre de l'alphabet un fichier nommé <lettreAlphabet>.txt dans le dossier data/
for lettre in alphabet:
    with open(f'data/{lettre}.txt', 'w'):
        pass

# 3) Supprimer les dossier impairs (a,c,e,...)
for index_lettre, lettre in enumerate(alphabet):
    if index_lettre % 2 == 1:
        os.remove(f'data/{lettre}.txt')

# 4) Ouvrir chaque fichier txt, et écrire dedans x * <lettre>, où x correspond à l'index+1 de la lettre dans l'alphabet
for file_name in os.listdir('data/'):
    lettre = file_name[0]
    index_lettre = alphabet.index(lettre)
    with open(f'data/{file_name}', 'w') as file_pointer:
        file_pointer.write(lettre * (index_lettre + 1))
