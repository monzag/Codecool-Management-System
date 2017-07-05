import os

from views import view

from controllers import assigment_controller


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


def submit_assigment(student):
    pass


def view_grades():
    pass


def create_new_student(name, surname, login, password, email):
    '''
    Create new object Student. 

    Returns:
        new_student - obj
    '''

    new_student = Student(name, surname, login, password, email)
    return new_student


def remove_student(index):
    '''
    Remove object Student from list by index.
    Raise IndexError when index out of range.

    Returns:
        list of students
    '''

    if index not in range(len(Student.list_of_students) - 1):
        raise IndexError('Student with this number not exist!')

    else:
        del Student.list_of_students[index]

    return Student.list_of_students


def edit_student():
    pass

'''
def list_student_with_grades():
    pass


def list_student_with_attendance():
    pass'''


def get_students():
    '''
    Returns list of students
    '''

    return Student.list_of_students

