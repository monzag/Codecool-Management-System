def get_user_by_login_and_password(login, password, codecoolers):
    '''
    Searches given list of Codecooler obj. and compares passwords and logins
    if find any match will return codecooler obj. otherwise None

    Parameters:
        login: str
        password: str
        codecoolers: list of Codecooler objs.

    Returns:
        codecooler: Codecooler obj.
    '''
    for codecooler in codecoolers:
        if codecooler.login == login and codecooler.password == password:
            return codecooler

    return None


def get_codecoolers_with_mails(codecoolers):
    '''
    creates 2d list of Codecooler objs. passed to function
    where each next inside list is data of another Codecooler obj.
    ex. [name, surname, email]

    Parameters:
        codecooler: list of Student obj.

    Returns:
        table: 2d list of information about Codecoolers objs.
    '''
    table = []
    for codecooler in codecoolers:
        table.append([codecooler.name, codecooler.surname, codecooler.email])
    
    return table


def remove_codecooler(codecooler, codecoolers):
    '''
    Given list of Codecoolers instance objs. and Codecooler instance obj.
    Deletes codecooler from system

    Parameters:
        codecoolers: list of Codecooler instance objs.

    Return:
        codecoolers: list of Codecooler instance objs.
    '''
    return codecoolers
