from collections import namedtuple

def calculateaverage(input_count, fields, student_data):
    total_marks = 0
    Student = namedtuple('Student', fields)

    for _ in range(input_count):
        marks, class_, name, _id = student_data.pop(0)
        student = Student(marks, class_, name, _id)
        total_marks += int(student.marks)

    return total_marks / input_count
    
