import unittest
from src.Assignment15.util import score_of_happiness

class TestCalculateHappiness(unittest.TestCase):
    def test_score_of_happiness(self):
        elements = [1, 2, 3, 4, 5]
        set_A = {1, 3, 5}
        set_B = {2, 4}

        result = score_of_happiness(elements, set_A, set_B)
        self.assertEqual(result, 1)  # This line should be updated to reflect the correct expected result

if __name__ == '__main__':
    unittest.main()
    
