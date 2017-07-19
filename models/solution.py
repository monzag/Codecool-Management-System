class Solution:

    def __init__(self, grade, submit_date, file_name):
        self.grade = grade
        self.submit_date = submit_date
        self.file_name = file_name

    @classmethod
    def from_list(list_of_attributes_values):
        '''
        '''
        grade, submit_date, file_name = list_of_attributes_values

        cls(grade, submit_date, file_name)
