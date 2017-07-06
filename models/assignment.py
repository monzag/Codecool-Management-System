import os


class Assignment:

    # all ssigments ever created and match with student
    list_of_assignments = []

    def __init__(self, login, name, add_date, deadline, max_grade, grade=0, status='undone', submit_date='not submitted'):
        self.name = name
        self.owner = login
        self.status = status
        self.add_date = add_date
        self.deadline = deadline
        self.submit_date = submit_date
        self.grade = grade
        self.max_grade = max_grade

        Assignment.list_of_assignments.append(self)

    @staticmethod
    def load_data_from_file(file_name):
        """
        Loads Codecooler obj. instance information from csv file, splits them, and
        creates a list.

        Return:
            list: list with Codecooler obj. instance data
        """

        file_path = os.getcwd() + '/data/' + file_name
        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such file")
        else:
            with open(file_path, 'r') as csvfile:
                read_data = csvfile.readlines()
                splitted_data_list = [line.replace('\n', '').split('|') for line in read_data]

        return splitted_data_list

    @classmethod
    def get_assignments_from_file(cls, file_name):
        """
        Creates objects with data from splitted list.

        Returns:
            None
        """
        splitted_data_list = cls.load_data_from_file(file_name)

        for element in splitted_data_list:
            name, owner, status, add_date, deadline, submit_date, grade, max_grade = element
            grade = int(grade)
            max_grade = int(max_grade)
            cls(owner, name, add_date, deadline, max_grade, grade, status, submit_date)

    @classmethod
    def save_assignments_to_file(cls):
        '''
        '''
        file_path = os.getcwd() + '/data/assignments.csv'
        with open() as data:
            data.write(cls.csv_string)

    @property
    def csv_string(self):
        csv_string = []
        for assignment in self.list_of_assignments:
            row = [assignment.name, assignment.owner, assignment.status, assignment.add_date, 
                   assignment.deadline, assignment.submit_date, str(assignment.grade), str(assignment.max_grade)]

            csv_string.append(row)

        return = '\n'.join('|'.join(row) for row in csv_string)