from Bases.Theory.DemoClasses.Heritage.Animal import Animal


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    @staticmethod
    def cry():
        print('Miao')
