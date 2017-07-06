import os

from views import view
from controllers import assignment_controller

from models.student import Student
# from models.assigemnt import Assigment


def student_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''

    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View grades', 'Submit assigment']

    end = False
    while not end:
        os.system('clear')

        view.print_menu(title, options, exit_message)
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
    table = assignment_controller.get_assignments_to_table(student)
    tittle_list = ['Assignment', 'status', 'deadline', 'grade', 'max_grade']
    view.print_table(table, tittle_list)
    labels = ['Write number of assignment']
    title = 'Input data'
    number_assignment = view.get_inputs(labels, title)
    assignment = student.assignments_list[number_assignment - 1]
    assignment_controller.change_assignment_to_done(assignment)
    # Save


def view_grades():
    # powiązane z assignmentami! W jakiej formie w końcu będą te pliki?
    pass


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




