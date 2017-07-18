class logins:

    list_of_logins = []

    def __init__(self, new_login):
        self.list_of_logins.append(new_login)
    
    def is_login_unique(self, new_login):
        return new_login in self.list_of_logins

    @staticmethod
    def is_login_proper(new_login):
        if 5 < new_login < 12:
            if '|' not in new_login:
                return True

        return False
