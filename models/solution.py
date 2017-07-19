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

    @classmethod
    def get_file_name(cls, assignment_name, student_name):
        '''
        Creates unique name for file storing solution added to data.

        Parameters:
            assignment_name : str
            student_name : str

        Returns:
            file_path : str

        '''
        file_name = assignment_name + '_' + student_name + '.txt'
        file_path = os.getcwd() + '/data/solutions/' + file_name

        return file_path

    @property
    def csv_string(self):
        return '{}|{}|{}'.format(self.grade, self.submit_date, self.file_name)
