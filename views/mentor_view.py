def menu_labels(user):

    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students', 'Add assignment', 'Grade assignment',
               'Check attendance', 'Add student', 'Remove student']

    return title, exit_message, options


def data_to_check_attendance():

    title = "Student attendance for today"
    exit_message = 'Back to Main Menu'
    options = ['Present', 'Late', 'Absent', 'Skip student']

    return title, exit_message, options


def attendance_checked():

    print("\nAll attendance for today is checked or no students in database.\n")


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
