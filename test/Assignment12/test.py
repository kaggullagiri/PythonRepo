import unittest
import numpy as np
from src.Assignment12.util import max_of_min

class TestCalculateMaxOfMin(unittest.TestCase):
    def test_calculate_max_of_min(self):
        test_input = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = max_of_min(test_input)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()