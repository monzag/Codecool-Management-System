import os
import re
from datetime import datetime

from models.assignment import Assignment
from models.solution import Solution
from models.student import Student

from views import assignment_view
from views import view


def print_student_assignments(student_index):
    '''
    Prints table representing students assignments.

    Paramaters:
        student_index : int

    Returns:
        None (void-print)
    '''
    titles = assignment_view.get_titles()
    table = get_assignments_to_table(student_index)
    view.print_table(table, titles)


def get_assignments_to_table(student_index):
    '''
    For a single Student obj. creates data necessery to print in view table

    Paramaters:
        student_index : int

    Returns:
        table : list of lists of strs
    '''
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


    return table


def submit_solution_to_assignment(assignment, student_index):
    '''
    For a specified studnet and assignement creates submision and saves it to file

    Paramaters:
        assignement : Assignement obj.
        student_index : int

    Returns:
        None

    Creates:
        file with solution

    Updates:
        Solution obj.
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
    Returns:
        today date as 'yyyy:mm:dd' string
    '''
    return '{:0>2}:{:0>2}:{:0>2}'.format(datetime.today().year, datetime.today().month, datetime.today().day)

def save_solution_to_file(file_name):
    '''
    Saves user submision to assignment into a file.
    '''
    text = assignment_view.get_submision_text()

    file_path = os.getcwd() + '/data/solutions/' + file_name
    with open(file_path, 'w+') as solution_file:
        solution_file.write(text)


def get_student_total_grade(student_index):
    '''
    Calculates total grade of all uploaded submisions of a student.

    Paramaters:
        student_index : int

    Returns:
        total_grade : str
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
    Fallows remowing student. Removes all his solutions stored in database.

    Parameters:
        student_index : int

    Returns:
        None

    Updated:
        Assignemnt, Solution classes data
    '''
    for assignment in Assignment.list_of_assignments:
        del assignment.solutions[student_index]

    Assignment.save_assignments_to_file('assignments.csv')


def assign_assignments_to_new_student():
    '''
    Fallows adding student. Creates Solution objs. for all assignemts stored in system

    Paramaters:
        None

    Returns:
        None

    Updates:
        Solution, Assignment class data
    '''
    for assignment in Assignment.list_of_assignments:
        assignment.solutions.append(Solution(0, '0', '0'))

    Assignment.save_assignments_to_file('assignments.csv')


def get_assignment_form_user_input():
    '''
    Asks user for input and tries to find Assignment under input index.
    Returns this assignement or None

    Paramaters:
        None

    Returns:
        assignment : Assignment obj.
        or None
    '''
    labels, title = assignment_view.get_assignment_index_outprints()
    user_input = view.get_inputs(labels, title)[0]

    assignment_indexes = [str(assignment_index + 1) for assignment_index in range(len(Assignment.list_of_assignments))]

    if user_input in assignment_indexes:
        assignment = Assignment.list_of_assignments[int(user_input) - 1]

        return assignment

    return None


def create_assignment():
    '''
    Creates new Assignemnt obj. and updated Solutions of all Students objs. in data
    '''
    name, add_date, deadline, max_grade, solutions = get_assignment_data()

    Assignment(name, add_date, deadline, max_grade, solutions)

    Assignment.save_assignments_to_file('assignments.csv')


def get_assignment_data():
    '''
    Gets valid data for all data necessery to create new Assignment obj.

    Parameters:
        None

    Returns:
        name      : str
        add_date  : str
        deadline  : str
        max_grade : int
        solutions : str
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
    Gets valid data form inputs necessery to create new Assignment obj.

    Parameters:
        None

    Returns:
        name      : str
        deadline  : str
        max_grade : int
    '''
    name_message, date_message, grade_message = assignment_view.get_new_assignemt_outprints()

    name = check_valid(is_name, name_message)
    deadline = check_valid(is_date, date_message)
    max_grade = int(check_valid(is_grade, grade_message))

    return name, deadline, max_grade


def check_valid(function, message):
    '''
    Repeat asking for input until function passed returns True

    Paramaters:
        function() : bool
        message    : str

    Returns:
        user_input : str
    '''
    is_valid = None
    while not is_valid:
        user_input = view.get_inputs([message], '')[0]
        is_valid = function(user_input)

    return ''.join(user_input)


def is_name(user_input):
    '''
    Checks if assignment name is valid and does not exist already

    Parameters:
        user_input : str

    Returns:
        bool
    '''
    assignment_names = [assignment.name for assignment in Assignment.list_of_assignments]
    if len(user_input) > 5 and user_input not in assignment_names:
        return True

    return False


def is_grade(user_input):
    '''
    Checks if given *user_input* is valid

    Paramaters:
        user_input : str

    Returns:
        bool
    '''
    if user_input.isdigit():
        if 0 < int(user_input) < 101:
            return True

    return False


def is_date(user_input):
    '''
    Using regex checks if user_input fitts expected date pattern

    Paramaters:
        user_input : str

    Returns:
        bool
    '''
    date_pattern = r'(201[7-9]).(1[0-2]|(0)?[1-9]).([0,1]|[1,2]\d|(0)?[1-9])$'

    match = re.match(date_pattern, user_input)
    if match:
        return True

    return False


def format_date(user_input):
    '''
    Given valid date as string adds '0' if day or month is one char

    Parameters:
        user_input : str

    Returns:
        date : str
    '''
    date_pattern = r'(?P<year>201[7-9]).(?P<month>1[0-2]|(0)?[1-9]).(?P<day>3[0,1]|[1,2]\d|(0)?[1-9])$'

    match = re.match(date_pattern, user_input)

    year = match.group('year')
    month = '{:0>2}'.format(match.group('month'))
    day = '{:0>2}'.format(match.group('day'))

    return '{}:{}:{}'.format(year, month, day)


def get_solutions_data():
    '''
    Findes maximum, minimum and average from every Assignemnt obj. stored
    and returns them as list of list where each next list represents
    different Assignemnt obj.

    Paramaters:
        None

    Returns:
        table : list of lists of str
    '''
    table = []
    for assignment in Assignment.list_of_assignments:
        row = []

        minimum = min(assignment.solutions, key=lambda solution: solution.grade)
        maximum = max(assignment.solutions, key=lambda solution: solution.grade)
        avarage = sum(map(lambda solution: solution.grade, assignment.solutions))
        avarage = avarage / (assignment.max_grade * len(assignment.solutions)) * 100


        row.append(assignment.name)
        row.append('{:2.2f}%'.format(avarage))
        row.append(str(minimum.grade))
        row.append(str(maximum.grade))
        row.append(str(assignment.max_grade))

        table.append(row)

    return table


def print_assignments():
    '''
    Prints list representing every Assignemnt obj. stored in data.

    Paramaters:
        None

    Returns:
        None (void-print)
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
    Lets user choose Assignemnt obj. and change it's attribiutes values

    Paramaters:
        None

    Returns:
        None

    Updates:
        Assignemnt obj.
    '''
    print_assignments()
    assignment = get_assignment_form_user_input()
    if assignment:
        name, deadline, max_grade = get_valid_inputs()
        deadline = format_date(deadline)
        assignment.name = name
        assignment.deadline = deadline
        assignment.max_grade = max_grade

        Assignment.save_assignments_to_file('assignments.csv')

    else:
        no_assignment_message = assignment_view.get_no_assignment_message()
        view.print_message(no_assignment_message)
