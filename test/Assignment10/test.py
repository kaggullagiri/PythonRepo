import unittest
from src.Assignment10.util import calculateaverage

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average(self):
        input_count = 3
        fields = ['MARKS', 'CLASS', 'NAME', 'ID']
        data = [['85', '10', 'Alice', '1'], ['75', '11', 'Bob', '2'], ['90', '12', 'Cathy', '3']]

        result = calculateaverage(input_count, fields, data)
        self.assertAlmostEqual(result, 83.33, delta=0.01, msg="Average calculation mismatch")

if __name__ == '__main__':
    unittest.main()
