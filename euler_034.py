# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
from math import factorial

def sum_of_digit_factorial(number):
    return sum([factorial(int(d)) for d in str(number)])

# start at 3 since we're told to exclude 1 and 2
# random upper bound, not proven
total = 0
for i in range(3,100000):
    if i == sum_of_digit_factorial(i):
        total += i
        print(i)
print("=> " + str(total))