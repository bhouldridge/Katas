#Euler Problem 3 test

import unittest
import problem3

class TestProblem3(unittest.TestCase):
    
    def test_prime_factors(self):
        self.assertEqual(problem3.prime_factors(2), [2])
        self.assertEqual(problem3.prime_factors(4), [2,2])
        self.assertEqual(problem3.prime_factors(6), [2,3])
        self.assertEqual(problem3.prime_factors(8), [2,2,2])
        self.assertEqual(problem3.prime_factors(13195), [5, 7, 13, 29])
    
    def test_largest_prime_facor(self):
        self.assertEqual(problem3.largest_prime_factor(2), 2)
        self.assertEqual(problem3.largest_prime_factor(3), 3)
        self.assertEqual(problem3.largest_prime_factor(4), 2)
        self.assertEqual(problem3.largest_prime_factor(6), 3)
        self.assertEqual(problem3.largest_prime_factor(13195), 29)
        self.assertEqual(problem3.largest_prime_factor(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()