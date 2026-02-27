import tkinter
from button_add_footballer import ButtonAddFootballer
from team_text_area import TeamTextArea


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # Étape 1 : Configurer le titre et la taille de la fenêtre (500x400)
        super().__init__()
        self.title('Gestion de Footballeurs')
        self.geometry('500x400')


        # Étape 2 : Créer un Frame pour la saisie et y ajouter un Label et un Entry
        self.entry_frame = None
        self.entry_name = None

        # Étape 3 : Créer un Frame pour les équipes
        self.teams_frame = None

        # Étape 7 : Instancier les deux TeamTextArea dans self.teams_frame
        self.team1_area = None
        self.team2_area = None

        # Étape 8 : Créer un Frame pour les boutons et instancier les deux ButtonAddFootballer
        self.buttons_frame = None
        self.btn_add_team1 = None
        self.btn_add_team2 = None

    def run(self):
        # Étape 1 (suite) : Lancer la boucle principale (mainloop)
        self.mainloop()
