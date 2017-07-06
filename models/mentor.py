from models.employee import Employee


class Mentor(Employee):

    list_of_mentors = []

    def __init__(self, *args):
        super().__init__(*args)
        Mentor.list_of_mentors.append(self)