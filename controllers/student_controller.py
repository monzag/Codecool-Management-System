from views import view
from views import view_student

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

    end = False
    while not end:
        title, options, exit_message = view_student.data_to_student_menu(user)
        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            view_grades(user)
        if option == 2:
            submit_assigment(user)
        if option == 3:
            display_all_students()
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
        text = view_student.invalid_assignment_in_submit()
        view.print_message(text)


def view_grades(student):
    '''
    Show table with data about assignment-grades'
    '''

    table = assignment_controller.get_assignments_to_table(student)
    title_list = view_student.title_to_view_grades()
    view.print_table(table, title_list)
