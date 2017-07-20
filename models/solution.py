import os


class Solution:

    def __init__(self, grade, submit_date, file_name):
        self.grade = grade
        self.submit_date = submit_date
        self.file_name = file_name

    @classmethod
    def from_list(cls, list_of_attributes_values):
        '''
        Alternative constructor for class obj.
        Uses list of strings.

        Parameters:
            list_of_attributes_values : list of str

        Returns:
            Solution obj.
        '''
        grade, submit_date, file_name = list_of_attributes_values

        return cls(int(grade), submit_date, file_name)

    @property
    def csv_string(self):
        return '{}|{}|{}'.format(self.grade, self.submit_date, self.file_name)

    @property
    def formated_grade(self):
        if self.grade > 0:
            return str(self.grade)
        else:
            return 'not graded yet'

    @property
    def formated_submit_date(self):
        if self.submit_date != '0':
            return self.submit_date
        else:
            return 'not submited yet'

    @property
    def can_be_graded(self):
        return self.grade == 0 and self.submit_date != '0'

    def get_content(self):
        '''
        '''
        file_path = os.getcwd() + '/data/solutions/' + self.file_name
        with open(file_path, 'r') as data:
            data = data.read()

        return data
