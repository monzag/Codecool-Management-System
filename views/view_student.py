def get_data_to_student_menu(user):
    '''
    Get data to print table in student menu (student controller).

    Args:
        user - object

    Returns:
        title, exit_message, options - string
    '''

    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View grades', 'Submit assigment', 'Show all students', 'Change password', 'Show general grade']

    return title, options, exit_message


def get_title_to_view_grades():
    '''
    Get title list to table in view_grades (student controller).

    Returns:
        title_list - list
    '''

    title_list = ['assignment', 'add date', 'deadline', 'submit date', 'grade', 'max grade']

    return title_list


def get_invalid_assignment_in_submit():
    '''
    Get text about invalid assignment to submit assignment (student controller).

    Returns:
        string
    '''

    return 'Assignment does not exist!'


def get_data_to_view_students():
    '''
    Data to table when student want to show all students. 

    Returns:
        list of strings
    '''
    return ["Name", "Surname", "e-mail"]


def get_titles_to_general_grade():
    '''
    Data to table when student want to show data about general grade of assignments. 

    Returns:
        list of strings
    '''
    return ['Assignment', 'Average', 'Min', 'Max', 'Total grade']


