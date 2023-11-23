import unittest
from src.Assignment2.util import threesubject_marks

class TestThreeSubjectMarks(unittest.TestCase):
    def setUp(self):
        # Set up test data
        self.student_marks = {
            "Giri": [90, 95, 92],
            "kalyan": [75, 70, 75],
        }

    def test_average_calculation(self):
        # Test the calculation of average marks
        student_name = "Giri"  # Choose a test student name
        expected_average = 92.33333333333333  # Fill in the expected average percentage for this student
        result = threesubject_marks(self.student_marks, student_name)
        self.assertEqual(result, expected_average, "Incorrect average calculation")

if __name__ == '__main__':
    unittest.main()