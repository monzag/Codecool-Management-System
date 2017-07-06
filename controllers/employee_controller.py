import os

from views import view

from controllers import codecooler_controller


def employee_menu(user, students):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Parameters:
        students: list of Student objs.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students']

    end = False
    while not end:
        os.system('clear')

        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            view_students()
        if option == 0:
            end = True


def view_students(students):
    '''
    Given list of Student obj. prints table consicting
    of their names, surnames, and mails

    Parameters:
        students: list of Student objs.

    Returns:
        None
    '''
    lables = ['name', 'surname', 'email']
    table = codecooler_controller.get_codecoolers_with_mails(students)
    view.print_table(table, lables)
    view.wait_until_key_pressed()