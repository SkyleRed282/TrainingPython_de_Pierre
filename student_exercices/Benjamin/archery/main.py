from student_exercices.Benjamin.archery.ArrowType import ArrowType
from student_exercices.Benjamin.archery.Bow import Bow
from student_exercices.Benjamin.archery.Quiver import Quiver

bad_arrow = ArrowType(2.5, 0.5)
good_arrow = ArrowType(15, 0.95)

q1 = Quiver(20)
q1.fill(10, bad_arrow)
q1.fill(15, bad_arrow)

q1.fill(10, good_arrow)

b1 = Bow(1500, 0.9, 800)
