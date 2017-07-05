import os

import views.view
import controllers.student_controller
import controllers.mentor_controller

from models.manager import Manager


def manager_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    otions = ['View students', 'View mentors', 'Add mentor', 'Remove mentor', 'Edit mentor data', 'Exit']

    end = False
    while end:
        os.system('clear')

        view.print_menu(title, options)
        option = view.input_number()
        
        if option == 1:
            view_students()
        if option == 2:
            view_mentors()
        if option == 3:
            add_mentor()
        if option == 4:
            remove_mentor()
        if option == 5:
            edit_mentor()
        if option == 0:
            end = True


def view_students():
    '''
    prints list of every student assigned to course
    print needs grade so mentor will know how student perform

    should use students_controller.get_students() to get list of all students

    should use views.view.print_students() for printing
    '''
    pass


def view_mentors():
    '''
    prints list of every mentor

    should use smentor_controller.get_mentors() to get list of all mentors

    should use views.view.print_mentors() for printing
    '''
    pass


def add_mentor():
    '''
    should use views.view.get_new_mentor_data() to get inputs about new mentor

    should use controllers.mentor_controller.create_new_mentor() to create mentor
    '''
    pass


def remove_mentor():
    '''
    should use controllers.mentor_controller to get list of all mentors
        (along with numbers)
    
    should use views.view.print_mentors() to print all mentors

    should use views.view.get_number() to detrmine which mentor should be deleted

    should use controllers.mentor_controler.remove_mentor() to remove mentor
    '''
    pass


def edit_mentor():
    '''
    should use controllers.mentor_controller to get list of all mentors
        (along with numbers)
    
    should use views.view.print_mentors() to print all mentors

    should use views.view.get_number() to detrmine which mentor should be edited

    should use controllers.mentor_controller.edit_student() to edit mentors data
    '''
    pass