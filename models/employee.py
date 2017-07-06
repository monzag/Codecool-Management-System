from models.codecooler import Codecooler

class Employee(Codecooler):

    list_of_employees = []

    def __init__(self, *args):
        super().__init__(*args)
        Employee.list_of_employees.append(self)