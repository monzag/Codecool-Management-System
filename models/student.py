from models.codecooler import Codecooler
import os


class Student(Codecooler):

    list_of_students = []

    def __init__(self, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)

    @classmethod
    def save_data_to_file(cls):
        '''
        Save students data to csv file. If file not exist, create file.
        '''
        list_to_save = Student.convert_list_of_object_to_data()
        filename = 'students.csv'
        with open(filename, 'w') as csvfile:
            for record in list_to_save:
                row = ','.join(record)
                csvfile.write(row + "\n")

    @classmethod
    def convert_list_of_object_to_data(cls):
        '''
        Unpack attributes of Student object as data to student_data list and add it to list_to_save.

        Returns:
            list_to_save - list of lists
        '''

        list_to_save = []
        for student in Student.list_of_students:
            name, surname, login, password, email = student.name, student.surname, student.login, student.password, student.email
            student_data = [name, surname, login, password, email]
            list_to_save.append(student_data)

        return list_to_save
