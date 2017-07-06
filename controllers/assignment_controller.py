from datetime import datetime

from views import view

from models.assignment import Assignment
from models.student import Student

import controllers.student_controller


def get_assignments_to_table(student):
    '''
    Given Student obj. creates table for view.print_table

    Parameters:
        student: Student obj.

    Returns:
        table: 2d list of table prints
    '''
    table = []
    for assignment in student.assignments_list:
        table.append([assignment.name,     assignment.status,     assignment.submit_date,
                      assignment.deadline, str(assignment.grade), str(assignment.max_grade)])

    return table


def create_assignment():
    '''
    Creates new assignment from data provided by mentor.

    Returns:
            None
    '''
    deadline = get_deadline()
    max_grade = get_max_grade()
    add_date = get_add_date()

    for student in Student.list_of_students:
        student.assignments_list.append(Assignment(student.login, student.name,
                                        add_date, deadline, max_grade))

    Assignment.save_assignments_to_file()


def add_assignment(assigment):
    '''
    Adds new assigemnt for every student stored in system

    Parameters:
        assigment : Assigment obj.

    Returns:
        None
    '''
    for student in student_controller.get_students():
        student.assigments_list.append(assigment)


def calculate_total_grade(list_of_assigments):
    '''
    Given list of assigments calculates total grade

    Paramters:
        list_of_assigments : list of Assigment obj.

    Returns:
        total_grade : int representing percents
    '''
    total_grade = 0

    if len(assigemnts) > 0:
        grades = 0
        max_grades = 0

        for assigment in assigments:
            grades += assigment.grade
            max_grades += assigment.max_grade

        total_grade = grades/max_grades * 100

    return total_grade


def change_assignment_to_done(assignment):
    '''
    Change undone assigment to done, and adds datetime
    obj. representing today date as it's sumbit date

    Paramateres:
        assigment: Assigment obj.

    Returns:
        None
    '''
    submit_date = '{}:{:0>2}:{:0>2}'.format(datetime.today().year, datetime.today().month, datetime.today().day)

    if assignment.status == 'undone':
        assignment.status = 'done'
        assignment.submit_date = submit_date


def view_student_assignments(student):
    '''
    '''
    labels = ['name', 'status', 'submit_date', 'deadline', 'grade', 'max_grade']
    table = get_assignments_to_table(student)

    view.print_table(table, labels)


def get_add_date():
    return '{}:{}:{}'.format(datetime.today().year, datetime.today().month, datetime.today().day)

def get_deadline():

    deadline = None

    while deadline == None:

        deadline_labels = ["Day", "Month", "Year"]
        deadline_title = "Type deadline"
        deadline_input = view.get_inputs(deadline_labels, deadline_title)

        if all([item.isdigit() for item in deadline_input]):
            deadline = deadline_input[0] + "-" + deadline_input[1] + "-" + deadline_input[2]
            return deadline
        else:
            deadline = None

def get_max_grade():

    max_grade = None

    while max_grade == None:

        labels = [ "Max grade"]
        title = "Type maximal grade"
        inputs = view.get_inputs(labels, title)

        if inputs[0].isdigit():
            max_grade = int(inputs[0])
            return max_grade
        else:
            max_grade = None
