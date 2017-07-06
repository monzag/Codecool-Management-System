import os

from views import view

from models.student import Student
from controllers import student_controller
from controllers import assignment_controller
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
    options = ['View students', 'Add assignment', 'Grade assignment',
               'Check attendance', 'Add student', 'Remove student']

    end = False
    while not end:

        os.system('clear')
        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            view_students()
            view.print_message("Press any key to continue.")
            view.wait_until_key_pressed()
        elif option == 2:
            add_assigment()
        elif option == 3:
            grade_assigment()
        elif option == 4:
            check_attendance()
        elif option == 5:
            add_student()
        elif option == 6:
            remove_student()
        elif option == 0:
            end = True

def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
        Nothing, it just prints the student list.
    '''

    titles = ["Name", "Surname", "e-mail", "Attendance"]
    students_info = []

    for student in Student.list_of_students:
        students_info.append([student.name, student.surname,
                             student.email, str(student.attendance)])

    view.print_table(students_info, titles)


def add_assignment():
    '''
    Creates new assignment and adds it to assignment list.
    '''
    pass


def grade_assignment():
    '''
    should use controllers.assigment_controller to create
        list of assigments

    should use view.print_assigments to print assigments
        (along with numbers to call exact assigment)

    should use view.input_umber() to select assigment

    should use controllers.assigment_controller.change_grade() to change grade
    '''
    pass


def check_attendance():
    """
    Chooses student by login and grades its attendance for today.
    Adds one day to days_passed after checking.
    """
    title = "Student attendance for today"
    exit_message = 'Back to Main Menu (NOTICE: You will have to check whole attendance again for today!)'
    options = ['Present', 'Late', 'Absent']

    for student in Student.list_of_students:
        index = Student.list_of_students.index(student)
        fullname = student.name + ' ' + student.surname

        view.print_message(fullname)
        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option in range(1, len(options) + 1):
            today_attendance = options[option - 1]
            student.attendance = update_attendance(index, student.days_passed, student.attendance, today_attendance)
        elif option == 0:
            pass # load data again
        else:
            # load data again
            view.print_message('There is no such option. Press any key to start again.')
            view.wait_until_key_pressed()


def update_attendance(index, days_passed, attendance, today_attendance):
    """
    Updates the attendance value.

    Args:
        index (int) - index of a student
        days_passed (int) - number of days passed in school so far
        attendance (int) - attendance value
        today_attendance (str) - option chosen (Present/Late/Absent)

    Returns:
        attendance (int) - updated attendance
    """
    if today_attendance == 'Present':
        days_of_presence = (attendance * 0.01) * days_passed
        attendance += (days_of_presence + 1) / (days_passed + 1)
    elif today_attendance == 'Late':
        todays_value = 100 / days_passed
        attendance -= todays_value * 0.2
    elif today_attendance == 'Absent':
        todays_value = 100 / days_passed
        attendance -= todays_value

    Student.list_of_students[int(index)].days_passed += 1

    if attendance > 100:
        attendance = 100

    return attendance

def add_student():
    """
    Creates new student and adds it to the students list.

    Returns:
            Nothing, it just adds the student to the list.
    """
    labels = ["Name", "Surname", "Login", "Password", "e-mail"]
    title = "Provide informations about new student"
    inputs = view.get_inputs(labels, title)

    new_student = Student(100, 1, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])

    Student.save_students()


def remove_student():
    """
    Removes object Student from list by index.

    Returns:
        Nothing, it just removes the student.
    """
    try:
        index = get_student_index()
    except (ValueError, IndexError):
        view.print_message('Index does not exist!')

    del Student.list_of_students[int(index)]

    Student.save_students()

def get_student_index():
    """
    Gets an index of student from student's list.
    Raises IndexError when index out of range.
    Raises ValueError when index is not int.

    Returns:
        index (int)
    """
    labels = ["Index"]
    title = "Type index number of student"
    index = view.get_inputs(labels, title)[0]

    if not index.isdigit():
        raise ValueError("Please type only numbers!")

    elif int(index) not in range(len(Student.list_of_students)):
        raise IndexError('Mentor with given index does not exist!')

    else:
        return int(index) - 1
