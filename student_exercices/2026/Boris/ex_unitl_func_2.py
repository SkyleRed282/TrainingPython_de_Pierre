"""
Wiederholungsübung 6: Funktionen - Fortgeschritten (Kapitel 0 bis 8)
Identifizieren Sie das Ergebnis für jeden Punkt oder beantworten Sie die gestellte Frage.
Vervollständigen Sie die Variablen 'antwort1' bis 'antwort10'.
"""

# 1. Welchen Typ hat 'ergebnis', wenn eine Funktion mehrere Werte mit Kommas trennt?
# def test():
#     return 1, 2
# ergebnis = test()
# (Antworten Sie mit dem Namen des Typs: list, tuple, dict oder set)
antwort1 = 'tuple'


# 2. Was wird ausgegeben? (Gültigkeitsbereich/Scope)
x = 10

def veraendere_x():
    x = 5

veraendere_x()
# Welchen Wert hat x jetzt?
antwort2 = 10


# 3. Was passiert hier? (Globale Variable)
y = 10
def benutze_global():
    global y
    y = 20

benutze_global()
# Welchen Wert hat y jetzt?
antwort3 = 20


# 4. Was ist das Ergebnis dieses Aufrufs? (*args)
def summiere(*zahlen):
    return sum(zahlen)

# summiere(1, 2, 3, 4)
antwort4 = 10


# 5. Welcher Wert wird für 'name' verwendet? (Standardwerte)
def hallo(name, nachricht="Guten Tag"):
    return f"{nachricht}, {name}"

# hallo("Boris")
# Was ist das Ergebnis?
antwort5 = "Guten Tag, Boris"


# 6. Was passiert bei diesem Funktionsaufruf? (**kwargs)
def zeige_alter(**daten):
    # daten = {
    # 'name':"Boris",
    # 'alter':25
    # }
    return daten["alter"]

# zeige_alter(name="Boris", alter=25)
antwort6 = 25


# 7. Was ist der Wert von 'liste' am Ende? (Veränderliche Objekte)
def hinzufuegen(l):
    l.append(4)

meine_liste = [1, 2, 3]
hinzufuegen(meine_liste)
# antwort7 = 
antwort7 = [1, 2, 3, 4]


# 8. Wie nennt man eine anonyme Funktion in Python, die mit dem Schlüsselwort 'lambda' beginnt?
# (Antworten Sie mit dem Wort: Lambda-Funktion, Methode oder Klasse)
antwort8 = 'Lambda-Funktion'


# 9. Was ist das Ergebnis? (Funktion als Argument)
def berechne(a, b, operation):
    return operation(a, b)

def mal(x, y):
    return x * y

# berechne(5, 4, mal)
antwort9 = 20


# 10. Was ist der Wert von 'resultat'? (Verschachtelte Funktionen)
def aussen(x):
    def innen(y):
        return x + y
    return innen(10)

# resultat = aussen(5)
antwort10 = 15


# --- TESTS ---
# Diese Sektion nicht ändern! Sie dient zur Überprüfung Ihrer Antworten.
if __name__ == "__main__":
    print("\n=== ÜBUNGSERGEBNISSE 6 (Funktionen Fortgeschritten) ===")

    # Erwartete Antworten
    korrekt1 = "tuple"
    korrekt2 = 10
    korrekt3 = 20
    korrekt4 = 10
    korrekt5 = "Guten Tag, Boris"
    korrekt6 = 25
    korrekt7 = [1, 2, 3, 4]
    korrekt8 = "Lambda-Funktion"
    korrekt9 = 20
    korrekt10 = 15

    results = [
        (1, antwort1, korrekt1),
        (2, antwort2, korrekt2),
        (3, antwort3, korrekt3),
        (4, antwort4, korrekt4),
        (5, antwort5, korrekt5),
        (6, antwort6, korrekt6),
        (7, antwort7, korrekt7),
        (8, antwort8, korrekt8),
        (9, antwort9, korrekt9),
        (10, antwort10, korrekt10)
    ]

    punkte = 0
    for nr, user, real in results:
        if user == real:
            print(f"Frage {nr}: Richtig! ✅")
            punkte += 1
        else:
            if user is None:
                print(f"Frage {nr}: Noch nicht beantwortet ⏳")
            else:
                print(f"Frage {nr}: Falsch ❌")

    print(f"\nGesamtpunktzahl: {punkte}/10")
