import os

from views import view

from controllers import student_controller
from controllers import assigment_controller
from controllers import codecooler_controller


def mentor_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    exit_message = 'Exit'
    options = ['View students', 'Add assigment', 'Grade assigment', 'Check attendence', 'Add student', 'Remove student']

    end = False
    while not end:
        os.system('clear')

        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            view_students()
        if option == 2:
            add_assigment()
        if option == 3:
            grade_assigment()
        if option == 4:
            check_attendance()
        if option == 5:
            add_student()
        if option == 6:
            try:
                remove_student()
            except ValueError, IndexError:
                views.view.print_message('Index does not exist!')
        if option == 0:
            end = True


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
            None
    '''

    titles = ["Name", "Surname", "e-mail", "Attendance", "Grade"]
    students_info = []

    for student in Student.list_of_students:
        students_info.append([student.name, student.surname,
                                  student.email, student.attendance,
                                  student.grade])

    views.view.print_table(students_info, titles)


def add_assigment():
    '''
    Creates new assignment and adds it to assignment list.
    '''
    pass


def grade_assigment():
    '''emove
    should use controllers.assigment_controller to create
        list of assigments

    should use views.view.print_assigments to print assigments
        (along with numbers to call exact assigment)

    should use views.view.input_umber() to select assigment

    should use controllers.assigment_controller.change_grade() to change grade
    '''
    pass


def check_attendance():


def add_student():
    """
    Creates new student and adds it to the students list

    Returns:
            None
    """
    labels = ["Name", "Surname", "Login", "Password", "e-mail"]
    title = "Provide informations about new student"
    inputs = views.view.get_inputs(labels, title)

    new_student = Student(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])


def remove_student():
    """
    Removes object Student from list by index.
    Raises IndexError when index out of range.
    Raises ValueError when index is not int.

    Returns:
            None
    """
    labels = ["Index"]
    title = "Type index number of student to remove"
    index = views.view.get_inputs(labels, title)[0]

    if not index.isdigit():
        raise ValueError("Please type only numbers!")

    elif int(index) not in range(len(Mentor.list_of_students)):
        raise IndexError('Mentor with given index does not exist!')

    else:
        del Mentor.list_of_mentors[int(index)]
