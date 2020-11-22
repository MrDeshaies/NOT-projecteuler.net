# # Euler 73
# Consider the fraction, n/d, where n and d are positive integers. If n<d and 
# HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order 
# of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 3 fractions between 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced 
# proper fractions for d ≤ 12,000?

# [Benoit: ok... We can look at each denominator, there are not many.
# For each, find lower bound and upper bound to search, e.g. for 12,000
# we need to look at 4000/12000 (=1/3) to 6000/12000 (=1/2).
# For those, the denominator would stay as-is if gcd(num,denom)=1]

from fractions import Fraction
from math import gcd

count = 0
for denominator in range(4,12_001):
    start = (denominator//3) + 1
    end = denominator//2
    for i in range(start, end+1):
        if gcd(i, denominator) == 1:
            count +=1
print(count)