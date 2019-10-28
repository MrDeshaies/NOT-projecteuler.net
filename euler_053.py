# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, (5c3)=10.
#
# In general, (ncr)=n!/(r!(n−r)!), where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
#
# It is not until n=23, that a value exceeds one-million: (23c10)=1144066.
#
# How many, not necessarily distinct, values of (ncr) for 1≤n≤100, are greater than one-million?
import math

def ncr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

UPPER_LIMIT = 100
greater_million = 0

for n in range(1,UPPER_LIMIT+1):
    for r in range(1,n+1):
        if ncr(n,r) > 1000000:
            greater_million += 1
print(greater_million)