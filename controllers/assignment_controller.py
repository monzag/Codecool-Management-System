import os
from datetime import datetime

from models.assignment import Assignment
from models.solution import Solution

from views import assignment_view
from views import view


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
        solution.file_name = assignment.name + '_' + str(student_index) + 'txt'
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

    file_path = os.getcwd() + '/data/solutions/' + file_name
    with open(file_path, 'w+') as solution_file:
        solution_file.write(text)


def get_student_total_grade(student_index):
    '''
    '''
    grade = 0
    max_grade = 0

    for assignment in Assignment.list_of_assignments:
        max_grade += assignment.max_grade
        grade += assignment.solutions[student_index].grade

    total_grade = grade / max_grade * 100

    return '{:3.2f} %'.format(total_grade)


def remove_student_solutions(student_index):
    '''
    '''
    for assignment in Assignment.list_of_assignments:
        del assignment.solutions[student_index]

    Assignment.save_assignments_to_file('assignments.csv')


def assign_assignments_to_new_student():
    '''
    '''
    for assignment in Assignment.list_of_assignments:
        assignment.solutions.append(Solution(0, '0', '0'))

    Assignment.save_assignments_to_file('assignments.csv')


def print_student_assignments(student_index):
    '''
    '''
    titles = ['name', 'add date', 'deadline', 'submit_date', 'grade', 'max_grade']

    table = []
    for assignment in Assignment.list_of_assignments:
        row = []

        row.append(assignment.name)
        row.append(assignment.add_date)
        row.append(assignment.deadline)
        row.append(assignment.solutions[student_index].formated_submit_date)
        row.append(assignment.solutions[student_index].formated_grade)
        row.append(str(assignment.max_grade))

        table.append(row)

    view.print_table(table, titles)
