from Bases.Theory.Classes.School.school import School
from Bases.Theory.Classes.School.student import Student

if __name__ == '__main__':
    school_1 = School(name='Montreux School')

    s1 = Student('Pierre', 'Anken')
    s2 = Student('Iman', 'Julaidan')

    school_1.register_student(s1)
    school_1.register_student(s2)

    school_1.build_class_room('A100')
    school_1.build_class_room('A200')


