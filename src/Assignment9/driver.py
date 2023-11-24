from util import average_marks

def userinput():
    return int(input()), input().split(), lambda: input().split()

if __name__ == "__main__":
    num_students, fields, student_data = userinput()
    average_marks = average_marks(num_students, fields, student_data)
    print("{:.2f}".format(average_marks))
    
    
