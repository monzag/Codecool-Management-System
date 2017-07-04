from employee import Employee


class Manager(Employee):

    def __init__(self, *args):
        super().__init__(*args)