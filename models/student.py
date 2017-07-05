from models.codecooler import Codecooler
import os


class Student(Codecooler):

    list_of_students = []

    def __init__(self, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)
        '''self.attendance = attendance
        self.assignments_list = assignments.list'''

    @classmethod
    def load_students_from_file(cls):
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
                splitted = [line.replace('\n', '').split(',') for line in read_data]

        return splitted

    @classmethod
    def get_students_from_file(cls):
        '''
        Get data all students and create each Student object (automatically append to list_of_students)
        '''

        data_all_students = Student.load_students_from_file()
        for student in data_all_students:
            name, surname, login, password, email = student[0], student[1], student[2], student[3], student[4]
            Student.create_new_student(name, surname, login, password, email)

    @classmethod
    def create_new_student(cls, name, surname, login, password, email):
        '''
        Create new object Student.

        Returns:
            new_student - obj
        '''

        new_student = Student(name, surname, login, password, email)
        return new_student

    '''def save_data_to_file(self, list_to_save):

        Save students data to csv file. If file not exist, create file.


        filename = 'students.csv'
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(list_to_save)'''
