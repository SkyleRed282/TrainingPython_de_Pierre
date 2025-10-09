def ia_aleatoire(plage_min: int, plage_max: int) -> int:
    return random.randint(plage_min, plage_max)


def ia_dichotomique(plage_min: int, plage_max: int) -> int:
    largeur_plage = (plage_max - plage_min + 1)
    return largeur_plage // 2 if largeur_plage > 1 else plage_min

# Devoir : Nouvelle fonction de proposition de nombre
# source des statistiques : https://www.reddit.com/r/dataisbeautiful/comments/iiafkd/oc_i_asked_100_people_to_pick_a_number_between/?tl=fr#lightbox
# J'ai essayé de faire une fonction de choix grâce à des statistiques

def ia_a_choix_statistique(plage_min: int, plage_max: int) -> int:
    nb_extremement_choisi = [69, 1, 37, 22, 24, 77, 97]
    nb_random_extremement_choisi = random.choice(nb_extremement_choisi)
    nb_tres_choisi = [19, 34, 56, 57, 72, 73, 2, 3, 7, 29, 31, 32, 36, 43, 64, 68, 100]
    nb_random_tres_choisi = random.choice(nb_tres_choisi)
    nb_pas_tres_choisi = [4, 5, 11, 14, 15, 16, 17, 21, 33, 45, 47, 53, 54, 59, 71, 74, 83, 85, 86, 88, 89, 92, 93, 96, 98]
    nb_random_pas_tres_choisi = random.choice(nb_pas_tres_choisi)
    nb_rarement_choisi = [6, 8, 9, 10, 12, 13, 18, 20, 23, 25, 26, 27, 28, 30, 35, 38, 39, 40, 41, 42, 44, 46, 48, 49, 50, 51, 52, 55, 58, 60, 61, 62, 63, 65, 66, 67, 70, 75, 76, 78, 79, 80, 81, 82, 84, 87, 90, 91, 94, 95, 99]
    nb_random_rarement_choisi = random.choice(nb_rarement_choisi)
    nb_choisi_des_list = [nb_random_extremement_choisi, nb_random_tres_choisi, nb_random_pas_tres_choisi, nb_random_rarement_choisi]
    return random.choice(nb_choisi_des_list)

if __name__ == '__main__':

    import random

    # L'utilisateur choisi un nombre dans sa tête
    input('Utilisateur: Pense à un nombre entre 1 et 100 et appuie sur ENTER pour démarer la partie.')

    feedback = ''
    nb_min, nb_max = 1, 100

    # L'IA propose un nombre possible jusqu'à le trouver

    while feedback != '=':

        nombre_propose = ia_a_choix_statistique(nb_min, nb_max)
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
