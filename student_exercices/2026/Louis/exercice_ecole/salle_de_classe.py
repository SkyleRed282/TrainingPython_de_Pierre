class SalleDeClasse:
    def __init__(self, nom_classe):
        # Point 4
        self.nom_classe = nom_classe
        self.eleves = []

    def ajouter_eleve(self, eleve):
        # Point 5
        self.eleves.append(eleve)

    def __len__(self):
        # Point 6
        return len(self.eleves)

    def moyenne_classe(self):
        # Point 7
        if not len(self):
            return 0

        somme_des_notes = 0
        for eleve in self.eleves:
            somme_des_notes += eleve.note

        return somme_des_notes / len(self)
