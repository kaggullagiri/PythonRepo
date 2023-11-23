import unittest
import numpy as np
from src.Assignment14.util import mean_var_std_stats

class TestCalculateStatistics(unittest.TestCase):
    def test_mean_var_std_stats(self):
        test_input = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        mean_result, var_result, std_result = mean_var_std_stats(test_input)

        # Assert mean results
        self.assertTrue(np.allclose(mean_result, np.array([2.0, 5.0, 8.0])))

        # Assert variance results
        self.assertTrue(np.allclose(var_result, np.array([6.0, 6.0, 6.0])))

        # Assert standard deviation result
        self.assertAlmostEqual(std_result, 2.58198889747, places=11)  # Update the expected value


if __name__ == '__main__':
    unittest.main()