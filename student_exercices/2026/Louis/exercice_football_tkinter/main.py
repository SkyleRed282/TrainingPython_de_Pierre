from main_window import MainWindow

"""
EXERCICE : Gestionnaire de Footballeurs (Niveau Débutant)
Complétez les fichiers team_text_area.py, button_add_footballer.py et main_window.py
en suivant les étapes ci-dessous.

ÉTAPES DE L'EXERCICE :
1.  Fenêtre principale (MainWindow) : Configurez le titre ('Gestion de Footballeurs'),
    la géométrie ('500x500') et lancez la mainloop dans run().
    -> Test : Lancez main.py, une fenêtre vide de 500x500 doit apparaître.

2.  Saisie du nom (InputFrame) : Dans InputFrame, ajoutez un Label ('Nom du footballeur :')
    et un Entry. Utilisez pack() pour les afficher. Instanciez InputFrame dans MainWindow.
    -> Test : Un champ de texte avec une étiquette doit être visible en haut.

3.  Conteneur d'équipes (MainWindow) : Instanciez TeamFrame dans MainWindow et affichez-le avec pack().
    -> Test : Pas de changement visuel immédiat, mais prépare l'affichage des colonnes.

4.  Structure TeamTextArea (TeamTextArea) : Créez un Frame (self.frame) dans le master.
    -> Test : Utilisé à l'étape 7.

5.  Label d'équipe (TeamTextArea) : Ajoutez un Label à self.frame qui affiche label_text.
    -> Test : Le texte 'Equipe 1' ou 'Equipe 2' devra apparaître plus tard.

6.  Zone de texte (TeamTextArea) : Initialisez la classe parente (super().__init__)
    avec self.frame, une largeur de 20 et une hauteur de 10. Packez la zone.
    -> Test : Les zones de texte apparaîtront à l'étape suivante.

7.  Affichage des équipes (TeamFrame) : Instanciez deux TeamTextArea ('Equipe 1' et 'Equipe 2')
    dans TeamFrame.
    -> Test : Deux colonnes avec titres et zones de texte vides doivent apparaître.

8.  Boutons (ActionButtonsFrame) : Instanciez deux ButtonAddFootballer dans ActionButtonsFrame.
    Instanciez ActionButtonsFrame dans MainWindow.
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
