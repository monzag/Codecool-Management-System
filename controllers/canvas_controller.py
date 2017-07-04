import os
import sys

from views import view

from controllers import student_controller
from controllers import employee_controller
from controllers import mentor_controller
from controllers import manager_controller


def start_up():
    '''
    '''
    view.print_welcome_screen()
    view.wait_until_key_pressed()

    status = choose_status()

    user_login_as(status)





def choose_status():
    '''
    '''
    title = 'Do you want to log as'
    otions = ['Student', 'Employee', 'Mentor', 'Manager', 'Exit']

    status = None
    while status:
        os.system('clear')

        view.print_menu(title, options)
        option = view.input_number()
        
        if option == 1:
            status = 'Student'
        if option == 2:
            status = 'Employee'
        if option == 3:
            status = 'Mentor'
        if option == 4:
            status = 'Manager'
        if option == 0:
            sys.exit()
    
    return status


def load_lists_from_file(status):
    '''
    '''
    student_controller.load_students_from_file()

    if status in ['Manager', 'Mentor', 'Employee']:
        employee_controller.load_employees_from_file()

    if status in ['Manager', 'Mentor']:
        mentor_controller.load_mentors_from_file()

    if status == ['Manager']:
        manager_controller.load_managers_from_file()


def get_password_and_login():
    '''
    '''
    login = view.input_login()
    password = view.input_password()

    return login, password


def log_in_user(status):
    '''
    '''
    attempt = 1
    is_user = False
    while is_user:
        os.system('clear')

        view.print_login_screen(status, attempt)
        login, password = get_password_and_login()

        attempt += 1
        is_user = is_user_in_system(status, login, password)


def is_user_in_system(status, login, password):
    '''
    '''
    if status == 'Student':
        return student_controller.match_login_and_password(login, password)
    
    pass
    