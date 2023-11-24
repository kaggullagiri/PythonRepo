import unittest
from src.Assignment16.util import word_count

class TestCountAndPrint(unittest.TestCase):
    def test_word_count(self):
        input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]

        unique_count, occurrences = word_count(input_list)

        self.assertEqual(unique_count, 3)
        self.assertListEqual(occurrences, [3, 2, 1])

if __name__ == '__main__':
    unittest.main()
    
