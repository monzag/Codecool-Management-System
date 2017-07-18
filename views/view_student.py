def data_to_student_menu(user):
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View grades', 'Submit assigment']

    return title, exit_message, options


def title_to_view_grades():
    title_list = ['Assignment', 'status', 'submit_date', 'deadline', 'grade', 'max_grade']

    return title_list


def invalid_assignment_in_submit():
    return 'Assignment does not exist!'
