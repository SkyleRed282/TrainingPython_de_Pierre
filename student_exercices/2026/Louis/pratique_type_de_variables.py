# Exercice : Tri par type
#
# L'objectif est de créer une fonction nommée 'trier_par_type' qui reçoit un tuple 
# contenant 30 variables de différents types (int, str, float, bool, etc.).
#
# La fonction doit retourner un dictionnaire où :
# - Chaque clé est un type (ex: int, str, float).
# - Chaque valeur est une liste contenant les éléments du tuple correspondant à ce type.
#
# Exemple d'entrée : (1, "hello", 2.5, 2, "world")
# Exemple de sortie : {int: [1, 2], str: ["hello", "world"], float: [2.5]}


def trier_par_type(donnees: tuple) -> dict:

    mon_dict = {}
    for elem in donnees:
        type_elem = type(elem)

        if type_elem not in mon_dict:
            mon_dict[type_elem] = []
        mon_dict[type_elem].append(elem)
        
    return mon_dict



if __name__ == '__main__':
    
    # Jeu de données de 30 variables
    mes_donnees = (
        10, "Python", 3.14, True, [1, 2], 
        "Louis", 42, False, 2.718, {"a": 1},
        None, (1, 2), 0, "", 1.0, 
        True, "Test", 100, [3], {"b": 2},
        None, (3, 4), "Dernier", 0.5, False,
        -5, 99.9, "Fin", 7, 8
    )


    resultat = trier_par_type(mes_donnees)

    # Tests unitaires
    assert isinstance(resultat, dict), "La fonction doit retourner un dictionnaire"
    
    # Vérification si tous les éléments sont présents dans le dictionnaire
    if resultat is not None:
        total_elements = sum(len(liste) for liste in resultat.values())
        assert total_elements == 30, f"Le dictionnaire devrait contenir 30 éléments au total, pas {total_elements}"

        # Vérifications spécifiques basées sur 'mes_donnees'
        if int in resultat:
            assert 10 in resultat[int]
            assert 42 in resultat[int]
            assert 0 in resultat[int]
            # On compte les entiers : 10, 42, 0, 100, -5, 7, 8
            assert len(resultat[int]) == 7
        
        if str in resultat:
            assert "Python" in resultat[str]
            assert "Louis" in resultat[str]
            assert "" in resultat[str]
            # On compte les chaines : "Python", "Louis", "", "Test", "Dernier", "Fin"
            assert len(resultat[str]) == 6

        if bool in resultat:
            # Note: en Python, isinstance(True, int) est True. 
            # Mais type(True) est bool. L'élève devra faire attention.
            assert True in resultat[bool]
            assert False in resultat[bool]
            # On compte les booleens : True, False, True, False
            assert len(resultat[bool]) == 4

        if float in resultat:
            # On compte les floats : 3.14, 2.718, 1.0, 0.5, 99.9
            assert len(resultat[float]) == 5

        print("Bravo ! Tous les tests sont passés.")
    else:
        print("La fonction a retourné None. À toi de jouer !")
