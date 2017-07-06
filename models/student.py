from models.codecooler import Codecooler
import os
from models.assignment import Assignment


class Student(Codecooler):

    list_of_students = []

    def __init__(self, attendance, *args):
        super().__init__(*args)
        Student.list_of_students.append(self)
        self.attendance = attendance
        self.assignments_list = self.get_assignment_list()

    @classmethod
    def get_codecoolers_from_file(cls, file_name):
        """
        Creates objects with data from splitted list.

        Returns:
                None
        """

        splitted_data_list = cls.load_data_from_file(file_name)
        print(splitted_data_list)

        for element in splitted_data_list:
            name, surname, login, password, mail, attendance = element
            attendance = int(attendance)
            cls(attendance, name, surname, login, password, mail)

    def get_assignment_list(self):
        '''
        Add Assignment objects to list if assignment's owner equal to Student login. 

        Returns:
            assignment_list - list with Assignment obj.
        '''

        assignment_list = []
        for assignment in Assignment.list_of_assignment:
            if assignment.owner == self.login:
                assignment_list.append(assignment)

        return assignment_list

    @classmethod
    def save_data_to_file(cls):
        '''
        Save students data to csv file. If file not exist, create file.
        '''
        list_to_save = cls.convert_list_of_object_to_data()
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
        for student in cls.list_of_students:
            name, surname, login, password, email = student.name, student.surname, student.login, student.password, student.email
            student_data = [name, surname, login, password, email]
            list_to_save.append(student_data)

        return list_to_save
