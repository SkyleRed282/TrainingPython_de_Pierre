from animal import Animal


class Dolphin(Animal):

    def cry(self):
        print(f'{self.name}: IIIIIIIII !')

    def move(self):
        print(f'{self.name}: swims in the ocean')

    def greetings(self, other_animal: Animal):
        if self == other_animal:
            print(f'Hello myself!')
        else:
            super().greetings(other_animal)
