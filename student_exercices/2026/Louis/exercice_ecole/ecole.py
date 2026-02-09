class Ecole:
    def __init__(self, nom_ecole):
        # Point 8
        self.nom_ecole = nom_ecole
        self.salles = []

    def ajouter_salle(self, salle):
        # Point 9
        self.salles.append(salle)

    def __str__(self):
        # Point 10
        total_eleves = 0
        for salle in self.salles:
            total_eleves += len(salle)

        return f"Dans l'école de {self.nom_ecole}, il y a {total_eleves}"
