from models.codecooler import Codecooler


class Student(Codecooler):

    list_of_students = []

    def __init__(self, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)
    
    def __str__(self):
        return '{} {}'.format(self.name, self.surname)