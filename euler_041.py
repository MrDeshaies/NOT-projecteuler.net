# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

import itertools
from euler import isPrime

largest_prime = 0
for size in range(1,10):
    # generate all the pandigital numbers of 'size'
    for i in itertools.permutations([str(x) for x in range(1,size+1)]):
        k = int("".join(i)) # convert tuple to int
        if isPrime(k) and k > largest_prime:
            largest_prime = k
            print(k)
print(largest_prime)