# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# 
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# 
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

from euler import find_primality
import math

def prime_factors_count(number,primality):
    count = 0
    for i in range(2,math.ceil(math.sqrt(number))):
        if number % i == 0:
            if primality[i]:
                count += 1
            if primality[number // i]:
                count += 1
    return count

UPPER_LIMIT = 1000000
TARGET = 4
count = 0
i = 1
primality = find_primality(UPPER_LIMIT)

while True:
    if prime_factors_count(i,primality) == TARGET:
        count += 1
        if count == TARGET:
            print([i-k for k in range(TARGET)])
            break
    else:
        count = 0
    i += 1