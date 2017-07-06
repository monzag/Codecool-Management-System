class Assigment:

    # all ssigments ever created and match with student
    list_of_assigments = []

    def __init__(self, login, name, add_date, deadline, max_grade):
        self.name = name
        self.owner = login
        self.status = 'undone'
        self.add_date = creation_date
        self.deadline = deadline
        self.submit_date = 'not submitted'
        self.grade = 0
        self.max_grade = max_grade

        Assigment.list_of_assigments.append(self)

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
    def get_assigments_from_file(cls, file_name):
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
            cls(name, owner, status, add_date, deadline, submit_date, grade, max_grade)