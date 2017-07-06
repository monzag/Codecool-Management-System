from datetime import datetime

from views import view

from models.assignment import Assignment
from models.student import Student

from controllers import student_controller


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


def create_assigment():
    '''
    Creates new assignment from data provided by mentor.

    Returns:
            None
    '''
    labels = ["Add date", "Deadline", "Max grade"]
    title = "Provide informations about new assignments"
    inputs = views.view.get_inputs(labels, title)

    for student in Student.list_of_students:
        student.assignments_list.append(Assignment(student.login, student.name,
                                        inputs[0], inputs[1], inputs[2]))


def add_assigment(assigment):
    '''
    Adds new assigemnt for every student stored in system

    Parameters:
        assigment : Assigment obj.

    Returns:
        None
    '''
    for student in student_controller.get_students():
        student.assigments_list.append(assigment)


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
