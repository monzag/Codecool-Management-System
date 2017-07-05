import controllers.student_controller 


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
    '''
    if len(assigemnts) > 0:
        grades = 0
        max_grades = 0

        for assigment in assigments:
            grades += assigment.grade
            max_grades += assigment.max_grade
        
        return grades/max_grades * 100
            
    else:
        return 0