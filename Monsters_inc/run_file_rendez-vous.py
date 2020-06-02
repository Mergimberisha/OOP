from monster_characteristics import *
from student_monster import *
from course import *

# Create two student objects
Mike = Student('Mike', 235, 'hairy red', 8, [])
Randall = Student('Randall', 432, 'Shiny blue', 7, [])


# Add a skill to each of your students
Mike.add_skill('Supersonic scream')
Randall.add_skill('Fly')

# Create(initialise) a course
monster_course = Course('Scarings101', '02/06/2020')



# Append student object / instances to list of student attributes in one of the course
monster_course.add_student(Mike)
monster_course.add_student(Randall)

for student in monster_course.list_of_students:
    print(student.get_skills())
    print(student.get_name())



# monster_course.add_skill()
# print(monster_course.add_skill_list)

# Extra - get the list of students, itterate over it and print the students name