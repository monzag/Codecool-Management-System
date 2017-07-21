from views import view


def get_submision_text():
    text = view.get_input('\nProvide assignment text:\n\n')

    return text


def print_fail_message():
    view.print_message('\nChosen assignment was already submited.\n')


def get_titles():
    return ['name', 'add date', 'deadline', 'submit_date', 'grade', 'max_grade']


def get_assignment_index_outprints():
    labels = ['Index']
    title = 'Type index number of assignment'

    return labels, title


def get_new_assignemt_outprints():
    name_message = 'Type name'
    date_message = 'Type deadline(yyyy:mm:dd)'
    grade_message = 'Type grade'

    return name_message, date_message, grade_message


def get_no_assignment_message():
    return 'There is no assignment under provided index.'
