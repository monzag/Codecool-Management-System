import os

import views.view
import controllers.student_controller
import controllers.assigment_controller

from models.mentor import Mentor


def mentor_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    otions = ['View students', 'Add assigment', 'Grade assigment', 'Check attendence', 'Add student', 'Remove student', 'Exit']

    end = False
    while end:
        os.system('clear')

        view.print_menu(title, options)
        option = view.input_number()

        if option == 1:
            view_students()
        if option == 2:
            add_assigment()
        if option == 3:
            grade_assigment()
        if option == 4:
            check_attendence()
        if option == 5:
            add_student()
        if option == 6:
            remove_student()
        if option == 0:
            end = True
