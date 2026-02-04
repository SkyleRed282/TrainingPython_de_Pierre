"""
Übung: Erkennung von Variablentypen
Niveau: Anfänger
Referenz: 2_variables_types.py

Ziel: Geben Sie den Typ (int, float, str, bool, list, tuple, dict, set oder type(None)) 
für jede abgefragte Variable an.
"""

# Hier ist eine komplexe Struktur, die Daten eines Bibliotheksverwaltungssystems darstellt
data_structure = {
    "name_der_bibliothek": "Die Große Bibliothek",
    "adresse": ("Rue de la Paix", 75000, "Paris"),
    "geöffnet": True,
    "statistiken": {
        "monatliche_besucher": [1200, 1500, 1100, 1800],
        "durchschnittsbewertung": 4.8
    },
    "kategorien": {"Fiction", "Science", "Geschichte", "Kunst"},
    "inventar": [
        {
            "titel": "Der kleine Prinz",
            "autor": "Antoine de Saint-Exupéry",
            "verfügbar": True,
            "exemplare": 5
        },
        {
            "titel": "1984",
            "autor": "George Orwell",
            "verfügbar": False,
            "exemplare": 0
        }
    ],
    "kontakt": None
}

# --- DEINE ANTWORTEN HIER ---
# Ersetze für jede untenstehende Variable None durch den Namen des erwarteten Typs.
# Verwende die Python-Typnamen (z.B. int, str, list, etc.)
# Hinweis: Für den Typ von None verwende: type(None)

# 1. Was ist der Typ von: data_structure["name_der_bibliothek"]
reponse_1 = str

# 2. Was ist der Typ von: data_structure["adresse"]
reponse_2 = tuple

# 3. Was ist der Typ von: data_structure["geöffnet"]
reponse_3 = bool

# 4. Was ist der Typ von: data_structure["statistiken"]
reponse_4 = dict

# 5. Was ist der Typ von: data_structure["statistiken"]["monatliche_besucher"]
reponse_5 = list

# 6. Was ist der Typ von: data_structure["statistiken"]["durchschnittsbewertung"]
reponse_6 = float

# 7. Was ist der Typ von: data_structure["kategorien"]
reponse_7 = set

# 8. Was ist der Typ von: data_structure["inventar"]
reponse_8 = list

# 9. Was ist der Typ von: data_structure["inventar"][0]
reponse_9 = dict

# 10. Was ist der Typ von: data_structure["kontakt"]
reponse_10 = type(None)


# --- NE PAS MODIFIER LA ZONE CI-DESSOUS (TESTS) ---
def check_answers():
    expected = [
        str,
        tuple,
        bool,
        dict,
        list,
        float,
        set,
        list,
        dict,
        type(None)
    ]
    
    reponses = [
        reponse_1, reponse_2, reponse_3, reponse_4, reponse_5,
        reponse_6, reponse_7, reponse_8, reponse_9, reponse_10
    ]
    
    print("\n--- Ergebnisse der Übung ---")
    richtig = 0
    for i, (rep, exp) in enumerate(zip(reponses, expected), 1):
        if rep == exp:
            print(f"Frage {i:2}: ✅ Richtig!")
            richtig += 1
        else:
            status = "❌ Falsch" if rep is not None else "⚪ Nicht beantwortet"
            print(f"Frage {i:2}: {status}")
            
    print(f"\nEndstand: {richtig}/10")
    if richtig == 10:
        print("Herzlichen Glückwunsch! Du hast die Variablentypen perfekt verstanden.")
    elif richtig > 0:
        print("Das ist ein guter Anfang, mach weiter so!")

if __name__ == "__main__":
    check_answers()
