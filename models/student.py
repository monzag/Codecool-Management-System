import os

from models.codecooler import Codecooler
from models.assignment import Assignment


class Student(Codecooler):

    list_of_students = []

    def __init__(self, attendance, days_passed, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)
        self.attendance = attendance
        self.days_passed = days_passed
        self.assignments_list = self.get_assignment_list()

    @classmethod
    def get_codecoolers_from_file(cls, file_name):
        """
        Creates objects with data from splitted list.

        Returns:
                None
        """

        splitted_data_list = cls.load_data_from_file(file_name)

        for element in splitted_data_list:
            name, surname, login, password, mail, attendance, days_passed = element
            attendance = int(attendance)
            days_passed = int(days_passed)
            cls(attendance, days_passed, name, surname, login, password, mail)

    def get_assignment_list(self):
        '''
        Add Assignment objects to list if assignment's owner equal to Student login. 

        Returns:
            assignment_list - list with Assignment obj.
        '''

        assignment_list = []
        for assignment in Assignment.list_of_assignments:
            if assignment.owner == self.login:
                assignment_list.append(assignment)

        return assignment_list

    @classmethod
    def save_students(cls):
        '''
        Save students data to csv file. If file not exist, create file.
        '''

        filename = 'students.csv'
        file_path = os.getcwd() + '/data/' + filename

        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(file_path, 'w') as csvfile:
                csvfile.write(cls.data_to_save())

    @classmethod
    def data_to_save(cls):
        '''
        Unpack attributes of all Students, each to row list and append it to string_to_save list'
        Change lists to string.

        Returns:
            string
        '''

        string_to_save = []
        for student in cls.list_of_students:
            row = [student.name, student.surname, student.login, student.password, student.email, str(student.attendance), str(student.days_passed)]
            string_to_save.append(row)

        print(string_to_save)
        return '\n'.join('|'.join(row) for row in string_to_save)
