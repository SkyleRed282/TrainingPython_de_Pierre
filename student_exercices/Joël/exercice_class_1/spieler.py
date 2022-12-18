class Spieler:

    def __init__(self, nummer: int, name: str):
        """
        Grunklasse für Spieler
        :param nummer: Spieler nummer
        :param name: Spieler name
        """
        self.nummer = nummer
        self.name = name

    def __str__(self):
        return f'Spieler {self.name}, Nummer  {self.nummer}'
