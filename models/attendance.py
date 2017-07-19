import os
import csv
import datetime

class Attendance:

    list_of_attendance = []

    def __init__(self, student_login, date, today_value):

        self.student_login = student_login
        self.date = date
        self.today_value = int(today_value)
        Attendance.list_of_attendance.append(self)
    @staticmethod
    def load_data_from_file(filename):

        file_path = os.getcwd() + '/data/' + filename

        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(file_path, 'r') as csvfile:
                read_data = csvfile.readlines()
                splitted_data_list = [line.replace('\n', '').split('|') for line in read_data]

        return splitted_data_list
