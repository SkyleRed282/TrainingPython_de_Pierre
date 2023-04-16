from student_exercices.Benjamin.archery.Archer import Archer
from student_exercices.Benjamin.archery.ArrowType import ArrowType
from student_exercices.Benjamin.archery.Bow import Bow
from student_exercices.Benjamin.archery.Quiver import Quiver
archer = Archer(1000, 'MAX MUSTERMANN')
quiver = Quiver(10, 81, 'BEARPAW Rückenköcher Back Pack Traditional')
bow = Bow(479, 0.9, 8, 'DRAKE Pathfinder Green Complete - 40-65 lbs - Compoundbogen')
arrow = ArrowType(5.60, 0.8, 'Komplettpfeil | PICEA - Holz - mit Naturfedern | 28-32 Zoll')


archer.buy(quiver, 1)
archer.buy(bow, 1)
archer.buy(arrow, 20)

print(archer)
archer.buy(bow, 1)