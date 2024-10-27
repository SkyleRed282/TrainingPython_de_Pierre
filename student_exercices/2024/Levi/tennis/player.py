class Player:
    def __init__(self, name: str, serving_skill: float = 1):
        self.name = name
        self.serving_skill = serving_skill  # Chance of a service failure
