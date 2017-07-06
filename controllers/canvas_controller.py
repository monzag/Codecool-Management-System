import os
import sys

from views import view

from models.codecooler import Codecooler
from models.student import Student
from models.employee import Employee
from models.mentor import Mentor
from models.manager import Manager
from models.assignment import Assignment

from controllers import codecooler_controller
from controllers import student_controller
from controllers import employee_controller
from controllers import mentor_controller
from controllers import manager_controller
from controllers import assignment_controller


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
    exit_message = 'Exit'
    options = ['Student', 'Employee', 'Mentor', 'Manager']

    status = None
    while not status:
        os.system('clear')

        view.print_menu(title, options, exit_message)
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
    user = None
    while not user:
        os.system('clear')

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
        or    login = view.input_login()
    password = view.input_password()
        None - if password and login doesn't match
    '''
    if status == 'Student':
        return codecooler_controller.get_user_by_login_and_password(login, password, Student.list_of_students)

    if status == 'Employee':
        return codecooler_controller.get_user_by_login_and_password(login, password, Employee.list_of_employees)

    if status == 'Mentor':
        return codecooler_controller.get_user_by_login_and_password(login, password, Mentor.list_of_mentors)

    if status == 'Manager':
        return codecooler_controller.get_user_by_login_and_password(login, password, Manager.list_of_managers)


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
    status = user.__class__.__name__

    if status == 'Student':
        student_controller.student_menu(user)

    if status == 'Employee':
        employee_controller.employee_menu(user, Student.list_of_students)

    if status == 'Mentor':
        mentor_controller.mentor_menu(user)
        # mentor_controller.mentor_menu(user, Student.list_of_students)

    if status == 'Manager':
        manager_controller.manager_menu(user)
        # manager_controller.manager_menu(user, Student.list_of_students, Mentor.list_of_mentors)


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
    Student.get_codecoolers_from_file('students.csv')
    Employee.get_codecoolers_from_file('employees.csv')
    Mentor.get_codecoolers_from_file('mentors.csv')
    Manager.get_codecoolers_from_file('managers.csv')
    Assignment.get_assignments_from_file('assignments.csv')

    user = start_up()
    operate_on_user(user)
    close_program()