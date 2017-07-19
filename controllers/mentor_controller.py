from views import view
import os
from models.attendance import Attendance
from models.assignment import Assignment
from models.student import Student
from controllers import student_controller
from controllers import assignment_controller
from controllers import codecooler_controller
from controllers.mail_validation import *
from views import mentor_view
import datetime


def mentor_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interactions, util user diecides to exit.

    Returns:
        None
    '''
    title, exit_message, options = mentor_view.menu_labels(user)

    end = False
    while not end:

        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            view_students()
            view.print_message("Press any key to continue.")
            view.wait_until_key_pressed()
        elif option == 2:
            assignment_controller.create_assignment()
        elif option == 3:
            grade_assignment()
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

    titles = ["Name", "Surname", "e-mail", "Attendance", 'Total grade']
    students_info = []

    for student in Student.list_of_students:
        students_info.append([student.name, student.surname,
                             student.email, str(student.get_attendance()), str(student.total_grade)])

    view.print_table(students_info, titles)


def grade_assignment():
    '''
    Prints the list of students to choose a student.
    Then prints assignments of the student.
    Then asks the user for the choice and changing the grade.
    '''
    view_students()
    student_id = None
    while not student_id:
        student_id = view.input_number()

    for student in Student.list_of_students:
        if Student.list_of_students.index(student) == student_id - 1:
            assignment_controller.view_student_assignments(student)

            assignment_id = None
            while not assignment_id:
                assignment_id = view.input_number()

                for assignment in student.assignments_list:
                    if student.assignments_list.index(assignment) == assignment_id - 1:
                        new_grade = get_new_grade(assignment.max_grade)
                        student.assignments_list[assignment_id - 1].grade = new_grade

                        student.total_grade = student.calculate_total_grade()
                        Student.save_students()
                        Assignment.save_assignments_to_file()


def get_new_grade(max_grade):
    '''
    Asks the user to enter the new grade.
    Checks if it's positive int and not greater than max_grade.

    Args:
        max_grade (int) - max possible grade of assignment

    Returns:
        new_grade (int) - new grade to change to
    '''
    new_grade = None
    while new_grade not in range(0, max_grade + 1):
        view.print_message("Please provide new grade value.")
        new_grade = view.input_number()

    return new_grade


def check_attendance():
    """
    Prints the name of the student if he didn't have been checked today.
    Adds its attendance for today based on input.
    Saves to file.
    """

    title, exit_message, options = mentor_view.data_to_check_attendance()
    students = Student.list_of_students
    attendances = Attendance.list_of_attendance

    for student in students:
        if datetime.date.today() not in [att.date for att in attendances if att.student_login == student.login]:
            os.system('clear')

            fullname = student.name + ' ' + student.surname
            view.print_message(fullname)
            view.print_menu(title, options, exit_message)

            option = get_option(options)
            if option == 0:
                break
            today_attendance = get_today_attendance(option)
            attendance = Attendance(student.login, datetime.date.today(), today_attendance)
            attendances.append(attendance)
            attendance.save_attendance_to_file('attendance.csv')

    mentor_view.attendance_checked()


def get_option(options):

    option = None

    while option not in range(0, len(options) + 1):
        option = view.input_number()

    return option


def get_today_attendance(option):

    if option == 1:
        return '100'
    elif option == 2:
        return '80'
    elif option == 3:
        return '0'


def add_student():
    """
    Creates new student and adds it to the students list.

    Returns:
            Nothing, it just adds the student to the list.
    """

    name, surname, login, email = get_valid_data()
    password = codecooler_controller.get_random_password()
    print('Password: ', password)
    total_grade = 100
    new_student = Student(100, 1, total_grade, name, surname, login, password, email)

    Student.save_students()


def get_valid_data():
    '''
    Get valid data and return it.

    Returns:
        name, surname, login, email - string
    '''
    name_txt, surname_txt, login_txt, email_txt = mentor_view.get_data_to_add_student()
    name = check_valid(is_alpha, name_txt)
    surname = check_valid(is_alpha, surname_txt)
    login = check_valid(is_login_already_exist, login_txt)
    email = check_valid(check_mail, email_txt)

    return name, surname, login, email


def check_valid(function, message):
    '''
    Get input from user and check valid by proper function.

    Args:
        function
        message - str

    Returns:
        user_input - string
    '''
    is_valid = None
    while not is_valid:
        title = 'Write the data below'
        user_input = view.get_inputs([message], title)[0]
        is_valid = function(user_input)
    return user_input


def is_login_already_exist(user_input):
    '''
    Check that user_input is not empty string.
    If not, check that login isn't occupied by another students.
    Returns True if not.

    Args:
        user_input - string

    Returns:
        bool
    '''
    if len(user_input) > 0:
        for student in Student.list_of_students:
            if student.login == user_input:
                return None

        return True


def is_alpha(user_input):
    '''
    Returns True if user_input is alpha.

    Args:
        user_input - string

    Returns:
        bool
    '''
    if user_input.isalpha():
        return True


def remove_student():
    """
    Removes object Student from list by index.

    Returns:
        Nothing, it just removes the student.
    """
    view_students()

    try:
        index = get_student_index()
        del Student.list_of_students[int(index)]
    except (ValueError, IndexError):
        view.print_message('Index does not exist!')

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

    elif int(index) - 1 not in range(len(Student.list_of_students)):
        raise IndexError('Mentor with given index does not exist!')

    else:
        return int(index) - 1
