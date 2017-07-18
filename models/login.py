class Logins:

    list_of_logins = []

    @classmethod
    def from_codecoolers(cls, codecoolers):
        '''
        From list of Codecooler obj. instances appends logins to class list_of_logins
        '''
        for codecooler in codecoolers:
            cls.list_of_logins.append(codecooler.login)

    def is_login_unique(self, new_login):
        return new_login in self.list_of_logins

    @staticmethod
    def is_login_proper(new_login):
        return 5 < new_login < 12 and '|' not in new_login

    def is_login_valid(self, new_login):
        return self.is_login_proper() and self.is_login_unique()
