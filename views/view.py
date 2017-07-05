import os
import sys
import termios
import getpass


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


def error_check(table, title_list):
    '''
    Checks if table is empty, has different amount of entries in lists
    or has different amount of entries between lists and titles.

    Args:
        table: list of lists with data
        title_list: list containing table headers

    Returns:
        boolean
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
