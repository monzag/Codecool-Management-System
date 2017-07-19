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
    def get_assignments_from_file(cls, file_name):
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

            solutions_list : list of Solution objs.
        '''
        solutions_list = []
        for solution in solutions:
            new_solution = Solution.from_list(solution)
            solutions_list.append(new_solution)

        return solutions_list

    @classmethod
    def save_to_file(cls, file_name):
        '''
        Save all stored Assignment objs. and it's solutions to file

        Parameters:
            file_name : str

        Returns:
            None
        '''
        file_path = os.getcwd() + '/data/' + file_name
        with open(file_path, 'w') as data:
            data.write(cls.get_file_string())

    @classmethod
    def get_file_string(cls):
        '''
        Creates string saved to file representing all stored Assignemt objs. and its Solution objs.

        Parameters:
            None

        Returns:
            str
        '''
        return '\n|assignment|\n'.join([cls.join_assignment_with_solutions(assignment) for assignment in Assignment.list_of_assignments])

    @staticmethod
    def join_solutions(solutions):
        '''
        Creates string of Solution objs. passed.

        Parameters:
            solutions : list of Solution objs.

        Returns:
            string : str
        '''
        string = '|solutions|\n'
        string += '\n'.join(map(lambda solution: solution.csv_string, solutions))

        return string

    @classmethod
    def join_assignment_with_solutions(cls, assignment):
        '''
        Create csv file string of single Assignment obj. and it's Solutions objs.

        Parameters:
            assignment : Assignemt obj.

        Returns:
            joined_string : str
        '''
        joined_string = assignment.csv_string + '\n'
        joined_string += cls.join_solutions(assignment.solutions)

        return joined_string

    @property
    def csv_string(self):
        return '{}|{}|{}|{}'.format(self.name, self.add_date, self.deadline, self.max_grade)

    @property
    def amount_of_assignments(self):
        return len(self.list_of_assignments)
