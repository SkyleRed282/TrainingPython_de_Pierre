from string import ascii_letters
# Donné un mot en paramètre et une lettre, retourner le nombre de fois que la lettre est présente dans le mot


#####

def count_letter(mot:str, letter:str):

    if letter not in ascii_letters:
        return 0

    counter = 0

    mot_lower = mot.lower()

    for lettre_mot in mot_lower:
        if lettre_mot == letter:
            counter += 1

    return counter

#####

if __name__ == '__main__':

    assert count_letter(mot='Chat',letter='c') == 1
    assert count_letter(mot='chat',letter='c') == 1
    assert count_letter(mot='canard',letter='A') == 0
    assert count_letter(mot='lapin',letter='r') == 0
    assert count_letter(mot="L'opéra",letter="'") == 0 # Seules les lettres sont acceptées (a-zA-Z)
