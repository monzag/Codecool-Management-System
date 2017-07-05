from models.codecooler import Codecooler


class Student(Codecooler):

    list_of_students = []

    def __init__(self, assigments_list, total_grade, *args):
        super().__init__(*args)
        self.total_grade = total_grade
        self.assigments_list = assigments_list

        Student.list_of_students.append(self)