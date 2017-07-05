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
        Nothing, it just prints the menu in the console.
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
    columns_number = len(table[0])

    outer_row = create_outer_row(table, columns_number, title_list, MIN_COLUMN_WIDTH, CELL_PADDING)


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

    return len(longest_value)


def create_outer_row(table, columns_number, title_list, MIN_COLUMN_WIDTH, CELL_PADDING):
    '''
    Generates a string to be later printed as an outer row in a table.

    Args:
        table (list) - list of lists of all the strings
        columns_number (int) - number of columns
        title_list (list) - list containing table headers
        MIN_COLUMN_WIDTH (int)
        CELL_PADDING (int)

    Returns:
        outer_row (str) - string ready to be printed
    '''

    outer_row = ''

    for column in range(columns_number):
        dashes_to_add = find_max_string_length(table, column, title_list)
        if dashes_to_add >= MIN_COLUMN_WIDTH:
            outer_row = outer_row + ('-' * (dashes_to_add + CELL_PADDING))
        else:
            outer_row = outer_row + ('-' * MIN_COLUMN_WIDTH)

    additional_dashes = columns_number - 1
    outer_row = outer_row + ('-' * additional_dashes)

    return outer_row


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
        answer = (input('{} '.format(label)))
        inputs.append(answer)
    print('')

    return inputs


def print_message(message):

    print(message)
    print('')


def print_welcome_screen():
    print('''

                                           ``-://++ooo/.
                                         -o+++ssssooooss+:`
                                       `/++///+ososssosy++o+-`
                                      -o++++o+:.`  `-:+so+//+o-
                                     /sssyy+            /+//+o+
                                    /soooss`             /oossy.
                                    :sooss-               +ysss:
                                    `sssys`              `ssoos+
                                     osso+o`             osoooso
                                     :o+//+o`          `:yysss+
                                     `+++/+oyo/:.` `-:+o++++o-
                                       .:+++ssoosssys++//+o/`
                                          -/syoooosssso++o-
                                            `-+o+//::--``




     `:+oo+:     -/+oo+:`    /++++/:`    :+++++.    `:+oo+:     .:+oo+:`      -/+oo/-     /+.
    /hy/--:.    ohs:.-+hy-   sho--/yy:   +hs---`   -yy+--::    +hy:../yy:   `shs-.-ohy.   sh:
    hh:        :hh`    ohs   sh+   /hy   +hyyyo    sh+        `hh:    /hh   :hh     sh+   sh:
    ohy-` ``   `yh+`  :yh:   sh+``-yh+   +hs       /hy:` `.    ohs.  .yh+   .yh/` `:hy-   sh:
     :osyyy+    `:oyyys+.    oyyyso+-    /yyyyy/    -+syyys`    :osyyso:     `/oyyys+.    oyyyyy


                                     PRESS ANY KEY TO CONTINUE
     ''')


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
    print('''
    +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+
    |T|H|A|N|K|S| |F|O|R| |U|S|I|N|G| |O|U|R| |P|R|O|G|R|A|M|
    +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+

                     PRESS ANY KEY TO QUIT
    ''')


print_welcome_screen()
wait_until_key_pressed()
input_login()
input_password()
print_end_screen()
wait_until_key_pressed()
