"""
Exercices sur les fonctions - Niveau 2.
Complétez les fonctions ci-dessous.
IMPORTANT : Vous devez valider les entrées (types, valeurs) dans vos fonctions pour que les tests passent.
"""


# 1. Écrire une fonction 'multiplier' qui prend deux paramètres.
# Elle doit retourner le produit si ce sont des nombres (int ou float), sinon retourner None.
def multiplier(a, b):
    if type(a) not in (int, float):
        return None

    if type(b) not in (int, float):
        return None

    return a * b


# 2. Écrire une fonction 'calculer_moyenne' qui prend une liste de nombres.
# Elle doit retourner la moyenne.
# Si l'entrée n'est pas une liste ou si elle est vide, retourner 0.
def calculer_moyenne(nombres):
    if type(nombres) is not list or not nombres:
        return 0

    return sum(nombres) / len(nombres)


# 3. Écrire une fonction 'compter_voyelles' qui prend une chaîne de caractères.
# Elle doit retourner le nombre de voyelles (a, e, i, o, u, y).
# Si l'entrée n'est pas une chaîne, retourner -1.
def compter_voyelles(texte):
    if type(texte) is not str:
        return -1

    voyelles = ("a", "e", "i", "o", "u", "y")
    compteur = 0

    for lettre in texte:
        if lettre in voyelles:
            compteur += 1
    return compteur

# 4. Écrire une fonction 'obtenir_valeur' qui prend un dictionnaire et une clé.
# Elle doit retourner la valeur associée à la clé si elle existe, sinon retourner "Clé absente".
# Valider que le premier paramètre est bien un dictionnaire.
def obtenir_valeur(dico, cle):
    if type(dico) is not dict:
        return

    if cle not in dico:
        return "Clé absente"

    return dico[cle]

# 5. Écrire une fonction 'est_majeur' qui prend un âge en paramètre.
# Elle doit retourner True si l'âge est >= 18, False sinon.
# Si l'âge est négatif ou n'est pas un nombre, retourner None.
def est_majeur(age):
    pass


if __name__ == '__main__':
    # Tests pour l'exercice 1
    try:
        assert multiplier(10, 2) == 20
        assert multiplier(2.5, 4) == 10.0
        assert multiplier("a", 2) is None
        print("Ex1 Ok")
    except AssertionError:
        print("Ex1 Échec")

    # Tests pour l'exercice 2
    try:
        assert calculer_moyenne([10, 20, 30]) == 20
        assert calculer_moyenne([]) == 0
        assert calculer_moyenne("pas une liste") == 0
        print("Ex2 Ok")
    except AssertionError:
        print("Ex2 Échec")

    # Tests pour l'exercice 3
    try:
        assert compter_voyelles("bonjour") == 3
        assert compter_voyelles("PHP") == 0
        assert compter_voyelles(123) == -1
        print("Ex3 Ok")
    except AssertionError:
        print("Ex3 Échec")

    # Tests pour l'exercice 4
    try:
        mon_dico = {"nom": "Louis", "age": 20}
        assert obtenir_valeur(mon_dico, "nom") == "Louis"
        assert obtenir_valeur(mon_dico, "ville") == "Clé absente"
        assert obtenir_valeur("pas un dico", "nom") == "Clé absente"
        print("Ex4 Ok")
    except AssertionError:
        print("Ex4 Échec")

    # Tests pour l'exercice 5
    try:
        assert est_majeur(20) is True
        assert est_majeur(15) is False
        assert est_majeur(-5) is None
        assert est_majeur("vingt") is None
        print("Ex5 Ok")
    except AssertionError:
        print("Ex5 Échec")
