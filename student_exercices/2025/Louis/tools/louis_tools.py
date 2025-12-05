import os

def rmtree(path: str) -> tuple[int, int]:
    deleted_files, deleted_folders = 0, 0

    print(f'Processing path: {path}')

    # Lister le contenu du dossier en cours
    for elem in os.listdir(path):

        elem_path = os.path.join(path, elem)

        # Pour chaque dossier appeler la fonction sur le dossier
        if os.path.isdir(elem_path):
            rmtree(elem_path)

        # Supprimer chaque fichier

    return deleted_files, deleted_folders
