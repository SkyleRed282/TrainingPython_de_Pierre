from typing import override


from personne import Personne

class Arbitre(Personne):

    def __init__(self, nom, age, experience):
        # Point 4 : Appeler le constructeur parent et initialiser experience
        super().__init__(nom, age)
        self.experience = experience

    @override
    def __str__(self):
        # Point 4 : Surcharger pour afficher "Arbitre [nom] ([age] ans) ([experience] ans d'XP)"
        return f"Arbitre {self.nom} ({self.age} ans) ({self.experience} ans d'XP)"
