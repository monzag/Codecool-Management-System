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


def view_students():
    '''
    prints list of every student assigned to course
    print needs grade so mentor will know how student perform

    should use students_controller.get_students() to get list of all students

    should use views.view.print_students() for printing
    '''
    pass


def add_assigment():
    '''
    should use views.view.get_assigment_inputs() to gather necessery data

    should use controllers.assigment_controller.create_new_assigment()
    '''
    pass


def grade_assigment():
    '''emove
    should use controllers.assigment_controller to create
        list of assigments

    should use views.view.print_assigments to print assigments
        (along with numbers to call exact assigment)

    should use views.view.input_umber() to select assigment

    should use controllers.assigment_controller.change_grade() to change grade
    '''
    pass


def view_students():
    '''
    prints list of every student assigned to course
    print needs attendence so mentor will know how student perform

    should use students_controller.get_students() to get list of all students

    should use views.view.print_students() for printing
    '''
    pass


def add_student():
    '''
    should use views.view.get_new_student_data() to get inputs about new student

    should use controllers.student_controller.create_new_student() to create student
    '''
    pass


def remove_student():
    '''
    should use controllers.student_controller to get list of all students
        (along with numbers)

    should use views.view.print_students() to print all students

    should use views.view.get_number() to dtermine which student should be deleted

    should use controllers.student_controler.remove_student() to remove student
    '''


def edit_student():
    '''
    should use controllers.student_controller to get list of all students
        (along with numbers)

    should use views.view.print_students() to print all students

    should use views.view.get_number() to detrmine which student should be edited

    should use controllers.student_controler.edit_student() to edit students data
    '''
    pass
