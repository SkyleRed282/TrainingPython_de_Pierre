def generate_grid():
    """
    Hier wird das Spielfeld generiert
    :return: Es wird in einer 2 dimensionalen Liste wiedergegeben.
    """

    # [
    #   ['','',''],     Element 1 Liste 1
    #   ['','',''],     Element 2 Liste 2
    #   ['','','']      Element 3 Liste 3
    # ]

    grid = []
    for _ in range(3):  # [0,1,2]
        grid.append(['-', '-', '-'])

    return grid


def print_grid(grid):
    """
    Druckt eigentlich das aktuelle Spielfeld
    :param grid: Spielfeld 3 x 3 Liste
    :return: None (gibt nichts zurück)
    """

    #  X   X
    #  O X
    #    O O
    for linie in range(3):  # [0,1,2] mit der for werden alle linie durchgegangen
        print(*grid[linie])  # mit * werden die Elemente der Liste entpackt. ['X','O','X'] => 'X','O','X'


def grid_is_full(grid):
    """
    Prüft, ob das Spielfeld voll ist.
    :param grid: Spielfeld 3 x 3 Liste
    :return: Ist das Spielfeld voll? True/False
    """
    for linie in grid:
        for symbol in linie:
            if symbol == '-':  # Falls das Symbol ist gleich minus, ist diese noch voll.
                return False
    return True


def get_winner(grid):
    """
    Prüft, ob ein Spieler gewonnen hat.
    :param grid: Spielfeld 3 x 3 Liste
    :return: x oder o oder None / x Spieler 1 o Spieler 2 None steht für kein Spieler hat gewonnen.
    """

    # Linie
    if grid[0][0] == grid[0][1] == grid[0][2] != '-':   # != '-':  Es muss ungleich - abgeglichen werden, da sonst 3 mal - auch ein Gewinnner ist.
        return grid[0][0]  # gibt das Symbol welches in der Linie ist wieder, vom entsprechenden Gewinner.

    if grid[1][0] == grid[1][1] == grid[1][2] != '-':
        return grid[1][0]

    if grid[2][0] == grid[2][1] == grid[2][2] != '-':
        return grid[2][0]

    # Spalten
    if grid[0][0] == grid[1][0] == grid[2][0] != '-':
        return grid[0][0]

    if grid[0][1] == grid[1][1] == grid[2][1] != '-':
        return grid[0][1]

    if grid[0][2] == grid[1][2] == grid[2][2] != '-':
        return grid[0][2]

    # Diagonals
    if grid[0][2] == grid[1][1] == grid[2][0] != '-':
        return grid[0][2]

    if grid[0][0] == grid[1][1] == grid[2][2] != '-':
        return grid[0][0]


# Leeres Grid erstelle 3x3
play_grid = generate_grid()

# Benutzer 1 / Benutzer 2 / Computer 1 Wer spielt gegen wen.
# antwort = input('Ist der Zweite Spieler ein Computer? Y / N ')
# ki = antwort == "Y"

# Werte festlegen für x und o sind die werte als string
symbols = ['x', 'o']
aktueller_spieler = 0  # 0 = Spieler 1  und 1 = Spieler 2

# Bedingung der Schleife, bis ein Spieler gewonnen hat, oder das Brett (3x3) ist voll und die Bedingung für den Sieg nicht erfüllt ist.
while not grid_is_full(play_grid) and not get_winner(
        play_grid):  # not ist wieder invertiert, Hängt zusammen mit def grid_is_full(grid): / and / hier noch keiner hat gewonnen.

    # Spielfeld Drucken
    print_grid(play_grid)

    # Der aktuelle Spieler setzt sein Symbol
    print('Spieler', aktueller_spieler + 1, '[', symbols[aktueller_spieler], ']:')
    position = input('Wo wird das Symbol gesetzt ? (Linie/Spalte) Zb 3/2 ')
    linie_index = int(position[0]) - 1  # Für die Benutzer ist in der Liste
    spalte_index = int(position[2]) - 1

    # Prüfung ob das Feld bereits besetzt ist
    current_value = play_grid[linie_index][spalte_index]
    if current_value != '-':  # Wert abgeglichen, ob ein - vorhanden ist (Zelle leer) !Ungleich
        print('Position schon besetzt!')
    else:  # Falls frei wird hier weitergefahren
        # Speichern
        play_grid[linie_index][spalte_index] = symbols[
            aktueller_spieler]  # Der Wert den wir bei Positionsabfrage gesetzt haben wird nun entsprechend gespeichert.

        # Spieler Wechseln
        if aktueller_spieler == 1:
            aktueller_spieler = 0
        else:
            aktueller_spieler = 1

    # Resultat
