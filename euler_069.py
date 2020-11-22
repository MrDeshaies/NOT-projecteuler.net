# euler 069
# Euler's Totient function, φ(n) [sometimes called the phi function], 
# is used to determine the number of numbers less than n which are 
# relatively prime to n.
# 
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and 
# relatively prime to nine, φ(9)=6.
#
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

# [Ben: two numbers are relatively prive (coprime) if their GCD is 1]
from math import gcd, sqrt, floor
from euler import list_primes, are_coprime, phi

def n_over_phi(n):
    return n / phi(n)

def solve_69(upper_limit):
    # brute force approach... O(n^2), doesn't scale
    start = 2
    n_over_phi_values = [n_over_phi(n) for n in range(start,upper_limit+1)]
    max_n_over_phi = max(n_over_phi_values)
    max_n = n_over_phi_values.index(max_n_over_phi) + start
    print("Largest n/φ(n) is for n={} with value {}".format(max_n, max_n_over_phi))

def solve_69_fast(upper_limit):
    # solve_69(10) = 6 = 2*3
    # solve_69(100) = 30 = 2*3*5
    # solve_69(1000) = 210 = 2*3*5*7
    # get it? you multiply the primes until you get the largest  number less than the limit
    primes = list_primes(100) # get enough of them
    n = 1
    factors_used = []
    for p in primes:
        if n*p > upper_limit:
            break
        n *= p
        factors_used.append(p)
    
    print("Largest n/φ(n) is for n={} with value {}".format(n, n_over_phi(n)))
    print("{} is the product of the primes {}".format(n, factors_used))

if __name__ == '__main__':
    solve_69_fast(1_000_000)