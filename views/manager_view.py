from string import punctuation


def get_valid_input(function, text):

    correct = None
    while not correct:
        user_input = input(text)
        correct = function(user_input)

    return user_input

def get_single_input(text):

    user_input = input(text)

    return user_input
