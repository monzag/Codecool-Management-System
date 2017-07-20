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
        With file name provaided creates list of Codecooler obj. instances,
        stored in this file. It tiggers init of fallowing object, which holds
        addition to class list.

        Paramaters:
            file_name : str

        Return:
            constructors : list of lists representing data needed to create obj.
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
        Creates Codecooler instance objs. from data stored in csv file.

        Parameters:
            file_name : str

        Returns:
            None

        Initializes:
            Codecooler obj. instances (all from file)
        """
        constructors = cls.load_data_from_file(file_name)

        for constructor in constructors:
            name, surname, login, password, email = constructor

            cls(name, surname, login, password, email)

    @classmethod
    def save_codecoolers_to_file(cls, filename, list_of_codecoolers):
        '''
        Save codecoolers data to csv file. If file not exist, create file.
        '''

        file_path = os.getcwd() + '/data/' + filename

        with open(file_path, 'w') as csvfile:
            csvfile.write(cls.data_to_save(list_of_codecoolers))

    @classmethod
    def data_to_save(cls, list_of_codecoolers):
        '''
        Unpack attributes of all codecoolers, each to row list and append it to string_to_save list'
        Change lists to string.

        Returns:
            string
        '''

        string_to_save = []
        for codecooler in list_of_codecoolers:
            row = [codecooler.name, codecooler.surname, codecooler.login, codecooler.password, codecooler.email]
            string_to_save.append(row)

        return '\n'.join('|'.join(row) for row in string_to_save)
