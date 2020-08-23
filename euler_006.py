# Euler 006
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025-385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# [Ben note: below is the straightforward O(n) algorithm. We could have a O(1) solution by deriving the 
# formula for sum (known to be n(n+1)/2) and the sum of squares (tbd).
# But... O(n) algo for 100,000,000 takes less than a minute... and deriving the formula more time ;)]

def sum_square_difference(limit):
    sum_square = sum([i*i for i in range(limit+1)])
    square_sum = sum(range(limit+1))**2
    return square_sum - sum_square

print(sum_square_difference(10))
print(sum_square_difference(100))