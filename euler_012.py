
import math
from euler import *

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# What is the value of the first triangle number to have over five hundred divisors?

stopNumberDivisors = 500

maxD=0
maxT=0

i = 1
triangle = 0
while True:
	triangle += i
	i += 1
	numDivisors = len(fact(triangle))
	if numDivisors > maxD:
		maxD = numDivisors
		maxT = triangle
		print(str(triangle) + ": " + str(numDivisors))
	if numDivisors >= stopNumberDivisors:
		break
