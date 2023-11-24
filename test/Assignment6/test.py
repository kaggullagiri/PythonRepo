import unittest
from src.Assignment6.util import print_formatted

class TestPrintFormatted(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_formatted(self, mock_stdout):
        test_input = 5
        expected_output = (
            " 1  1  1  1\n"
            " 2  2  2 10\n"
            " 3  3  3 11\n"
            " 4  4  4100\n"
            " 5  5  5 101\n"
        )

        print_formatted(test_input)
        self.assertEqual(mock_stdout.getvalue(), expected_output, "Output mismatch")
        

