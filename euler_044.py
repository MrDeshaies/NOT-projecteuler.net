# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# 
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
# 
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
# and D = |Pk − Pj| is minimised; what is the value of D?
from math import sqrt,modf

def generate_pentagonal(how_many):
    pentagonal_numbers = []
    for i in range(1,how_many+1):
        n = int(i * (3*i - 1) / 2)
        pentagonal_numbers.append(n)
    return pentagonal_numbers

def is_pentagonal(x):
    # nifty formula lifted from wiki. it's pentagonal when 'n' is a whole number
    # actually easy to derive taking the formula to generate, and applying the
    # quadratic formula to it...
    n = (sqrt(24*x + 1) + 1) / 6
    return modf(n)[0] == 0.0

def pentagonal_diff(pentagonal_numbers,k,j):
    pk, pj = pentagonal_numbers[k], pentagonal_numbers[j]
    diff = abs(pj-pk)
    if is_pentagonal(pk+pj) and is_pentagonal(diff):
        return diff
    return 0

pentagonal_numbers = generate_pentagonal(5000)
for k in range(0,len(pentagonal_numbers)):
    for j in range(k+1,len(pentagonal_numbers)):
        d = pentagonal_diff(pentagonal_numbers,k,j)
        if d == 0:
            continue
        print("{0}, {1} => {2}".format(k,j,d))