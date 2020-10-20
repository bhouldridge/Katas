#Euler Problem 5 Test

import unittest
import problem5

class TestProblem5(unittest.TestCase):
 
    def test_count_generator(self):
        test_generator = problem5.count_generator(2520,20)
        self.assertEqual(next(test_generator), 2520)
        self.assertEqual(next(test_generator), 2540)
        self.assertEqual(next(test_generator), 2560)
        
        test_generator = problem5.count_generator(2,3)
        self.assertEqual(next(test_generator), 2)
        self.assertEqual(next(test_generator), 5)
        self.assertEqual(next(test_generator), 8)
        
    def test_is_multiple_of_integers_under_19(self):
        self.assertEqual(problem5.is_multiple_of_integers_under_19(2520), False)
        self.assertEqual(problem5.is_multiple_of_integers_under_19(670442572800), True)
    
    def test_smallest_multiple(self):
        self.assertEqual(problem5.smallest_multiple(), 232792560)
        
if __name__ == '__main__':
    unittest.main()