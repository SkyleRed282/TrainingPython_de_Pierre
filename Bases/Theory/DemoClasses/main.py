from Bases.Theory.DemoClasses.car import Car
from Bases.Theory.DemoClasses.parking import Parking

if __name__ == '__main__':

    parking1 = Parking()

    all_car = []
    for i in range(25):
        if i % 5 == 0:
            Car.set_price(Car.price+1000)
        all_car.append(Car())

    for car in all_car:
        print(car)
        parking1.park_car(car)

    del parking1
