def data_to_student_menu(user):
    '''
    Get data to print table in student menu (student controller).

    Args:
        user - object

    Returns:
        title, exit_message, options - string
    '''

    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View grades', 'Submit assigment']

    return title, exit_message, options


def title_to_view_grades():
    '''
    Get title list to table in view_grades (student controller). 

    Returns:
        title_list - list
    '''

    title_list = ['Assignment', 'status', 'submit_date', 'deadline', 'grade', 'max_grade']

    return title_list


def invalid_assignment_in_submit():
    '''
    Get text about invalid assignment to submit assignment (student controller). 

    Returns:
        string
    '''

    return 'Assignment does not exist!'
