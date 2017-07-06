from views import view

from controllers import assignment_controller

from models.student import Student
from models.assignment import Assignment


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
    view_grades(student)

    number = None
    while not number:
        number = view.input_number()

    if number <= len(student.assignments_list):
        assignment = student.assignments_list[number - 1]
        assignment_controller.change_assignment_to_done(assignment)
        Assignment.save_assignments_to_file()

    else:
        view.print_message('Assignment does not exist!')


def view_grades(student):
    '''
    Show table with data about assignment-grades'
    '''

    table = assignment_controller.get_assignments_to_table(student)
    tittle_list = ['Assignment', 'status', 'submit_date', 'deadline', 'grade', 'max_grade']
    view.print_table(table, tittle_list)


def get_students():
    '''
    Returns list of students
    '''

    return Student.list_of_students





