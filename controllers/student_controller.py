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