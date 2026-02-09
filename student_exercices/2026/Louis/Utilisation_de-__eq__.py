class ColectionDeGamers:

    def __init__(self, nom: str, colect_de_jeux_video: tuple, age: int):
        self.nom = nom
        self.colect_de_jeux_video = colect_de_jeux_video
        self.age = age

    def __eq__(self, autre):
        if not isinstance(autre, ColectionDeGamers):
            return NotImplemented
        return self.colect_de_jeux_video == autre.colect_de_jeux_video or self.age == autre.age

    def __str__(self):
        return f'{self.nom} a {self.age}ans, voici la colection de {self.nom} : {self.colect_de_jeux_video}'



if __name__ == '__main__':
    colection_de_gamer_a = ColectionDeGamers('Chris', ("New super mario Bros.", "Celeste", "Counter-Strike 2"), 16)
    colection_de_gamer_b = ColectionDeGamers('Ben', ("New super mario Bros.", "Celeste", "Counter-Strike 2"), 15)
    colection_de_gamer_c = ColectionDeGamers('Arthur', ("Celeste", "New super mario Bros.", "Mario kart wii"), 16)
    print(colection_de_gamer_b == colection_de_gamer_c)