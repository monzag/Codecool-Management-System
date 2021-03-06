from string import punctuation


def get_valid_input(function, text):
    """
    Get input from user and use check function to
    validate input.

    Return:
            str: user input if input is valid
            None: if user input is invalid
    """

    correct = None
    while not correct:
        user_input = input(text)
        correct = function(user_input)

    return user_input


def get_single_input(text):
    """
    Get input from user.

    Return:
            str: user input
    """

    user_input = input(text)

    return user_input


def manager_menu_titles(user):
    """
    Holds string and list of string titles for printing manager_menu_titles
    menu.

    Return:
            list: list of string titles
            str: menu title
            str: exit message
    """

    title = "Manager menu"
    options = ['View students', 'View mentors', 'Add mentor', 'Remove mentor', 'Change password']
    exit_message = "Exit"

    return title, options, exit_message


def view_students_titles():
    """
    Hold strings w column titles for printing students
    list.

    Return:
            list: list of strings
    """

    titles = ["Name", "Surname", "e-mail"]

    return titles


def value_error_message():
    """
    Hold string containing value error message.

    Return:
            str: error message
    """

    message = "Please type in only numbers!"

    return message


def index_error_message():
    """
    Hold string containing index error message.

    Return:
            str: error message
    """

    message = 'Mentor with given index does not exist!'

    return message


def view_mentors_titles():
    """
    Hold strings w column titles for printing mentors
    list.

    Return:
            list: list of strings
    """

    titles = ["Name", "Surname", "e-mail"]

    return titles


def input_titles_for_mentor_add():
    """
    Hold list of strings which are titles for every
    input when creating mentor object.

    Return:
            list: list of strings
    """

    titles = ["Type login: ", "Type password: ", "Type name: ",
              "Type surname: ", "Type mail: "]

    return titles


def input_titles_for_mentor_remove():
    """
    Hold list of strings which are titles for every
    input when creating mentor object.

    Return:
            list: list of strings
    """
    label = ["Index"]
    title = "Type index number of mentor to remove"

    return title, label


def recipent_error():

    print("\nE-mail can not be delivered!\n")
