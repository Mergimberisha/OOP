from student_monster import *

class Course:
    def __init__(self, module_name, list_of_students, start_date):
        self.module_name = module_name
        self.list_of_students = list_of_students
        self.start_date = start_date

    def add_student(self, student):
        self.list_of_students.append(student)
        return 'Great!,Student Added'

    def get_students(self):
        all_students = ''
        for student in self.list_of_students:
            all_students += f'{student.get_name()}, '
        return all_students