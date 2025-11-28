# Ce script va faire des générations de "donjons" en caractères spéciaux

# 1) On demande à l'utilisateur s'il veut générer un donjon

generer_ou_pas = None
while generer_ou_pas not in ("oui", "non") :
    generer_ou_pas = input('Voulez-vous générer un donjon ?\n(répondez par "oui" ou "non") : ')

    if generer_ou_pas not in ("oui", "non"):
        print(f'{generer_ou_pas} n\'est pas une réponse valable.\n')

# 2) exécuter la suite du script selon le choix de l'utilisateur

if generer_ou_pas == "oui" :


else:
# demander à l'utilisateur s'il veut clean les fichiers et arrêter le script ou simplement arrêter le script
    clean_les_files_ou_arreter_le_script = None

    while clean_les_files_ou_arreter_le_script not in ("nettoyer et arrêter", "arrêter"):
        clean_les_files_ou_arreter_le_script = input('Voulez-vous nettoyer les fichiers et arrêter le script ou simplement arrêter le script ?\n(répondez par "nettoyer et arrêter" ou "arrêter") : ')

        if clean_les_files_ou_arreter_le_script not in ("nettoyer et arrêter", "arrêter"):
            print(f'{clean_les_files_ou_arreter_le_script} n\'est pas une réponse valable.\n')
