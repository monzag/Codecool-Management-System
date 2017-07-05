from employee import Employee


class Mentor(Employee):

    list_of_mentors = []

    def __init__(self, *args):
        super().__init__(*args)
        Mentor.list_of_mentors.append(self)


def load_data_from_file():
    """
    Loads mentors information from csv file, splits them, and
    creates a list.

    Return:
            list: list with mentors data
    """

    filename = 'mentors_data.csv'
    if not os.path.exists(filename):
        raise FileNotFoundError("There is no such a file")

    else:
        with open(filename, 'r') as csvfile:
            read_data = csvfile.readlines()
            splitted_data_list = [line.replace('\n', '').split('|') for line in read_data]

    return splitted_data_list

def create_mentors():
    """
    Creates objects with data from splitted list.

    Returns:
            None
    """
    splitted_data_list = load_data_from_file()

    for element in splitted_data_list:
        Mentor(element[0], element[1], element[2], element[3], element[4])
