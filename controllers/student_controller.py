import os

# import views.view
# import controllers.assigment_controller

from models.student import Student
# from models.assigemnt import Assigment


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


def get_user_by_login_and_password(login, password):
    '''
    Find proper Student object in list_of_students by login and password.
    Raise AttributeError if user enter bad login/password.

    Returns:
        student - obj
    '''

    for student in Student.list_of_students:
        if student.login == login and student.password == password:
            return student

    raise AttributeError('Bad login/password')


def submit_assigment(student):
    '''
    Choose assignment from list and change status assignment 'done'.
    Save change to file'

    Args:
        student - obj
    '''
    table = get_assignment_data()
    tittle_list = ['Lp', 'Assignment', 'status', 'deadline']
    views.view.print_table(table, tittle_list)
    labels = ['Write number of assignment: ']
    title = 'Input data'
    number_assignment = views.view.get_inputs(labels, title)
    assignment = student.assignments_list[number_assignment - 1]
    assignment_controller.change_assignment_to_done(assignment)
    # zdecydować czy w pliku students.csv będą dane dotyczące assignmentu? Co zapisywać do pliku!!


def get_assignment_data():
    '''Wypakuj obiekty i utwór listę list'''
    # TO DO!!
    student.assignments_list
    # assignments_list -
    pass


def view_grades():
    pass


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

    save_data_to_file(Student.list_of_students)


def get_students():
    '''
    Returns list of students
    '''

    return Student.list_of_students

'''

def list_student_with_grades():
    pass


def list_student_with_attendance():
    pass'''

# Add id's assignment to list




