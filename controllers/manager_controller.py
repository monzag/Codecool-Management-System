import os

import views.view
from models.student import Student
from models.mentor import Mentor


def manager_menu(user):
    '''
    Prints user specific features and asks him for operation
    to perform. Resolve all interacions, util user diecides to exit.

    Returns:
        None
    '''

    titles = 'Hi {}! What would you like to do'.format(user.name)
    options = ['View students', 'View mentors', 'Add mentor', 'Remove mentor',
               'Edit mentor data', 'Exit']

    show_menu = True

    while show_menu:
        os.system('clear')

        option = views.view.get_inputs(labels, title)[0]
        views.view.print_table(options, titles)

        if option == 1:
            view_students()

        if option == 2:
            view_mentors()

        if option == 3:
            add_mentor()

        if option == 4:

            try:
                remove_mentor()
            except ValueError:
                print("Please type in only numbers!")
            except IndexError:
                print ('Mentor with given index does not exist!')

        if option == 0:
            show_menu = False


def view_students():
    '''
    Prints list of every student's name, surname, e-mail, attendance, grade.

    Returns:
            None
    '''

    titles = ["Name", "Surname", "e-mail", "Attendance", "Grade"]
    students_info = []

    for student in Student.list_of_students:
        all_students_info.append([student.name, student.surname,
                                  student.email, student.attendance,
                                  student.grade])

    views.view.print_table(students_info, titles)


def view_mentors():
    '''
    Prints list of every mentor's name, surname and e-mail.

    Returns:
            None
    '''

    titles = ["Name", "Surname", "e-mail"]
    mentors_info = []

    for mentor in Mentors.list_of_mentors:
        mentors_info.append([mentor.name, mentor.surname, mentor.email])

    views.view.print_table(mentors_info, titles)


def add_mentor():
    """
    Creates new mentor and adds mentor to the mentor's list

    Return:
            None
    """
    labels = ["Login", "Password", "Name", "Surname", "e-mail"]
    title = "Provide informations about new mentor"
    inputs = views.view.get_inputs(labels, title)

    new_mentor = Mentor(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])


def remove_mentor():
    '''
    Remove object Mentor from list by index.
    Raise IndexError when index out of range.
    Returns:
            None
    '''
    labels = ["Index"]
    title = "Type index number of mentor to remove"
    index = views.view.get_inputs(labels, title)[0]

    if not index.isdigit():
        raise ValueError

    elif int(index) not in range(len(Mentor.list_of_students)):
        raise IndexError

    else:
        del Mentor.list_of_mentors[int(index)]
