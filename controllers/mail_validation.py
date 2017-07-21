from string import punctuation


def check_mail(mail):
    """
    Check if email contains forbidden signs and if
    is in proper format.

    Return:
            True: if mail is valid_name
            None: if mail is invalid
    """

    characters_list = list(punctuation)
    no_forbidden_characters = True

    at_index = characters_list.index('@')
    dot_index = characters_list.index('.')
    del characters_list[at_index], characters_list[dot_index]
    #Remove from list characters, which are allowed
    for character in characters_list:

        if character in mail:
            no_forbidden_characters = False

    splitted_mail = mail.split("@")

    if no_forbidden_characters:
        # Check if '@' appears only once in mail and if "." is used
        if mail.count("@") == 1 and splitted_mail[1].count(".") >= 1:

            try:

                if not (splitted_mail[1][0] == "." or splitted_mail[1][-1] == "." or splitted_mail[1][0] == " "):
                    return True

            except IndexError:
                return None
