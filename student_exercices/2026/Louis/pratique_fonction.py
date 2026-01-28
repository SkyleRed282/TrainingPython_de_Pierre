"""
Exercices sur les fonctions.
Complétez les fonctions ci-dessous selon les instructions.
"""


# 1. Écrire une fonction qui ne prend pas de paramètre et qui retourne la chaîne "Bonjour"
def dire_bonjour() -> str:
    # Piste d'amélioration : Ajouter un "Type Hint" pour indiquer que la fonction retourne un 'str' -> def dire_bonjour() -> str:
    return "Bonjour"


# 2. Écrire une fonction qui prend deux nombres en paramètres et retourne leur somme
def additionner(a, b):
    # Piste d'amélioration : Spécifier le type des paramètres (a: int, b: int) et ajouter une Docstring pour documenter l'usage.
    return a + b


# 3. Écrire une fonction qui prend un nombre en paramètre et retourne True s'il est pair, False sinon
def est_pair(nombre):
    # Piste d'amélioration : On peut aussi s'assurer que l'entrée est bien un nombre entier avant le calcul.
    return nombre % 2 == 0


# 4. Écrire une fonction qui prend une liste de nombres et retourne le plus grand
# Ne pas utiliser la fonction intégrée max()
def trouver_maximum(liste):
    # Piste d'amélioration : Gérer le cas où la liste est vide (if not liste: return None) pour éviter une erreur.
    elem_max = None

    for elem in liste:
        if elem_max is None or elem_max < elem :
            elem_max = elem

    return elem_max


# 5. Écrire une fonction qui prend un prénom et retourne "Bonjour [prénom] !"
def saluer_personne(prenom):
    # Piste d'amélioration : Utiliser la méthode .capitalize() sur prenom pour s'assurer qu'il commence par une majuscule.
    return f"Bonjour {prenom} !"


if __name__ == '__main__':
    # Tests pour l'exercice 1
    print("Test 1: dire_bonjour")
    assert dire_bonjour() == "Bonjour"

    # Tests pour l'exercice 2
    print("Test 2: additionner")
    assert additionner(5, 3) == 8
    assert additionner(-1, 1) == 0

    # Tests pour l'exercice 3
    print("Test 3: est_pair")
    assert est_pair(4) is True
    assert est_pair(7) is False

    # Tests pour l'exercice 4
    print("Test 4: trouver_maximum")
    assert trouver_maximum([1, 5, 3, 9, 2]) == 9
    assert trouver_maximum([-1, -5, -2]) == -1

    # Tests pour l'exercice 5
    print("Test 5: saluer_personne")
    assert saluer_personne("Louis") == "Bonjour Louis !"
