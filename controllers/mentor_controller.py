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

        views.view.print_menu(title, options, exit_message)
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
            remove_student()
        if option == 0:
            end = True


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
        Nothing, it just prints the student list.
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
    '''
    should use controllers.assigment_controller to create
        list of assigments

    should use views.view.print_assigments to print assigments
        (along with numbers to call exact assigment)

    should use views.view.input_umber() to select assigment

    should use controllers.assigment_controller.change_grade() to change grade
    '''
    pass


def check_attendance():
    """
    Chooses student by login and grades its attendance for today.
    Adds one day to days_passed after checking.
    """
    title = "Student attendance for today"
    exit_message = 'Back to Main Menu'
    options = ['Present', 'Late', 'Absent']

    end = False
    while not end:
        view_students()

        try:
            index = get_student_index()
        except ValueError, IndexError:
            return views.view.print_message('Index does not exist!')

        fullname = Student.list_of_students[int(index)].name + ' ' + Student.list_of_students[int(index)].surname
        attendance = Student.list_of_students[int(index)].attendance
        days_passed = Student.list_of_students[int(index)].days_passed

        views.view.print_message(fullname, "\nAttendance: ", attendance)
        views.view.print_menu(title, options, exit_message)
        option = is_option_valid(len(options))

        if option == 1:
            Student.list_of_students[int(index)].days_passed += 1
        elif option == 2:
            todays_value = 100 / days_passed
            attendance -= todays_value * 0.2
            Student.list_of_students[int(index)].attendance = attendance
            Student.list_of_students[int(index)].days_passed += 1
        elif option == 3:
            todays_value = 100 / days_passed
            attendance = -= todays_value
            Student.list_of_students[int(index)].attendance = attendance
            Student.list_of_students[int(index)].days_passed += 1
        elif option == 0:
            end = True
        else:
            views.view.print_message('There is no such option. Press any key to start again.')
            views.view.wait_until_key_pressed()


def add_student():
    """
    Creates new student and adds it to the students list.

    Returns:
            Nothing, it just adds the student to the list.
    """
    labels = ["Name", "Surname", "Login", "Password", "e-mail"]
    title = "Provide informations about new student"
    inputs = views.view.get_inputs(labels, title)

    new_student = Student(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])


def remove_student():
    """
    Removes object Student from list by index.

    Returns:
        Nothing, it just removes the student.
    """
    try:
        index = get_student_index()
    except ValueError, IndexError:
        return views.view.print_message('Index does not exist!')

    del Mentor.list_of_mentors[int(index)]

def get_student_index():
    """
    Gets an index of student from student's list.
    Raises IndexError when index out of range.
    Raises ValueError when index is not int.

    Returns:
        index (int)
    """
    labels = ["Index"]
    title = "Type index number of student to remove"
    index = views.view.get_inputs(labels, title)[0]

    if not index.isdigit():
        raise ValueError("Please type only numbers!")

    elif int(index) not in range(len(Mentor.list_of_students)):
        raise IndexError('Mentor with given index does not exist!')

    else:
        return int(index)


def is_option_valid(options_number):

    try:
        option = input_number()
        if option in range(options_number + 1):
            return option
        else:
            return False
    except ValueError:
        return False
