import os
import sys
import termios
import getpass


def print_menu(title, options, exit_message):
    '''Prints the menu options.

    Args:
        title (str) - title of the menu
        options (list) - list of strings as option names
        exit_message (str) - string to be printed as the last option to quit

    Returns:
        Nothing, it just prints the menu in the console.import os
import sys

from views import view

from models.codecooler import Codecooler
from models.student import Student
from models.employee import Employee
from models.mentor import Mentor
from models.manager import Manager

from controllers import student_controller
from controllers import employee_controller
from controllers import mentor_controller
from controllers import manager_controller
    '''

    option_number = 1

    print('{}:'.format(title))
    for option in options:
        print('    ({}) '.format(option_number) + option)
        option_number += 1
    print('    (0) {}'.format(exit_message))
    print('')


def print_table(table, title_list):
    '''Prints the table with provided data.

    Args:
        table (list) - list of lists with data to be printed
        title_list (list) - list of column titles to be printed at the top

    Returns:
        Nothing, it just prints the table in the console.
        If table is empty or its data is invalid, then returns None.
    '''

    if is_table_wrong(table, title_list):
        return None

    MIN_COLUMN_WIDTH = 8
    CELL_PADDING = 2
    columns_amount = len(table[0])

    outer_row = create_border_row(table, columns_amount, title_list, 'outer', MIN_COLUMN_WIDTH, CELL_PADDING)
    middle_row = create_border_row(table, columns_amount, title_list, 'middle', MIN_COLUMN_WIDTH, CELL_PADDING)
    title_row = create_data_row(table, 1, title_list, MIN_COLUMN_WIDTH, CELL_PADDING, is_title=True)

    print(outer_row)
    print(title_row)
    for i in range(len(table)):
        data_row = create_data_row(table, i, title_list, MIN_COLUMN_WIDTH, CELL_PADDING, is_title=False)
        print(middle_row)
        print(data_row)
    print(outer_row)


def is_table_wrong(table, title_list):
    '''
    Checks if table is empty, has different amount of entries in lists
    or has different amount of entries between lists and titles.

    Args:
        table (list) - list of lists with data
        title_list (list) - list containing table headers

    Returns:
        bool
    '''

    if table == []:
        print_message("The table is empty! Check if CSV exists in a current folder.")
        return True
    for row in table:
        if len(table[0]) != len(row):
            print_message("Rows has different amount of data. Check the CSV file.")
            return True
    if len(title_list) != len(table[0]):
        print_message("The table has wrong amount of data! Compare title_list with CSV file.")
        return True

    return False


def find_max_string_length(table, item_index, title_list):
    '''
    Finds longest string from all items of a given column index.

    Args:
        table (list) - list of lists of all the strings
        item_index (int) - specific index in lists in table
        title_list (list) - list containing table headers

    Returns:
        int - longest length value for a given index
    '''

    longest_string = ''

    for a_list in table:
        if len(str(a_list[item_index])) > len(longest_string):
            longest_string = str(a_list[item_index])

    if len(str(title_list[item_index])) > len(longest_string):
        longest_string = str(title_list[item_index])

    return len(longest_string)


def create_border_row(table, columns_amount, title_list, row_type, MIN_COLUMN_WIDTH, CELL_PADDING):
    '''
    Generates a string to be later printed as an outer row in a table.

    Args:
        table (list) - list of lists of all the strings
        columns_amount (int) - number of columns
        title_list (list) - list containing table headers
        row_type (str) - 'outer' or 'middle'
        MIN_COLUMN_WIDTH (int)
        CELL_PADDING (int)

    Returns:
        border_row (str) - string ready to be printed
    '''

    border_row = '|'

    for column in range(columns_amount):
        dashes_to_add = find_max_string_length(table, column, title_list)
        if dashes_to_add >= MIN_COLUMN_WIDTH:
            border_row = border_row + ('-' * (dashes_to_add + CELL_PADDING) + '|')
        else:
            border_row = border_row + ('-' * MIN_COLUMN_WIDTH + '|')

    if row_type == 'outer':
        for char in border_row:
            border_row.replace('|', '-')

    return border_row


def create_data_row(table, list_index, title_list, MIN_COLUMN_WIDTH, CELL_PADDING, is_title=False):
    '''
    Generates a string to be later printed as a row with data in a table.

    Args:
        table (list) - list of lists of all the strings
        list_index (int) - index of a specific row (list) in a table
        title_list (list) - list containing table headers
        MIN_COLUMN_WIDTH (int)
        CELL_PADDING (int)
        is_title: boolean (if True, creates title row, if False, creates data row)

    Returns:
        data_row: string ready to be printed
    '''

    data_row = '|'

    for column in range(len(table[list_index])):
        max_string_length = find_max_string_length(table, column, title_list)
        if max_string_length >= MIN_COLUMN_WIDTH:
            cell_width = max_string_length + CELL_PADDING
        else:
            cell_width = MIN_COLUMN_WIDTH

        if is_title == False:
            data_row = data_row + (table[list_index][column].center(cell_width, ' ')) + '|'
        else:
            data_row = data_row + (title_list[column].center(cell_width, ' ')) + '|'

    return data_row


def get_inputs(labels, title):
    '''Prints input prompts and gets inputs.

    Args:
        labels (list) - list containing input details
        title (str) - title of input prompt

    Returns:
        inputs (list) - list with inputs received
    '''
    inputs = []

    print(title)
    for label in labels:
        answer = (input('{}:  '.format(label)))
        inputs.append(answer)
    print('')

    return inputs


def print_message(message):

    print(message)
    print('')


def print_welcome_screen():

    file_path = os.getcwd() + "/views/start_message.txt"
    with open(file_path, "r") as startup:
        for line in startup:
            print(line, end='')


def input_login():

    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    login = input("  LOGIN:  ")

    return login


def input_password():

    print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    password = getpass.getpass("  PASSWORD:  ")

    return password


def wait_until_key_pressed():
    ''' Waits for a key press on the console and returns it. '''

    result = None
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    try:
        result = sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    os.system("clear")
    return result

def print_end_screen():

    with open("quit_message.txt", "r") as startup:
        for line in startup:
            print(line, end='')
    print('''''')


print_welcome_screen()
wait_until_key_pressed()
input_login()
input_password()
print_end_screen()
wait_until_key_pressed()

table = [['asdfageg', 'adafewg', 'w,a', '34235', '3424 4524 sdfsdf2 wedsdasd s'], ['asdfageg', 'adafewg', 'w,a', '34235', '3424 4524 sdfsdf2 wedsdasd s'], ['asdfageg', 'adafewg', 'w,a', '34235', '3424 4524 sdfsdf2 wedsdasd s'],
['asdfageg', 'adafewg', 'w,a', '34235', '3424 4524 sdfsdf2 wedsdasd s'], ['asdfageg', 'adafewg', 'w,a', '34235', '3424 4524 sdfsdf2 wedsdasd s'], ['asdfageg', 'adafewg', 'w,a', '34235', '3424 4524 sdfsdf2 wedsdasd s']]

title_list = ['costam', 'nictam', '3453sfsdfsfds', 'guwno', 'blablaasf']

print_table(table, title_list)
