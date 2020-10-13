#Euler Problem 2 Test

import unittest
import problem2

class TestProblem2(unittest.TestCase):
    
    def test_fibonocci_generator(self):
        self.assertEqual(list(problem2.fibonocci_generator(2)), [1,2])
        self.assertEqual(list(problem2.fibonocci_generator(100)), [1,2,3,5,8,13,21,34,55,89])
        
        
    def test_sum_of_even(self):
        self.assertEqual(problem2.sum_of_even([1,2]),2)
        self.assertEqual(problem2.sum_of_even([1,2,3,5,8,13,21,34,55,89]),44)
        
        
if __name__ == '__main__':
    unittest.main()