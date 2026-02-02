from __future__ import annotations


class Eleve:
    _compteur = 1
    _liste_eleves = []

    def __init__(self):
        self.numero = Eleve._compteur
        self.amis = []
        Eleve._compteur += 1
        Eleve._liste_eleves.append(self)

    # static method
    @staticmethod
    def tous():
        return Eleve._liste_eleves

    def __str__(self):
        return f'E{self.numero}'

    def __repr__(self):
        return self.__str__()

    # class method
    def faire_ami(self, autre_eleve: Eleve):
        if self not in autre_eleve.amis:
            autre_eleve.amis.append(self)
        else:
            print('On est déjà amis!')

        if autre_eleve not in self.amis:
            self.amis.append(autre_eleve)
        else:
            print('On est déjà amis!')


if __name__ == '__main__':

    Eleve()
    Eleve()
    Eleve()

    print(Eleve.tous())
