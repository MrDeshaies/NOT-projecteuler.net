# Euler 66
# Consider quadratic Diophantine equations of the form:
# x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

from math import sqrt, floor
from fractions import Fraction

# Source for continued-fraction expansion solution to Pell from paper of H.W. Lenstra Jr.
# http://www.ams.org/notices/200202/fea-lenstra.pdf
# Continued-fraction expansion of square root stolen from my solution to Euler 064.

def is_perfect_square(x):
    return int(sqrt(x)) ** 2 == x

def find_period_squareroot_continued_fraction(num):
    a0 = floor(sqrt(num))
    if num == a0**2:
        return 0 # perfect square...
    
    # algorithm lifted from https://en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend
    m = 0
    d = 1
    a = a0
    partial_denominators = [a]
    
    while True:
        m = d*a - m
        d = (num - m**2) / d
        a =  floor((a0 + m) / d)
        partial_denominators.append(a)
        if a == 2 * a0:
            return partial_denominators

def build_continued_fraction_approximation(partial_denominators):
    partial_denominators = partial_denominators.copy()

    if len(partial_denominators) == 1:
        return Fraction(partial_denominators[0])
    
    # build the fraction bottom-up
    result = Fraction(partial_denominators.pop())
    partial_denominators.reverse()
    for term in partial_denominators:
        result = Fraction(term) + Fraction(1,result)
    return result

def solve_pell(d):
    partial_denominators = find_period_squareroot_continued_fraction(d)
    # from the H.W. Lenstra Jr. paper:
    #    Truncating the expansion at the end of the first period,
    #    one finds that the fraction is a fair approximation.
    #    If the period length is even, one proceeds as
    #    above; if the period length is odd, one truncates at
    #    the end of the second period.
    if len(partial_denominators) > 3 and len(partial_denominators) % 2 == 0:
        # we repeat the period when the period length is odd  (the first term is not part of the period)
        partial_denominators = partial_denominators + partial_denominators[1:]
    
    candidate = build_continued_fraction_approximation(partial_denominators)
    [x,y] = [candidate.numerator,candidate.denominator]
    if x**2 - d*y**2 == 1: # see if it satisfies the equation
        return [x,y]
    
    # sometimes the above fails for some reason, but truncating the last term solves it...
    candidate = build_continued_fraction_approximation(partial_denominators[:-1])
    [x,y] = [candidate.numerator,candidate.denominator]
    if x**2 - d*y**2 == 1:  # see if it satisfies the equation
        return [x,y]
    else:
        print("Failed to find a solution for d="+str(d))
        exit(1)

def brute_force_pell(d):
    """Simple but crappy version that chokes starting at d=61"""
    y = 1
    while True:
        x = 1 + d * y**2
        if is_perfect_square(x):
            print("When D={}, x^2 is {} and x = {}".format(d, x, int(sqrt(x))))
            break
        else:
            y += 1

if __name__ == '__main__':
    maxD = 0
    maxX = 0
    for d in range(2,1001):
        if is_perfect_square(d):
            continue # there are no (non-trivial) solutions when d is perfect square
        [x,y] = solve_pell(d)
        print("[{},{}] is a solution for d={}".format(x,y,d))
        if x > maxX:
            maxD = d
            maxX = x
    print("Max D was {} with x={}".format(maxD,maxX))
