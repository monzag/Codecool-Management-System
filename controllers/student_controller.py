from views import view
from views import view_student

from controllers import assignment_controller
from controllers import codecooler_controller

from models.student import Student
from models.assignment import Assignment


def student_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''

    end = False
    while not end:
        title, options, exit_message = view_student.get_data_to_student_menu(user)
        view.print_menu(title, options, exit_message)
        option = view.input_number()

        if option == 1:
            view_grades(user)
        if option == 2:
            submit_assigment(user)
        if option == 3:
            view_all_students()
        if option == 4:
            change_password(user)
        if option == 5:
            show_general_grade()
        if option == 0:
            end = True


def submit_assigment(student):
    '''
    Choose assignment from list and change status assignment 'done'.
    Save change to file'

    Args:
        student - obj
    '''
    student_index = Student.list_of_students.index(student)
    view_grades(student)

    number = None
    while not number:
        number = view.input_number()

    if number <= Assignment.amount_of_assignments():
        assignment = Assignment.list_of_assignments[number - 1]
        assignment_controller.submit_solution_to_assignment(assignment, student_index)
        Assignment.save_assignments_to_file('assignments.csv')

    else:
        text = view_student.get_invalid_assignment_in_submit()
        view.print_message(text)


def view_grades(student):
    '''
    Show table with data about assignment-grades'
    '''
    student_index = Student.list_of_students.index(student)

    table = assignment_controller.get_assignments_to_table(student_index)
    title_list = view_student.get_title_to_view_grades()
    view.print_table(table, title_list)


def view_all_students():
    '''
    Prints list of every student's name, surname, e-mail.
    '''

    students_info = []

    for student in Student.list_of_students:
        students_info.append([student.name, student.surname, student.email])

    titles = view_student.get_data_to_view_students()
    view.print_table(students_info, titles)


def show_general_grade():
    '''
    Get data about general grade of assignments and display it in table.
    '''
    grades_info = assignment_controller.get_solutions_data()
    titles = view_student.get_titles_to_general_grade()
    view.print_table(grades_info, titles)


def change_password(student):
    '''
    Change old password to new.

    Args:
        student - object
    '''

    codecooler_controller.change_password(student)
    Student.save_codecoolers_to_file('students.csv', Student.list_of_students)
