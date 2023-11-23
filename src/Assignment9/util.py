from collections import namedtuple

def average_marks(num_students, fields, student_data):
    students = namedtuple('my_student', fields)
    total_marks = sum(int(students(*student_data()).MARKS) for _ in range(num_students))
    return total_marks / num_students