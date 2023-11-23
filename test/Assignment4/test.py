import unittest
from src.Assignment4.util  import Findingday

class TestFindingDay(unittest.TestCase):
    def test_finding_day(self):
        # Testing the date given in mm dd yyyy format to know day
        result = Findingday(11, 23, 2023)
        expected_day = "THURSDAY"
        self.assertEqual(result, expected_day, "Incorrect day calculation")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
