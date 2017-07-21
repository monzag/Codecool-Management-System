def menu_labels(user):

    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students', 'Add assignment', 'Edit assignment', 'Grade assignment',
               'Check attendance', 'Add student', 'Remove student', 'Change password']

    return title, exit_message, options

def data_to_view_students():

    return ["Name", "Surname", "e-mail", "Attendance", 'Total grade']


def assignment_already_graded():

    print('Assignment was already graded, or was not submited yet!')


def no_such_assignment():

    print('There is no such assignment!')


def data_to_check_attendance():

    title = "Student attendance for today"
    exit_message = 'Back to Main Menu'
    options = ['Present', 'Late', 'Absent', 'Skip student']

    return title, exit_message, options


def print_all_checked():

    print("\nAll students are checked for today.\n")


def print_empty_database_msg():

    print('\nNo students in database.\n')


def print_how_many_unchecked(unchecked_students_num):

    print("\nStudents left to be checked: {}\n".format(unchecked_students_num))


def get_data_to_add_student():
    '''
    Get proper label when student is added by mentor.

    Returns:
        name, surname, login, email - string
    '''
    return 'Name', 'Surname', 'Login', 'E-mail'


def print_new_password(password):

    print('Password: ', password)


def data_get_student_index():

    labels = ["Index"]
    title = "Type index number of student"

    return labels, title


def index_doesnt_exist():

    print("Index does not exist!")


def recipent_error():

    print("\nE-mail can not be delivered!\n")

def title_check_valid():

    return 'Type the data below'
