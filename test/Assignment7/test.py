import unittest
from src.Assignment7.util import split_num_char

class TestSplitNumChar(unittest.TestCase):
    def test_split_num_char_basic(self):
        test_string = "hello123world456"
        test_key = 3
        expected_output = ['hel', 'lo1', '23w', 'orl', 'd45', '6']

        result = list(split_num_char(test_string, test_key))
        self.assertEqual(result, expected_output, "Basic test failed")

    def test_split_num_char_empty_string(self):
        test_string = ""
        test_key = 5
        expected_output = []

        result = list(split_num_char(test_string, test_key))
        self.assertEqual(result, expected_output, "Empty string test failed")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
    
