# DRY: Don't repeat yourself
from dog import Dog
from chihuahua import Chihuahua
from dolphin import Dolphin

animals = [
    Dog('Boris'),
    Chihuahua('Rex'),
    Dolphin('Flipper')
]


for animal, other_animal in zip(animals, animals[::-1]):
    animal.cry()
    animal.move()
    animal.greetings(other_animal)
    print()

