import os
import csv
import datetime


class Attendance:

    list_of_attendance = []

    def __init__(self, student_login, date, today_value):
        '''
        Constructs the Attendance object.

        Attrs:
            student_login (str) - login attribute of Student object
            date (Datetime obj) - date of attendance checked
            today_value (int) - 100 for present, 80 for late, 0 for absent
        '''

        self.student_login = student_login
        self.date = date
        self.today_value = int(today_value)
        Attendance.list_of_attendance.append(self)

    @staticmethod
    def load_data_from_file(filename):
        '''
        With file name provided creates list of Attendance object instances,
        stored in this file. It triggers init of following object, which holds
        addition to class list.

        Args:
            filename (str)

        Return:
            constructors : list of lists representing data needed to create objects
        '''
        file_path = os.getcwd() + '/data/' + filename

        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(file_path, 'r') as csvfile:
                read_data = csvfile.readlines()
                splitted_data_list = [line.replace('\n', '').split('|') for line in read_data]

        return splitted_data_list

    @classmethod
    def get_attendance_from_file(cls, filename):
        """
        Creates objects with data from splitted list.

        Args:
            filename (str)
        """

        splitted_data_list = cls.load_data_from_file(filename)

        for element in splitted_data_list:
            student_login, date, attendance = element
            date = cls.create_datetime(cls, date)
            cls(student_login, date, attendance)

    @staticmethod
    def create_datetime(self, date):

        year, month, day = date.split('-')
        return datetime.date(int(year), int(month), int(day))

    def save_attendance_to_file(self, filename):
        '''
        
        '''
        filepath = os.getcwd() + '/data/' + filename

        if os.path.exists(os.getcwd() + '/data/' + filename):
            with open(filepath, 'a') as csvfile:
                csvfile.write(self.data_to_save() + '\n')

        else:
            with open(filepath, 'w') as csvfile:
                csvfile.write(self.data_to_save() + '\n')

    def data_to_save(self):

        row = [self.student_login, str(self.date), str(self.today_value)]

        return '|'.join(row)

    @classmethod
    def overwrite_file(cls, filename):

        filepath = os.getcwd() + '/data/' + filename

        with open(filepath, 'w') as csvfile:
            csvfile.write(cls.data_to_overwrite())

    @classmethod
    def data_to_overwrite(cls):

        string_to_save = []
        for attendance in cls.list_of_attendance:
            row = [attendance.student_login, str(attendance.date), str(attendance.today_value)]
            string_to_save.append(row)

        if string_to_save == []:
            return ''

        string_to_save = '\n'.join('|'.join(row) for row in string_to_save) + '\n'

        return string_to_save

    def __eq__(self, other):
        return self.student_login == other.student_login and self.date == other.date
