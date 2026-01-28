# Exercice : Accès aux données dans des structures complexes
# 
# Voici une structure de données imbriquée sur 5 niveaux.
# Ton objectif est d'écrire l'expression Python permettant d'accéder à une valeur spécifique.
#
# Pour chaque question, remplace le 'None' par l'expression correspondante.
# Exemple : Si on te demande la valeur de 'id' du premier élément de 'niveau_1', 
# tu devrais répondre : structure_complexe["niveau_1"][0]["id"]
#
# Les asserts à la fin vérifieront tes réponses.

structure_complexe = {
    "niveau_1": [
        {
            "id": 1,
            "donnees": (
                {"score": 10.5, "valide": True, "tags": ["python", "code"]},
                {"score": 9.0, "valide": False, "tags": ["test"]}
            ),
            "metadata": {"auteur": "Louis", "version": 2}
        },
        {
            "id": 2,
            "donnees": (
                {"score": 15, "valide": True, "tags": []},
            ),
            "metadata": None
        }
    ],
    "actif": True,
    "nom": "Projet Alpha"
}

# Questions : Écris l'expression pour accéder à...

# 1. Le nom du projet ("Projet Alpha") ?
reponse_1 = structure_complexe["nom"]

# 2. La liste de tous les éléments du niveau 1 ?
reponse_2 = structure_complexe["niveau_1"]

# 3. Le premier dictionnaire dans "niveau_1" ?
reponse_3 = structure_complexe["niveau_1"][0]

# 4. Le tuple "donnees" du premier élément de "niveau_1" ?
reponse_4 = structure_complexe["niveau_1"][0]["donnees"]

# 5. Le score (10.5) du premier dictionnaire de "donnees" du premier élément de "niveau_1" ?
reponse_5 = structure_complexe["niveau_1"][0]["donnees"][0]["score"]

# 6. Le tag "code" (le deuxième tag) du premier dictionnaire de "donnees" ?
reponse_6 = structure_complexe["niveau_1"][0]["donnees"][0]["tags"][1]

# 7. La valeur du champ "actif" ?
reponse_7 = structure_complexe["actif"]

# 8. L'auteur dans les metadata du premier élément ?
reponse_8 = structure_complexe["niveau_1"][0]["metadata"]["auteur"]

# 9. Le score (15) du deuxième élément de "niveau_1" ?
reponse_9 = structure_complexe["niveau_1"][1]["donnees"][0]["score"]

# 10. Le deuxième dictionnaire de "donnees" du premier élément ?
reponse_10 = structure_complexe["niveau_1"][0]["donnees"][1]


#####
# Zone de vérification (ne pas modifier)
#####

if __name__ == "__main__":
    try:
        assert reponse_1 == "Projet Alpha", "Erreur Q1 : Mauvais accès au nom du projet"
        assert reponse_2 == structure_complexe["niveau_1"], "Erreur Q2 : Mauvais accès au niveau_1"
        assert reponse_3 == structure_complexe["niveau_1"][0], "Erreur Q3"
        assert reponse_4 == structure_complexe["niveau_1"][0]["donnees"], "Erreur Q4"
        assert reponse_5 == 10.5, "Erreur Q5"
        assert reponse_6 == "code", "Erreur Q6"
        assert reponse_7 is True, "Erreur Q7"
        assert reponse_8 == "Louis", "Erreur Q8"
        assert reponse_9 == 15, "Erreur Q9"
        assert reponse_10 == structure_complexe["niveau_1"][0]["donnees"][1], "Erreur Q10"
        
        print("Félicitations ! Tu as correctement accédé à toutes les valeurs.")
    except AssertionError as e:
        print(f"Oups ! {e}. Vérifie bien ton expression.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
