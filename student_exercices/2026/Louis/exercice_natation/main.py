"""
EXERCICE : GESTION D'UNE PISCINE (POO)
Difficulté : Débutant - 10 étapes progressives

OBJECTIF : Implémenter les classes Nageur, LigneDeNage, Bassin et Piscine.
L'exercice se fait en complétant les fichiers correspondants (nageur.py, ligne_de_nage.py, bassin.py, piscine.py).

CONSIGNES :
1.  Classe Nageur : Ajouter un constructeur avec 'nom' (str) et 'temp_min' (int/float).
    - Si 'nom' est None ou n'est pas une chaîne, lever une ValueError.
2.  Classe Nageur : Ajouter la méthode __str__ pour afficher "Nageur [nom] (Min: [temp_min]°C)".
3.  Classe LigneDeNage : Ajouter un constructeur avec 'numero' (int) et une liste vide 'nageurs'.
4.  Classe LigneDeNage : Ajouter la méthode 'ajouter_nageur(nageur)' :
    - Vérifier que 'nageur' est bien une instance de la classe Nageur (sinon ne rien faire).
    - Ajouter le nageur seulement si la ligne contient moins de 2 personnes.
5.  Classe LigneDeNage : Ajouter la méthode __len__ pour obtenir le nombre de nageurs dans la ligne.
6.  Classe Bassin : Ajouter un constructeur avec 'nom', 'temperature' et une liste vide 'lignes'.
7.  Classe Bassin : Ajouter la méthode 'ajouter_ligne(ligne)' :
    - Vérifier que 'ligne' est bien une instance de LigneDeNage.
8.  Classe Piscine : Ajouter un constructeur avec 'nom', l'état 'ouverte' (False par défaut) et une liste vide 'bassins'.
9.  Classe Piscine : Ajouter la méthode 'ouvrir()' pour passer l'état à True.
10. Classe Piscine : Ajouter la méthode 'entrer(nageur, bassin)' :
    - Vérifier que 'nageur' est un Nageur et 'bassin' est un Bassin (sinon retourner False).
    - Le nageur ne peut entrer que si la piscine est ouverte.
    - Le nageur refuse d'entrer si la température du bassin est inférieure à sa 'temp_min'.
    - Le nageur ne peut entrer que s'il y a une place libre dans l'une des lignes du bassin.
    - Si le nageur entre, il doit être ajouté à la première ligne disponible du bassin.
    - Retourner True si le nageur a pu entrer, False sinon.

LANCEZ LE FICHIER POUR VÉRIFIER VOS RÉPONSES.
"""

from nageur import Nageur
from ligne_de_nage import LigneDeNage
from bassin import Bassin
from piscine import Piscine

def tester_exercice():
    points = 0
    print("=== VÉRIFICATION DE L'EXERCICE NATATION ===\n")

    # 1. Test Nageur __init__
    try:
        n1 = Nageur("Jean", 25)
        n2 = Nageur("Alice", 28)
        
        # Test mauvais types / null
        error_caught = False
        try:
            Nageur(None, 20)
        except ValueError:
            error_caught = True
            
        if n1.nom == "Jean" and n1.temp_min == 25 and error_caught:
            print("Point 1 (Init Nageur) : OK")
            points += 1
        else:
            if not error_caught:
                print("Point 1 (Init Nageur) : ERREUR (Le constructeur doit lever ValueError si nom est None)")
            else:
                print("Point 1 (Init Nageur) : ERREUR (Attributs mal nommés)")
    except Exception as e:
        print(f"Point 1 (Init Nageur) : ERREUR ({e})")

    # 2. Test Nageur __str__
    try:
        if str(n1) == "Nageur Jean (Min: 25°C)":
            print("Point 2 (Str Nageur) : OK")
            points += 1
        else:
            print(f"Point 2 (Str Nageur) : ERREUR (Attendu 'Nageur Jean (Min: 25°C)', reçu '{str(n1)}')")
    except Exception as e:
        print(f"Point 2 (Str Nageur) : ERREUR ({e})")

    # 3. Test LigneDeNage __init__
    try:
        l1 = LigneDeNage(1)
        if l1.numero == 1 and isinstance(l1.nageurs, list):
            print("Point 3 (Init Ligne) : OK")
            points += 1
        else:
            print("Point 3 (Init Ligne) : ERREUR (Attributs mal nommés ou liste manquante)")
    except Exception as e:
        print(f"Point 3 (Init Ligne) : ERREUR ({e})")

    # 4. Test ajouter_nageur (max 2)
    try:
        l1.ajouter_nageur(n1)
        l1.ajouter_nageur(n2)
        l1.ajouter_nageur(Nageur("Trop", 20))
        l1.ajouter_nageur("Pas un nageur") # Test type incorrect
        
        if len(l1.nageurs) == 2 and n1 in l1.nageurs and n2 in l1.nageurs:
            print("Point 4 (Ajout Nageur/Limite) : OK")
            points += 1
        else:
            print(f"Point 4 (Ajout Nageur/Limite) : ERREUR (La limite de 2 nageurs n'est pas respectée ou l'ajout de mauvais type a réussi. Taille: {len(l1.nageurs)})")
    except Exception as e:
        print(f"Point 4 (Ajout Nageur/Limite) : ERREUR ({e})")

    # 5. Test LigneDeNage __len__
    try:
        if len(l1) == 2:
            print("Point 5 (Len Ligne) : OK")
            points += 1
        else:
            print("Point 5 (Len Ligne) : ERREUR (Doit retourner le nombre de nageurs)")
    except Exception as e:
        print(f"Point 5 (Len Ligne) : ERREUR ({e})")

    # 6. Test Bassin __init__
    try:
        b1 = Bassin("Olympique", 27)
        if b1.nom == "Olympique" and b1.temperature == 27 and isinstance(b1.lignes, list):
            print("Point 6 (Init Bassin) : OK")
            points += 1
        else:
            print("Point 6 (Init Bassin) : ERREUR (Attributs mal nommés ou liste manquante)")
    except Exception as e:
        print(f"Point 6 (Init Bassin) : ERREUR ({e})")

    # 7. Test ajouter_ligne
    try:
        b1.ajouter_ligne(l1)
        b1.ajouter_ligne("Pas une ligne") # Test type incorrect
        if l1 in b1.lignes and len(b1.lignes) == 1:
            print("Point 7 (Ajout Ligne) : OK")
            points += 1
        else:
            print("Point 7 (Ajout Ligne) : ERREUR (La ligne n'a pas été ajoutée ou un mauvais type a été accepté)")
    except Exception as e:
        print(f"Point 7 (Ajout Ligne) : ERREUR ({e})")

    # 8. Test Piscine __init__
    try:
        p = Piscine("Aqualand")
        if p.nom == "Aqualand" and p.ouverte == False and isinstance(p.bassins, list):
            print("Point 8 (Init Piscine) : OK")
            points += 1
        else:
            print("Point 8 (Init Piscine) : ERREUR (Attributs mal nommés ou état initial incorrect)")
    except Exception as e:
        print(f"Point 8 (Init Piscine) : ERREUR ({e})")

    # 9. Test ouvrir
    try:
        p.ouvrir()
        if p.ouverte == True:
            print("Point 9 (Ouvrir Piscine) : OK")
            points += 1
        else:
            print("Point 9 (Ouvrir Piscine) : ERREUR (L'état n'est pas passé à True)")
    except Exception as e:
        print(f"Point 9 (Ouvrir Piscine) : ERREUR ({e})")

    # 10. Test entrer (Logique complète)
    try:
        p_close = Piscine("Fermée")
        b_froid = Bassin("Glace", 10)
        l_vide = LigneDeNage(2)
        b_froid.ajouter_ligne(l_vide)
        p_close.bassins.append(b_froid) # On force l'ajout pour le test
        
        # Cas 1 : Piscine fermée
        res1 = p_close.entrer(n1, b_froid)
        
        # Cas 2 : Trop froid
        p_close.ouvrir()
        res2 = p_close.entrer(n1, b_froid) # Jean veut 25°C, Bassin est à 10°C
        
        # Cas 3 : OK
        b_chaud = Bassin("Chaud", 30)
        l_ok = LigneDeNage(3)
        b_chaud.ajouter_ligne(l_ok)
        p.bassins.append(b_chaud)
        res3 = p.entrer(n1, b_chaud)
        
        # Cas 4 : Plus de place
        l_pleine = LigneDeNage(4)
        l_pleine.ajouter_nageur(Nageur("A", 20))
        l_pleine.ajouter_nageur(Nageur("B", 20))
        b_plein = Bassin("Plein", 30)
        b_plein.ajouter_ligne(l_pleine)
        p.bassins.append(b_plein)
        res4 = p.entrer(n2, b_plein) # Alice ne peut pas entrer
        
        # Cas 5 : Mauvais types
        res5 = p.entrer("Jean", b_chaud)
        res6 = p.entrer(n1, "Bassin chaud")
        
        # Vérification ajout physique
        l_physique = LigneDeNage(5)
        b_physique = Bassin("Physique", 30)
        b_physique.ajouter_ligne(l_physique)
        p.bassins.append(b_physique)
        n3 = Nageur("Bob", 20)
        p.entrer(n3, b_physique)
        res7 = n3 in l_physique.nageurs

        if res1 == False and res2 == False and res3 == True and res4 == False and res5 == False and res6 == False and res7 == True:
            print("Point 10 (Logique Entrer) : OK")
            points += 1
        else:
            print(f"Point 10 (Logique Entrer) : ERREUR (Un des cas n'a pas fonctionné. R1:{res1}, R2:{res2}, R3:{res3}, R4:{res4}, R5:{res5}, R6:{res6}, R7:{res7})")
            
    except Exception as e:
        print(f"Point 10 (Logique Entrer) : ERREUR ({e})")

    print(f"\nSCORE FINAL : {points}/10")
    if points == 10:
        print("FÉLICITATIONS ! Tu es le roi de la piscine.")

if __name__ == "__main__":
    tester_exercice()
