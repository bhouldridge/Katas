#Euler Problem 4
#A palindromic number reads the same both ways. The largest palindrome made 
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome_generator(maximum):
    """Returns panlindromes that are less than the maximum
    starting with the largest possible"""
    
    for num in range(maximum, 0, -1):
        if is_palindrome()
        
def is_palindrome(string):
    """Return True if given argument is a palindrome and False if not."""
    
    return False not in (map(
        lambda x: string[x] == string[-(x+1)],
        range(int(len(string)/2))))
            