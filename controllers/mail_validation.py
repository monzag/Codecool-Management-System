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
    splitted_mail = mail.split("@")

    for character in characters_list:
        # Remove from characters list signs that are allowed.
        if character == "@" or character == ".":
            characters_list.remove(character)
            continue

        if character in mail:
            no_forbidden_characters = False

    if no_forbidden_characters:
        # Check if '@' appears only once in mail and if "." is used
        if mail.count("@") == 1 and splitted_mail[1].count(".") >= 1:

            try:

                if not (splitted_mail[1][0] == "." or splitted_mail[1][-1] == "."):
                    return True

            except IndexError:
                return None
