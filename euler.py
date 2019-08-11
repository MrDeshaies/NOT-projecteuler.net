import math

def isPrime(x):
    if x == 2:
        return True
    # even except 2 not prime. this lets us only check odd factors
    if x%2 == 0:
        return False
    
    high_limit = math.sqrt(x)
    candidate = 3
    while candidate <= high_limit:
        if x%candidate == 0:
            return False
        candidate += 2
    return True;

def fact(number):
    result = []
    i = 1
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
