import tkinter

class TeamTextArea(tkinter.Text):
    def __init__(self, master, label_text):
        # Étape 4 : Créer un Frame pour grouper le Label et le Text
        self.frame = None # À compléter : tkinter.Frame(master)
        # self.frame.pack(side=tkinter.LEFT, padx=10, pady=10)
        
        # Étape 5 : Ajouter un Label au dessus de la zone de texte
        self.label = None # À compléter : tkinter.Label(self.frame, text=label_text)
        # self.label.pack()
        
        # Étape 6 : Initialiser la zone de texte (super().__init__) et l'afficher
        # super().__init__(self.frame, width=20, height=10)
        # self.pack()
        pass
