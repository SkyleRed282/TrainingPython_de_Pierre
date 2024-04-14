from datetime import datetime, timedelta


class Evenement:

    def __init__(self, date: datetime, duree: timedelta, nom: str):
        self.__date = date
        self.__duree = duree
        self.__nom = nom

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_duree(self):
        return self.__duree

    def set_duree(self, duree):
        self.__duree = duree

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def __str__(self):
        date_format_str = '%d/%m/%Y'
        heure_format_str = '%H:%M'

        fin_dt = self.__date + self.__duree

        s = self.__date.strftime(f'{self.__nom}, le {date_format_str}')  # Nom, le DD/MM/YYYY'

        # Si même jour
        if self.__date.date() == fin_dt.date():
            return f'{s}, de {self.__date.strftime(heure_format_str)} à {fin_dt.strftime(heure_format_str)}'

        # Si jour différent
        return f"{s} à {self.__date.strftime(heure_format_str)} , jusqu’au {fin_dt.strftime(heure_format_str)} à {fin_dt.strftime(heure_format_str)}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.__date < other.__date

    def __gt__(self, other):
        return self.__date > other.__date