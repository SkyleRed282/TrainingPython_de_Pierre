class Livre:
    
    # variable statique
    nombre_livres = 0

    def __init__(self, titre):
        self.titre = titre
        Livre.nombre_livres += 1

    @staticmethod
    def get_nombre_livres():
        return Livre.nombre_livres

    def set_titre(self, titre):
        self.titre = titre

