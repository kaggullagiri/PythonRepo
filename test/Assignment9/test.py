import unittest
from src.Assignment9.util import average_marks, userinput

class TestAverageMarks(unittest.TestCase):
    def test_average_marks(self):
        num_students = 3
        fields = ['Physics', 'Math', 'English']
        student_data = [['85', '90', '95'], ['75', '80', '85'], ['60', '70', '80']]

        result = average_marks(num_students, fields, student_data)
        self.assertAlmostEqual(result, 80.0, delta=0.01, msg="Average calculation mismatch")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
