import os
import smtplib

from models.student import Student
from models.mentor import Mentor
from models.manager import Manager
from models.login import Logins

from controllers.mail_validation import *
from controllers import codecooler_controller
from controllers.send_mail import *

import views.view
from views.manager_view import *


def manager_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''

    show_menu = True

    title, options, exit_message = manager_menu_titles(user)

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
            Mentor.save_codecoolers_to_file('mentors.csv', Mentor.list_of_mentors)

        if option == 4:

            try:
                remove_mentor()

            except ValueError:
                message = value_error_message()
                views.view.print_message(message)

            except IndexError:
                message = index_error_message()
                views.view.print_message(message)

        if option == 5:
            change_password(user)

        if option == 0:
            end = True


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
            None
    '''

    titles = view_students_titles()
    students_info = []

    for student in Student.list_of_students:
        students_info.append([student.name, student.surname,
                             student.email])

    views.view.print_table(students_info, titles)


def view_mentors():
    '''
    Prints list of every mentor's name, surname and e-mail.

    Returns:
            None
    '''

    titles = view_mentors_titles()
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
    titles = input_titles_for_mentor_add()

    login = get_valid_input(Logins.is_login_valid, titles[0])
    password = codecooler_controller.get_random_password()
    name = get_valid_input(check_name, titles[2])
    surname = get_valid_input(check_name, titles[3])
    mail = get_valid_input(check_mail, titles[4])

    new_mentor = Mentor(name, surname, login, password, mail)
    Mentor.save_codecoolers_to_file('mentors.csv', Mentor.list_of_mentors)

    msg = 'Password: {}'.format(password)

    try:
        send_email(msg, mail)
        views.view.print_send_password_msg()

    except smtplib.SMTPRecipientsRefused:
        recipent_error()

def remove_mentor():
    '''
    Remove object Mentor from list by index.
    Raise IndexError when index out of range.
    Returns:
            None
    '''
    view_mentors()

    title, label = input_titles_for_mentor_remove()
    user_input = views.view.get_inputs(label, title)[0]

    if not user_input.isdigit():
        raise ValueError

    elif int(user_input) - 1 not in range(len(Mentor.list_of_mentors)):
        raise IndexError

    else:
        index = int(user_input) - 1
        del Mentor.list_of_mentors[index]
        Mentor.save_codecoolers_to_file('mentors.csv', Mentor.list_of_mentors)


def check_name(name):

    if name.isalpha():
        return True


def change_password(user):
    '''
    Change old password to new. Save changes.

    Args:
        user - object
    '''

    codecooler_controller.change_password(user)
    Manager.save_codecoolers_to_file('managers.csv', Manager.list_of_managers)
