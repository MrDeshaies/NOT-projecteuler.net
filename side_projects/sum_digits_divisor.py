# the divisors of the sum of the digits of a number also divide a number. True? Nah.
# a friend was saying so, so I wrote this program to prove it wrong.
# it's easy to see why it wouldn't be the case for prime numbers.....

# add parent dir to path, so we can import euler
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from euler import fact

def sum_digits(number):
    return sum([int(d) for d in str(number)])

def is_divisible_by_all(number, factors):
    return all([number%i == 0 for i in factors])

for i in range(10,200):
    if not is_divisible_by_all(i, fact(sum_digits(i))):
        print(i)
