import os
import datetime
import smtplib

from models.login import Logins
from models.attendance import Attendance
from models.assignment import Assignment
from models.student import Student
from models.mentor import Mentor

from controllers import student_controller
from controllers import assignment_controller
from controllers import codecooler_controller
from controllers.mail_validation import *
from controllers.send_mail import *

from views import view
from views import mentor_view


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
            assignment_controller.edit_assignment()
        elif option == 4:
            grade_assignment()
        elif option == 5:
            check_attendance()
        elif option == 6:
            add_student()
        elif option == 7:
            remove_student()
        elif option == 8:
            change_password(user)
        elif option == 0:
            end = True


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
        Nothing, it just prints the student list.
    '''

    titles = mentor_view.data_to_view_students()
    students_info = []

    for student_index, student in enumerate(Student.list_of_students):

        table_row = []
        table_row.append(student.name)
        table_row.append(student.surname)
        table_row.append(student.email)
        table_row.append(str(student.get_attendance()))
        table_row.append(assignment_controller.get_student_total_grade(student_index))

        students_info.append(table_row)

    view.print_table(students_info, titles)


def grade_assignment():
    '''
    Prints the list of students to choose a student.
    Then prints assignments of the student.
    Then asks the user for the choice and changing the grade.
    '''
    if Student.list_of_students == []:
        return mentor_view.print_empty_database_msg()

    view_students()
    student_index = get_student_index()
    if student_index is not None:

        assignment_controller.print_student_assignments(student_index)
        assignment = assignment_controller.get_assignment_form_user_input()

        if assignment:
            solution = assignment.solutions[student_index]

            if solution.can_be_graded:

                view.print_message(solution.get_content())
                solution.grade = get_new_grade(assignment.max_grade)
                Assignment.save_assignments_to_file('assignments.csv')

            else:
                mentor_view.assignment_already_graded()

        else:
            mentor_view.no_such_assignment()

    else:
        mentor_view.index_doesnt_exist()


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
    '''
    Prints the name of the student if he hasn't been checked today.
    Adds his attendance for today based on input.
    Updates attendance list and saves to file.
    '''

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
            if option == 4:  # skips a student
                continue
            elif option == 0:
                break  # breaks checking for now

            update_attendance(option, student, attendances)

    show_attendance_status(students, attendances)


def update_attendance(option, student, attendance_list):
    '''
    Updates the attendance list and saves to file.

    Args:
        option (int) - option choosed from menu
        student (Student obj)
        attendance_list (class Attendance list)
    '''
    today_attendance = get_today_attendance(option)
    attendance = Attendance(student.login, datetime.date.today(), today_attendance)
    attendance_list.append(attendance)
    attendance.save_attendance_to_file('attendance.csv')


def show_attendance_status(students, attendances):

    if attendances == []:
        return mentor_view.print_empty_database_msg()

    unchecked_students = 0

    for student in students:
        if datetime.date.today() not in [att.date for att in attendances if att.student_login == student.login]:
            unchecked_students += 1

    if unchecked_students == 0:
        return mentor_view.print_all_checked()

    elif unchecked_students > 0:
        return mentor_view.print_how_many_unchecked(unchecked_students)


def get_option(options):
    '''
    Asks user to choose an option and validates if it's accurate.

    Args:
        options (list) - list of options

    Returns:
        option (int)
    '''
    option = None

    while option not in range(0, len(options) + 1):
        option = view.input_number()

    return option


def get_today_attendance(option):

    if option == 1:  # present
        return '100'
    elif option == 2:  # late
        return '80'
    elif option == 3:  # absent
        return '0'


def add_student():
    """
    Creates new student and adds it to the students list.

    Returns:
            Nothing, it just adds the student to the list.
    """

    name, surname, login, email = get_valid_data()
    password = codecooler_controller.get_random_password()
    new_student = Student(name, surname, login, password, email)
    assignment_controller.assign_assignments_to_new_student()

    Student.save_codecoolers_to_file('students.csv', Student.list_of_students)

    msg = 'Password: {}'.format(password)

    try:
        send_email(msg, email)
        view.print_send_password_msg()

    except smtplib.SMTPRecipientsRefused:
        mentor_view.recipent_error()


def get_valid_data():
    '''
    Get valid data and return it.

    Returns:
        name, surname, login, email - string
    '''
    name_txt, surname_txt, login_txt, email_txt = mentor_view.get_data_to_add_student()
    name = check_valid(is_alpha, name_txt)
    surname = check_valid(is_alpha, surname_txt)
    login = check_valid(Logins.is_login_valid, login_txt)
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
        title = mentor_view.title_check_valid()
        user_input = view.get_inputs([message], title)[0]
        is_valid = function(user_input)

    return ''.join(user_input)


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
    '''
    Removes object Student from list by index.

    Returns:
        If there are no students, returns printed message.
        Otherwise, returns nothing, only removes student.
    '''
    students = Student.list_of_students
    if students == []:
        return mentor_view.print_empty_database_msg()

    view_students()
    student_index = get_student_index()

    if student_index is not None:
        students.remove(students[int(student_index)])
        assignment_controller.remove_student_solutions(student_index)

        Student.save_codecoolers_to_file('students.csv', students)
        clean_attendance_data()

    else:
        mentor_view.index_doesnt_exist()


def clean_attendance_data():
    '''
    Eliminates all duplicate or outdated attendances (i.e. after removing students)
    '''
    attendances = Attendance.list_of_attendance
    atts_to_remove = []

    for attendance in attendances:
        if attendance.student_login not in [student.login for student in Student.list_of_students]:
            atts_to_remove.append(attendance)

    for att in atts_to_remove:
        attendances.remove(att)

    remove_duplicates(attendances)

    Attendance.overwrite_file('attendance.csv')


def remove_duplicates(attendances):
    '''
    Checks if there are any equal attendances.
    If True, removes any duplicates.

    Args:
        attendances (class Attendance list)
    '''

    for att in attendances:
        for att2 in Attendance.list_of_attendance:
            if att.__eq__(att2):
                attendances.remove(att2)


def get_student_index():
    """
    Gets an index of student from student's list.
    Raises IndexError when index out of range.
    Raises ValueError when index is not int.

    Returns:
        index (int)
    """
    labels, title = mentor_view.data_get_student_index()
    user_input = view.get_inputs(labels, title)[0]

    student_indexes = [str(student_index + 1) for student_index in range(len(Student.list_of_students))]

    if user_input in student_indexes:
        return int(user_input) - 1

    return None


def change_password(user):
    '''
    Change old password to new. Save changes.

    Args:
        user - object
    '''

    codecooler_controller.change_password(user)
    Mentor.save_codecoolers_to_file('mentors.csv', Mentor.list_of_mentors)
