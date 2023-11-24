import unittest
import numpy as np
from src.Assignment13.util import Linear_Algebra_determinant

class TestCalculateDeterminant(unittest.TestCase):
    def test_calculate_determinant(self):
        test_input = np.array([[1, 2], [3, 4]])
        result = Linear_Algebra_determinant(test_input)
        self.assertEqual(result, -2.0)

if __name__ == '__main__':
    unittest.main()
    
