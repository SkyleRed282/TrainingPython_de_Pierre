# Choisir un nombre entre 1 et 100
import random

nombre_mystere = random.randint(1, 100)

nombre_choisi = -1

# Tant qu'il n'a pas été deviné
while nombre_choisi != nombre_mystere:

    # Demander un nombre
    nombre_choisi_str = input('Entrer un nombre entre 1 et 100: ')
    if not nombre_choisi_str.isdigit():
        print(f'{nombre_choisi_str} n\'est pas un nombre valable.')
        continue

    nombre_choisi = int(nombre_choisi_str)

    # Dire si il est > ou <
    if nombre_choisi < nombre_mystere:
        print('Le nombre mystère est plus grand')
    elif nombre_choisi > nombre_mystere:
        print('Le nombre mystère est plus petit')

print('\nBravo tu as trouvé le nombre mystère!')

# poser la question

recommencer_une_partie = 0


while recommencer_une_partie != 1 or 2:
    # veut-il recommencer ?
    réponse_par_oui_ou_non = input('\nVoulez-vous recommencer une partie ?\n(répondez par "oui" ou "non") :')

    # il dis n'importe quoi


    # il dis oui


    # il dis non


# Devoir: Après la victoire, demander à l'utilisateur, s'il veut jouer une nouvelle partie
# 1) Boucle dans un boucle => input => test si input => Y or N => forcer Y ou N (répéter la question).