#Euler Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime_factors(number):
    
    factors = []
    guess = 2
    remainder = number
    while remainder != 1:
        while remainder % guess == 0:
            factors.append(guess)
            remainder = remainder / guess
        guess += 1
    return factors

def largest_prime_factor(number):
    """Return the largest prime factor of input number"""
       
    return max(prime_factors(number))