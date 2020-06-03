from monster_characteristics import *
from student_monster import *
from course import *

# Create two student objects
mike = Student('mike', 235, 'hairy red', 8, [])
randall = Student('randall', 432, 'Shiny blue', 7, [])


# Add a skill to each of your students
mike.add_skill('Supersonic scream')
randall.add_skill('Fly')

# Create(initialise) a course
monster_course = Course('Scarings101', '02/06/2020')



# Append student object / instances to list of student attributes in one of the course
monster_course.add_student(mike)
monster_course.add_student(randall)

for student in monster_course.list_of_students:
    print(student.get_skills())
    print(student.get_name())



# monster_course.add_skill()
# print(monster_course.add_skill_list)

# Extra - get the list of students, itterate over it and print the students name