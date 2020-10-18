# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably 
# large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is 
# only 1.
# 
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

from euler import sum_digits

max_sum = 0
for a in range(100):
    for b in range(100):
        max_sum = max(max_sum, sum_digits(a**b))
print(max_sum)

# the whole thing as a one liner... ugh, readability!
print( max([sum([int(d) for d in str(a**b)]) for a in range(100) for b in range(100)]))

# getting crazy now
import itertools
print(max( map(lambda x: sum([int(d) for d in str(x)]), \
    map(lambda n: n[0] ** n[1], itertools.product(range(100), repeat=2)))))