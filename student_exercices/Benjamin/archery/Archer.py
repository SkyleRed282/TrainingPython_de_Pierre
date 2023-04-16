from student_exercices.Benjamin.archery.Buyable import Buyable


class Archer:

    def __init__(self, money: float, name: str):
        self.money = money
        self.name = name
        self.quiver = None
        self.bow = None
        self.inventory = {}

    def buy(self, buyable: Buyable, amount: int):
        total_price = buyable.price * amount

        # if enough money
        if self.money >= total_price:
            self.money -= total_price
            self.inventory[str(buyable)] = self.inventory.get(str(buyable), 0) + amount
        else:
            # if NOT enough money
            print(f'Total price: {total_price} is bigger then your money: {self.money}')

    def __str__(self):
        detail = f'{self.name} inventory:\n'
        if self.inventory:
            for key, value in self.inventory.items():
                detail += f' - {key} x{value}\n'
        else:
            detail += ' - Empty inventory'
        return detail
