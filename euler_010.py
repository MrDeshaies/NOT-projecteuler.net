#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
from euler import list_primes

limit = 2000000
total = sum(list_primes(limit))
print(total)