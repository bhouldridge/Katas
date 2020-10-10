#Euler Problem 1 test

import unittest
import problem1

class TestProblem1(unittest.TestCase):
    
    def test_multiples_of_3_and_5(self):
        self.assertEqual(problem1.sum_multiples_of_3_and_5(2), 0)
        self.assertEqual(problem1.sum_multiples_of_3_and_5(3), 0)
        self.assertEqual(problem1.sum_multiples_of_3_and_5(4), 3)
        self.assertEqual(problem1.sum_multiples_of_3_and_5(5), 3)
        self.assertEqual(problem1.sum_multiples_of_3_and_5(6), 8)
        self.assertEqual(problem1.sum_multiples_of_3_and_5(10), 23)
    
if __name__ == '__main__':
    unittest.main()