import os

import views.view
from models.student import Student
from models.mentor import Mentor
from controllers.mail_validation import *
from views.manager_view import *


def manager_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''

    titles = 'Hi {}! What would you like to do'.format(user.name)
    options = ['View students', 'View mentors', 'Add mentor', 'Remove mentor',
               'Exit']

    show_menu = True

    title = "Manager menu"
    options = ['View students', 'View mentors', 'Add mentor', 'Remove mentor']
    exit_message = "Exit"

    end = False

    while not end:

        views.view.print_menu(title, options, exit_message)
        option = views.view.input_number()

        if option == 1:
            view_students()
            views.view.print_message("Press any key to continue.")
            views.view.wait_until_key_pressed()

        if option == 2:
            view_mentors()
            views.view.print_message("Press any key to continue.")
            views.view.wait_until_key_pressed()

        if option == 3:
            add_mentor()
            Mentor.save_data_to_file()

        if option == 4:
            try:
                remove_mentor()
            except ValueError:
                print("Please type in only numbers!")
            except IndexError:
                print('Mentor with given index does not exist!')

        if option == 0:
            end = True


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
            None
    '''

    titles = ["Name", "Surname", "e-mail", "Attendance"]
    students_info = []

    for student in Student.list_of_students:
        students_info.append([student.name, student.surname,
                             student.email, str(student.attendance)])

    views.view.print_table(students_info, titles)


def view_mentors():
    '''
    Prints list of every mentor's name, surname and e-mail.

    Returns:
            None
    '''

    titles = ["Name", "Surname", "e-mail"]
    mentors_info = []

    for mentor in Mentor.list_of_mentors:
        mentors_info.append([mentor.name, mentor.surname, mentor.email])

    views.view.print_table(mentors_info, titles)


def add_mentor():
    """
    Creates new mentor and adds mentor to the mentor's list

    Return:
            None
    """

    login = get_single_input("Type login: ")
    password = get_single_input("Type password: ")
    name = get_valid_input(check_name, "Type name: ")
    surname = get_valid_input(check_name, "Type surname: ")
    mail = get_valid_input(check_mail, "Type mail: ")

    new_mentor = Mentor(name, surname, login, password, mail)


def remove_mentor():
    '''
    Remove object Mentor from list by index.
    Raise IndexError when index out of range.
    Returns:
            None
    '''
    view_mentors()

    labels = ["Index"]
    title = "Type index number of mentor to remove"
    user_input = views.view.get_inputs(labels, title)[0]

    if not user_input.isdigit():
        raise ValueError

    elif int(user_input) - 1 not in range(len(Mentor.list_of_mentors)):
        raise IndexError

    else:
        index = int(user_input) - 1
        del Mentor.list_of_mentors[index]
        Mentor.save_data_to_file()


def check_name(name):

    if name.isalpha():
        return True
