import unittest
from src.Assignment1.util import listproblem

class TestListCommands(unittest.TestCase):
    def test_list_operations(self):
        # Example test case
        l1 = []
        commands = [['insert', '0', '56'], ['insert', '1', '78'], ['append','92'], ['print']]
        output =[56,78,92]
        result = listproblem(commands)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()