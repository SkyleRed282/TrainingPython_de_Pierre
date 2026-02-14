"""
Wiederholungsübung: Grundlagen von Python (Teile 0 bis 5)
Identifizieren Sie das Ergebnis für jeden Punkt oder beantworten Sie die gestellte Frage.
"""

# 1. Was ist das Ergebnis dieser Berechnung?
# 10 % 3 + 5 // 2
antwort1 = 3

# 2. Was ist der Endwert von 'x'?
x = 10
x += 5  # x = x + 5
x = x * 2
antwort2 = 30

# 3. Welchen Typ hat die Variable 'a'?
a = "123"
antwort3 = str

# 4. Was wird dieser Code anzeigen?
# 'abc' * 3
antwort4 = 'abcabcabc'

# 5. Was ist das Ergebnis dieses Vergleichs?
# 5 != 5 or 10 > 2
antwort5 = True

# 6. Identifizieren Sie den angezeigten Wert (Indizierung):
meine_liste = ['Apfel', 'Banane', 'Kirsche']
# meine_liste[1]
antwort6 = 'Banane'

# 7. Was enthält 'meine_liste' nach diesen Operationen?
meine_liste2 = [1, 2]
meine_liste2.append(3)  # [1, 2, 3]
meine_liste2.extend([4, 5])  # [1, 2, 3, 4, 5]
antwort7 = [1, 2, 3, 4, 5]

# 8. Was ist das Ergebnis dieses Zugehörigkeitstests?
# 'ba' in 'banane'
antwort8 = True

# 9. Was wird dieser bedingte Block anzeigen?
punktzahl = 85
if punktzahl >= 90:
    ergebnis = "A"
elif punktzahl >= 80:
    ergebnis = "B"
else:
    ergebnis = "C"
antwort9 = "B"

# 10. Welche Funktion ermöglicht es, eine Zeichenkette in eine Ganzzahl umzuwandeln?
# (Geben Sie den Namen der Funktion als String ein, z.B. "print")
antwort10 = 'int' # int('123') => 123 / str(123) => '123' / float('3.4') => 3.4

# --- TESTS ---
print("\n=== ÜBUNGSERGEBNISSE ===")

# Korrekte Antworten berechnen
korrekt1 = 10 % 3 + 5 // 2
korrekt2 = 30
korrekt3 = type("123")
korrekt4 = 'abc' * 3
korrekt5 = 5 != 5 or 10 > 2
korrekt6 = 'Banane'
korrekt7 = [1, 2, 3, 4, 5]
korrekt8 = 'ba' in 'banane'
korrekt9 = "B"
korrekt10 = "int"

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
