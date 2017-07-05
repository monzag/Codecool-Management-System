from models.codecooler import Codecooler


class Student(Codecooler):

    list_of_students = []

    def __init__(self, assigments_list, *args):
        super().__init__(*args)
        self.total_grade = 0
        self.assigments_list = assigments_list

        Student.list_of_students.append(self)