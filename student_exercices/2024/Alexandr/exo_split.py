

# Methode qui reçoit un string en paramètre avec des separateurs (toujours le même) (-*. )
# Decouper le texte dans une liste, où chaque case est un bout du string entre les séparateurs
# Exemple: dfgdfgdfg*dfgdfg*wretert => ['dfgdfgdfg','dfgdfg','wretert']


def split_string(some_string:str):

    #identifier le separateur
    #balayer le texte pour identifier le separateur(quelque chose qui n'est pas une lettre)
    for character in some_string:
        if not character.isalpha():
            return some_string.split(character)
            #decouper le texte avec le separateur et mettre le resultat dans une liste

print(split_string("dfgdfgdfg*dfgdfg*wretert"))


