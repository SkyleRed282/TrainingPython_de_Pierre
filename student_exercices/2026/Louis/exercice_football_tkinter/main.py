from main_window import MainWindow

"""
EXERCICE : Gestionnaire de Footballeurs (Niveau Débutant)
Complétez les fichiers team_text_area.py, button_add_footballer.py et main_window.py
en suivant les étapes ci-dessous.

ÉTAPES DE L'EXERCICE :
1.  Fenêtre principale (MainWindow) : Configurez le titre ('Gestion de Footballeurs'),
    la géométrie ('500x400') et lancez la mainloop dans run().
    -> Test : Lancez main.py, une fenêtre vide de 500x400 doit apparaître.

2.  Saisie du nom (MainWindow) : Dans __init__, créez un Frame, un Label ('Nom du footballeur :')
    et un Entry. Utilisez pack() pour les afficher.
    -> Test : Un champ de texte avec une étiquette doit être visible en haut.

3.  Conteneur d'équipes (MainWindow) : Créez un Frame appelé teams_frame et affichez-le avec pack().
    -> Test : Pas de changement visuel immédiat, mais nécessaire pour la suite.

4.  Structure TeamTextArea (TeamTextArea) : Créez un Frame (self.frame) dans le master.
    -> Test : Importez et testez l'instanciation (interne).

5.  Label d'équipe (TeamTextArea) : Ajoutez un Label à self.frame qui affiche label_text.
    -> Test : Le texte 'Equipe 1' ou 'Equipe 2' devra apparaître plus tard.

6.  Zone de texte (TeamTextArea) : Initialisez la classe parente (super().__init__)
    avec self.frame, une largeur de 20 et une hauteur de 10. Packez la zone.
    -> Test : Les zones de texte apparaîtront à l'étape suivante.

7.  Affichage des équipes (MainWindow) : Instanciez deux TeamTextArea ('Equipe 1' et 'Equipe 2')
    dans self.teams_frame.
    -> Test : Deux colonnes avec titres et zones de texte vides doivent apparaître.

8.  Boutons (MainWindow) : Créez un Frame pour les boutons. Instanciez deux ButtonAddFootballer.
    -> Test : Deux boutons doivent apparaître en bas.

9.  Configuration Bouton (ButtonAddFootballer) : Dans __init__, appelez super().__init__
    en passant le texte et la commande self.add_footballer.
    -> Test : Cliquer sur le bouton ne doit pas faire d'erreur (mais rien ne se passe encore).

10. Logique d'ajout (ButtonAddFootballer) : Dans add_footballer, récupérez le texte du champ,
    insérez-le dans la zone de texte de l'équipe, puis videz le champ.
    -> Test : Tapez un nom, cliquez sur un bouton : le nom doit s'afficher dans la bonne liste !
"""

if __name__ == "__main__":
    app = MainWindow()
    app.run()
