import os


class Codecooler:

    def __init__(self, name, surname, login, password, email):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.email = email

    @staticmethod
    def load_data_from_file(file_name):
        """
        Loads Codecooler obj. instance information from csv file, splits them, and
        creates a list.

        Return:
            list: list with Codecooler obj. instance data
        """

        file_path = os.getcwd() + '/data/' + file_name

        constructors = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as csvfile:
                file_rows = csvfile.readlines()

            constructors = [line.replace('\n', '').split('|') for line in file_rows]

        return constructors

    @classmethod
    def get_codecoolers_from_file(cls, file_name):
        """
        Creates objects with data from splitted list.

        Returns:
                None
        """
        constructors = cls.load_data_from_file(file_name)

        for constructor in constructors:
            name, surname, login, password, email = constructor

            cls(name, surname, login, password, email)
