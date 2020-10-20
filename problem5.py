#Euler Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def count_generator(start, step):
    """generator that starts as start and counts by step"""
    current = start
    yield current
    
    while True:
        current += step
        yield current
        
def is_multiple_of_integers_under_19(number):
    """Returns True if the number is divisable by all integers less than 19"""
    
    return all(map(lambda x: number % x == 0, range(11,20)))
    

def smallest_multiple():
    """Find the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20)"""
    
    multiple_of_380 = count_generator(0, 380)
    while True:
        guess = next(multiple_of_380)
        if is_multiple_of_integers_under_19(guess):
            return guess
        