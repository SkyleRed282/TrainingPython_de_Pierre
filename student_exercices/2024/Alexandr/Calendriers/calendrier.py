from datetime import datetime
from evenement import Evenement


class Calendrier:
    def __init__(self, evenements: [Evenement] = None):
        if evenements is None:
            evenements = []

        self.__evenements = evenements

    def ajouter_evenement(self, nouvel_evenement):
        self.__evenements.append(nouvel_evenement)

    def liste_evenements(self, date_debut: datetime, date_fin: datetime):
        return [e for e in self.__evenements if e.get_date() < date_fin and (e.get_date() + e.get_duree()) >date_debut]
