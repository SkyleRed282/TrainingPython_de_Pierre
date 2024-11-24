class Animal:

    def __init__(self, name=str):
        self.name = name

    def cry(self):
        raise NotImplementedError('Cry not defined')

    def move(self):
        raise NotImplementedError('Move not defined')

    def greetings(self, other_animal: object):
        if isinstance(other_animal, type(self)):
            self.cry()
            print(f'{other_animal.name}')
        else:
            print(f'{other_animal.name}, what are you for an animal type ?!')