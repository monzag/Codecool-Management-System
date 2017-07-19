import os

from models.solution import Solution


class Assignment:

    list_of_assignments = []

    def __init__(self, name, add_date, deadline, max_grade, solutions):
        self.name = name
        self.add_date = add_date
        self.deadline = deadline
        self.max_grade = max_grade
        self.solutions = solutions

        Assignment.list_of_assignments.append(self)

    @classmethod
    def from_file(cls, file_name):
        '''
        Given file name creates all Assignment objs stored in data.

        Parameters:
            file_name : str

        Returns:
            None

        Initializes:
            Assignment objs. (stored in classlist)
        '''
        file_path = os.getcwd() + '/data/' + file_name
        if os.path.exists(file_path):
            with open(file_path, 'r') as data:
                assignments_data = data.read().split('|assignment|')

            cls.from_assignments_in_file(assignments_data)

    @staticmethod
    def split_assignment_and_solutions(file_rows):
        '''
        Changes list of plain text representing one assignment in csv file into
        lists of attribiutes values needed to create Assignemnt and Solutions objs.

        Parameters:
            file_rows : string

        Returns:
            assignment : list of strs
            solutions : list of lists of strs
        '''
        assignment, solutions = file_rows.split('|solutions|')

        assignment = assignment.replace('\n', '').split('|')

        solutions = solutions.split('\n')
        solutions = [solution.split('|') for solution in solutions if solution != '']

        return assignment, solutions

    @classmethod
    def from_assignments_in_file(cls, assignments_list):
        '''
        For one assignements stored in data change it's csv form into a lists of
        attribiutes values and create Assignemt obj.

        Parameters:
            assignments_list : list of strs

        Returns:
            None

        Initializes:
            Assignemnt objs. (stored in classlist)
        '''
        for assignment_data in assignments_list:
            assignment, solutions = cls.split_assignment_and_solutions(assignment_data)

            name, add_date, deadline, max_grade = assignment
            solutions = cls.assign_solutions(solutions)

            cls(name, add_date, deadline, int(max_grade), solutions)

    @staticmethod
    def assign_solutions(solutions):
        '''
        Create list of Solution objs.

        Parameters:
            solutions : list of lists of str

        Returns:
            solutions_list : list of Solution objs.
        '''
        solutions_list = []
        for solution in solutions:
            new_solution = Solution.from_list(solution)
            solutions_list.append(new_solution)

        return solutions_list
