# It was proposed by Christian Goldbach that every odd composite number can be written 
# as the sum of a prime and twice a square.
# 
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from euler import find_primality
from math import sqrt, modf

def test_goldbach_with_prime(x,prime):
    diff = x - prime
    if diff == 0:
        return True
    # can diff be expressed as 2 times a square?
    diff = diff / 2
    magic = sqrt(diff)
    if modf(diff)[0] != 0.0 or modf(magic)[0] != 0.0:
        return False
    #print("{0} = {1} + 2x{2}^2".format(x,prime,magic))
    return True

def test_goldbach(x,primality):
    if primality[x] or x % 2 == 0: # primes (non-composite) or even automatically get a pass
        return True
    
    # go down with the primes (I note above that the solution is often the first lesser prime)
    n = x
    while n > 0:
        if not primality[n]:
            n -= 1
            continue
        if test_goldbach_with_prime(x,n):
            return True
        n -= 1

SEARCH_UPPER_LIMIT = 10000
primality = find_primality(SEARCH_UPPER_LIMIT)

# only consider odd numbers starting at 9
for x in range(9,SEARCH_UPPER_LIMIT,2):
    if not test_goldbach(x,primality):
        print("Uh oh: " + str(x))
        break