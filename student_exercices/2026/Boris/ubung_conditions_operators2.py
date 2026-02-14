"""
Wiederholungsübung 2: Grundlagen von Python (Teile 0 bis 5)
Identifizieren Sie das Ergebnis für jeden Punkt oder beantworten Sie die gestellte Frage.
"""

# 1. Was ist das Ergebnis dieser Berechnung?
# (10 + 2) * 3 // 4
antwort1 = 9

# 2. Welcher Buchstabe befindet sich an Index 4 in diesem String?
s = "Python"
# s[4]
antwort2 = 'o'

# 3. Was ist das Ergebnis dieses logischen Ausdrucks?
# (True and False) or (not False)
antwort3 = True

# 4. Welchen Wert hat 'y'?
y = 20
y *= 3
y -= 10
antwort4 = 50

# 5. Was ist die Länge dieser Liste?
meine_liste = [10, [20, 30], 40]  # [10]
# len(meine_liste)
antwort5 = 3

# 6. Was ist das Ergebnis dieses Vergleichs?
# 15 >= 15 and 7 < 3
antwort6 = False

# 7. Was enthält 'liste_b' am Ende?
liste_a = [1, 2]
liste_b = liste_a * 2
antwort7 = [1, 2, 1, 2]

# 8. Welcher Wert wird aus dem Dictionary abgefragt?
mein_dict = {"name": "Boris", "alter": 25}
# mein_dict.get("alter")
antwort8 = 25

# 9. Was wird dieser bedingte Block anzeigen?
x = 5
if x > 10:
    ergebnis = "Gross"
elif x > 0:
    ergebnis = "Positiv"
else:
    ergebnis = "Negativ"
antwort9 = "Positiv"

# 10. Wie lautet der Name der Funktion, mit der man die Länge eines Objekts ermittelt?
# (Geben Sie den Namen als String ein, z.B. "print")
antwort10 = 'len'

# --- TESTS ---
print("\n=== ÜBUNGSERGEBNISSE 2 ===")

# Korrekte Antworten berechnen
korrekt1 = (10 + 2) * 3 // 4
korrekt2 = "o"
korrekt3 = (True and False) or (not False)
korrekt4 = 50
korrekt5 = 3
korrekt6 = 15 >= 15 and 7 < 3
korrekt7 = [1, 2, 1, 2]
korrekt8 = 25
korrekt9 = "Positiv"
korrekt10 = "len"

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
        print(f"Frage {nr}: Falsch ❌")

print(f"\nGesamtpunktzahl: {punkte}/10")
