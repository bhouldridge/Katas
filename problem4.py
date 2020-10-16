#Euler Problem 4
#A palindromic number reads the same both ways. The largest palindrome made 
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product(maximum):
    """Find the largest palindrome made from the product of two 3-digit numbers"""

    palindrome = palindrome_generator(maximum)    
    guess = next(palindrome)
    while guess > 10000:
        check = three_digit_products(guess)
        if check == False:
            guess = next(palindrome)
        else:
            return check
        
    return max(filter(lambda x: three_digit_products(x) != False , palindrome_generator(maximum)))
            

def three_digit_products(number):
    """return the two, three digit numbers, of which the number given
    is their product. Return False if number is not a product of two,
    three digit numbers."""
    
    if number < 10000 or number > 998001:
        return False
    else:
        for guess in range(999, 99, -1):
            if number % guess == 0:
                return (int(number/guess), guess)
        return False
    

def palindrome_generator(maximum):
    """Returns palindromes that are less than the maximum
    starting with the largest possible"""
    
    for num in range(maximum, 0, -1):
        if is_palindrome(str(num)):
            yield num
            
        
def is_palindrome(string):
    """Return True if the given argument is a palindrome, and False if not."""
    
    return False not in (map(
        lambda x: string[x] == string[-(x+1)],
        range(int(len(string)/2))))