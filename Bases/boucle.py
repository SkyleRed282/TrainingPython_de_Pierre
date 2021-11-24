from string import ascii_lowercase

if __name__ == '__main__':

    print('\nFor each')
    for lettre in ascii_lowercase[:3]:
        print(lettre)

    print('\nFor ')
    for numero_lettre in range(3):
        print(ascii_lowercase[numero_lettre])

    print('\nWhile')
    numero_lettre = 0
    while numero_lettre < 3:
        print(ascii_lowercase[numero_lettre])
        numero_lettre += 1

    print('\nBreak')
    for x in ascii_lowercase:
        print(x)
        if x == 'c':
            break

    print('\nContinue')
    for chiffre in range(11):
        if chiffre % 2 == 1:
            continue
        # sera fait seulement si chiffre pair
        print(chiffre)

    print('\nfibo')
    chiffre_1 = 0
    chiffre_2 = 1

    # 0 1 1 2 3 5 7 9
    for x in range(10):
        print(chiffre_1)
        chiffre_1, chiffre_2 = chiffre_2, chiffre_1 + chiffre_2






