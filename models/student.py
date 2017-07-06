from models.codecooler import Codecooler
import os
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
        list_to_save = cls.convert_list_of_students_to_data()
        filename = 'students.csv'
        cls.save_data(filename)

    @classmethod
    def save_data(cls, filename):
        '''
        Save data to proper filename. Raise error if file not exist.

        Args:
            filename - string
        '''
        file_path = os.getcwd() + '/data/' + filename

        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(file_path, 'w') as csvfile:
                for record in list_to_save:
                    row = '|'.join(record)
                    csvfile.write(row + "\n")

    @classmethod
    def convert_list_of_students_to_data(cls):
        '''
        Unpack attributes of Student object as data to student_data list and add it to list_to_save.

        Returns:
            list_to_save - list of lists
        '''

        list_to_save = []
        for student in cls.list_of_students:
            name, surname, login, password, email, attendance, days_passed = student.name, student.surname, student.login, student.password, student.email, student.attendance, student.days_list
            student_data = [name, surname, login, password, email, attendance, days_passed]
            list_to_save.append(student_data)

        return list_to_save

    @classmethod
    def convert_list_of_assignments_to_data(cls):
        '''
        Unpack attributes of Assignment object as data to assignment_data list and add it to list_to_save.

        Returns:
            list_to_save - list of lists
        '''

        list_to_save = []
        for assignment in self.assignments_list:
            login, name, add_date, deadline, max_grade, grade, status, submit_date = assignment.login, assignment.name, assignment.add_date, assignment.deadline, assignment.max_grade, assignment.grade, assignment.status, assignment.submit_date
            assignment_data = [login, name, add_date, deadline, max_grade, grade, status, submit_date]
            list_to_save.append(assignment_data)

        return list_to_save
