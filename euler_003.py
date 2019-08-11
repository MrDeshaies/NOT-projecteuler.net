import math
import time
from euler import *

# find the largest prime factor of 600851475143

def findLargestPrimeFactor(top):
    factors = fact(top)
    factors.sort(reverse=True)
    for i in factors:
        if isPrime(i):
            print "The largest prime factor of " + str(top) + " is " + str(i)
            return

top = 600851475143
findLargestPrimeFactor(top)
