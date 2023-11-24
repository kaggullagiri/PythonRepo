import unittest
from src.Assignment17.util import to_check_piling


class TestCheckArrangement(unittest.TestCase):
    def test_to_check_piling(self):
        test_cases = [
            (3, [3, 2, 1]),
            (4, [4, 2, 5, 3]),
        ]

        results = to_check_piling(test_cases)

        # Updated the expected results to match the corrected logic
        self.assertEqual(results, ["Yes", "Yes"])

if __name__ == '__main__':
    unittest.main()
    
    
