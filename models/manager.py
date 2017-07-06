from models.employee import Employee


class Manager(Employee):

    list_of_managers = []

    def __init__(self, *args):
        super().__init__(*args)
        Manager.list_of_mentors.append(self)