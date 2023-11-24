import unittest
from src.Assignment8.util import printingpattern

class TestPrintingPattern(unittest.TestCase):
    def test_printingpattern_basic(self):
        test_thickness = 5
        expected_output = [
            '----*----',
            '--***--',
            '-*****-',
            '*******',
            '-*****-',
            '--***--',
            '----*----'
        ]

        result = printingpattern(test_thickness)
        self.assertEqual(result, expected_output, "Basic test failed")
if __name__ == '__main__':
    unittest.main()
    
