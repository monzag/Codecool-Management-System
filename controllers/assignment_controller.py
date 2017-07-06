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
    # submit_date = datetime.today()

    if assignment.status == 'undone':
        assignment.status = 'done'
        assignment.submit_date = '01:01:2016' # submit_date
