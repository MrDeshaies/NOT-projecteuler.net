# Euler 65
# convergents for e are [2; 1,2,1,  1,4,1,  1,6,1,  1,8,1, ... 1,2k,1]
# So the first 10 terms are 2, 3, 8/3, 11/4, 19/7, 82/32 ... 1457/536.
# Find the sum of digits in the numerator of the 100th convergent 
# of the continued fraction for e.

from fractions import Fraction
from math import ceil
from euler import sum_digits, convert_convergents_to_fraction

def generate_convergents_for_e(n):
    result = [2]
    groups = ceil((n-1)/3)
    for k in range(1,groups+1):
        result += [1,2*k,1]
    return result[0:n]

if __name__ == '__main__':
    for i in [100]:#range(1,11):
        convergents = generate_convergents_for_e(i)
        convergent_fraction = convert_convergents_to_fraction(convergents)
        sum_digits_numerator = sum_digits(convergent_fraction.numerator)
        print("{}: {} (sum digits numerator: {})".format(i,convergent_fraction, sum_digits_numerator))
