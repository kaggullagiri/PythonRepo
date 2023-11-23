import unittest
from src.assignment5.util import split_num_char


class Test_and_Merge_The_Tools(unittest.TestCase):
    def test_and_merge_the_tools(self):
        self.assertEqual(list(split_num_char("AABCAAADA", 3)), ['AB', 'CA', 'AD'])

if __name__ == '__main__':
    unittest.main()