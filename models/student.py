from models.codecooler import Codecooler


class Student(Codecooler):

    list_of_students = []

    def __init__(self, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)
        '''self.attendance = attendance
        self.assignments_list = assignments.list'''

    @classmethod
    def load_students_from_file(self):
        '''
        Read students data from csv file.
        Raise error if file not exist.

        Returns:
            splitted - list of lists
        '''

        filename = 'students.csv'
        if not os.path.exists(filename):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(filename, 'r') as csvfile:
                read_data = csvfile.readlines()
                splitted = [line.replace('\n', '').split('|') for line in read_data]

        return splitted

    '''def save_data_to_file(self, list_to_save):

        Save students data to csv file. If file not exist, create file.


        filename = 'students.csv'
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(list_to_save)'''
