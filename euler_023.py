from euler import *
import math

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
# any further by analysis even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

UPPER_LIMIT = 28123

def isAbundant(x):
    return sum(factLessItself(x)) > x

def findAllAbundantsBelow(limit):
    abundants = []
    for i in range(1,UPPER_LIMIT):
        if isAbundant(i):
            abundants.append(i)
    return abundants

def findAsSumOfTwoAbundants(target,abundants):
    # find two numbers, x and y, from the abundants array which sum up to target
    for x in abundants:
        if x > target:
            return [] # didn't find anything
        y = findMatchingY(target, x, abundants)
        if y != None:
            return [x,y]
    return []

def findMatchingY(target, x, abundants):
    # use binary search to find the correct y
    l = 0
    r = len(abundants)-1
    while l <= r:
        i = math.floor( (l+r) / 2)
        sum = abundants[i] + x
        if sum < target:
            l = i+1
        elif sum > target:
            r = i-1
        if sum == target:
            return abundants[i]
    return None

# first, find all abundant number up to upper_limit
abundants = findAllAbundantsBelow(UPPER_LIMIT)
print(len(abundants))

# now find the sum for the non-matching numbers
sum = 0
for i in range(1,UPPER_LIMIT):
    sumComponents = findAsSumOfTwoAbundants(i,abundants)
    if len(sumComponents) == 0:
        sum += i
    if i % 1000 == 0:
        print("At " + str(i) + " of " + str(UPPER_LIMIT))
print("Sum is " + str(sum))
