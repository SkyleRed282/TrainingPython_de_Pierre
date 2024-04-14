from datetime import datetime, timedelta

from evenement import Evenement
from calendrier import Calendrier

if __name__ == '__main__':

    evenement1 = Evenement(datetime.strptime('12/04/2021 00h00','%d/%m/%Y %Hh%M'), timedelta(hours=2),'Exercise')
    evenement2 = Evenement( datetime.strptime('12/04/2021,00h00', '%d/%m/%Y,%Hh%M'), timedelta(hours=3), 'TP')
    print(evenement1 < evenement2)

    # Test final
    e1 = Evenement(datetime.now(), timedelta(hours=2),'cours')
    e2 = Evenement(datetime.strptime('12/04/2020, 14h50', '%d/%m/%Y, %Hh%M'), timedelta(hours=2), 'TP')
    print(e1)
    print(e2)
    c = Calendrier([e1, e2])
    print([e1, e2])
    print(c.liste_evenements(datetime.strptime('12/04/2020', '%d/%m/%Y'), datetime.strptime('15/04/2020 15h50', '%d/%m/%Y %Hh%M')))