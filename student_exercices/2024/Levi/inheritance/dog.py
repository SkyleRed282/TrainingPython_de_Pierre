from animal import Animal


class Dog(Animal):

    def cry(self):
        print(f'{self.name}: Wouaff !')

    def move(self):
        print(f'{self.name}: Runs on 4 legs')

    def greetings(self, other_animal: Animal):

        if self == other_animal:
            print(f'Hello myself!')

        else:
            super().greetings(other_animal)
