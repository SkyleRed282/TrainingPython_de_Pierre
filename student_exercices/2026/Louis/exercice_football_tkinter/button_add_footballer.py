import tkinter

class ButtonAddFootballer(tkinter.Button):
    def __init__(self, master, text, team_text_area, entry_field):
        # Étape 9 : Configurer le bouton avec son texte et sa commande
        # super().__init__(...)
        self.team_text_area = team_text_area
        self.entry_field = entry_field

    def add_footballer(self):
        # Étape 10 : Récupérer le nom, l'ajouter au textarea et vider le champ
        # 1. Récupérer le texte de self.entry_field
        # 2. Si le nom n'est pas vide, l'insérer dans self.team_text_area
        # 3. Vider le champ de saisie
        pass
