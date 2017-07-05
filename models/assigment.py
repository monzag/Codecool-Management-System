class Assigment:

    def __init__(self, name, creation_date, deadline, max_grade):
        self.name = name
        self.status = 'undone'
        self.creation_date = creation_date # datetime obj.
        self.deadline = deadline # datetime obj.
        self.submit_date = None
        self.grade = 0 # acually not sure bout that!
        self.max_grade = max_grade