import os
import sys

from views import view

from models.login import Logins
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

    user = None
    while not user:
        os.system('clear')
        user = log_in_as_user(status)

    return user


def load_database():
    '''
    Initialize all objects stored in data/..
    Close program if there is not enough database to function properly.

    Parameters, Returns: None

    Initialize:
        Student objs.
        Mentor objs.
        Employee objs.
        Manager objs.
        Assigments objs.
        Logins.list_of_logins
    '''
    Assignment.get_assignments_from_file('assignments.csv')
    Student.get_codecoolers_from_file('students.csv')
    Employee.get_codecoolers_from_file('employees.csv')
    Mentor.get_codecoolers_from_file('mentors.csv')
    Manager.get_codecoolers_from_file('managers.csv')

    if len(Manager.list_of_managers) < 1 or len(Employee.list_of_employees) < 1:
        err_msg = 'There is no database stored. Contact our support at zaganiacz.m@gmail.com'
        view.print_message(err_msg)
        sys.exit()

    Logins.from_codecoolers(Student.list_of_students, Employee.list_of_employees, Manager.list_of_managers, Mentor.list_of_mentors)


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
    os.system('clear')
    login, password = get_password_and_login()
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
    codecoolers = Student.list_of_students + Employee.list_of_employees + Mentor.list_of_mentors + Manager.list_of_managers
    codecooler_controller.get_user_by_login_and_password(login, password, codecoolers)


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
        employee_controller.employee_menu(user)

    if status == 'Mentor':
        mentor_controller.mentor_menu(user)

    if status == 'Manager':
        manager_controller.manager_menu(user)


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
    load_database()
    user = start_up()
    operate_on_user(user)
    close_program()
