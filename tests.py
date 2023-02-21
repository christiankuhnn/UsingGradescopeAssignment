import unittest
import answer


class TestLast(unittest.TestCase):
    def test_gets_last(self):
        actual = answer.addNumbers(["2\n", "2\n", "3\n"])
        self.assertEqual(actual, 7)
        
        actual = answer.addNumbers([])
        self.assertEqual(actual, "EMPTY")
        
        actual = answer.addNumbers(["2\n", "-2\n", "3\n"])
        self.assertEqual(actual, 5)
        
        actual = answer.addNumbers(["2\n", "-2\n", "-3\n"])
        self.assertEqual(actual, 2)
        
        
        actual = answer.addNumbers(["2\n", "-999\n", "3\n"])
        self.assertEqual(actual,2)
    
   
        
if __name__ == '__main__':
    unittest.main()   