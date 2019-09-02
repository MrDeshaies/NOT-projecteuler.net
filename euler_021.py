from euler import *
import math

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

def factLessItself(x):
    if x == 1:
        return [1] # shortcut this special case
    divisors = fact(x)
    divisors.pop()
    return divisors

def sumDivisors(x):
    return sum(factLessItself(x))

amicableSet = set()

#skip 1, since d(1) = 1, so does not satisby a!=b
for x in range(2,10000):
    if x in amicableSet:
        continue
    d = sumDivisors(x)
    y = sumDivisors(d)
    if d != x and y == x:
        print( str(x) + " and " + str(d) + " are best buds.")
        amicableSet.update([x,d])

print(amicableSet)
print(sum(amicableSet))