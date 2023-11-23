import unittest
from src.Assignment5.util import StringMutation

class TestStringMutation(unittest.TestCase):
    def test_string_mutation(self):
        original_string = "example"
        position = 3
        character = "p"
        expected_result = "exapple"  # The expected mutated string

        result = StringMutation(original_string, position, character)
        self.assertEqual(result, expected_result, "Mutation failed")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
