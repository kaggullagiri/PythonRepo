import unittest
from src.Assignment11.util import round_array

class TestProcessArray(unittest.TestCase):
    def test_process_array(self):
        input_array = ['1.5', '2.3', '4.8']
        floor_result, ceil_result, rint_result = round_array(input_array)

        self.assertTrue((floor_result == [1.0, 2.0, 4.0]).all())
        self.assertTrue((ceil_result == [2.0, 3.0, 5.0]).all())
        self.assertTrue((rint_result == [2.0, 2.0, 5.0]).all())

if __name__ == '__main__':
    unittest.main()
    
