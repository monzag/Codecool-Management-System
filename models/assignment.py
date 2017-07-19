import os

from models.solution import Solution

class Assignment:

    list_of_assignments = []

    def __init__(self, name, add_date, deadline, max_grade):
        self.name = name
        self.add_date = add_date
        self.deadline = deadline
        self.max_grade = max_grade
        self.solutions = solutions

        Assignment.list_of_assignments.append(self)

    @classmethod
    def from_folder(cls):
        '''
        '''
        file_path = os.getcwd() + '/data/assigments/'
        for file_name in os.listdir(file_path):
            if file_name.endswith('.csv'):
                cls.from_file(file_path + file_name)

    def from_file(cls, file_path):
        '''
        '''
        if os.path.exists(file_path):

            with open(file_path, 'r') as data:
                file_rows = data.read.split('$')

            name, add_date, deadline, max_grade = file_rows[0].replace('\n', '').split('|')
            solutions = cls.assign_solutions(file_rows)

            cls(name, add_date, deadline, max_grade, solutions)

    @classmethod
    def assign_solutions(cls, file_rows):
        '''
        '''
        solutions = []

        for row in file_rows[1:]:
            row = row.replace('\n', '').split('|')
            solution = Solutions.from_list(row)
            solutions.append(solution)

        return solutions

    @classmethod
    def save_assignments():
        pass
