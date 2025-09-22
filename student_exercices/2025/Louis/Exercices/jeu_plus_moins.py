# Choisir un nombre entre 1 et 100
import random

nombre_mystere = random.randint(1, 100)

nombre_choisi = -1

# Tant qu'il n'a pas été deviné
while nombre_choisi != nombre_mystere:

    # Demander un nombre
    nombre_choisi_str = input('Entrer un nombre entre 1 et 100: ')
    if not nombre_choisi_str.isdigit():
        print(f'{nombre_choisi_str} n\'est pas un nombre valable.\n')
        continue

    nombre_choisi = int(nombre_choisi_str)

    # Dire si il est > ou <
    if nombre_choisi < nombre_mystere:
        print('Le nombre mystère est plus grand\n')
    elif nombre_choisi > nombre_mystere:
        print('Le nombre mystère est plus petit\n')

print('\nBravo tu as trouvé le nombre mystère!\n')

# poser la question

recommencer_une_partie = 0


while recommencer_une_partie != "oui" or "non":
    # veut-il recommencer ?
    reponse_par_oui_ou_non = input('Voulez-vous recommencer une partie ?\n(répondez par "oui" ou "non" lettre pour lettre) : ')
# Demander "oui" ou "non"
    if reponse_par_oui_ou_non != "oui" or "non":
        print(f'\n{reponse_par_oui_ou_non} n\'est pas lettre pour lettre "oui" ou "non" !\nveuillez recommencer\n')
        continue

    reponse_par_oui_ou_non = str(reponse_par_oui_ou_non_str)
    # il dis oui


    # il dis non


# Devoir: Après la victoire, demander à l'utilisateur, s'il veut jouer une nouvelle partie
# 1) Boucle dans un boucle => input => test si input => Y or N => forcer Y ou N (répéter la question).