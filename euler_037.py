# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from euler import find_primality

UPPER_LIMIT=1000000 # increased until we found 11, which the problem gives
primality = find_primality(UPPER_LIMIT)

def is_truncatable_prime(number,truncate_lambda):
    s = str(number)
    while len(s) > 0:
        if not primality[int(s)]:
            return False
        s = truncate_lambda(s)
    return True

truncate_left  = lambda x : x[1:]
truncate_right = lambda x : x[:-1]

truncatable_primes = []

prime_numbers = [x for x,prime in enumerate(primality) if prime]
for i in prime_numbers:
    if i < 11:
        continue # skip 2, 3, 5, 7 as we're told to
    if is_truncatable_prime(i,truncate_left) and is_truncatable_prime(i,truncate_right):
        truncatable_primes.append(i)
print("found {0} primes".format(len(truncatable_primes)))
print(truncatable_primes)
print("Their sum is {0}".format(sum(truncatable_primes)))