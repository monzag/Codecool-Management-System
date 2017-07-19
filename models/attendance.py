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
