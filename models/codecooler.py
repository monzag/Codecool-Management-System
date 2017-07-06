class Codecooler:

	def __init__(self, name, surname, login, password, email):
		self.name = name
		self.surname = surname
		self.login = login
		self.password = password
		self.email = email

    @classmethod
    def load_students_from_file(cls):
        '''
        Read students data from csv file.
        Raise error if file not exist.

        Returns:
            splitted - list of lists
        '''

        file_path = os.getcwd() + '/data/students.csv'
        if not os.path.exists(file_path):
            raise FileNotFoundError("There is no such a file")

        else:
            with open(filename, 'r') as csvfile:
                read_data = csvfile.readlines()
                splitted = [line.replace('\n', '').split(',') for line in read_data]

        return splitted

    @classmethod
    def get_students_from_file(cls):
        '''
        Get data all students and create each Student object (automatically append to list_of_students)
        '''

        data_all_students = Student.load_students_from_file()
        for student in data_all_students:
            name, surname, login, password, email = student[0], student[1], student[2], student[3], student[4]
            Student.create_new_student(name, surname, login, password, email)

    @classmethod
    def create_new_student(cls, name, surname, login, password, email):
        '''
        Create new object Student.

        Returns:
            new_student - obj
        '''

        new_student = Student(name, surname, login, password, email)
        return new_student

    @classmethod
    def save_data_to_file(cls):
        '''
        Save students data to csv file. If file not exist, create file.
        '''
        list_to_save = Student.convert_list_of_object_to_data()
        filename = 'students.csv'
        with open(filename, 'w') as csvfile:
            for record in list_to_save:
                row = ','.join(record)
                csvfile.write(row + "\n")

    @classmethod
    def convert_list_of_object_to_data(cls):
        '''
        Unpack attributes of Student object as data to student_data list and add it to list_to_save.

        Returns:
            list_to_save - list of lists
        '''

        list_to_save = []
        for student in Student.list_of_students:
            name, surname, login, password, email = student.name, student.surname, student.login, student.password, student.email
            student_data = [name, surname, login, password, email]
            list_to_save.append(student_data)

        return list_to_save
