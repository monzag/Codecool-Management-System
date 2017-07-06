from models.employee import Employee


class Mentor(Employee):

    list_of_mentors = []

    def __init__(self, *args):
        super().__init__(*args)
        Mentor.list_of_mentors.append(self)

    @classmethod
    def save_data_to_file(cls):
        '''
        Save mentors data to csv file. If file not exist, create file.
        '''
        list_to_save = Mentor.convert_list_of_object_to_data()
        filename = 'mentors.csv'
        with open(filename, 'w') as csvfile:
            for record in list_to_save:
                row = ' | '.join(record)
                csvfile.write(row + "\n")

    @classmethod
    def convert_list_of_object_to_data(cls):
        '''
        Unpack attributes of Student object as data to student_data list and add it to list_to_save.
        Returns:
            list_to_save - list of lists
        '''

        list_to_save = []
        for mentor in Mentor.list_of_mentors:
            list_to_save.append([mentor.login, mentor.password, mentor.name,
                                mentor.surname, mentor.email])

        return list_to_save