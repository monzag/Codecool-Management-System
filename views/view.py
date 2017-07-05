def print_menu(title, options, exit_message):

    option_number = 1

    print('{}:'.format(title))
    for option in options:
        print('    ({}) '.format(option_number) + option)
        option_number += 1
    print('    (0) {}'.format(exit_message))
    print('')


def print_table():
    pass


def get_inputs(labels, title):

    inputs = []

    print(title)
    for label in labels:
        answer = (input('{} '.format(label)))
        inputs.append(answer)
    print('')

    return inputs


def print_message(message):

    print(message)
    print('')


def print_welcome_screen():
    print('''''')
    
def view.wait_until_key_pressed():
    input("PRESS ANY KEY TO CONTINUE")
