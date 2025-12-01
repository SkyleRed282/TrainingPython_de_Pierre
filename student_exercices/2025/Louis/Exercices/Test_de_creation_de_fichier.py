import os
import time
# Ce script va donner le nom de chaque moment de la journée par rapport à l'heure

# 1) On demande à l'utilisateur s'il veut avoir le nom de chaque moment de la journée

avoir_les_noms_ou_pas = None
while avoir_les_noms_ou_pas not in ("oui", "non") :
    avoir_les_noms_ou_pas = input('Voulez-vous avoir le nom de chaque moment de la journée ?\n(répondez par "oui" ou "non") : ')

    if avoir_les_noms_ou_pas not in ("oui", "non"):
        print(f'{avoir_les_noms_ou_pas} n\'est pas une réponse valable.\n')

# 2) exécuter la suite du script selon le choix de l'utilisateur

if avoir_les_noms_ou_pas == "oui" :
# donner le nom de chaque moment de la journée

    if not os.path.exists('Journée'):
        os.mkdir(path='Journée')

    for hours_time in range(1, 25):
        if not os.path.exists(f'Journée/{hours_time}'):
            os.mkdir(path=f'Journée/{hours_time}')
    for morning_hours in range(2, 12):
        with open(f'journée/{morning_hours}/Morning.txt', 'w'):
            pass
else:
# demander à l'utilisateur s'il veut clean les fichiers et arrêter le script ou simplement arrêter le script
    clean_les_files_ou_arreter_le_script = None

    while clean_les_files_ou_arreter_le_script not in ("nettoyer et arrêter", "arrêter"):
        clean_les_files_ou_arreter_le_script = input('Voulez-vous nettoyer les fichiers et arrêter le script ou simplement arrêter le script ?\n(répondez par "nettoyer et arrêter" ou "arrêter") : ')

        if clean_les_files_ou_arreter_le_script not in ("nettoyer et arrêter", "arrêter"):
            print(f'{clean_les_files_ou_arreter_le_script} n\'est pas une réponse valable.\n')

    if clean_les_files_ou_arreter_le_script == "nettoyer et arrêter":
        if os.path.exists('Journée'):
            for hours_time in range(1, 25):
                os.rmdir(path=f'Journée/{hours_time}')
                os.rmdir(path='journée')
        else:
            print("il a aucun fichier à nettoyer")

    else:
        print("T'avais vraiment besoin de démarrer le script ?")
        time.sleep(4)
        print("bon...")
        time.sleep(1)
        print("d'accord")