import math
from euler import isPrime

# What is the 10,001st prime number?
primesFound = 1
x = 3
while True:
    if isPrime(x):
        primesFound += 1
    if primesFound == 10001:
        print(x)
        break
    x += 2