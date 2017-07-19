import os


class Solution:

    def __init__(self, grade, submit_date, file_name):
        self.grade = grade
        self.submit_date = submit_date
        self.file_name = file_name

    @classmethod
    def from_list(cls, list_of_attributes_values):
        '''
        '''
        grade, submit_date, file_name = list_of_attributes_values

        return cls(grade, submit_date, file_name)

    @classmethod
    def get_file_name(cls, assignment_name, student_name):
        '''
        '''
        file_name = assignment_name + '_' + student_name
        file_path = os.getcwd() + '/data/solutions/' + file_name

        return file_path
