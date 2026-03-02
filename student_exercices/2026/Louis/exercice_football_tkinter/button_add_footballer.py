import tkinter

class ButtonAddFootballer(tkinter.Button):

    def __init__(self, master, text, team_text_area, entry_field):
        # Étape 9 : Configurer le bouton avec son texte et sa commande
        super().__init__(
            master=master,
            text=text,
            command=self.add_footballer
        )
        self.team_text_area = team_text_area
        self.entry_field = entry_field

    def add_footballer(self):
        # Étape 10 : Récupérer le nom, l'ajouter au textarea et vider le champ
        # 1. Récupérer le texte de self.entry_field
        name = self.entry_field.get()
        # 2. Si le nom n'est pas vide, l'insérer dans self.team_text_area
        if name.strip():
            self.team_text_area.insert(tkinter.END, name.strip() + "\n")

            # 3. Vider le champ de saisie
            self.entry_field.delete(0, tkinter.END)
