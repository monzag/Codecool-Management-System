import os

from views import view

from controllers import student_controller
from controllers import mentor_controller


def manager_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''
    title = 'Hi {}! What would you like to do'.format(user.name)
    otions = ['View students', 'View mentors', 'Add mentor', 'Remove mentor',
              'Edit mentor data', 'Exit']

    end = False
    while end:
        os.system('clear')

        view.print_menu(title, options)
        option = view.input_number()

        if option == 1:
            view_students()
        if option == 2:
            view_mentors()
        if option == 3:
            add_mentor()
        if option == 4:
            remove_mentor()
        if option == 5:
            edit_mentor()
        if option == 0:
            end = True


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
            None
    '''
    students = students_controller.get_students()
    titles = ["Name", "Surname", "e-mail", "Attendance", "Grade"]
    all_students_info = []

    for student in students:
        all_students_info.append([student.name, student.surname,
                                  student.email, student.attendance,
                                  student.grade])

    views.view.print_table(all_students_info, titles)


def view_mentors():
    '''
    Prints list of every mentor's name, surname and e-mail.

    Returns:
            None
    '''

    mentors = mentor.controller.get_mentors()
    titles = ["Name", "Surname", "e-mail"]
    all_mentors_info = []

    for mentor in mentors:
        all_mentors_info.append([mentor.name, mentor.surname, mentor.email])

    views.view.print_table(all_mentors_info, titles)


def add_mentor():
    '''
    should use views.view.get_new_mentor_data() to get inputs about new mentor

    should use controllers.mentor_controller.create_new_mentor() to create mentor
    '''
    pass


def remove_mentor():
    '''
    should use controllers.mentor_controller to get list of all mentors
        (along with numbers)

    should use views.view.print_mentors() to print all mentors

    should use views.view.get_number() to detrmine which mentor should be deleted

    should use controllers.mentor_controler.remove_mentor() to remove mentor
    '''
    pass


def edit_mentor():
    '''
    should use controllers.mentor_controller to get list of all mentors
        (along with numbers)

    should use views.view.print_mentors() to print all mentors

    should use views.view.get_number() to detrmine which mentor should be edited

    should use controllers.mentor_controller.edit_student() to edit mentors data
    '''
    pass
