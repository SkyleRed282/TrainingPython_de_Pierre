from typing import overload

from personne import Personne

class Entraineur(Personne):
    def __init__(self, nom, age, diplome):
        # Point : Cette classe servait d'exemple, mais pour l'exercice
        # l'élève doit maintenant l'implémenter lui-même ou elle doit échouer au test d'héritage
        super().__init__(self, nom, age)
        self.diplome = diplome

    @overload
    def __str__(self):
        return f"Entraineur {self.nom} ({self.age} ans) - {self.diplome}"
