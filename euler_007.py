import math
from euler import *

# What is the 10,001st prime number?
primesFound = 0
x = 2
while True:
    if isPrime(x):
        primesFound += 1
    if primesFound == 10001:
        print(x)
        break
    x += 1
