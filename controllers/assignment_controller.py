from datetime import datetime

import controllers.student_controller 


def load_assigments_from_file():
    '''
    '''
    pass


def save_assigments_to_file():
    '''
    '''
    pass


def create_assigment():
    '''
    '''
    pass


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


def change_assigment_to_done(assigment):
    '''
    Change undone assigment to done, and adds datetime
    obj. representing today date as it's sumbit date

    Paramateres:
        assigment: Assigment obj.
    
    Returns:
        None
    '''
    submit_date = datetime.today()

    if assigment.status == 'undone':
        assigment.status = 'done'
        assigment.submit_date = submit_date
