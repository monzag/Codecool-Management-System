import os

import views import view

from controllers import student_controller


def employee_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    otions = ['View students', 'Exit']

    end = False
    while end:
        os.system('clear')

        view.print_menu(title, options)
        option = view.input_number()
        
        if option == 1:
            view_students()
        if option == 0:
            end = True


def view_students():
    '''
    prints list of every student assigned to course
    print needs email so employees can contact with student

    should use students_controller.get_students() to get list of all students

    should use views.view.print_students() for printing
    '''
    pass