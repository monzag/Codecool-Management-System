from datetime import datetime

from models.assignment import Assignment

from views import assignment_view


def get_assignments_to_table(student_index):
    '''
    '''
    table = []
    for assignment in Assignment.list_of_assignments:
        solution = []
        solution.append(assignment.name)
        solution.append(assignment.add_date)
        solution.append(assignment.deadline)
        solution.append(assignment.solutions[student_index].formated_submit_date)
        solution.append(assignment.solutions[student_index].formated_grade)
        solution.append(str(assignment.max_grade))

        table.append(solution)

    return table


def submit_solution_to_assignment(assignment, student_index):
    '''
    '''
    solution = assignment.solutions[student_index]

    if solution.submit_date == '0':

        solution.submit_date = get_submit_date()
        solution.file_name = solution.get_file_name(student_index, assignment.name)
        save_solution_to_file(solution.file_name)

    else:
        assignment_view.print_fail_message()


def get_submit_date():
    '''
    '''
    return '{}:{}:{}'.format(datetime.today().year, datetime.today().month, datetime.today().day)


def save_solution_to_file(file_name):
    '''
    '''
    text = assignment_view.get_submision_text()

    with open(file_name, 'w+') as solution_file:
        solution_file.write(text)
