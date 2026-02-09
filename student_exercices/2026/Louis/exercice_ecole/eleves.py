class Eleve:
    def __init__(self, nom: str, note: int):
        # Point 1
        self.nom = nom
        self.note = note

    def __str__(self):
        # Point 2
        return f"Élève : {self.nom} (Note: {self.note})"

    def __eq__(self, other):
        # Point 3
        return type(other) is Eleve and self.note == other.note
