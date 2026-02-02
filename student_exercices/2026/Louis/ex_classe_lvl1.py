class Ecole:

    def __init__(self, nom: str, sdc: tuple):
        self.nom = nom
        self.sdc = sdc

    def __str__(self):
        return f'Ecole {self.nom} {self.sdc}'

    # Devoir: utiliser une fonction de base de la classe Objet (__xxx__) pas encore vue.

if __name__ == '__main__':
    ecole_a = Ecole('A', ('S1', 'S2', 'S3'))
    ecole_b = Ecole('B', ('SX1', 'SX2', 'SX3'))
    print(ecole_a)
    print(ecole_b)
