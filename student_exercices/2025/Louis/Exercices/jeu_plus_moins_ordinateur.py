def ia_aleatoire(plage_min: int, plage_max: int) -> int:
    return random.randint(plage_min, plage_max)


def ia_dichotomique(plage_min: int, plage_max: int) -> int:
    largeur_plage = (plage_max - plage_min + 1)
    return plage_min + largeur_plage // 2 if largeur_plage > 1 else plage_min


def ia_tier_random(plage_min: int, plage_max: int) -> int:
    largeur_plage = (plage_max - plage_min + 1)
    tier = (largeur_plage // 3)
    return plage_min + tier * random.randint(1, 2) if largeur_plage > 1 else plage_min


if __name__ == '__main__':

    import random

    # L'utilisateur choisi un nombre dans sa tête
    input('Utilisateur: Pense à un nombre entre 1 et 100 et appuie sur ENTER pour démarer la partie.')

    feedback = ''
    nb_min, nb_max = 1, 100

    # L'IA propose un nombre possible jusqu'à le trouver

    while feedback != '=':

        nombre_propose = ia_tier_random(nb_min, nb_max)
        print(f'IA: Je propose {nombre_propose}.')

        # L'utilisateur informe l'IA si <>=
        feedback = ''
        while feedback not in ("<", ">", "="):
            feedback = input('Utilisateur: Le nombre proposé est (<=>): ')

        if feedback == "<":
            nb_min = nombre_propose + 1
        elif feedback == ">":
            nb_max = nombre_propose - 1

    print('IA: I am the best!')
