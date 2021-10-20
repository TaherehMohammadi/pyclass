# Tahereh Mohammadi - Thursday 14-18
# making Class, Example 5

class TrainingCourse:
    def __init__(self, name, category, teacher, hours, time):
        self.course_name = name
        self.course_category = category
        self.teacher_name = teacher
        self.course_duration = hours
        self.class_time = time
        self.class_capacity = 8
    def __str__(self):
        return f'{self.course_name} teaches by {self.teacher_name}'
    def register(self, student_first_name, student_last_name):
        self.class_capacity -= 1
        if self.class_capacity > 0:
            return f'{student_first_name} {student_last_name} is registerd in {self.course_name} class.'
        else:
            return 'Class capacity is full.'

python = TrainingCourse('Python', 'Programming Language', 'Keshavarz', 40, 'Thusdays 14-18')
sql = TrainingCourse('SQL Server 2019 Implementation', 'Data Base', 'Ghorbani', 54, 'Sundays & Tuesdays 16-18')

print(python)
print(python.class_time)
print(python.register('Tahereh', 'Mohammadi'))
print(python.register('Ali', 'Rezaei'))
print(python.register('Mina', 'Mayeli'))
print(python.register('Fatemeh', 'Golami'))
print(python.register('Arman', 'Farhadi'))
print(python.register('Omid', 'Tanha'))
print(python.register('Nushin', 'Saravi'))
print(python.register('Mahyar', 'Noruzi'))
print(python.register('Kamyar', 'Noruzi'))
print('---------------------------------------------------')
print(sql)
print('---------------------------------------------------')
