# Euler Problem 4 Test

import unittest
import problem4

class TestProblem4(unittest.TestCase):
 
    def test_is_palindrome(self):
        self.assertEqual(problem4.is_palindrome('5'), True)
        self.assertEqual(problem4.is_palindrome('10'), False)
        self.assertEqual(problem4.is_palindrome('11'), True)
        self.assertEqual(problem4.is_palindrome('12341899814321'), True)
        
    def test_palindrome_generator(self):
        self.assertEqual(list(problem4.palindrome_generator(2)), [2, 1])
        self.assertEqual(list(problem4.palindrome_generator(20)),
                         [11, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(list(problem4.palindrome_generator(50)),
                         [44,33,22,11, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(next(problem4.palindrome_generator(500)), 494)
        self.assertEqual(next(problem4.palindrome_generator(7196)), 7117)
        self.assertEqual(next(problem4.palindrome_generator(68610)), 68586)
        self.assertEqual(next(problem4.palindrome_generator(90009000)), 90000009)
        
    def test_three_digit_products(self):
        self.assertEqual(problem4.three_digit_products(10000), (16,625))
        self.assertEqual(problem4.three_digit_products(10642), (17,626))
        self.assertEqual(problem4.three_digit_products(461579), False)
        
    def test_largest_palindrome_product(self):
        self.assertEqual(problem4.largest_palindrome_product(998001), (913,993))
        self.assertEqual(problem4.largest_palindrome_product(493394), (547, 902))
        
if __name__ == '__main__':
    unittest.main()