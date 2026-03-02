"""
Wiederholungsübung 5: Funktionen (Kapitel 0 bis 8)
Identifizieren Sie das Ergebnis für jeden Punkt oder beantworten Sie die gestellte Frage.
Vervollständigen Sie die Variablen 'antwort1' bis 'antwort10'.
"""

# 1. Welches Schlüsselwort wird verwendet, um eine Funktion in Python zu definieren?
# (Antworten Sie mit einer Zeichenkette)
antwort1 = 'def'


# 2. Was wird durch diesen Code ausgegeben?
def begruessen():
    print("Hallo")


# begrüßen()
antwort2 = "Hallo"


# 3. Welchen Wert hat 'ergebnis'?
def addition(a, b):
    return a + b


ergebnis = addition(3, 5)
antwort3 = 8


# 4. Was gibt eine Funktion zurück, die keine 'return'-Anweisung enthält?
# (Antworten Sie mit dem speziellen Python-Typ, z.B. None, True, False...)
def nichts_tun():
    pass


wert = nichts_tun()
antwort4 = None


# 5. Was ist das Ergebnis dieses Aufrufs?
def verdoppeln(n):
    return n * 2


# verdoppeln(10)
antwort5 = 20


# 6. Welchen Wert hat 'x' am Ende?
def quadrat(nbr):
    return nbr * nbr

x = quadrat(quadrat(2))
antwort6 = 16


# 7. Was wird dieser Code ausgeben?
def vorstellung(name="Unbekannt"):
    return "Hallo " + name

vorstellung()
antwort7 = "Hallo Unbekannt"


# 8. Was ist das Ergebnis dieses Aufrufs mit einem benannten Parameter?
def subtraktion(a, b):
    return a - b


# subtraktion(b=10, a=25)
antwort8 = 15

# 9. Wie nennt man die Variablen 'x' und 'y' in 'def meine_funktion(x, y):'?
# A) Argumente
# B) Parameter
# C) Ausgaben
# (Antworten Sie mit dem Buchstaben A, B oder C)
antwort9 = 'B'


# 10. Was ist der Endwert von 'total'?
def eins_addieren(n):
    return n + 1


total = 0
for _ in range(3): # [0,1,2]
    total = eins_addieren(total)

antwort10 = 3

# --- TESTS ---
# Diese Sektion nicht ändern! Sie dient zur Überprüfung Ihrer Antworten.
if __name__ == "__main__":
    print("\n=== ÜBUNGSERGEBNISSE 5 (Funktionen) ===")

    # Erwartete Antworten
    korrekt1 = "def"
    korrekt2 = "Hallo"
    korrekt3 = 8
    korrekt4 = None
    korrekt5 = 20
    korrekt6 = 16
    korrekt7 = "Hallo Unbekannt"
    korrekt8 = 15
    korrekt9 = "B"
    korrekt10 = 3

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
