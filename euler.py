import math
import re

def isPrime(x):
    # 0 and negative aren't prime
    if x <= 1:
        return False
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

    # hardcode a few numbers as the math below only works for number > 4
    if number == 1:
        return [1]
    elif number == 2:
        return [1,2]
    elif number == 3:
        return [1,3]
    elif number == 4:
        return [1,2,4]
    
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
                result.append(int(x))
            maxPossibleFactor = min(maxPossibleFactor,x)
        i = i+1
    result.sort()
    return result

def factLessItself(x):
    """Return a list of factors for the number, including 1 but NOT the number itself"""
    if x == 1:
        return [] # shortcut this special case
    divisors = fact(x)
    divisors.pop()
    return divisors

def find_primality(limit):
    """Builds a list from 0 to limit where values are a boolean indicating if the index is a prime.
       In other words, find_primality(x)[n] will be true if n is a prime, for n <= x"""
    # implementation of Sieve of Eratosthenes
    sieve = [True] * (limit+1)
    sieve[0] = sieve[1] = False

    for i in range(2, math.ceil(math.sqrt(limit))+1):
        if sieve[i]:
            for j in range(i*i, limit+1, i):
                sieve[j] = False
    return sieve

def list_primes(limit):
    primality = find_primality(limit)
    prime_numbers = [x for x,prime in enumerate(primality) if prime]
    return prime_numbers

def digit_repeats(number):
    number_string = str(number)
    return re.search(r"(.).*\1", number_string) != None

def pandigital(number):
    number_string = str(number)
    return len(number_string) == 9 and pandigital_partial(number_string)

def pandigital_partial(number):
    number_string = str(number)
    if len(number_string) > 9:
        return False
    return all([str(x) in number_string for x in range(1,len(number_string)+1)])
