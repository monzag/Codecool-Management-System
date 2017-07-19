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
