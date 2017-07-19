from datetime import datetime

from models.assignment import Assignment


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

    if str(solution.grade) + solution.submit_date != '00':

        new_submit_date = '{}:{}:{}'.format(datetime.today().year, datetime.today().month, datetime.today().day)
        solution.submit_date = new_submit_date

        file_path = solution.get_file_name(student_index, assignment_name)
        solution.file_name = file_path

        solution_text = assignment_view.get_solution_text()
