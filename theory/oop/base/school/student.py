class Student:

    # Class constructor called by new class instance creation Student()
    def __init__(self, first_name: str, last_name: str, middle_name: str = ''):
        self.middle_name = middle_name
        self.first_name = first_name
        self.last_name = last_name

    # String representation of the class instances of Student
    def __str__(self):
        if self.middle_name :
            return f'Student: {self.first_name}\t{self.middle_name}\t{self.last_name}'
        else:
            return f'Student: {self.first_name}\t{self.last_name}'

    def __repr__(self):
        return self.__str__()
