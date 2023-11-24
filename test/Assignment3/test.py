import unittest
from src.Assignment3.util import second_highest

class TestSecondHighest(unittest.TestCase):
    def test_second_highest_basic(self):
        scores = [20, 30, 15, 16, 25, 94]
        expected_runner_up = 30
        result = second_highest(scores)
        self.assertEqual(result, expected_runner_up, "Basic test failed")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
    
