#Euler Problem 2 Test

import unittest
import problem2

class TestProblem2(unittest.TestCase):
    
    def test_fibonocci_generator(self):
        self.assertEqual(list(problem2.fibonocci_generator(2)), [0,1])
        
        
    def test_sum_of_even(self):
        self.assertEqual(problem2.sum_of_even(2),0 )
        
if __name__ == '__main__':
    unittest.main()