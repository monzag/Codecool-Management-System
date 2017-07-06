import os

class Codecooler:

	def __init__(self, name, surname, login, password, email):
		self.name = name
		self.surname = surname
		self.login = login
		self.password = password
		self.email = email

def load_data_from_file():
    """
    Loads Codecooler obj. instance information from csv file, splits them, and
    creates a list.

    Return:
        list: list with Codecooler obj. instance data
    """

    file_path = os.getcwd() + '/data/' + file_name
    if not os.path.exists(file_path):
        raise FileNotFoundError("There is no such a file")

    else:
        with open(file_path, 'r') as csvfile:
            read_data = csvfile.readlines()
            splitted_data_list = [line.replace('\n', '').split('|') for line in read_data]

    return splitted_data_list

@classmethod
def get_codecoolers_from_file(file_name):
    """
    Creates objects with data from splitted list.

    Returns:
            None
    """
    splitted_data_list = load_data_from_file(file_name)

    for element in splitted_data_list:
        cls(element[0], element[1], element[2], element[3], element[4])
