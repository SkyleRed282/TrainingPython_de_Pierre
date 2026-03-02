import tkinter
from team_text_area import TeamTextArea
from button_add_footballer import ButtonAddFootballer


class InputFrame(tkinter.Frame):

    def __init__(self, master):
        super().__init__(master)
        # Étape 2 : Ajouter un Label et un Entry dans ce Frame
        self.label = tkinter.Label(
            master=self,
            text='Nom du footballeur :',
        )
        self.label.pack(padx=10, pady=10)

        name_entry_var = tkinter.StringVar()
        self.entry = tkinter.Entry(
            master=self,
            textvariable=name_entry_var,
            width=30
        )
        self.entry.pack(padx=10, pady=10)
        self.configure(bg="#99e699")


class TeamFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Étape 7 : Instancier les deux TeamTextArea dans ce Frame
        self.team1_area = TeamTextArea(self, 'Equipe 1')
        self.team2_area = TeamTextArea(self, 'Equipe 2')

        self.configure(bg="#ff6666")

class ActionButtonsFrame(tkinter.Frame):
    def __init__(self, master, team1_area, team2_area, entry_field):
        super().__init__(master)
        # Étape 8 : Instancier les deux ButtonAddFootballer dans ce Frame
        self.btn_add_team1 = ButtonAddFootballer(
            self,
            "Ajouter à l'Equipe 1",
            team1_area,
            entry_field
        )
        self.btn_add_team1.pack(side=tkinter.LEFT, padx=5, pady=10)

        self.btn_add_team2 = ButtonAddFootballer(
            self,
            "Ajouter à l'Equipe 2",
            team2_area,
            entry_field
        )
        self.btn_add_team2.pack(side=tkinter.LEFT, padx=5, pady=10)

        self.configure(bg="#ffc299")


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # Étape 1 : Configurer le titre et la taille (500x500)
        self.title("Gestion de Footballeurs")
        self.geometry("500x500")

        # Étape 2 : Instancier InputFrame
        self.input_frame = InputFrame(self)
        self.input_frame.pack()

        # Étape 3 : Instancier TeamFrame
        self.team_frame = TeamFrame(self)
        self.team_frame.pack(padx=10, pady=10)

        # Étape 8 : Instancier ActionButtonsFrame
        self.buttons_frame = ActionButtonsFrame(
            self,
            self.team_frame.team1_area,
            self.team_frame.team2_area,
            self.input_frame.entry
        )
        self.buttons_frame.pack(pady=10)
        self.configure(bg="#80bfff")

    def run(self):
        # Étape 1 (suite) : Lancer la boucle principale
        self.mainloop()
