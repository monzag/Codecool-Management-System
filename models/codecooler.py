class Codecooler:

	def __init__(self, name, surname, login, password, email):
		self.name = name
		self.surname = surname
		self.login = login
		self.password = password
		self.email = email

    @staticmethod
    def load_codecoolers_from_file(file_name):
        '''
        Read Codecooler obj data from csv file.
        Raise error if file not exist.

        Returns:
            splitted - list of lists
        '''

        file_path = os.getcwd() + '/data/' + file_name
        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(file_path, 'r') as csvfile:
                read_data = csvfile.readlines()
                splitted = [line.replace('\n', '').split(',') for line in read_data]

        return splitted

    @classmethod
    def get_codecooler_from_file(cls, file_name):
        '''
        Get data all codecoolers and create each Codecooler object (automatically append to list_of_codecoolers)
        '''
        data_all_codecoolers = cls.load_codecoolers_from_file(file_name)
        for codecooler in data_all_codecoolers:
            name, surname, login, password, email = codecooler[0], codecooler[1], codecooler[2], codecooler[3], codecooler[4]
            cls.create_new_codecooler(name, surname, login, password, email)

    @classmethod
    def create_new_codecooler(cls, name, surname, login, password, email):
        '''
        Create new object Student.

        Returns:
            new_student - obj
        '''

        new_student = Student(name, surname, login, password, email)
        return new_student
