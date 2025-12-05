import os
import time


def rmtree(path: str, level:int) -> tuple[int, int]:
    deleted_files, deleted_folders = 0, 0

    print(f'[{level}] Processing path: {path}')

    # Lister le contenu du dossier en cours
    for elem in os.listdir(path):

        elem_path =f'{path}/{elem}'
        print(f'[{level}] Processing elem_path: {elem_path}')

        # Pour chaque dossier appeler la fonction sur le dossier
        if os.path.isdir(elem_path):
            f_del,fol_del = rmtree(elem_path, level+1)
            deleted_files += f_del
            deleted_folders += fol_del

        # Supprimer chaque fichier
        else:
            print(f'[{level}] Deleting file: {elem_path}')
            os.remove(elem_path)
            deleted_files += 1

    print(f'[{level}] Deleting folder: {path}')
    os.rmdir(path)
    deleted_folders += 1

    return deleted_files, deleted_folders



DELETE_FILES = '1'

Q1 = 'Voulez-vous avoir le nom de chaque moment de la journée ?\n(répondez par "y" ou "n") : '

# Ce script va donner le nom de chaque moment de la journée par rapport à l'heure

# 1) On demande à l'utilisateur s'il veut avoir le nom de chaque moment de la journée


while (avoir_les_noms_ou_pas := input(Q1)) not in ("y", "n") :

    if avoir_les_noms_ou_pas not in ("y", "n"):
        print(f'{avoir_les_noms_ou_pas} n\'est pas une réponse valable.\n')

# 2) exécuter la suite du script selon le choix de l'utilisateur

if avoir_les_noms_ou_pas == "y" :
    # donner le nom de chaque moment de la journée

    if not os.path.exists('Journée'):
        os.mkdir(path='Journée')

    for hours_time in range(0, 24):
        if not os.path.exists(f'Journée/{hours_time}'):
            os.mkdir(path=f'Journée/{hours_time}')

    for morning_hours in range(0, 12):
        with open(f'journée/{morning_hours}/Morning.txt', 'w'):
            pass

    with open('journée/12/lunch.txt', 'w'):
        pass

    for afternoon_hours in range(13, 18):
        with open(f'journée/{afternoon_hours}/Afternoon.txt', 'w'):
            pass

    for evening_hours in range(18, 24):
        with open(f'journée/{evening_hours}/evening.txt', 'w'):
            pass
else:
# demander à l'utilisateur s'il veut clean les fichiers et arrêter le script ou simplement arrêter le script
    clean_les_files_ou_arreter_le_script = None

    while clean_les_files_ou_arreter_le_script not in (DELETE_FILES, "2"):
        clean_les_files_ou_arreter_le_script = input('Voulez-vous nettoyer les fichiers et arrêter le script ou simplement arrêter le script ?\n(répondez par [1] "nettoyer et arrêter" ou [2] "arrêter") : ')

        if clean_les_files_ou_arreter_le_script not in (DELETE_FILES, "2"):
            print(f'{clean_les_files_ou_arreter_le_script} n\'est pas une réponse valable.\n')

    if clean_les_files_ou_arreter_le_script == DELETE_FILES:
        if os.path.exists('Journée'):
            rmtree('Journée', 0)
        else:
            print("il a aucun fichier à nettoyer")

    else:
        print("T'avais vraiment besoin de démarrer le script ?")
        time.sleep(4)
        print("bon...")
        time.sleep(1)
        print("d'accord")