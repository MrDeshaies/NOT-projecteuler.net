# Euler Problem 057... Better view this one online
# 
# The continued fraction expansion of sqrt(2) = ...
# The first expansions are 3/2, 7/5, 17/12, 41/29...
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
# is the first example where the number of digits in the numerator exceeds the number of digits 
# in the denominator.
#
#In the first one-thousand expansions, how many fractions contain a numerator 
# with more digits than the denominator?

from fractions import Fraction

def is_numerator_longer(f):
    return len(str(f.numerator)) > len(str(f.denominator))

# format is always 1 + [1/(2+b)], with the b becoming the value in the [] for the next expansion
b = Fraction(0) # initialize at 0, first value is 1/2
count_longer_numerator = 0
for i in range(1000):
    b = Fraction(1, Fraction(2)+b)
    current = Fraction(1) + b
    if is_numerator_longer(current):
        count_longer_numerator += 1
print(count_longer_numerator)