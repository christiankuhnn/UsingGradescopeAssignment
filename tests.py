import unittest
import answer


class TestLast(unittest.TestCase):
    def test_gets_last(self):
        actual = answer.addNumbers(["2\n", "2\n", "3\n"])
        self.assertEqual(actual, 5)
        
        actual = answer.addNumbers([])
        self.assertEqual(actual,None)
        
        actual = answer.addNumbers(["2\n", "-2\n", "3\n"])
        self.assertEqual(actual, 3)
        
        actual = answer.addNumbers(["2\n", "-999\n", "3\n"])
        self.assertEqual(actual,None)
    
    def test_handles_empty(self):
        actual = answer.print_all_lines([])
        self.assertEqual(actual, None)
        
    