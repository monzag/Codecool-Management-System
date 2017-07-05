from models.codecooler import Codecooler
import os


class Student(Codecooler):

    list_of_students = []

    def __init__(self, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)
        '''self.attendance = attendance
        self.assignments_list = assignments.list'''

