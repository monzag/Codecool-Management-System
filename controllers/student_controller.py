import os

import views.view
import controllers.assigment_controller

from models.student import Student
from models.assigemnt import Assigment


def student_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''

    title = 'Hi {}! What would you like to do'.format(user.name)
    otions = ['View grades', 'Submit assigment', 'Exit']

    end = False
    while end:
        os.system('clear')

        view.print_menu(title, options)
        option = view.input_number()

        if option == 1:
            view_grades(user)
        if option == 2:
            submit_assigment(user)
        if option == 0:
            end = True


def submit_assigment(student):
    '''
    Choose assignment from list and change status assignment 'done'.
    Save change to file'

    Args:
        student - obj
    '''
    table = get_assignment_data()
    tittle_list = ['Lp', 'Assignment', 'status', 'deadline']
    views.view.print_table(table, tittle_list)
    labels = ['Write number of assignment: ']
    title = 'Input data'
    number_assignment = views.view.get_inputs(labels, title)
    assignment = student.assignments_list[number_assignment - 1]
    assignment_controller.change_assignment_to_done(assignment)
    # zdecydować czy w pliku students.csv będą dane dotyczące assignmentu? Co zapisywać do pliku!!


'''def load_students_from_file():
    '''
    '''Read students data from csv file.
    Raise error if file not exist.

    Returns:
        splitted - list of lists'''
    '''

    filename = 'students.csv'
    if not os.path.exists(filename):
        raise FileNotFoundError("There is no such a file")

    else:
        with open(filename, 'r') as csvfile:
            read_data = csvfile.readlines()
            splitted = [line.replace('\n', '').split('|') for line in read_data]

    return splitted'''


'''def save_data_to_file(list_to_save):
    '''
    '''Save students data to csv file. If file not exist, create file.'''
    '''

    filename = 'students.csv'
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list_to_save)'''


def get_assignment_data():
    '''Wypakuj obiekty i utwór listę list'''
    # TO DO!!
    student.assignments_list
    # assignments_list -
    pass


def view_grades():
    pass


def create_new_student(name, surname, login, password, email):
    '''
    Create new object Student. 

    Returns:
        new_student - obj
    '''

    new_student = Student(name, surname, login, password, email)
    return new_student


def remove_student(index):
    '''
    Remove object Student from list by index.
    Raise IndexError when index out of range.

    Returns:
        list of students
    '''

    if index not in range(len(Student.list_of_students) - 1):
        raise IndexError('Student with this number not exist!')

    else:
        del Student.list_of_students[index]

    save_data_to_file(Student.list_of_students)

    def get_students_from_file():
        '''
        '''
        data_all_students = Student.load_students_from_file()
        for student in data_all_students:
            name, surname, login, password, email = student[0], student[1], student[2], student[3], student[4]
            create_new_student(name, surname, login, password, email)

        return Student.list_of_students


def get_students():
    '''
    Returns list of students
    '''

    return Student.list_of_students

'''

def list_student_with_grades():
    pass


def list_student_with_attendance():
    pass'''

# Add id's assignment to list




