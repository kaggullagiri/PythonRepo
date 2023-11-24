import unittest
from src.Assignment18.util import Iterables_and_Iterators_probability


class TestCalculateProbability(unittest.TestCase):
    def test_Iterables_and_Iterators_probability(self):
        letters = ['a', 'b', 'c']
        k = 2
        target_letter = 'a'

        result = Iterables_and_Iterators_probability(letters, k, target_letter)

        # Update the expected result to match the corrected logic
        self.assertAlmostEqual(result, 0.6667, places=4)

if __name__ == '__main__':
    unittest.main()
    
