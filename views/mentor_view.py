def menu_labels(user):

    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students', 'Add assignment', 'Grade assignment',
               'Check attendance', 'Add student', 'Remove student']


def data_to_check_attendance():

    title = "Student attendance for today"
    exit_message = 'Back to Main Menu (NOTICE: You will have to check whole attendance again for today!)'
    options = ['Present', 'Late', 'Absent']

    return title, exit_message, options


def attendance_checked():

    print("\nAll attendance for today is checked.\n")


def data_to_add_student():

    labels = ["Name", "Surname", "Login", "Password", "e-mail"]
    title = "Provide informations about new student"
    
