import os
from models.codecooler import Codecooler
from models.assignment import Assignment
from models.attendance import Attendance


class Student(Codecooler):

    list_of_students = []

    def __init__(self, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)

    @classmethod
    def get_codecoolers_from_file(cls, file_name):
        """
        Creates objects with data from splitted list.

        Returns:
            None
        """

        splitted_data_list = cls.load_data_from_file(file_name)

        for element in splitted_data_list:
            name, surname, login, password, mail = element
            cls(name, surname, login, password, mail)

    def get_attendance(self):

        attendances = Attendance.list_of_attendance
        total_attendance = 0
        days_count = 0

        for att in attendances:
            if att.student_login == self.login:
                total_attendance += att.today_value
                days_count += 1
        if days_count == 0:
            return 100

        return total_attendance // days_count

    @classmethod
    def save_students(cls):
        '''
        Save students data to csv file. If file not exist, create file.
        '''

        filename = 'students.csv'
        file_path = os.getcwd() + '/data/' + filename

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
            row = [student.name, student.surname, student.login, student.password, student.email]
            string_to_save.append(row)

        return '\n'.join('|'.join(row) for row in string_to_save)
