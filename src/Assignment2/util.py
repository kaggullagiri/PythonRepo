def threesubject_marks(d, student_name):
    for name, scores in d.items():
        if student_name == name:
            percentage = sum(scores) / len(scores)
            print("Average percentage for {} is: {:.2f}%".format(name, percentage))
            return percentage

    print("Student {} not found.".format(student_name))
    return None
