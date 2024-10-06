from theory.oop.base.school.student import Student


students = []
for student_number in range(10):

    if student_number %2 == 0:
        new_student = Student(
            f'Firstname_{student_number}',
            f'Lastname_{student_number}',
            f'Middlename_{student_number}'

        )
    else:
        new_student = Student(
            f'Firstname_{student_number}',
            f'Lastname_{student_number}'
        )

    students.append(new_student)


students[4].middle_name = 'Fred'

for student in students:

    print(student)

