# (Euler 064)
# [ben problem description has too much formatting; go see online https://projecteuler.net/problem=64]
# All square roots are periodic when written as continued fractions ...
# How many continued fractions for n <= 10,000 have an odd period?

from math import sqrt, floor

def sqrt_ipart(num):
    return floor(sqrt(num))

def find_period(num):
    # print("Finding period for " + str(num))
    a0 = sqrt_ipart(num)
    if num == a0**2:
        return 0 # perfect square...
    
    # algorithm lifted from https://en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend
    m = 0
    d = 1
    a = a0
    period = 0
    
    while True:
        m = d*a - m
        d = (num - m**2) / d
        a =  floor((a0 + m) / d)
        period += 1
        if a == 2 * a0:
            return period

def solve_064():
    match_count = 0
    for n in range(10_000+1):
        period = find_period(n)
        if period % 2 == 1:
            match_count += 1
    print(match_count)

if __name__ == '__main__':
    solve_064()