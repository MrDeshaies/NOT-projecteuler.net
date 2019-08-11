import math

def isPrime(x):
    # even numbers except 2 are not prime. this lets us only check odd factors
    if x == 2:
        return True
    if x%2 == 0:
        return False
    
    # if non-prime, a factor would always exist <= the square root of a number. Think about it...
    high_limit = math.sqrt(x)
    candidate = 3
    while candidate <= high_limit:
        if x%candidate == 0:
            return False
        candidate += 2 # only consider odd factors
    return True

def fact(number):
    """Return a list of factors for the number, including 1 and number"""
    result = []
    i = 1

    # the max possible factor. Initially we start at number/2. Let's say we find 3 is a factor,
    # we record 3 and x/3 as factors, and set the net upper bound as x/3.
    # E.g. if number is 32, first max = 16
    #      try 2, factors 2 and 16 recorded (max=16)
    #      try 3, nope. (max=16)
    #      try 4, factors 4 and 8 recorded (max=8)
    #      try 5, 6, 7, done. Don't need to check higher than 8, since 16x2 already recorded.

    maxPossibleFactor = math.ceil(number/2)
    while ( i < maxPossibleFactor ):
        if number % i == 0:
            result.append(i)
            x = number / i
            if x != i:
                result.append(x)
            maxPossibleFactor = min(maxPossibleFactor,x)
        i = i+1
    result.sort()
    return result
