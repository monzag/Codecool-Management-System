from views import view

from models.codecooler import Codecooler
from models.student import Student
from models.employee import Employee
from models.mentor import Mentor
from models.manager import Manager
from models.assigment import Assigment

from controllers import codecooler_controller
from controllers import student_controller


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
    Codecooler obj. instance, function returns fallowing object 
    otherwise will retry loging user to system

    Parameters:
        status : str - representing group to search in

    Returns:
        user : Codecooler obj. instance
    '''
    user = None
    while not user:
        login, password = get_password_and_login()
        user = find_user_in_system(status, login, password)

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


def find_user_in_system(status, login, password):
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
        student_menu(user)

    if status == 'Employee':
        employee_menu(user)

    if status == 'Mentor':
        mentor_menu(user)

    if status == 'Manager':
        manager_menu(user)


def close_program():
    '''
    Prints end screen
    '''
    view.print_end_screen()


def hold_session():
    '''
    Holds procedural logic of program
    '''
    Student.get_students_from_file()
    Employee.get_employees_from_file()
    Mentor.get_mentors_from_file()
    #Manager.get_manager_from_file()

    user = start_up()
    operate_on_user(user)
    close_program()

def student_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View grades', 'Submit assigment']

    end = False
    while not end:

        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            student_controller.view_grades(user)
        if option == 2:
            assigment_controller.submit_assigment(user)
        if option == 0:
            end = True


def employee_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, until user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students']

    end = False
    while not end:

        view.print_menu(title, options, exit_message)
        option = view.input_number()
        
        if option == 1:
            view_students_mails(Student.list_of_students)
        if option == 0:
            end = True


def view_students_mails(students):
    lables = ['name', 'surname', 'email']
    mails = codecooler_controller.get_codecoolers_with_mails(students)
    view.print_table(mails, lables)


def mentor_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students', 'Add assigment', 'Grade assigment', 'Check attendence', 'Add student', 'Remove student']

    end = False
    while not end:

        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            pass
        if option == 2:
            # add_assigment()
            pass
        if option == 3:
            # grade_assigment()
            pass
        if option == 4:
            pass
        if option == 5:
            pass
        if option == 6:
            pass
        if option == 0:
            end = True

def remove_student(students):
    student = students[0]
    students = codecooler_controller.remove_codecooler(student, students)

    return students


def manager_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, until user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    otions = ['View students', 'View mentors', 'Add mentor', 'Remove mentor',
              'Edit mentor data']

    end = False
    while not end:

        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            student_controller.view_students(Student.list_of_students)
        if option == 2:
            mentor_controller.view_mentors(Mentors.list_of_mentors)
        if option == 3:
            # add_mentor()
            pass
        if option == 4:
            # remove_mentor()
            pass
        if option == 5:
            # edit_mentor()
            pass
        if option == 0:
            end = True