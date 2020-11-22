# Euler 70
# Euler's Totient function, φ(n) [sometimes called the phi function], is used 
# to determine the number of positive numbers less than or equal to n which 
# are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all 
# less than nine and relatively prime to nine, φ(9)=6.
#
# The number 1 is considered to be relatively prime to every positive number, 
# so φ(1)=1.
#
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation 
# of 79180.
# 
# Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and 
# the ratio n/φ(n) produces a minimum.

from euler import is_permutation, phi, list_primes
from math import sqrt

# the example given, 87109 only has factors 11 and 7919.
# it makes sense that n/φ(n) would be a minimum for a number with few factors.
# Thus, limit the search to primes * another prime.
# Further, the ratio would be minimized when the two primes (x and y) are close
# to sqrt(n). So start there for x, lowering it slowly while increasing y.

UPPER_BOUND = 10**7
SQRT_UPPER = sqrt(UPPER_BOUND)
LOWER_BOUND = 1000
primes = list_primes(UPPER_BOUND // LOWER_BOUND)
print(len(primes))

def fast_solve():
    # find out where to start
    sqrt_index = 0
    for i in range(len(primes)):
        if primes[i] > SQRT_UPPER:
            sqrt_index = i
            break

    x_index = sqrt_index
    while x_index > 0:
        print("Trying with x at index {} with value {}".format(x_index, primes[x_index]))
        y_index = sqrt_index
        while y_index < len(primes):
            n = primes[x_index] * primes[y_index]
            if n > UPPER_BOUND:
                break
            p = phi(n)
            if is_permutation(n, p):
                print("n={}, phi(n)={}, ratio={}".format(n,p, n/p))
                return
            y_index += 1
        x_index -= 1

def slow_solve():
    min_ratio = 999999999
    for x in primes[200:LOWER_BOUND]:
        for y in primes:
            n = x*y
            if n > UPPER_BOUND:
                break
            p = phi(n)
            if is_permutation(n, p):
                ratio = n/p
                if ratio < min_ratio:
                    min_ratio = ratio
                    print("(x,y)=({},{}), n={}, phi(n)={}, ratio={}".format(x,y,n,p, n/p))

if __name__ == '__main__':
    fast_solve()