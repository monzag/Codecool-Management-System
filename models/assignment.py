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
    def from_file(cls, file_name):
        '''
        '''
        file_path = os.getcwd() + '/data/' + file_name
        if os.path.exist(file_path):
            with open(file_path, 'r') as data:
                assigments_data = data.split('|assignment|')

                cls.for_assignment_in_file(assignements_data)

    @staticmethod
    def split_assignment_and_solutions(file_rows):
        '''
        '''
        assignment, solutions = file_rows.split('|solutions|')

        assignment = assignment.replace('\n', '').split('|')

        solutions = solutions.split('\n')
        solutions = [solution.split('|') for solution in solutions]

        return assignment, solutions

    @classmethod
    def for_assignment_in_file(cls, assignments_list):
        '''
        '''
        for assignment_data in assignments_lists:
            assignment, solutions = cls.split_assignment_and_solutions(assignment_data)

            name, add_date, deadline, max_grade = assignment
            solutions = cls.assign_solutions(solutions)

            cls(name, add_date, deadline, max_grade, solutions)

    @staticmethod
    def assign_solutions(solutions):
        '''
        '''
        solutions_list = []
        for solution in solutions:
            solution = Solution.from_list(solution)
            solutions_list.append(solution)

        return solutions
