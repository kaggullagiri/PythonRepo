
from src.Assignment2.util import threesubject_marks

if __name__ == '__main__':
    n = int(input("Enter the no.students: "))
    student_marks = {}

    # Input student data
    for i in range(n):
        name, *line = input("Enter student and Enter three subject marks : ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # here we can tally average percentage
    student_name = input("Enter the studentname to tally: ")
    threesubject_marks(student_marks, student_name)
    
    


