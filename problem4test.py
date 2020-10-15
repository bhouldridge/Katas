# Euler Problem 4 Test

import unittest
import problem4

class TestProblem4(unittest.TestCase):
 
    def test_is_palindrome(self):
        self.assertAlmostEqual(problem4.is_palindrome('5'), True)
        self.assertAlmostEqual(problem4.is_palindrome('10'), False)
        self.assertAlmostEqual(problem4.is_palindrome('11'), True)
        self.assertAlmostEqual(problem4.is_palindrome('12341899814321'), True)
        
if __name__ == '__main__':
    unittest.main()