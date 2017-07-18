class Logins:

    list_of_logins = []

    @classmethod
    def from_codecoolers(cls, *args):
        '''
        From list of Codecooler obj. instances appends logins to class list_of_logins
        '''
        for codecoolers in args:
            for codecooler in codecoolers:
                cls.list_of_logins.append(codecooler.login)

    @classmethod
    def is_login_unique(cls, new_login):
        return not new_login in cls.list_of_logins

    @staticmethod
    def is_login_proper(new_login):
        return (4 < len(new_login) < 12) and ('|' not in new_login)

    @classmethod
    def is_login_valid(cls, new_login):
        return cls.is_login_proper(new_login) and cls.is_login_unique(new_login)
