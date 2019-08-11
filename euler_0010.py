#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
from euler import *

limit = 2000000
sum = 0
x = 2
while True:
    if x >= limit:
        break
    if isPrime(x):
        sum += x
    x += 1
print sum
