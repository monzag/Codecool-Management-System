import os
import sys

from views import view

from controllers import student_controller
from controllers import employee_controller
from controllers import mentor_controller
from controllers import manager_controller


def start_up():
    '''
    function starts program by displaying about-screen
    and leading user thorugh logging into a system

    determines identity of user and his privilige in
    accessing sertain functions of program


    Returns:
        user : Codecooler obj. instance
    '''
    view.print_welcome_screen()
    view.wait_until_key_pressed()

    status = choose_status()
    user = log_in_as_user(status)

    return user


def choose_status():
    '''
    Asks user about his privilige in accessing cerain program
    features, and determining fallowing logging system

    Returns:
        status : str - representing privilige
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
    Depending on user privilige loads certain data into a program:
    
    -> for each group program will load group own users, to find one
       who is trying to access program
    -> employees and mentors have access to list of students
    -> manager have access to all

    Parameters:
        status: str - representing privilige

    Return:
        None
    '''
    student_controller.load_students_from_file()

    if status in ['Manager', 'Employee']:
        employee_controller.load_employees_from_file()

    if status in ['Manager', 'Mentor']:
        mentor_controller.load_mentors_from_file()

    if status == 'Manager':
        manager_controller.load_managers_from_file()


def log_in_as_user(status):
    '''
    holds loging to system:

    if user provided login and password were assosiated with existing 
    Codecooler obj. instance, fucntion returns fallowing object 
    otherwise will retry loging user to system

    Parameters:
        status : str - representing grout to serch in

    Returns:
        user : Codecooler obj. instance
    '''
    attempt = 1
    is_user = None
    while user:
        os.system('clear')

        view.print_login_screen(status, attempt)
        login, password = get_password_and_login()

        attempt += 1
        user = is_user_in_system(status, login, password)

    return user


def get_password_and_login():
    '''
    Takes loggin information from user

    Returns:
        login: str
        pasword: str
    '''
    login = view.input_login()
    password = view.input_password()

    return login, password


def is_user_in_system(status, login, password):
    '''
    Determines whenever given login and password exist in certain grup

    Parameters:
        status: str - representing privilige group
        login: str
        password: str

    Returns:
        Codecooler obj. instance
        or
        None - if password and login doesn't match
    '''
    if status == 'Student':
        return student_controller.get_user_by_login_and_password(login, password)

    if status == 'Employee':
        return employee_controller.get_user_by_login_and_password(login, password)

    if status == 'Mentor':
        return mentor_controller.get_user_by_login_and_password(login, password)

    if status == 'Manager':
        return manager_controller.get_user_by_login_and_password(login, password)


def operate_on_user(user):
    '''
    Depending on type of user, opens differen priviliges menus which 
    are declared in different modules and hold users operation logic.

    Fallowing disallows certain groups on accessing features they 
    souldn't have access to.

    Parameters:
        user : Codecooler obj. instance

    Returns:
        None
    '''
    if isinstance(user, Studen):
        student_controller.student_menu()
    if isinstance(user, Employee):
        employee_controller.employee_menu()
    if isinstance(user, Mentor):
        mentor_controller.mentor_menu()
    if isinstance(user, Manager):
        manager_controller.manager_menu()


def close_program():
    '''
    Prints end screen
    '''
    os.system('clear')
    view.print_end_screen()


def hold_session():
    '''
    Holds procedural logic of program
    '''
    user = start_up()
    operate_on_user(user)
    close_program()