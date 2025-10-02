# Choisir un nombre entre 1 et 100
import random
import time

# l'utilisateur choisi la difficulté
difficulte_choisi = None
while difficulte_choisi not in ("facile", "moyenne", "difficile"):
    difficulte_choisi = input('En quelle difficulté voulez-vous jouer ?\n\n(Ceci est la difficulté de la session,\n il ne cera pas possible de modiffier\n la difficulté en cours de session !)\n\n("facile"/"moyenne"/"difficile"): ')

    # le paramètre lier à la difficulté selectionné est selectionner
    if difficulte_choisi not in ("facile", "moyenne", "difficile"):
        print(f'{difficulte_choisi} n\'est pas une difficulté valable.\n')

if difficulte_choisi == "facile":
    max_secondes_choisi = 35
    nb_vies_select = 9
    nombre_max_choisi = 100
elif difficulte_choisi == "moyenne":
    max_secondes_choisi = 25
    nb_vies_select = 7
    nombre_max_choisi = 100
else:
    max_secondes_choisi = 25
    nb_vies_select = 6
    nombre_max_choisi = 150


NOMBRE_MIN = 1
NOMBRE_MAX = nombre_max_choisi
MAX_SECONDES = max_secondes_choisi

continuer_a_jouer = True

while continuer_a_jouer:

    nombre_mystere = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre_min_actuel = NOMBRE_MIN
    nombre_max_actuel = NOMBRE_MAX
    start_ts = time.time() # retourne le nombre de secondes écoulées depuis le January 1, 1970 à minuit
    temps_restant = MAX_SECONDES

    nombre_choisi = -1
    nb_vies = nb_vies_select

    # Tant qu'il n'a pas été deviné et qu'il reste des vies
    while nombre_choisi != nombre_mystere and nb_vies > 0 and temps_restant > 0:

        temps_restant = round(MAX_SECONDES - (time.time() - start_ts), 1)

        # Demander un nombre
        nombre_choisi_str = input(
            f'{nb_vies}❤️ {temps_restant}⏲️ | Entrer un nombre entre {nombre_min_actuel} et {nombre_max_actuel}: ')

        # Le text contient un nombre valide?
        if not nombre_choisi_str.isdigit():
            print(f'{nombre_choisi_str} n\'est pas un nombre valable.\n')
            continue

        nombre_choisi = int(nombre_choisi_str)

        # Est-ce que le nonbre est dans la plage demandée?
        if not nombre_min_actuel <= nombre_choisi <= nombre_max_actuel:
            print(f'{nombre_choisi} n\'est pas entre {nombre_min_actuel} et {nombre_max_actuel}.\n')
            continue

        # Dire si il est > ou <
        if nombre_choisi < nombre_mystere:
            nombre_min_actuel = nombre_choisi + 1
            print('Le nombre mystère est plus grand\n')
            nb_vies -= 1

        elif nombre_choisi > nombre_mystere:
            nombre_max_actuel = nombre_choisi - 1
            print('Le nombre mystère est plus petit\n')
            nb_vies -= 1

    # Gagné ou perdu?
    if nb_vies and temps_restant >0:
        print('\nBravo tu as trouvé le nombre mystère!\n')
    else:
        print(f'\nPerdu! {nb_vies}❤️ {temps_restant}⏲️\n')

    # veut-il recommencer ?
    reponse_par_oui_ou_non = None
    while reponse_par_oui_ou_non not in ("oui", "non"):
        reponse_par_oui_ou_non = input('Voulez-vous recommencer une partie ?\n("oui"/"non" ): ')

    if reponse_par_oui_ou_non != "oui":
        break

print('\nAu revoir!')
