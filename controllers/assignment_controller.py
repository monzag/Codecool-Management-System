import os
import re
from datetime import datetime

from models.assignment import Assignment
from models.solution import Solution
from models.student import Student

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

        solution.submit_date = get_today_date()
        solution.file_name = assignment.name + '_' + str(student_index) + 'txt'
        save_solution_to_file(solution.file_name)

    else:
        assignment_view.print_fail_message()


def get_today_date():
    '''
    '''
    return '{:0>2}:{:0>2}:{:0>2}'.format(datetime.today().year, datetime.today().month, datetime.today().day)

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
    today = get_today_date()

    for assignment in Assignment.list_of_assignments:
        solution = assignment.solutions[student_index]

        if today > assignment.deadline or solution.grade > 0:
            max_grade += assignment.max_grade
            grade += solution.grade

    if max_grade > 0:
        total_grade = grade / max_grade * 100
    else:
        total_grade = 100

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


def get_assignment_form_user_input():
    '''
    '''
    labels = ['Index']
    title = 'Type index number of assignment'
    user_input = view.get_inputs(labels, title)[0]

    assignment_indexes = [str(assignment_index + 1) for assignment_index in range(len(Assignment.list_of_assignments))]

    if user_input in assignment_indexes:
        assignment = Assignment.list_of_assignments[int(user_input) - 1]

        return assignment

    return None


def create_assignment():
    '''
    '''
    name, add_date, deadline, max_grade, solutions = get_assignment_data()

    Assignment(name, add_date, deadline, max_grade, solutions)

    Assignment.save_assignments_to_file('assignments.csv')


def get_assignment_data():
    '''
    '''
    add_date = get_today_date()
    name, deadline, max_grade = get_valid_inputs()
    deadline = format_date(deadline)

    solutions = []
    for index in range(len(Student.list_of_students)):
        solutions.append(Solution(0, '0', '0'))

    return name, add_date, deadline, max_grade, solutions


def get_valid_inputs():
    '''
    '''
    name = check_valid(is_name, 'name')
    deadline = check_valid(is_date, 'deadline(yyyy:mm:dd)')
    max_grade = int(check_valid(is_grade, 'max grade'))

    return name, deadline, max_grade


def check_valid(function, message):
    '''
    '''
    is_valid = None
    while not is_valid:
        user_input = view.get_inputs([message], 'type stuff')[0]
        is_valid = function(user_input)

    return ''.join(user_input)


def is_name(user_input):
    '''
    '''
    assignment_names = [assignment.name for assignment in Assignment.list_of_assignments]
    if len(user_input) > 5 and user_input not in assignment_names:
        return True

    return False


def is_grade(user_input):
    '''
    '''
    if user_input.isdigit():
        if 0 < int(user_input) < 101:
            return True

    return False


def is_date(user_input):
    '''
    '''
    date_pattern = r'(201[7-9]).(1[0-2]|(0)?[1-9]).([0,1]|[1,2]\d|(0)?[1-9])$'

    match = re.match(date_pattern, user_input)
    if match:
        return True

    return False


def format_date(user_input):
    '''
    '''
    date_pattern = r'(?P<year>201[7-9]).(?P<month>1[0-2]|(0)?[1-9]).(?P<day>3[0,1]|[1,2]\d|(0)?[1-9])$'

    match = re.match(date_pattern, user_input)

    year = match.group('year')
    month = '{:0>2}'.format(match.group('month'))
    day = '{:0>2}'.format(match.group('day'))

    return '{}:{}:{}'.format(year, month, day)


def get_solutions_data():
    '''
    '''
    table = []
    for assignment in Assignment.list_of_assignments:
        row = []

        minimum = min(assignment.solutions, key=lambda solution: solution.grade)
        maximum = max(assignment.solutions, key=lambda solution: solution.grade)
        avarage = sum(map(lambda solution: solution.grade, assignment.solutions))
        avarage /= assignment.max_grade * len(assignment.solutions) * 100

        row.append(assignment.name)
        row.append('{:2.2f}%'.format(avarage))
        row.append(str(minimum.grade))
        row.append(str(maximum.grade))
        row.append(str(assignment.max_grade))

        table.append(row)

    return table


def print_assignments():
    '''
    '''
    titles = ['name', 'add date', 'deadline', 'max_grade']

    table = []
    for assignment in Assignment.list_of_assignments:
        row = []

        row.append(assignment.name)
        row.append(assignment.add_date)
        row.append(assignment.deadline)
        row.append(str(assignment.max_grade))

        table.append(row)

    view.print_table(table, titles)


def edit_assignment():
    '''
    '''
    print_assignments()
    assignment = get_assignment_form_user_input()
    if assignment:
        name, deadline, max_grade = get_valid_inputs()
        assignment.name = name
        assignment.deadline = deadline
        assignment.max_grade = max_grade

        Assignment.save_assignments_to_file('assignments.csv')

    else:
        view.print_message('There is no such assignment')
