#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
from euler import *

limit = 2000000
primality = find_primality(limit)
total = sum([x for x,prime in enumerate(primality) if prime])
print(total)