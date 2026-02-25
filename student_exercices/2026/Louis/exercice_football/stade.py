class Stade:
    def __init__(self, nom, ville, capacite):
        self.nom = nom
        self.ville = ville
        self.capacite = capacite

    def __str__(self):
        # Point 8 : Retourner "[nom] à [ville] ([capacite] places)"
        return f"{self.nom} à {self.ville} ({self.capacite} places)"
